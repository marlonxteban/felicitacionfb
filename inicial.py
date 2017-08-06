import facebook

# obtener accesstoken
#https://developers.facebook.com/tools/explorer?method=GET&path=id&version=v2.9

#id_user
#me?fields=id,name

#sdk python
# https://facebook-sdk.readthedocs.io/en/latest/api.html

token = 'EAACEdEose0cBAHhRgKZBC6upHDmQKng1ZAXrxhqAD1PetLGgm3AaZB3yZA839rnRo8926ZBD5y0fVM649IqaCj5z5GweftSWXVNDdAfpp7LzoaZCmYJd1LL5EsLCB85dlXGSHgCrK4e6ZB3GruReclUK1RoOUJq9frSvRiNbxozjVJwaMnOlaBz6FxwwouBJTYZD'
post_id= '1407771765926512'
id_usuario = '1407731869263835'

graph = facebook.GraphAPI(access_token=token, version='2.9')

# Get all of the authenticated user's friends
friends = graph.get_all_connections(id='me', connection_name='friends')

for friend in friends:
	for key, value in friend.items() :
		print(key, value)
# Write 'Hola Que hace' to the active user's wall.
#graph.put_object(parent_object='me', connection_name='feed', message='Hola que hace')

 # Write a comment on a post. el primer parametro es idusuario_idpost bo puede ser solo idpost
graph.put_comment(id_usuario+'_'+post_id, message='Interesante esta API')