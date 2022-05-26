from string import ascii_letters
from locust import HttpUser, task, between

npm = "1906293322"

class IdempotentGetTasks(HttpUser):
	wait_time = between(1,5)

	@task
	def read_idempotent(self):
		self.client.get(f"/read/1906293322")