import random


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

def get_link() -> str:
    return random.choice(gif_links)





def helper(comment: dict) -> None:
    if 'comment' in comment and 'id' in comment:
        comment['file_path'] = 'animation.gif'
        comment['link'] = get_link()
        comment['message'] = 'Helper'
