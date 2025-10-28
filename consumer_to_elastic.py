import json

import requests
from kafka import KafkaConsumer

# Configuração do consumidor Kafka
consumer = KafkaConsumer(
    "transacoes",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="grupo_elasticsearch",
)

# URL do Elasticsearch
ELASTICSEARCH_URL = "http://localhost:9200/transacoes/_doc/"

print("Aguardando mensagens para indexação no Elasticsearch...")

for mensagem in consumer:
    data = mensagem.value  # Mensagem recebida
    print(f"Indexando no Elasticsearch: {data}")

    # Enviar os dados para o Elasticsearch
    response = requests.post(ELASTICSEARCH_URL, json=data)

    if response.status_code in [200, 201]:
        print("Documento indexado com sucesso!")
    else:
        print(f"Erro ao indexar documento: {response.text}")
