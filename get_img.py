import httpx
import asyncio
import os
import data
import user

def get_one_img(comment: dict) -> None:
    response = httpx.get(f'{data.github_url}/frame_{comment["frame_number"]}.jpg', timeout=20)

    if response.status_code == 200:
        file_path = f'images/{comment["id"]}/frame_{comment["frame_number"]}.jpg'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            file.write(response.content)
            comment['file_path'] = file_path
    else:
        comment['file_path'] = ''
        comment['id'] = ''




async def get_manys_img(session: httpx.AsyncClient, frame_number: str, id: str) -> None:
    try:
        response = await session.get(f'{data.github_url}/frame_{frame_number}.jpg', timeout=15)

        if response.status_code == 200:
            file_path = os.path.join(f'images/{id}/frame_{frame_number}.jpg')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return f'images/{id}'
        else:
            return f"Failed to download frame {frame_number}: Status {response.status_code}"

    except Exception as e:
        return f"Error downloading frame {frame_number}: {str(e)}"


# Função principal para gerar o gif
async def img_fetch(comment: dict) -> None:

    if user.str_command_download in comment.get('comment'):
        get_one_img(comment)

    elif user.str_command_gif in comment['comment']:
        async with httpx.AsyncClient() as session:
            tasks = []
            start_frame = int(comment['frame_number'])
            end_frame = start_frame + 20

            for frame_number in range(start_frame, end_frame):
                tasks.append(get_manys_img(session, frame_number, comment['id']))

            file_paths = await asyncio.gather(*tasks)
            
            if file_paths == ['Failed to download frame 0: Status 404']:
                comment['file_path'] = ''
                comment['id'] = ''
            else:
                comment['file_path'] = file_paths[0]



def get_img(comment: dict) -> None:
    if comment.get('comment') and comment.get('id') and comment.get('frame_number'):
        asyncio.run(img_fetch(comment))



    