import subprocess
import httpx
import data
import os
import glob

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
            response = httpx.post(data.giphy_url, files=files, data=dados, timeout=20)
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
    if data.GIPHY_API_KEY and comment.get('file_path', None):
        file_path = comment.get('file_path')
        if file_path:
            # Define comandos de acordo com o sistema operacional
            image_magick_command = 'magick' if os.name == 'nt' else 'convert'
            resize_image_command_base = ['magick', 'mogrify'] if os.name == 'nt' else ['mogrify']

            # Obtém todos os arquivos de imagem .jpg no diretório
            image_files = glob.glob(f'{file_path}/frame*.jpg')

            if image_files:
                # Comando para redimensionar as imagens
                resize_image_command = resize_image_command_base + ['-resize', '90%'] + image_files

                try:
                    subprocess.run(resize_image_command, check=True)
                    print("Imagens redimensionadas com sucesso!")
                except subprocess.CalledProcessError as e:
                    print(f'Erro ao redimensionar as imagens: {e}')

            # Comando para criar o GIF
            commands = [
                image_magick_command,
                '-delay', '30',
                '-loop', '0',
                f'{file_path}/frame*.jpg',
                '-colors', '32',
                '-layers', 'optimize',
                f'{file_path}/animation.gif',
            ]

            try:
                subprocess.run(commands, check=True)
                comment['file_path'] = f'{file_path}/animation.gif'
                print("GIF criado com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f'Erro ao criar o GIF: {e}')

            # Função de upload do GIF
            upload_gif(comment)

