# configuracoes do repositorio github para pegar os frames
REPO_OWNER: str =     'JavaRaf'
REPO: str =           'bot'
BRANCH: str =         'master'
FRAMES_FOLDER: str =  'frames'


# response messages
message_response_frame_download: str = 'Filename: Frame {FRAME}\n\nResolution: 1920x1080\nDownload Link: {LINK}'

message_response_gif_download: str = 'Filename: Animation\n\nFormat: GIF\nDownload Link: {LINK}'

message_response_helper: str = '\n\nCommands:\n- `!dl` to download the frame in post. Use `-f` to specify the frame number.\n\
- `!gif` to create a GIF with the next 20 frames.\n\
- `!help` to view the list of available commands.\n\n{LINK}'




# commands
str_command_download: str =  '!dl'
str_command_gif: str =       '!gif'
str_command_help: str =      '!help'