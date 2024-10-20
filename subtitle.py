import os
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing

def subtitle(comments_list: list) -> list:
    for comment in comments_list:
        if 'subtitle' in comment and 'file_path' in comment and 'frame_number' in comment:
            subtitle = comment['subtitle']
            partes = subtitle.split(' ')

            # Definindo o tamanho do fundo com base no número de partes
            if len(partes) <= 5:
                background_size = (0, 150)
            elif len(partes) <= 10:
                partes.insert(5, '\n')
                subtitle = ' '.join(partes)
                background_size = (0, 280)
            elif len(partes) <= 15:
                partes.insert(5, '\n')
                partes.insert(10, '\n')
                subtitle = ' '.join(partes)
                background_size = (0, 340)

            file_path = comment['file_path']
            output_name = f'./images/frame_{comment["frame_number"]}_{comment["id"]}.jpg'

            # Verificar se o arquivo existe
            if not os.path.exists(file_path):
                print(f"Arquivo não encontrado: {file_path}")
                continue  # Pula para o próximo comentário

            # Abrir a imagem original
            with Image(filename=file_path) as img:
                # Criar um fundo para o texto
                with Image(width=img.width, height=background_size[1], background=Color('white')) as background:
                    # Compor o fundo e a imagem original
                    img.composite(background, 0, 0)  # Colocar o fundo na parte superior

                    # Desenhar o texto na imagem
                    with Drawing() as draw:
                        draw.font = 'font/Cooper.otf'
                        draw.font_size = 100
                        draw.fill_color = Color('black')

                        # Configurar gravity para centralizar o texto na parte superior
                        img.gravity = 'north'  # Define a gravidade para a parte superior
                        draw.text(0, 20, subtitle)  # Posição do texto (x, y)
                        draw(img)

                    # Salvar a imagem resultante
                    img.save(filename=output_name)

            comment['file_path'] = output_name

    return comments_list
