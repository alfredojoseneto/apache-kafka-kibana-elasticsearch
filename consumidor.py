from kafka import KafkaConsumer
import json
# Configuração do consumidor Kafka
consumer = KafkaConsumer(
    'transacoes', # Nome do tópico
    bootstrap_servers='0.0.0.0:9092', # Endereço do Kafka
    value_deserializer=lambda v: json.loads(v.decode('utf-8')), # Deserializa JSON
    auto_offset_reset='earliest', # Lê mensagens antigas se não houver offset salvo
    group_id='meu_grupo' # Define um grupo de consumidores
)
print("Aguardando mensagens...")
for mensagem in consumer:
    print(f"Mensagem recebida: {mensagem.value}")