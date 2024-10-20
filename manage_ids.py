




def save_id(comment: dict) -> None:
    with open('replyed_ids.txt', 'a', encoding='utf-8') as file:
        file.write(f'{comment["id"]}\n')



def remove_replyed_ids(comments_list: list) -> None:

    replyed_ids = []
    try:
        with open('replyed_ids.txt', 'r', encoding='utf-8') as file:
            replyed_ids = file.read().splitlines()
            
            for comment in reversed(comments_list): 
                if comment['id'] in replyed_ids:
                    comments_list.remove(comment)
    
    except FileNotFoundError:
        with open('replyed_ids.txt', 'w', encoding='utf-8') as file:
            print("Arquivo replyed_ids.txt não encontrado\ncriando um")
            return
        

