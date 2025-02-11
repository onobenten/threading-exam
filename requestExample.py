import requests


#GET
user_input = input("enter id: ")
get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"


get_response = requests.get(url)
print(get_response.json())

#Post
to_do_item = {"userId": 2, "title" : "my to do","completed": False}
post_url = f"https://jsonplaceholder.typicode.com/todos"
#optional header
headers = {"Content-Type": "application/json"}
post_response = requests.post(post_url, json=to_do_item, headers=headers)
print(post_response.json())
#json.dumps jsona dönüştürür.