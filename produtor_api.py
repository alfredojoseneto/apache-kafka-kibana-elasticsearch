import json
import time

import requests
from kafka import KafkaProducer

# Configuração do produtor Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",  # Endereço do Kafka
    value_serializer=lambda v: json.dumps(v).encode(
        "utf-8"
    ),  # Serializa JSON para bytes
)

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # API de câmbio

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()

        # Criar mensagem para Kafka
        mensagem = {
            "moeda_origem": "USD",
            "moeda_destino": "EUR",
            "taxa_cambio": data["rates"]["EUR"],
            "timestamp": data["time_last_updated"],
        }

        print(f"Enviando: {mensagem}")
        producer.send("transacoes", mensagem)  # Enviar mensagem para o tópico
        time.sleep(3)  # Envia a cada 10 segundos
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        time.sleep(10)  # Espera um tempo maior antes de tentar novamente
