from page_id import get_id
from get_img import get_img
from comments import get_comments
from finder import finder
from subtitle import subtitle
from respond import respond
from time import time, sleep
import os, sys


def main():
    #obtem o ID da página do Facebook
    get_id()
    #busca comentarios relacionados à página
    comments_list: list = get_comments()
    # busca comentários
    finder(comments_list)
    # obtem imagens relacionadas aos comentários
    get_img(comments_list)
    #legendar as imagens
    subtitle(comments_list)

    #responder aos comentários
    respond(comments_list)

    print('Finished!')




if __name__ == '__main__':
    start: float = time()
    while (time() - start) < (180 * 60):  # 3 hours
        main()
        sleep(50)


