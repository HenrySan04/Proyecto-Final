import requests
import os
import json
from perfil import Perfil
import uuid
from datetime import datetime

class Multimedia:
    def __init__(self):
        self.posts_data = self.fetch_data()
        self.perfil = Perfil()

# sacar el data del api y guardar toda la data que se vaya agregando para almacenarlo en el programa
    def fetch_data(self):
        if os.path.exists('posts_data.json'):
            with open('posts_data.json', 'r') as f:
                posts_data = json.load(f)
        else:
            response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/posts.json")
            posts_data = json.loads(response.text)
        return posts_data
    
# funcion para publicar un nuevo post recuerda que id en el api de perfil es igual a publisher en el api de multimedia
    def publish_post(self, filter_type, filter_value, tipo, caption, tags):
        self.perfil.users_data = self.perfil.fetch_data()  # Fetch the latest user data
        for user in self.perfil.users_data:
            if user.get(filter_type) == filter_value:
                user_id = user.get("id")
                random_url = "https://metrogram.com/" + str(uuid.uuid4())
                current_date = datetime.utcnow().isoformat() + "Z"
                new_post = {"publisher": user_id, "type": tipo, "caption": caption, "date": current_date, "tags": tags, "multimedia": {"type": tipo, "url": random_url}, "likes": [], "comments": []}
                self.posts_data.append(new_post)  # Append the new post to posts_data
                with open('posts_data.json', 'w') as f:
                    json.dump(self.posts_data, f)  # Write the updated posts data back to the file
                with open('posts_data.json', 'r') as f:
                    self.posts_data = json.load(f)
                return
                

# funcion para ver posts de un usuario en especifico introduciendo su id pero con el api de perfil. Al saber el id del usuario podemos saber el id del publisher en el api de multimedia
    def view_post(self, filter_type, filter_value):
     with open('users_data.json', 'r') as f:
        self.perfil.users_data = json.load(f)
     with open('posts_data.json', 'r') as f:
        self.posts_data = json.load(f)
     matching_posts = [post for post in self.posts_data if post.get(filter_type) == filter_value]
     for user in self.perfil.users_data:
        if user.get(filter_type) == filter_value:
            user_id = user.get("id")
            matching_posts = [post for post in self.posts_data if post.get("publisher") == user_id]
            return matching_posts
     return []
    
# funcion para ver posts de un usuario en especifico introduciendo su id pero con el api de multimedia
    def view_post2(self, filter_type, filter_value):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        matching_posts = [post for post in self.posts_data if post.get(filter_type) == filter_value]
        return matching_posts
        
# funcion para buscar posts con el filtro que desees ej: caption, url, etc. que tambien funcione con el url que esta en multimedia
    def search_posts(self, filter_type, filter_value):
        matching_posts = []  # Initialize matching_posts as an empty list
        for post in self.posts_data:
            if filter_type in post and post.get(filter_type) == filter_value:
                matching_posts.append(post)
            elif filter_type == "url" and post["multimedia"]["url"] == filter_value:  # tengo que hacer esto porque el url esta en multimedia
                matching_posts.append(post)
        return matching_posts
    
    def like_post(self, filter_type1, filter_value1, filter_type2, filter_value2, url):
        # Load the posts data
        with open('posts_data.json', 'r') as f:
            posts_data = json.load(f)

        # buscar user1 y user2
        user1_id = next((user.get("id") for user in self.perfil.users_data if user.get(filter_type1) == filter_value1), None)
        if user1_id is None:
            print("User1 not found.")
            return

        # sacar el id del user2
        user2_id = next((user.get("id") for user in self.perfil.users_data if user.get(filter_type2) == filter_value2), None)
        if user2_id is None:
            print("User2 not found.")
            return

        # buscar el post y agregar el like
        for i, post in enumerate(self.posts_data):
            if post.get("publisher") == user2_id and post["multimedia"]["url"] == url:
                if "likes" not in post:
                    self.posts_data[i]["likes"] = []  # Add "likes" key if it doesn't exist
                self.posts_data[i]["likes"].append(user1_id)
                break
        else:
            print("Post not found.")
            return

        # escribir los cambios en el archivo
        with open('posts_data.json', 'w') as f:
            json.dump(self.posts_data, f)

        # volver a cargar los datos
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)

    def comment_post(self, filter_type, filter_value, filter_type2, filter_value2, url, comment):
        # cargar los datos
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)

        # buscar el user1
        user1 = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        if user1 is None:
            print("User1 not found.")
            return
        user1_id = user1.get("id")
        username = user1.get("username")

        # buscar el user2
        user2_id = next((user.get("id") for user in self.perfil.users_data if user.get(filter_type2) == filter_value2), None)
        if user2_id is None:
            print("User2 not found.")
            return

        # buscar el post y agregar el comentario
        for i, post in enumerate(self.posts_data):
            if post.get("publisher") == user2_id and post["multimedia"]["url"] == url:
                if "comments" not in post:
                    self.posts_data[i]["comments"] = []  # Add "comments" key if it doesn't exist
                self.posts_data[i]["comments"].append({"comment": comment, "username": username, "id": user1_id})
                break
        else:
            print("Post not found.")
            return 

        # escribir los cambios en el archivo
        with open('posts_data.json', 'w') as f:
            json.dump(self.posts_data, f)
        
# ver urls de todos los posts de un usuario en especifico recuerda que id en el api de perfil es igual a publisher en el api de multimedia
    def view_post_urls(self, filter_type, filter_value):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        for user in self.perfil.users_data:
            if user.get(filter_type) == filter_value:
                user_id = user.get("id")
                matching_posts = [post for post in self.posts_data if post.get("publisher") == user_id]
                return [post["multimedia"]["url"] for post in matching_posts]
        return []
        
    def view_all_posts(self):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        return self.posts_data
    