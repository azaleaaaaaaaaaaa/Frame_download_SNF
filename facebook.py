import httpx
import data
from time import sleep
import user


def upload_img(file_path: str): 
    retries = 0
    while retries < 3:
        try:
            # Verificar se o caminho fornecido está correto
            with open(f'{file_path}', 'rb') as frame:
                files = {'file': (file_path, frame, 'image/jpeg')}
                
                dados = {
                    'published': 'false',
                    'access_token': data.FB_TOKEN
                }
                response = httpx.post(f'{data.fb_url}/me/photos', files=files, data=dados, timeout=10)
                
                if response.status_code == 200:
                    foto_id = response.json().get('id')
                    if foto_id:
                        return foto_id
                else:
                    print(f'Erro ao fazer upload: {response.status_code}, {response.text}')
                    retries += 1
                    sleep(3)
            
        except Exception as e:
            print(f'Erro ao fazer upload: {e}')
            retries += 1
            sleep(3)    


def publish(foto_id: str, id_comentario: str, message: str):
    retries = 0
    while retries < 3:
        dados = {
            'message': message,
            'attachment_id': foto_id,
            'access_token': data.FB_TOKEN
        }
        response = httpx.post(f'{data.fb_url}/{id_comentario}/comments', data=dados, timeout=10)
        
        if response.status_code == 200:
            id = response.json().get('id')
            if id:
                return id
        else:
            print('erro ao enviar a imagem pro fb', response.status_code, response.text)
            retries += 1
            sleep(3)




def facebook_manager(found_comments):
    for comment in found_comments:
        if 'file_path' in comment and 'id' in comment and 'link' in comment:
            file_path = comment['file_path']
            id_comentarios = comment['id']
            link = comment['link']

            foto_id = upload_img(file_path)

            if foto_id:
                message = f'{user.message} {link}'
                response = publish(foto_id, id_comentarios, message)

                return response
    
    return None


