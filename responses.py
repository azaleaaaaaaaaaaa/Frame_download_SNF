import user
from make_gif import make_gif
from imgBB import imgBB
from facebook import post_fb, publish_fb
from save_ids import save_id







def response(comment: dict) -> None:

    if 'file_path' in comment and 'id' in comment:

        if user.str_command_gif in comment['comment']:
            make_gif(comment)
        
        if user.str_command_download in comment['comment']:
            imgBB(comment)
        

        post_fb(comment)
        publish_fb(comment)
        save_id(comment)

