from kafka import KafkaProducer
from kafka import KafkaConsumer

def put_messages(topic_name='my-topic-name1', message='default_message'):

    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    for i in range(100):
        print(str(i))
        producer.send(topic=topic_name, value=b'some_message_bytes2')

def get_messages(topic_name='my-topic-name1', buffer_size=100):
    
    consumer = KafkaConsumer(topic_name)

    queue = []

    for _ in range(buffer_size):
        queue.append(next(consumer).value.decode('utf-8'))
    
    return queue