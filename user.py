# configuracoes do repositorio github para pegar os frames
REPO_OWNER: str =     'JavaRaf'
REPO: str =           'bot'
BRANCH: str =         'master'
FRAMES_FOLDER: str =  'frames'


# response messages
message_response_frame_download: str = 'Filename: Frame {FRAME}\n\nResolution: 1920x1080\nDownload Link: {LINK}'

message_response_gif_download: str = 'Filename: Animation\n\nFormat: GIF\nDownload Link: {LINK}'

message_response_helper: str = '\n\nCommands:\n\n\
"!dl" - Downloads the frame.\n\
    \t"!dl -f FRAME" - Downloads especified frame.\n\
    \t"!dl -t TEXT" - Adds text to the frame before generating the download link.\n\n\
"!gif" - Generates a GIF using the next 20 frames from the current frame.\n\n\
    \t"!gif -f FRAME" - Generates a GIF starting from frame especified.\n\n\
"!help" - Shows this message.\n\n\
    {LINK_GIF}.'




# commands
str_command_download: str =  '!dl'
str_command_gif: str =       '!gif'
str_command_help: str =      '!help'