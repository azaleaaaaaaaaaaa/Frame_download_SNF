from imgBB import imgBB
from facebook import facebook_manager, publish
from manage_ids import save_id
from user import gif
from upload_gif import upload_gif



def respond(found_comments: list):

    for comment in found_comments:

        if 'file_path' in comment and 'frame_number' in comment:
            imgBB(comment)
            facebook_manager(comment)

            if comment['response_id']:
                save_id(comment) # salva o id do comentario respondido

        elif gif in comment['comment']:
            comment['link'] = upload_gif(comment['file_path'])
            publish(foto_id='', id_comentarios=comment['id'], message=f'{comment['link']}') 



