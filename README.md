# 🚀 Apache Kafka with Python, Elasticsearch and Kibana Integration

This project demonstrates a complete data pipeline using Apache Kafka for message streaming, with Python producers and consumers, and integration with Elasticsearch and Kibana for data visualization.

## 📁 Project Structure

```text
apache-kafka-kibana-elasticsearch\
    ├── consumer_to_elastic.py
    ├── consumidor_processamento.py
    ├── consumidor.py
    ├── dados_cambio.json
    ├── docker-compose.yml
    ├── produtor_api.py
    ├── produtor.py
    └── README.md
```

- 📊 `produtor.py` - Simulates transaction data with different currencies
- 🔄 `produtor_api.py` - Fetches real-time exchange rates from an external API
- 👀 `consumidor.py` - Basic consumer that prints messages to console
- 💾 `consumidor_processamento.py` - Consumer that saves messages to a JSON file
- 📈 `consumer_to_elastic.py` - Consumer that indexes messages into Elasticsearch
- 🐳 `docker-compose.yml` - Infrastructure setup with Kafka, Elasticsearch, and Kibana
- 📝 `dados_cambio.json` - Storage file for exchange rate data

## 🏗️ Infrastructure

The project uses Docker Compose to set up the following services:

- 📨 Apache Kafka (v7.6.1)
- 🔍 Zookeeper (v7.6.1)
- 🔎 Elasticsearch (v8.5.0)
- 📊 Kibana (v8.5.0)

## 🛠️ Prerequisites

- 🐳 Docker and Docker Compose
- 🐍 Python 3.x
- 📦 pip (Python package manager)

## 🚀 Setup

1. Start the infrastructure:

```bash
docker compose up -d
```

2. Create a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required Python packages:

```bash
pip install kafka-python requests
```

4. Create the Kafka topic:

```bash
docker exec -it c_kafka kafka-topics --create --topic transacoes \
    --bootstrap-server 0.0.0.0:9092 --partitions 1 --replication-factor 1
```

## 📜 Available Scripts

### 🔄 Producers

1. 💳 Simulated Transaction Producer:

```bash
python produtor.py
```

- Generates mock transaction data with various currencies
- Sends data to 'transacoes' topic every 2 seconds

2. 📊 Real-time Exchange Rate Producer:

```bash
python produtor_api.py
```

- Fetches USD/EUR exchange rates from an external API
- Sends updates to 'transacoes' topic every 3 seconds

### 👥 Consumers

1. 🖥️ Basic Consumer:

```bash
python consumidor.py
```

- Prints received messages to console
- Uses consumer group 'meu_grupo'

2. 💾 Processing Consumer:

```bash
python consumidor_processamento.py
```

- Saves messages to `dados_cambio.json`
- Uses consumer group 'grupo_cambio'

3. 📊 Elasticsearch Consumer:

```bash
python consumer_to_elastic.py
```

- Indexes messages into Elasticsearch
- Uses consumer group 'grupo_elasticsearch'

## 📊 Monitoring

1. 📋 List Kafka topics:

```bash
docker exec -it c_kafka kafka-topics --list --bootstrap-server 0.0.0.0:9092
```

2. Monitor messages in topic:

```bash
docker exec -it c_kafka kafka-console-consumer \
    --bootstrap-server 0.0.0.0:9092 --topic transacoes --from-beginning
```

3. Access Kibana:

- Open http://localhost:5601 in your browser
- Create an index pattern for 'transacoes'
- Use Discover to view incoming data

## 🔌 Service Ports

- 📨 Kafka: 9092
- 🔍 Zookeeper: 2181
- 🔎 Elasticsearch: 9200
- 📊 Kibana: 5601
