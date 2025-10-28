```bash
# criação dos tópicos
$ docker exec -it c_kafka kafka-topics --create --topic transacoes --bootstrap-server 0.0.0.0:9092 --partitions 1 --replication-factor 1

# Para listar os tópicos existentes:
$ docker exec -it c_kafka kafka-topics --list --bootstrap-server 0.0.0.0:9092

# verificação do resultado
$ docker exec -it c_kafka kafka-console-consumer --bootstrap-server 0.0.0.0:9092 --topic transacoes --from-beginning

# criação do virtrual env
$ python -m venv .venv

# ativaço do ambiente
$ source .venv/bin/activate

# execução do produtor
$ python produtor.py

# execução do consumidor
$ python consumidor.py
```
