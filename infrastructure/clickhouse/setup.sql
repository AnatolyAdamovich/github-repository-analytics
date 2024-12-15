/* создание consumer */
CREATE TABLE default.kafka_commits
(
    `commit_id` String,
    `author` String,
    `message` String,
    `commit_date` String
)
ENGINE = Kafka
SETTINGS 
    kafka_broker_list = 'kafka:9092', 
    kafka_topic_list = 'github_commits_topic', 
    kafka_group_name = 'github_commits_group', 
    kafka_format = 'JSONEachRow', 
    kafka_num_consumers = 1;

/* создание целевой таблицы */
CREATE TABLE default.commits
(
    `commit_id` String,
    `author` String,
    `message` String,
    `commit_date` Date
)
ENGINE = MergeTree
ORDER BY commit_date
SETTINGS index_granularity = 8

/* создание materialized view для миграции данных */
CREATE MATERIALIZED VIEW default.transfer_mv TO default.commits
(
    `commit_id` String,
    `author` String,
    `message` String,
    `commit_date` Date
) AS
SELECT
    commit_id,
    author,
    message,
    CAST(commit_date, 'date') AS commit_date
FROM default.kafka_data