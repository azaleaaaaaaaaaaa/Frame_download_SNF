from imgBB import imgBB
from facebook import facebook_manager



def respond(found_comments: list):
    found_comments = imgBB(found_comments)
    response = facebook_manager(found_comments)

    if response:
        print(f'respondido com sucesso {response}')


