from os import environ
from user import REPO_OWNER, REPO, BRANCH, FRAMES_FOLDER


# facebook
fb_version: str = 'v20.0'
fb_url: str = f'https://graph.facebook.com/{fb_version}'
FB_TOKEN: str = environ.get('FB_TOKEN')


# imgBB
img_url: str = 'https://api.imgbb.com/1/upload'
IMG_TOKEN: str = environ.get('IMG_TOKEN')


#github
url: str = f'https://raw.githubusercontent.com/{REPO_OWNER}/{REPO}/{BRANCH}/{FRAMES_FOLDER}'