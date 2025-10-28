from kafka import KafkaProducer
import json
import time
# Configuração do produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='0.0.0.0:9092', # Endereço do Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serializa JSON para bytes
)
# Simular envio de transações
transacoes = [
    {"id": 1, "valor": 100.50, "moeda": "EUR"},
    {"id": 2, "valor": 250.00, "moeda": "USD"},
    {"id": 3, "valor": 75.30, "moeda": "BRL"},
    {"id": 4, "valor": 180.75, "moeda": "GBP"},
    {"id": 5, "valor": 520.00, "moeda": "USD"},
    {"id": 6, "valor": 300.10, "moeda": "EUR"},
    {"id": 7, "valor": 45.90, "moeda": "BRL"},
    {"id": 8, "valor": 999.99, "moeda": "JPY"},
    {"id": 9, "valor": 1200.00, "moeda": "CAD"},
    {"id": 10, "valor": 610.45, "moeda": "USD"},
    {"id": 11, "valor": 87.60, "moeda": "CHF"},
    {"id": 12, "valor": 432.15, "moeda": "BRL"},
    {"id": 13, "valor": 59.99, "moeda": "EUR"},
    {"id": 14, "valor": 740.20, "moeda": "GBP"},
    {"id": 15, "valor": 120.80, "moeda": "USD"},
    {"id": 16, "valor": 310.55, "moeda": "BRL"},
    {"id": 17, "valor": 890.30, "moeda": "EUR"},
    {"id": 18, "valor": 2300.00, "moeda": "JPY"},
    {"id": 19, "valor": 450.00, "moeda": "CAD"},
    {"id": 20, "valor": 102.25, "moeda": "USD"},
    {"id": 21, "valor": 640.00, "moeda": "CHF"},
    {"id": 22, "valor": 15.75, "moeda": "BRL"},
    {"id": 23, "valor": 370.50, "moeda": "EUR"},
    {"id": 24, "valor": 290.10, "moeda": "USD"},
    {"id": 25, "valor": 1750.00, "moeda": "JPY"},
    {"id": 26, "valor": 85.90, "moeda": "BRL"},
    {"id": 27, "valor": 910.00, "moeda": "GBP"},
    {"id": 28, "valor": 340.40, "moeda": "USD"},
    {"id": 29, "valor": 78.25, "moeda": "EUR"},
    {"id": 30, "valor": 500.00, "moeda": "BRL"},
    {"id": 31, "valor": 2500.75, "moeda": "CAD"},
    {"id": 32, "valor": 630.80, "moeda": "USD"},
    {"id": 33, "valor": 95.60, "moeda": "CHF"}
]
for transacao in transacoes:
    print(f"Enviando: {transacao}")
    producer.send('transacoes', transacao) # Enviar mensagem para o tópico
    time.sleep(2) # Simula um tempo entre os envios
    producer.flush() # Garante que todas as mensagens foram enviadas
    print("Todas as transações foram enviadas!")