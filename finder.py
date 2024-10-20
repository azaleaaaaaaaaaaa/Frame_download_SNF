from user import download, help
from data import fb_url, FB_TOKEN
from manage_ids import remove_replyed_ids
from os import environ
from time import sleep
import httpx
import re




def get_post_title(comment: dict) -> dict:
    post_id = f'{environ.get("PAGE_ID")}_{comment["id"].split("_")[0]}'
    retries = 0
    
    while retries < 3:
        try:
            response = httpx.get(f'{fb_url}/{post_id}', params={'access_token': FB_TOKEN}, timeout=5)
            
            if response.status_code == 200:
                response_data = response.json()
                
                if 'message' in response_data:
                    number = re.findall(r'Frame\s*(\d+)', response_data['message'])
                    ep_number = re.findall(r'Episode\s*(\d+)', response_data['message'])
                    
                    if number:
                        comment['frame_number'] = number[0]

                    
                    if ep_number:
                        comment['episode'] = ep_number[0]  # Acessar o primeiro elemento
                    
                    break  # Certifique-se de que o break está aqui

        except httpx.RequestError as e:
            print(f"Request error: {e}. Retrying ({retries + 1}/3)...")
        
        retries += 1
        sleep(3)
    

def get_frame(comment: dict) -> None:   
    frame_number = re.findall(r'-\s*f\s*(\d+)', comment['comment'])
    
    
    if not frame_number:
        get_post_title(comment)
    
    else:
        comment['frame_number'] = frame_number[0].lstrip('0')
        comment['episode'] = 'this_episode'

        

def get_subtitle(comment: dict) -> str:
    subtitle = re.findall(r'-t\s*(.*)', comment['comment'])
    if subtitle:
        comment['subtitle'] = subtitle[0]


def finder(comments_list: list) -> None:

    remove_replyed_ids(comments_list)

    for comment in comments_list:
        if download in comment['comment']:
            get_subtitle(comment)
            get_frame(comment)
        
        else:
            comments_list.remove(comment)
        
        
    


            


