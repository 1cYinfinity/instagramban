//Author : 1cYinfinity
//MIT Licences 

import requests
from bs4 import BeautifulSoup

def ban_instagram_id(username, your_username, your_password):
    try:
        # Step 1: Log in to Instagram
        session = requests.Session()
        login_url = "https://www.instagram.com/accounts/login/"
        login_payload = {
            'username': your_username,
            'password': your_password
        }

        session.headers.update({'User-Agent': 'Mozilla/5.0'})
        session.get(login_url)
        session.post(login_url, data=login_payload, allow_redirects=True)

        # Step 2: Get the target user's profile page
        target_url = f'https://www.instagram.com/{username}/'
        response = session.get(target_url)

        # Step 3: Extract the target user's user_id
        soup = BeautifulSoup(response.text, 'html.parser')
        user_id_tag = soup.find('script', text=lambda t: 'window._sharedData' in t)
        user_id_start = user_id_tag.text.find('"profilePage_') + len('"profilePage_')
        user_id_end = user_id_tag.text.find('"', user_id_start)
        user_id = user_id_tag.text[user_id_start:user_id_end]

        # Step 4: Ban the user
        ban_url = f'https://www.instagram.com/web/friendships/{user_id}/unfollow/'
        session.post(ban_url)

        print(f"Successfully banned Instagram ID: {username}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_username = input("Enter the Instagram ID to ban: ")
    your_instagram_username = input("Enter your Instagram username: ")
    your_instagram_password = input("Enter your Instagram password: ")

    ban_instagram_id(target_username, your_instagram_username, your_instagram_password)
