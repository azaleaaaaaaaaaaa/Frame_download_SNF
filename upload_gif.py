import httpx
import os
import data



def upload_gif(file_path: str):
    if not file_path.endswith('.gif'):
        print("O arquivo precisa ser uma GIF.")
        return
    
    # Verifique se o caminho fornecido está correto
    try:
        with open(file_path, 'rb') as gif_file:
            files = {'file': gif_file}
            dados = {
                'api_key': data.GIPHY_API_KEY
            }
            response = httpx.post(data.giphy_url, files=files, data=dados, timeout=15)
            if response.status_code == 200:
                response_data = response.json()
                gif_id = response_data['data']['id']
                gif_url = f'https://giphy.com/gifs/{gif_id}'
                print(f'GIF enviado com sucesso! ID da GIF: {gif_url}')
                return gif_id
            else:
                print(f'Erro ao enviar a GIF: {response.status_code}, {response.text}')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')

