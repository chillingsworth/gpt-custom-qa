
from qa import answer
import pika

class RabbitMQ:

    def __init__(self, question_queue, answer_queue):
        
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        self.question_queue = question_queue
        self.answer_queue = answer_queue
        # self.consumer = consumer
        self.channel.queue_declare(self.question_queue)
        self.channel.queue_declare(self.answer_queue)
    
    def publish(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.answer_queue,
                        body=b'What is an annuity?')
    
    def consume(self):
        self.channel.basic_consume(queue=self.question_queue,
                      auto_ack=True,
                      on_message_callback=self.consumer)
        
        self.channel.start_consuming()
        
    def __del__(self):
        self.connection.close()

    def consumer(self, ch, method, properties, body):
        # print("Question: ", body)
        ans = answer(str(body))
        # print("Answer: ", ans)
        self.publish(ans)

r = RabbitMQ('question_queue', 'answer_queue')
r.consume()