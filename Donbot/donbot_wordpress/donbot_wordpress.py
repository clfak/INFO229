#!/usr/bin/env python
import pika
import time
import os
import wordpress_xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts



time.sleep(10)

########### CONNEXIÓN A RABBIT MQ #######################
HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'donbot'
channel.exchange_declare(exchange='donbot', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="wordpress", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='donbot', queue=queue_name, routing_key="wordpress")


##########################################################
usuario = "clfak"
contraseña = "password"
sitio = "https://info229bot.wordpress.com/xmlrpc.php" 
cliente = Client(sitio, usuario, contraseña)

########## ESPERA Y PUBLICA CUANDO RECIBE UN MENSAJE ####

print(' donbot_wordpress Waiting for messages...')


def callback(ch, method, properties, body):
    print(body)
    if str(body).startswith("[wordpress]") and len(str(body))<300:
        query = str(body)[11:]
        q = query.split('-')
        nueva_entrada = WordPressPost()
        nueva_entrada.title = q[0]
        nueva_entrada.content = q[1]
        id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
        print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
        print("Publicando entrada...")
        nueva_entrada.post_status = 'publish'
        resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))
        print(resultado)
        if resultado is True:
            print("Entrada publicada")
        else:
            print("Algo salió mal")

        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        channel.basic_publish(exchange='donbot', routing_key="publicar_slack", body="publicado!")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

###########################################################

