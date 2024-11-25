
Setup: Define the following tokens before running the application:

FB_TOKEN: Facebook token (required).
IMG_TOKEN: Imgbb token (required).
GIPHY_API_KEY: Giphy API key (optional).
Commands:

Command: !dl
Description: Generates a download link for a specific frame.
Options:

-f: Specify the frame number to download.
-t: Add custom text to the frame before generating the link.
Example Usage:
!dl -f 15 -t "Custom Text": Downloads frame 15 with the text "Custom Text" added.
Command: !gif
Description: Creates a GIF using 20 frames starting from a specified frame.
Options:

-f: Define the starting frame for the GIF.
Example Usage:
!gif -f 10: Creates a GIF starting from frame 10.
