import data
import httpx
from time import sleep


def send_img(file_path: str, name: str) -> str:
    retries = 0
    while retries < 3:
        try:
            dados = {'key': data.IMG_TOKEN, 'name': f'{name}', 'expiration': 600000}

            with open(file_path, 'rb') as file:
                files = {'image': file}
                
                response = httpx.post(data.img_url, data=dados, files=files, timeout=10)
                if response.status_code == 200:
                    response_data = response.json()
                    link = response_data['data']['url']
                    
                    if link:
                        return link   
                else:
                    print('erro no imgbb', response.status_code)
                    print(response.text)
                    sleep(5)
                    retries += 1
                    
        except FileNotFoundError:
            print(f"O arquivo {file_path} não foi encontrado.")


def imgBB(found_comments: list) -> list:
    for comment in found_comments:
        if 'file_path' in comment and 'frame_number' in comment:
            file_path = comment['file_path']
            frame_number = comment['frame_number']
            link = send_img(file_path, frame_number)

            if link:
                comment['link'] = link
    
    return found_comments
    
 
