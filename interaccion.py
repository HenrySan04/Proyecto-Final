import json
from perfil import Perfil
from multimedia import Multimedia

class Interaccion:
    def __init__(self):
        self.perfil = Perfil()
        self.multimedia = Multimedia()
        
# esto es para seguir usuarios usar tambien filter_type2 para filtrar el usuario que se quiere seguir guardar este data en users_data
    def follow_user(self, filter_type1, filter_value1, filter_type2, filter_value2):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        user1 = next((user for user in self.perfil.users_data if user.get(filter_type1) == filter_value1), None)
        user2 = next((user for user in self.perfil.users_data if user.get(filter_type2) == filter_value2), None)

        if user1 is None or user2 is None:
            print("One or both users not found.")
            return

        if user1["type"] == "professor" or user2["type"] == "professor":
            user1["following"].append(user2["id"])
            print(f"\n{user1['username']} ahora sigue a {user2['username']}.")
        elif user1["type"] == "student" and user2["type"] == "student":
            if user1.get("major") == user2.get("major"):
                user1["following"].append(user2["id"])
                print(f"\n{user1['username']} ahora sigue a {user2['username']}.")
            else:
                print(f"\n{user1['username']} estudia una carrera diferente a la de {user2['username']}.")
                if "requests" not in user2:
                    user2["requests"] = []
                if user1["id"] not in user2["requests"]:
                    user2["requests"].append(user1["id"])
                    print("\nSolicitud enviada.")
                else:
                    print("\nYa has enviado una solicitud a este usuario.")
        else:
            print("Invalid user type.")

        with open('users_data.json', 'w') as f:
            json.dump(self.perfil.users_data, f)
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)


    def accept_follow_request(self, filter_type, filter_value, opciones):
        user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        if user is None:
            print("User not found.")
            return
        if "requests" not in user or opciones not in user["requests"]:
            print("No such request.")
            return
        if "following" not in user:
            user["following"] = []
        if opciones not in user["following"]:
            user["following"].append(opciones)
        user["requests"].remove(opciones)
        with open('users_data.json', 'w') as f:
            json.dump(self.perfil.users_data, f)

    def decline_follow_request(self, filter_type, filter_value, opciones):
        user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        if user is None:
            print("User not found.")
            return
        if "requests" not in user or opciones not in user["requests"]:
            print("No such request.")
            return
        user["requests"].remove(opciones)
        with open('users_data.json', 'w') as f:
            json.dump(self.perfil.users_data, f)

    def show_follow_requests(self, filter_type, filter_value):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        # Buscar el usuario
        user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)

        if user is None:
            print("User not found.")
            return []

        # Sacar las solicitudes de seguimiento
        follow_requests = user.get("requests", [])
        print("Follow requests:")
        for request in follow_requests:
            print(request)

        return follow_requests
  
    def unfollow_user(self, filter_type1, filter_value1, filter_type2, filter_value2):
        # buscar user1 y user2
        user1 = next((user for user in self.perfil.users_data if user.get(filter_type1) == filter_value1), None)
        user2_id = next((user.get("id") for user in self.perfil.users_data if user.get(filter_type2) == filter_value2), None)

        if user1 is None or user2_id is None:
            print("One or both users not found.")
            return

        # Quitar a user2 de la lista de following de user1
        if user2_id in user1["following"]:
            user1["following"].remove(user2_id)

        # escribir los cambios en el archivo
        with open('users_data.json', 'w') as f:
            json.dump(self.perfil.users_data, f)

# recordar que 'id' en users es el mismo que 'publisher' en posts
    def view_following_posts(self, filter_type, filter_value):
        # buscar el usuario
        user = next((user for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)

        if user is None:
            print("User not found.")
            return

        # sacar el list de los users q sigue
        following = user["following"]

        # sacar los posts de los users q sigue
        matching_posts = [post for post in self.multimedia.posts_data if post.get("publisher") in following]

        return matching_posts
        
    def delete_post_comment(self, filter_type, filter_value, url, comment_to_delete):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        with open('users_data.json', 'r') as f:
            self.users_data = json.load(f)
        user_id = next((user.get("id") for user in self.perfil.users_data if user.get(filter_type) == filter_value), None)
        matching_posts = [post for post in self.posts_data if post.get("publisher") == user_id]
        for post in matching_posts:
            if post["multimedia"]["url"] == url:  
                for comment in post["comments"]:
                    if comment["comment"] == comment_to_delete:
                        post["comments"].remove(comment)
                        break
        with open('posts_data.json', 'w') as f:
            json.dump(self.posts_data, f)
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)

    def view_user_posts(self, filter_type, filter_value):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        with open('users_data.json', 'r') as f:
            self.users_data = json.load(f)
        user_id = next((user.get("id") for user in self.users_data if user.get(filter_type) == filter_value), None)
        matching_posts = [post for post in self.posts_data if post.get("publisher") == user_id]
        if not matching_posts:
            print("No posts found for this user.")
            return
        for post in matching_posts:
            print(f'\n{post["multimedia"]["url"]}')

    def view_post_comments_url(self, url):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        matching_post = next((post for post in self.posts_data if post.get("multimedia", {}).get("url") == url), None)
        if matching_post is None:
            print("Post not found.")
            return
        for comment in matching_post["comments"]:
            print(comment["comment"])
            
    def view_post_likes_url(self, url):
        with open('posts_data.json', 'r') as f:
            self.posts_data = json.load(f)
        matching_post = next((post for post in self.posts_data if post.get("multimedia", {}).get("url") == url), None)
        if matching_post is None:
            print("Post not found.")
            return
        print(matching_post.get('likes', 0))