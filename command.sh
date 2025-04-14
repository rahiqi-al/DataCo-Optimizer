Créer_topic
docker exec -it kafka kafka-topics --create --topic user-interactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Publier_message_topic
docker exec -it kafka kafka-console-producer --broker-list localhost:9092 --topic user-interactions

Consommer_messages_topic
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic user-interactions --from-beginning

-------------------------------------------------------------------------------------------------------------------------------------------------------

dbt:
docker start dbt && docker exec dbt bash -c "cd /usr/app/dbt && dbt run" && docker stop dbt

docker exec -it dbt bash -c "cd /usr/app/dbt && dbt run"

docker exec dbt bash -c "cd /usr/app/dbt && dbt run"

-------------------------------------------------------------------------------------------------------------------------------------------------------

snowflake:
SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO();

SELECT CURRENT_REGION(), CURRENT_ACCOUNT_NAME();

