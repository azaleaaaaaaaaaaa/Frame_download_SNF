import random
from user import gif_links


def get_link() -> str:
    return random.choice(gif_links)



def helper(comment: dict) -> None:
    if 'comment' in comment and 'id' in comment:
        comment['file_path'] = 'animation.gif'
        comment['link'] = get_link()
        comment['message'] = 'Helper'
