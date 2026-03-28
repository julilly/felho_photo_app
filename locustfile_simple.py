from locust import HttpUser, task, between

class SimplePhotoViewer(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.get("/login/")
        csrf_token = response.cookies.get("csrftoken", "")

        self.client.post(
            "/login/", 
            data={
                "username": "felhasznalo",
                "password": "jelszo123", 
                "csrfmiddlewaretoken": csrf_token
            }, 
            headers={"Referer": f"{self.user.host}/login/"}
        )

    @task
    def view_existing_photo(self):
        self.client.get("/photo/4/")