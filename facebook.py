import httpx
import data
from time import sleep
import user
import os


def upload_img(file_path: str): 
    retries = 0
    while retries < 3:
        try:
            # Verifica a extensão do arquivo para definir o tipo MIME e o endpoint correto
            if file_path.endswith('.jpg'):
                mimetype = 'image/jpeg'
                endpoint = f'{data.fb_url}/me/photos'
            
            # Verificar se o caminho fornecido está correto
            with open(file_path, 'rb') as frame:
                files = {'file': (os.path.basename(file_path), frame, mimetype)}
                
                dados = {
                    'published': 'false',
                    'access_token': data.FB_TOKEN  # Use o FB_TOKEN diretamente
                }
                response = httpx.post(endpoint, files=files, data=dados, timeout=15)
                
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
            print('erro ao postar a imagem pro fb', response.status_code, response.text)
            retries += 1
            sleep(3)



def facebook_manager(comment: dict) -> None:

    if 'file_path' in comment and 'id' in comment and 'link' in comment:
        file_path = comment['file_path']
        id_comentarios = comment['id']
        link = comment['link']

        foto_id = upload_img(file_path)

        if foto_id:
            message = f'{user.message.format(EP=comment["episode"], FRAME=comment["frame_number"], LINK=link)}'
            response = publish(foto_id, id_comentarios, message)

            if response:
                comment['response_id'] = response




