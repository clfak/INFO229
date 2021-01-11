from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts



def is_posted(user):
	
	usuario = user
	contraseña = "password"
	sitio = "https://info229bot.wordpress.com/xmlrpc.php" 
	cliente = Client(sitio, usuario, contraseña)
	text = "Titulo publicacion - Contenido"
	text1 = text.split('-')
	nueva_entrada = WordPressPost()
	nueva_entrada.title = text1[0]
	nueva_entrada.content = text1[1]
	id_entrada_publicada = cliente.call(posts.NewPost(nueva_entrada))
	print("Correcto! Se guardó la entrada como borrador, y su id es {}".format(id_entrada_publicada))
	print("Publicando entrada...")
	nueva_entrada.post_status = 'publish'
	resultado = cliente.call(posts.EditPost(id_entrada_publicada, nueva_entrada))

	print(resultado)
	if resultado is True:
		return True
	return False
