import page_id
from get_img import get_img
from comments import get_comments
from finder import finder
from subtitle import subtitle
from respond import respond




def main():
    #obtem o ID da página do Facebook
    page_id.get_id()
    #busca comentarios relacionados à página
    comments_list = get_comments()
    # busca comentários
    found_comments = finder(comments_list)
    # obtem imagens relacionadas aos comentários
    found_comments = get_img(found_comments)
    #legendar as imagens
    found_comments = subtitle(found_comments)

    #responder aos comentários
    respond(found_comments)





if __name__ == '__main__':
    main()


