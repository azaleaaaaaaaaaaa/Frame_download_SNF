import httpx
from time import sleep
from data import github_url
from user import gif


def down_img(frame_number: int, id: str) -> str:

    retries: int = 0
    while retries < 3:
        response = httpx.get(f'{github_url}/frame_{frame_number}.jpg', timeout=7)

        if response.status_code == 200:
            file_path = f'images/frame_{frame_number}_{id}.jpg'
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
        
        else:
            retries += 1
            sleep(3)

def get_img(comments_list: list) -> str:

    for comment in comments_list:
        if not gif in comment['comment']:

            if 'frame_number' in comment:
                frame_number = comment['frame_number']
                id = comment['id']
                file_path = down_img(frame_number, id)
        
                if file_path:
                    comment['file_path'] = file_path
                else:
                    print(f'Error: Failed to download image for frame {frame_number}')
    

