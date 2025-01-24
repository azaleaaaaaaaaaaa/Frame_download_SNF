# information to find the frames
REPO_OWNER: str =     'azaleaaaaaaaaaaa' # your github username
REPO: str =           'makeinee2' # repository where frames are saved
BRANCH: str =         'master' # branch where frames are saved
FRAMES_FOLDER: str =  'frames' # directory where frames are saved


# response messages
message_response_frame_download: str = 'Filename: Frame {FRAME}\n\nResolution: 1920x1080\nDownload Link: {LINK}'

message_response_gif_download: str = 'Filename: Animation\n\nFormat: GIF\nDownload Link: {LINK}'

# resposta ao pedido de download 
message_response_helper: str = (
    "\n\n"
    "!dl - Download current frame.\n"
    "\t!dl -f FRAME - Download specified frame.\n"
    "\t!dl -t TEXT - Add text to frame before download.\n\n"
    "!gif - Create GIF from next 30 frames.\n"
    "\t!gif -f FRAME - Create GIF from specified frame.\n\n"
    "!help - Show this message.\n\n"
    "{LINK_GIF}."
)


# commands
str_command_download: str =  '!dl'
str_command_gif: str =       '!gif'
str_command_help: str =      '!help'


# frieren anime gifs link, these gifs are used together with the !help command. Change them to your links
gif_links = [
    
]
