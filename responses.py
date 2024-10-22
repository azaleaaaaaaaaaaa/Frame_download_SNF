import user
from make_gif import make_gif
from imgBB import imgBB
from facebook import post_fb, publish_fb
from save_ids import save_id
from subtitle import subtitle



def response(comment: dict) -> None:

    if (comment.get('file_path') and comment.get('id')) or (comment.get('message') == user.str_command_help.lower() and comment['file_path']) != None:

        if user.str_command_gif.lower() in comment.get('comment', '').lower():
            make_gif(comment)
        
        if user.str_command_download.lower() in comment.get('comment', '').lower():
            subtitle(comment)
            imgBB(comment)
        
        
        post_fb(comment)
        publish_fb(comment)
        save_id(comment)

