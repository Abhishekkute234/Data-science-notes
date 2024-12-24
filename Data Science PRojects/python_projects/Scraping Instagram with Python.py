import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'aman.kharwal')

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)

# Login with username and password in the script
bot.login(user="your username",passwd="your password")

# Interactive login on terminal
bot.interactive_login("your username") # Asks for password in the terminal

# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)

# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'wwe')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
    
box=[1,2,4,5,6,7]   
    
for i in box:
    print(i)    
    
    
# import requests
# from bs4 import BeautifulSoup

# def download_instagram_reel(reel_url, output_path):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
    
#     response = requests.get(reel_url, headers=headers)
#     if response.status_code != 200:
#         raise Exception(f"Failed to load page, status code: {response.status_code}")

#     soup = BeautifulSoup(response.content, 'html.parser')
#     video_tag = soup.find('meta', property='og:video')

#     if not video_tag or not video_tag['content']:
#         raise Exception("Could not find reel video URL")

#     video_url = video_tag['content']
#     video_response = requests.get(video_url, headers=headers)

#     if video_response.status_code != 200:
#         raise Exception(f"Failed to download video, status code: {video_response.status_code}")

#     with open(output_path, 'wb') as f:
#         f.write(video_response.content)

#     print(f"Downloaded reel to {output_path}")

# # Example usage:
# reel_url = "https://www.instagram.com/reel/XXXXXXXXXXX/"
# output_path = "reel.mp4"
# download_instagram_reel(reel_url, output_path)
    