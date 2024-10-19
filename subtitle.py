import subprocess



def subtitle(found_comments: list) -> list:

    for comment in found_comments:

        if 'subtitle' in comment:
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
            
            gravity = '-gravity North'
            font =   '-font font/Cooper.otf'                     
            font_size = '-pointsize 100'                         
            backgound_color = '-background White'
            splice = f'-splice {backgound_size}'
            annotate = '-annotate +0+20'
            output_name = f'images/frame_{comment["frame_number"]}.jpg'
            
            subprocess.run(f'convert {comment["file_path"]} {gravity} {backgound_color} {splice} {font} {font_size} {annotate} "{subtitle}" {output_name}')
                            #magick for windows
                            #convert for linux
            
    return found_comments
