import subprocess


def subtitle(comment_list: list) -> None:

    for comment in comment_list:
        if 'subtitle' in comment and 'file_path' in comment and 'frame_number' in comment:
            subtitle = comment['subtitle']

            partes = subtitle.split(' ')
            if len(partes) <= 5:
                backgound_size = '0x150'
            elif len(partes) <= 10:
                partes.insert(5, '\n')
                subtitle = ' '.join(partes)
                backgound_size = '0x280'
            elif len(partes) <= 15:
                partes.insert(5, '\n')
                partes.insert(10, '\n')
                subtitle = ' '.join(partes)
                backgound_size = '0x340'

            file_path = comment['file_path']
            gravity = '-gravity'
            gravity_value = 'North'
            font = '-font'
            font_path = 'font/Cooper.otf'
            font_size = '-pointsize'
            font_size_value = '100'
            backgound_color = '-background'
            backgound_color_value = 'White'
            splice = '-splice'
            splice_value = backgound_size
            annotate = '-annotate'
            annotate_position = '+0+20'
            output_name = f'images/frame_{comment["frame_number"]}_{comment["id"]}.jpg'

            # Criação da lista de comandos
            command = [
                'convert',  # Ou 'magick' se estiver usando no Windows
                file_path,
                gravity, gravity_value,
                backgound_color, backgound_color_value,
                splice, splice_value,
                font, font_path,
                font_size, font_size_value,
                annotate, annotate_position,
                subtitle,
                output_name
            ]

            try:
                # Executa o comando
                subprocess.run(command, check=True)
                comment['file_path'] = output_name
            except subprocess.CalledProcessError as e:
                print(f"Ocorreu um erro ao executar o comando: {e}")

