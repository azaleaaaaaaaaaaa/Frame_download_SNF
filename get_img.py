import httpx
from time import sleep
from data import github_url


def down_img(frame_number: int) -> str:

    retries: int = 0
    while retries < 3:
        response = httpx.get(f'{github_url}/frame_{frame_number}.jpg', timeout=7)

        if response.status_code == 200:
            with open(f'images/frame_{frame_number}.jpg', 'wb') as file:
                file.write(response.content)
            return f'images/frame_{frame_number}.jpg'
        else:
            print(f'Error: {response.status_code} {response.content}')
            retries += 1
            sleep(3)

def get_img(comments_list: list) -> str:

    for comment in comments_list:

        if 'frame_number' in comment:
            frame_number = comment['frame_number']
            file_path = down_img(frame_number)
    
            if file_path:
                comment['file_path'] = file_path
            else:
                print(f'Error: Failed to download image for frame {frame_number}')
    

