import httpx
import asyncio
import os
from data import github_url
import subprocess

# Função para baixar uma única imagem
async def get_img(session: httpx.AsyncClient, frame_number: int, id: str) -> str:
    try:
        response = await session.get(f'{github_url}/frame_{frame_number}.jpg')

        if response.status_code == 200:
            file_path = f'images/gif_{id}/frame_{frame_number}.jpg'
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Cria diretórios se não existirem
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path  # Retorna o caminho do arquivo salvo
        else:
            return f"Failed to download frame {frame_number}: Status {response.status_code}"
    except Exception as e:
        return f"Error downloading frame {frame_number}: {str(e)}"


# Função principal para gerar o gif
async def fetch_frames(comment: dict) -> None:
    print("make_gif chamado")  # Verifica se a função foi chamada
    async with httpx.AsyncClient() as session:
        tasks = []
        start_frame = int(comment['frame_number'])
        end_frame = start_frame + 20

        for frame_number in range(start_frame, end_frame):
            print(f"Baixando frame {frame_number}")  # Debug para acompanhar downloads
            tasks.append(get_img(session, frame_number, comment['id']))

        results = await asyncio.gather(*tasks)



        comment['file_path'] = f'images/gif_{comment["id"]}'

def montar_gif(comment: dict):
    if 'file_path' in comment:
        commands = [
            'magick',
            '-delay','40',
            '-loop', '0',
            'images/gif_'+comment["id"]+'/frame*.jpg',
            '-colors', '128',
            '-fuzz', '10%',
            '-layers', 'optimize',
            f'{comment["file_path"]}/animation.gif',
        ]
        try:
            subprocess.run(commands, check=True)
            print('GIF criado com sucesso')
            comment['file_path'] += '/animation.gif'
        except subprocess.CalledProcessError as e:
            print(f'Erro ao criar o GIF: {e}')


def call_make_gif(comment: dict):
    asyncio.run(fetch_frames(comment))
    montar_gif(comment)







