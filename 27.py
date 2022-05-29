import requests
response = requests.get("https://api.github.com/users/avielb/repos")
print(response.status_code)