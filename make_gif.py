import subprocess
import httpx
import data
import os

def upload_gif(comment: dict):
    if not comment['file_path'].endswith('.gif'):
        print("O arquivo precisa ser uma GIF.")
        return
    
    # Verifique se o caminho fornecido está correto
    try:
        with open(comment['file_path'], 'rb') as gif_file:
            files = {'file': gif_file}
            dados = {
                'api_key': data.GIPHY_API_KEY
            }
            response = httpx.post(data.giphy_url, files=files, data=dados, timeout=15)
            if response.status_code == 200:
                response_data = response.json()
                link = 'https://giphy.com/gifs/' + response_data.get("data", {}).get("id", '')
                comment['link'] = link
                print(f'GIF criada com sucesso: {link}')

            else:
                print(f'Erro ao enviar a GIF: {response.status_code}, {response.text}')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')


def make_gif(comment: dict) -> None:

    if data.GIPHY_API_KEY and comment.get('file_path'):
        file_path = comment.get('file_path')
        if file_path:
            image_magick_command = 'magick' if os.name == 'nt' else 'convert'
            commands = [
                image_magick_command,
                '-delay', '30',
                '-loop', '0',
                f'{file_path}/frame*.jpg',
                '-colors', '32',
                '-fuzz', '10%',
                '-layers', 'optimize',
                f'{file_path}/animation.gif',
            ]

            try:
                subprocess.run(commands, check=True)
                comment['file_path'] = f'{file_path}/animation.gif'
            except subprocess.CalledProcessError as e:
                print(f'Erro ao criar o GIF: {e}')

            upload_gif(comment)

