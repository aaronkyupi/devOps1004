import requests, names
from selenium import webdriver

my_driver = webdriver.Chrome()
my_driver2 = webdriver.Chrome()

unis = requests.get("http://universities.hipolabs.com/search?country=Israel")
my_driver.get("https://www.ycombinator.com/")
my_driver2.get("https://hub.docker.com")
repos = requests.get("https://api.github.com/users/avielb/repos")
my_names = ["Aaron", "Moshe", "Israel"]

for i in range(3):
    if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
        my_names.append(i)

assert my_driver.title == "Y Combinator"
assert my_driver2.title == "Docker Hub Container Image Library | App Containerization"
assert len(repos.json()) > 5  # We have 30 repos
assert len(my_names) == 3
assert len(unis.json()) > 5
