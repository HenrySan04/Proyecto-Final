from perfil import Perfil
from multimedia import Multimedia
import json

"""Gestión de moderación
Este módulo permitirá a los usuarios administrativos moderar el contenido de las app. Para ello, se deberá desarrollar lo siguiente:

Un usuario administrador puede realizar:
Eliminar un post que considera ofensivo
Eliminar un comentario ofensivo
Eliminar un usuario que infringido múltiples veces las reglas 
Recuerda que el api de perfil.py y multimedia.py ya tienen las funciones para eliminar usuarios, posts y comentarios."""

class Moderacion:
    def __init__(self):
        self.perfil = Perfil()
        self.multimedia = Multimedia()
    
# funcion para eliminar un post que considera ofensivo
    def delete_post(self, filter_type, filter_value, url):
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        matching_user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        if matching_user is not None:
            matching_posts = [post for post in self.multimedia.posts_data if post.get(filter_type) == filter_value]
            for post in matching_posts:
                if post["url"] == url:
                    self.multimedia.posts_data.remove(post)
        with open('posts_data.json', 'w') as f:
            json.dump(self.multimedia.posts_data, f)
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
    
    def delete_comment(self, filter_type, filter_value, url, comment_content):
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        for post in self.multimedia.posts_data:
            if post.get(filter_type) == filter_value and post["url"] == url:
                for comment in post["comments"]:
                    if comment["comment"] == comment_content:
                        comment["removed"] = True
                        break
        with open('posts_data.json', 'w') as f:
            json.dump(self.multimedia.posts_data, f)
    
    def delete_user(self, filter_type, filter_value):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        matching_user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        if matching_user is not None:
            matching_user["deleted"] = True
        with open('users_data.json', 'w') as f:
            json.dump(self.perfil.users_data, f)
    
    def delete_user_posts(self, filter_type, filter_value):
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        if filter_type in self.perfil.users_data and filter_value in self.perfil.users_data:
            matching_posts = [post for post in self.multimedia.posts_data if post.get(filter_type) == filter_value]
            for post in matching_posts:
                self.multimedia.posts_data.remove(post)
        with open('posts_data.json', 'w') as f:
            json.dump(self.multimedia.posts_data, f)
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
