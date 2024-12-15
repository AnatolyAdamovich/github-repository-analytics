/* создание kafka consumer для приема изменений */
CREATE TABLE kafka_users_changes
(
    `payload` String
)
ENGINE = Kafka
SETTINGS 
    kafka_broker_list = 'kafka:9092', 
    kafka_topic_list = 'github.public.github_users', 
    kafka_group_name = 'github_users_group', 
    kafka_format = 'JSONEachRow';

/* создание целевой таблицы */
CREATE TABLE github_users
(
    `user_id` String,
    `name` String,
    `age` Integer,
    `position` String,
    `team` String
)
ENGINE = ReplacingMergeTree
ORDER BY (user_id, name);


/* создание materialized view для миграции данных */