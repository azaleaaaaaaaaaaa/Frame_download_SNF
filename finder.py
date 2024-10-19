from user import download, help
import re

def remove_replyed_ids(comments_list: list) -> list:
    with open('replyed_ids.txt', 'r', encoding='utf-8') as file:
        replyed_ids = file.read().splitlines()
        
    for comment in comments_list:
        if comment['id'] in replyed_ids:
            comments_list.remove(comment)
    
    return comments_list



def get_frame(comment: dict) -> dict:   
    
    number = re.findall(r'-\s*f\s*(\d+)', comment['comment'])
    if number:
        frame_number = number[0]
        comment['frame_number'] = frame_number
    
    return comment

def get_subtitle(comment: dict) -> str:
    subtitle = re.findall(r'-t\s*(.*)', comment['comment'])
    if subtitle:
        comment['subtitle'] = subtitle[0]

    return comment



def finder(comments_list: list) -> list:
    found_comments: list = []

    comments_list = remove_replyed_ids(comments_list)

    for comment in comments_list:

        if download in comment['comment']:
            comment = get_subtitle(comment)
            comment = get_frame(comment)
            found_comments.append(comment)
        


            

    return found_comments
        
    


            


