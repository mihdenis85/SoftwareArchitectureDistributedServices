import requests

API_URL = "http://localhost"

def register(username):
    response = requests.post(f"{API_URL}:8001/register", json={"username": username})
    print(response.json())

def post_message(username, content):
    response = requests.post(f"{API_URL}:8002/post", json={"username": username, "content": content})
    print(response.json())

def like_message(username, content):
    response = requests.post(f"{API_URL}:8002/like", json={"username": username, "content": content})
    print(response.json())

def get_feed():
    response = requests.get(f"{API_URL}:8003/feed")
    feed = response.json()
    if isinstance(feed, dict) and 'error' in feed:
        print(feed['error'])
        return
    for idx, message in enumerate(feed):
        print(f"{idx}: [{message['timestamp']}] {message['username']}: {message['content']} (Likes: {message['likes']})")

def main():
    while True:
        command = input("Enter command (register, post, like, feed, exit): ")
        if command == "register":
            username = input("Username: ")
            register(username)
        elif command == "post":
            username = input("Username: ")
            content = input("Message: ")
            post_message(username, content)
        elif command == "like":
            username = input("Username: ")
            content = input("Message id: ")
            like_message(username, content)
        elif command == "feed":
            get_feed()
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
