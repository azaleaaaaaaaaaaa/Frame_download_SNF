from imgBB import imgBB
from facebook import facebook_manager
from manage_ids import save_id



def respond(found_comments: list):

    for comment in found_comments:

        if 'file_path' in comment and 'frame_number' in comment:
            imgBB(comment)
            facebook_manager(comment)

            if comment['response_id']:
                save_id(comment) # salva o id do comentario respondido


