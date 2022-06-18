import json

import pika

import os

params = pika.URLParameters(os.getenv("AMQP"))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body) ,properties=properties)
