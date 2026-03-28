from locust import HttpUser, task, between, SequentialTaskSet
import io
import random
import re
import uuid
from PIL import Image

class UserJourney(SequentialTaskSet):
    def on_start(self):
        self.username = f"user_{uuid.uuid4().hex[:8]}"
        self.password = "TestPassword123!"
        self.my_photo_id = None

    def fetch_csrf(self, url):
        response = self.client.get(url)
        return response.cookies.get("csrftoken", "")
    
    @task
    def register_and_login(self):
        csrf_token = self.fetch_csrf("/register/")
        headers = {"Referer": f"{self.user.host}/register/"}
        
        self.client.post("/register/", data={
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "csrfmiddlewaretoken": csrf_token
        }, headers=headers)

    @task
    def upload_valid_photo(self):
        csrf_token = self.fetch_csrf("/upload/")
        headers = {"Referer": f"{self.user.host}/upload/"}
        
        #random image
        img = Image.new('RGB', (10, 10), color='red')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        img_byte_arr.name = f"random_image_{random.randint(1, 1000)}.jpg"
        
        self.client.post("/upload/", data={
            "name": f"Test Photo", 
            "csrfmiddlewaretoken": csrf_token
        }, files={"image": img_byte_arr}, headers=headers)
            
    @task
    def find_and_view_my_photo(self):
        response = self.client.get("/")
        
        my_ids = re.findall(r'/delete/(\d+)/', response.text)
        
        if my_ids:
            self.my_photo_id = my_ids[0]
            self.client.get(f"/photo/{self.my_photo_id}/")

    @task
    def delete_my_photo(self):
        if self.my_photo_id:
            self.client.get(f"/delete/{self.my_photo_id}/")
            self.my_photo_id = None

    @task
    def logout(self):
        self.client.get("/logout/")


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [UserJourney]