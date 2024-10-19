from imgBB import imgBB
from facebook import facebook_manager



def respond(found_comments: list):

    #mover o loop for pra ca
    found_comments = imgBB(found_comments)
    response_fb_id = facebook_manager(found_comments)

    if response_fb_id:
        with open('replyed_ids.txt', 'a', encoding='utf-8') as file:
            file.write(f'{response_fb_id}\n')

