import json
from perfil import Perfil
from multimedia import Multimedia
from interaccion import Interaccion 
from moderacion import Moderacion                                                   
import matplotlib.pyplot as plt
import numpy as np

class Estadisticas:
    def __init__(self):
        self.perfil = Perfil()
        self.multimedia = Multimedia()
        self.interaccion = Interaccion()
        self.moderacion = Moderacion()
    
    def users_posts(self):
        try:
            with open('users_data.json', 'r') as f:
                self.perfil.users_data = json.load(f)
            with open('posts_data.json', 'r') as f:
                self.multimedia.posts_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON data: {e}")
            return {}

        users_posts = {}
        for user in self.perfil.users_data:
            user_id = user.get("id")
            username = user.get("username")
            if user_id and username:
                user_posts = self.multimedia.view_post2("publisher", user_id)
                users_posts[username] = len(user_posts)

        return users_posts
    
    def major_comments_removed(self):
        majors_comments_removed = {}
        for user in self.perfil.users_data:
            major = user.get("major")
            user_posts = self.multimedia.view_post2("id", user["id"])
            removed_comments = 0
            for post in user_posts:
                removed_comments += sum(1 for comment in post.get("comments", []) if comment.get("removed") == True)
            if major not in majors_comments_removed:
                majors_comments_removed[major] = removed_comments
            else:
                majors_comments_removed[major] += removed_comments
        return majors_comments_removed
    
    def careers_posts(self):
        with open('users_data.json', 'r') as f:
            users_data = json.load(f)
        with open('posts_data.json', 'r') as f:
            posts_data = json.load(f)

        # Crea un diccionario con los usuarios que tienen una carrera
        user_careers = {user["id"]: user["major"] for user in users_data if user["type"] == "student" and "major" in user}

        # Cuenta los posts por carrera
        careers_posts = {}
        for post in posts_data:
            user_id = post["publisher"]
            career = user_careers.get(user_id)
            if career is not None:
                if career in careers_posts:
                    careers_posts[career] += 1
                else:
                    careers_posts[career] = 1

        return careers_posts
    
    def careers_comments(self):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        careers_comments = {}
        for user in self.perfil.users_data:
            career = user.get("major")
            user_posts = self.multimedia.view_post2("publisher", user["id"])
            comments = 0
            for post in user_posts:
                comments += len(post.get("comments", []))
            careers_comments[career] = comments
        return careers_comments
    
    def post_interactions(self):
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        post_interactions = {}
        for post in self.multimedia.posts_data:
            likes = len(post.get("likes", []))
            comments = len(post.get("comments", []))
            post_interactions[post["multimedia"]["url"]] = likes + comments
        return post_interactions

    def users_interactions(self): 
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        users_interactions = {}
        for user in self.perfil.users_data:
            user_posts = self.multimedia.view_post2("publisher", user["id"])
            likes = 0
            comments = 0
            for post in user_posts:
                likes += len(post.get("likes", []))
                comments += len(post.get("comments", []))
            users_interactions[user["username"]] = likes + comments
        return users_interactions
        
    def users_deleted_in_moderation(self):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        deleted_users = [user["username"] for user in self.perfil.users_data if user.get("deleted") == True]
        return deleted_users
    
    def users_with_posts_removed(self):
        with open('users_data.json', 'r') as f:
            self.perfil.users_data = json.load(f)
        with open('posts_data.json', 'r') as f:
            self.multimedia.posts_data = json.load(f)
        users_with_posts_removed = {}
        for user in self.perfil.users_data:
            user_posts = self.multimedia.view_post2("publisher", user["id"])
            posts_removed = sum(1 for post in user_posts if post.get("removed") == True)
            users_with_posts_removed[user["username"]] = posts_removed
        return users_with_posts_removed
    