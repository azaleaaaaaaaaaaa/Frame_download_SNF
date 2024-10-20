import subprocess



def subtitle(comments_list: list) -> list:

    for comment in comments_list:

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
            

            file_path = f'{comment['file_path']}'
            gravity = '-gravity North'
            font =   '-font font/Cooper.otf'                     
            font_size = '-pointsize 100'                         
            backgound_color = '-background White'
            splice = f'-splice {backgound_size}'
            annotate = '-annotate +0+20'
            output_name = f'images/frame_{comment["frame_number"]}_{comment["id"]}.jpg'
                            #magick for windows
                            #convert for linux
            subprocess.run(f'convert {file_path} {gravity} {backgound_color} {splice} {font} {font_size} {annotate} "{subtitle}" {output_name}')
            comment['file_path'] = output_name



# comments_list = [
#     {'file_path': 'images/frame_1.jpg', 'frame_number': '1', 'comment': '-t "Subtitulo 1"', 'subtitle': 'Subtitulo 1'},
# ]
# subtitle(comments_list)
