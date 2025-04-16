import json
import pandas as pd
from confluent_kafka import Producer
from confluent_kafka.admin import NewTopic ,AdminClient
import time

def run_producer():

    KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'
    TOPIC = 'supply_chain_data'

    producer_config = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'queue.buffering.max.messages': 1000000,  # Increase queue size
        'queue.buffering.max.ms': 10000  # Wait up to 10s
    }

    producer = Producer(producer_config)

    admin = AdminClient(producer_config)
    if TOPIC not in admin.list_topics().topics:
        topic = NewTopic(TOPIC, num_partitions=1, replication_factor=1)
        admin.create_topics([topic])

    csv_path = '/project/data/DataCoSupplyChainDataset.csv'
    df = pd.read_csv(csv_path , encoding='latin-1')
    
    # Send each row to Kafka
    for _, row in df.iterrows():
        data = {
            'order_id': str(row['Order Id']),
            'customer_id': str(row['Order Customer Id']),
            'product_category': row['Category Name'],
            'quantity': int(row['Order Item Quantity']),
            'unit_price': float(row['Order Item Product Price']),
            'total_amount': float(row['Order Item Total']),
            'customer_city': row['Customer City'],
            'order_status': row['Order Status'],
            'order_timestamp': row['order date (DateOrders)'],
            'expected_delivery': row['shipping date (DateOrders)'],
            'warehouse_id': str(row['Department Id']),
            'delivery_status': row['Delivery Status'],
            'late_delivery_risk': int(row['Late_delivery_risk'])
        }
        
        producer.produce(
            TOPIC,
            key=data['order_id'].encode('utf-8'),
            value=json.dumps(data).encode('utf-8')
        )
        time.sleep(0.01)  # 10ms delay to prevent queue overload
    
    producer.flush()

if __name__ == '__main__':
    run_producer()