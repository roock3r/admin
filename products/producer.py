import json

import pika

params = pika.URLParameters('amqps://mjwxsfts:FjoGL8uUVxSv8jgz9cqMzppHxN7xZ2Xg@shrimp.rmq.cloudamqp.com/mjwxsfts')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body) ,properties=properties)
