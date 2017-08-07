import facebook

##varias pruebas con API de Facebook, limitaciones halladas para hacer la aplicacion

# obtener accesstoken
#https://developers.facebook.com/tools/explorer?method=GET&path=id&version=v2.9

#id_user
#me?fields=id,name

#sdk python
# https://facebook-sdk.readthedocs.io/en/latest/api.html

token = 'EAACEdEose0cBALJoQZCNDxHA3Ke0ZBQrXbC2aMmHDyIXqiws0HtL9OQ1iU8kO7ZC8bf1YmkEBG6yZBw8yCex9vIp8V5o4NWJfAJyp5ZBnO7prPOoR7YenZATr26ReV66pctG6VwtjyPstzN7L4GJkTgKCnjvilIAZCKxNJWPgTISG1pOJRTWduVmsngVneG4XIZD'
post_id= '1407771765926512'
id_usuario = '1407731869263835' #marlon
id_amigo = '267966646573702'




graph = facebook.GraphAPI(access_token=token, version='2.9')
user = graph.get_object("me")

# Get all of the authenticated user's friends
friends = graph.get_connections('me', "friendlists") #diccionario * data *pagin, data es una lista de diccionarios, donde la llave es `id` y el valor es el identificador de la lista de amigos
#friends = graph.get_all_connections(id='me', connection_name='friends')

#amigos = graph.get_object('me',fields='friends')
#print(amigos['friends'])

amigos = graph.get_connections(user["id"], "friends")
#print(amigos['data'])
amigo1 = amigos['data'][0]['id']
print(amigo1)
infoAmigo1 = graph.get_object(id=amigo1, fields='nombre,birthday')


######################## Listas de amigos ######################
print("\n listas de amigos:")

friendlists = friends['data']
listatest = friendlists[0]['id']

for friendlist in friendlists:
	#print(friendlist['id'])
	print(graph.get_object(friendlist['id'],fields='name, members'))
#print(type(nombrelistatest))
#print(nombrelistatest)

	#nombreLista = graph.get_object(friendlist[0], fields='name')
	#print(nombreLista)


	#for key, value in friend.items() :
		#print(key, value)
# Write 'Hola Que hace' to the active user's wall.
#graph.put_object(parent_object='me', connection_name='feed', message='Hola que hace')

 # Write a comment on a post. el primer parametro es idusuario_idpost bo puede ser solo idpost
#graph.put_comment(id_usuario+'_'+post_id, message='Interesante esta API')