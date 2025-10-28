import json
import os

from kafka import KafkaConsumer

# Configuração do consumidor Kafka
consumer = KafkaConsumer(
    "transacoes",  # Nome do tópico
    bootstrap_servers="localhost:9092",  # Endereço do Kafka
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="grupo_cambio",
)

# Criar ou abrir um arquivo para armazenar os dados
file_path = "dados_cambio.json"
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)

print("Aguardando mensagens...")

for mensagem in consumer:
    print(f"Mensagem recebida: {mensagem.value}")

    # Adiciona a mensagem ao arquivo JSON
    with open(file_path, "r+") as f:
        dados_existentes = json.load(f)
        dados_existentes.append(mensagem.value)
        f.seek(0)
        json.dump(dados_existentes, f, indent=4)
