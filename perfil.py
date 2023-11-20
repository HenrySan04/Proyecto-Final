import requests
import json
import uuid
import os
from datetime import datetime

class Perfil:
    def __init__(self):
        self.users_data = self.fetch_data()
    
    def fetch_data(self):
        if os.path.exists('users_data.json'):
            with open('users_data.json', 'r') as f:
                users_data = json.load(f)
        else:
            response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json")
            users_data = json.loads(response.text)
        return users_data

    def register_user(self, name, lastName, email, username, tipo, department, career, multimedia):
        random_id = str(uuid.uuid4())
        actual_date = datetime.utcnow().isoformat() + "Z"
        self.users_data.append({"id": random_id,"firstName": name, "lastName": lastName, "email": email, "username": username, "type": tipo, "department": department, "major": career, "following": []})
        multimedia.posts_data.append({"publisher": random_id, "type": "photo", "caption": "Nuevo en Metrogram!", "date": actual_date, "tags": [], "multimedia": {"type": "photo", "url": "https://metrogram.com/" + str(uuid.uuid4())}, "likes": [], "comments": []})
        with open('users_data.json', 'w') as f:
            json.dump(self.users_data, f)
        with open('posts_data.json', 'w') as f:
            json.dump(multimedia.posts_data, f)

    def view_users(self):
        return self.users_data
    
    def search_profiles(self, filter_type, filter_value):
        print("Puedes buscar por: firstName, lastName, email, type, department, career, username o id")
        matching_profiles = [user for username, user in self.users_data.items() if user.get(filter_type) == filter_value]
        return matching_profiles

    def change_account_info(self, filter_type, filter_value, new_info_type, new_info_value):
        matching_profiles = [user for user in self.users_data if user.get(filter_type) == filter_value]
        for profile in matching_profiles:
            profile[new_info_type] = new_info_value

    def delete_account(self, filter_type, filter_value):
        matching_profiles = [user for user in self.users_data if user.get(filter_type) == filter_value]
        for profile in matching_profiles:
            self.users_data.remove(profile)

    def view_profile(self, filter_type, filter_value):
        with open('users_data.json', 'r') as f:
            self.users_data = json.load(f)
        matching_profiles = [user for user in self.users_data if user.get(filter_type) == filter_value]
        with open('users_data.json', 'w') as f:
            json.dump(self.users_data, f)
        with open('users_data.json', 'r') as f:
            self.users_data = json.load(f)
        return matching_profiles
        
    def view_following(self, filter_type, filter_value):
        with open('users_data.json', 'r') as f:
            self.users_data = json.load(f)
        user = next((user for user in self.users_data if user.get(filter_type) == filter_value), None)
        if user is None:
            print("User not found.")
            return
        return user["following"]
    
    