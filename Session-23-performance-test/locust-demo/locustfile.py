from locust import HttpUser, between, task

class MyTestStressUser(HttpUser):
    wait_time = between(1,2)
    

    @task
    def get_posts(self):
        self.client.get("/posts")
        self.client.get("/todos")
        