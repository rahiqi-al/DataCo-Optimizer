import json
import pandas as pd
from confluent_kafka import Consumer, KafkaError
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

def run_consumer():

    KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
    TOPIC = 'supply_chain_data'
    SNOWFLAKE_CONFIG = {
        'user': 'ali',
        'password': 'xSPJ8viZmZfjMxD',
        'account': 'xbmgybc-in88930',
        'warehouse': 'dataco',
        'database': 'dataco',
        'schema': 'public',
        'role': 'ACCOUNTADMIN'
    }

    consumer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'supply_chain_consumer',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe([TOPIC])

    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    records = []

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                if records:
                    df = pd.DataFrame(records)
                    success, nchunks, nrows, _ = write_pandas(
                        conn, df, 'RAW_SUPPLY_CHAIN_DATA', auto_create_table=True
                    )
                    consumer.commit()
                    records = []
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break

            data = json.loads(msg.value().decode('utf-8'))
            records.append({
                'order_id': data['order_id'],
                'customer_id': data['customer_id'],
                'product_category': data['product_category'],
                'quantity': data['quantity'],
                'unit_price': data['unit_price'],
                'total_amount': data['total_amount'],
                'customer_city': data['customer_city'],
                'order_status': data['order_status'],
                'order_timestamp': data['order_timestamp'],
                'expected_delivery': data['expected_delivery'],
                'warehouse_id': data['warehouse_id'],
                'delivery_status': data['delivery_status'],
                'late_delivery_risk': data['late_delivery_risk']
            })

            if len(records) >= 1000:
                df = pd.DataFrame(records)
                success, nchunks, nrows, _ = write_pandas(
                    conn, df, 'RAW_SUPPLY_CHAIN_DATA', auto_create_table=True
                )
                consumer.commit()
                records = []

    except KeyboardInterrupt:
        pass
    finally:
        if records:
            df = pd.DataFrame(records)
            success, nchunks, nrows, _ = write_pandas(
                conn, df, 'RAW_SUPPLY_CHAIN_DATA', auto_create_table=True
            )
            consumer.commit()
        consumer.close()
        conn.close()

