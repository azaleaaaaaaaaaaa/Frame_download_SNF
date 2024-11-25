
FB_TOKEN = 'token do fb'  # required
IMG_TOKEN = 'token da imgbb'  # required
GIPHY_API_KEY = 'token da giphy' # optional


Command: !dl
Description: Returns the download link for the specified frame.

Options:
-f: Specifies the frame number you want to download.
-t: Adds text to the frame before generating the download link.
Command: !gif
Description: Creates a GIF using the next 20 frames from the current frame of the post.

Options:
-f: Defines the starting frame for generating the GIF.
Example Usage:
!dl -f 15 -t "Custom Text": Downloads frame 15 with the text "Custom Text" added.
!gif -f 10: Creates a GIF starting from frame 10.
