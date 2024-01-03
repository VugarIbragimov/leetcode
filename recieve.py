import pika
import traceback
import sys


conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

print('Waiting for messages')


def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(queue='first-queue', auto_ack=True,
                      on_message_callback=callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)


# connection.close()
