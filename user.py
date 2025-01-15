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
    'https://tenor.com/u6VPyMH13as.gif',
    'https://tenor.com/musZYHpVfgn.gif',
    'https://tenor.com/mgwzEa6YgQd.gif',
    'https://tenor.com/GjSe2bu70C.gif',
    'https://tenor.com/p9S8RUtWayc.gif',
    'https://tenor.com/k9heYmpONyl.gif',
    'https://tenor.com/cmTOqfBJsdW.gif',
    'https://tenor.com/oeumqwaGvV0.gif',
    'https://tenor.com/gOOs9aQ8SQ1.gif',
    'https://tenor.com/c0xhpT2T2dv.gif',
    'https://tenor.com/kcDgh7yYa25.gif',
    'https://tenor.com/mEDW0Styr1l.gif',
    'https://tenor.com/dCvbROmddKF.gif',
    'https://tenor.com/dyJlcFZAC2T.gif',
    'https://tenor.com/qlMK4KL0vuw.gif',
    'https://tenor.com/t3vlQH3HtAQ.gif',
    'https://tenor.com/uZKVp9yMI7R.gif',
    'https://tenor.com/mKHxy599eY.gif',
    'https://tenor.com/kcpbzOjymxH.gif',
    'https://tenor.com/ojZPnfT2tD4.gif',
    'https://tenor.com/fvzLumsqN1Z.gif',
    'https://tenor.com/dXqc9lzHwgr.gif',
    'https://tenor.com/kQMiUhGFpwg.gif',
    'https://tenor.com/viT8CGWPKL6.gif',
    'https://tenor.com/v5YBcNIt76N.gif',
    'https://tenor.com/mMwDfZU2j6C.gif',
    'https://tenor.com/lqJebHu0uK0.gif',
    'https://tenor.com/obwbgCfagdb.gif',
    'https://tenor.com/vl0fgWe9qtr.gif',
    'https://tenor.com/bA76EF5Mdya.gif'
]
