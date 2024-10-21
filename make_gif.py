import subprocess
import httpx
import data

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
                link = f'https://giphy.com/gifs/{response_data["data"]["id"]}'
                comment['link'] = link
                print(f'GIF enviado com sucesso! ID da GIF: {link}')

            else:
                print(f'Erro ao enviar a GIF: {response.status_code}, {response.text}')
    except Exception as e:
        print(f'Erro ao abrir o arquivo: {e}')


def make_gif(comment: dict) -> None:
    if 'file_path' in comment:
        commands = [
            'magick',
            '-delay','20',
            '-loop', '0',
            f'{comment["file_path"]}/frame*.jpg',
            '-colors', '128',
            '-fuzz', '10%',
            '-layers', 'optimize',
            f'{comment["file_path"]}/animation.gif',
        ]
        try:
            subprocess.run(commands, check=True)
            comment['file_path'] += '/animation.gif'
            print('GIF criado com sucesso')
        except subprocess.CalledProcessError as e:
            print(f'Erro ao criar o GIF: {e}')
    
    upload_gif(comment)

