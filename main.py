from page_id import get_id 
from comments import get_comments
from get_img import get_img
from finder import finder_commands
from responses import response
from save_ids import remove_replyed_ids
import time
import os 



def main():

    get_id()
    if os.environ.get('PAGE_ID') == None:
        print('Failed to get page id: No page ID found or wrong page ID')
        os.sys.exit(1)
    
    comments_list: list[dict] = get_comments()
    remove_replyed_ids(comments_list)


    for comment in comments_list:
        finder_commands(comment)
        get_img(comment)
        response(comment)
        
        

if __name__ == '__main__':
    start: float = time.time()
    while (time.time() - start) < (180 * 60):  # 3 hours
        main()
        time.sleep(50)
        print('Sleeping for 50 seconds...\n')