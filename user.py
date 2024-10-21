# configuracoes do repositorio github para pegar os frames
REPO_OWNER: str =     'JavaRaf'
REPO: str =           'bot'
BRANCH: str =         'master'
FRAMES_FOLDER: str =  'frames'


# message apresentada junto a image de resposta
message_response_frame_download: str = 'Filename: Frame {FRAME}\n\nResolution: 1920x1080\nLink: {LINK}'
message_response_gif_download: str = 'Filename: Animation\n\nFormat: GIF\nLink: {LINK}'



# commands
str_command_download: str =  '!dl'
str_command_gif: str =       '!gif'
str_command_help: str =      '!help'