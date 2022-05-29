import requests

#
# 1. function input name from users
# 2. print hello {name} for each name in the names.txt file
# 3. use urls from urls.txt to call to the url_caller we wrote before

def url_caller(url):
   response = requests.get(url)
   if response.status_code == 200:
      print(f"{url} is ok")

def call_urls():
    with open("urls.txt) as urls:"
              "for line ")
def save_names():
    n = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{n}\n")
    my_file.close()

def show_names():
    with open("names.txt") as my_file:
    for line in my_file.readlines():
        printf(f"Hello {line}", end='')


# import requests
# def save_name():
#     n = input("enter your name: ")
#     my_file = open("names.txt", "a")
#     my_file.write(f"{n}\n")
#
#
#
# def show_names():
#     with open("names.txt") as moshe:
#         for line in moshe.readlines():
#             print(f"hello {line}", end='')
# def url_caller(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(f"{url} is ok")
#
# def call_urls():
#     with open("urls.txt") as urls:
#         for line in urls.readlines():
#             url_caller(line.strip())
#
# # save_name()
# call_urls()

