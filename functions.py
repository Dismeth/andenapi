import os
from PIL import Image
import glob

def welcome_screen():
    "Help message"
    print('Combine bmp')
    print('use -h for help')


def message(messageID):
    "Put all the error messages in the same place"
    message = dict(quit='Thanks for joining', invalid_path='Invalid path, please specify path')
    if messageID in message:
        return message[messageID]
    else:
        return 'Error: message not found'


def help_screen():
    "Help message"
    print('/////////////////')
    print('To load:')
    print('   load $path')
    print('Example: load c:\stash\ ')


def menu():
    "Create menu etc"
    menu_items = dict(help=1, h=1, quit=99, exit=99, q=99, load=2, l=2, quickload=3, ql=3)
    return menu_items


def find_images(path, file_extension):
    try:
        file_extension
    except NameError:
        file_extension = 'bmp'
    try:
        path
    except NameError:
        path = './'

    images = glob.glob(path + '*.' + file_extension)
    return images

def create_new_image(images):
    result = Image.new("RGB", (1920, 1080))

    for index, file in enumerate(images):
        path = os.path.expanduser(file)
        img = Image.open(path)
        img.thumbnail((64, 64), Image.ANTIALIAS) # 1080 y
        x_2 = 1920 // 64
        y_2 = 18
        x = index // x_2 * 64
        y = index % y_2 * 64
        w, h = img.size
        print('pos {0},{1} size {2},{3} index {4}'.format(x, y, w, h,index))
        result.paste(img, (x, y, x + w, y + h))

    result.save(os.path.expanduser('C:\\0Utvikling\\image.jpg'))