from rembg import remove
import PIL
from PIL import Image
import os
import glob
import pathlib
import filetype

Image.MAX_IMAGE_PIXELS = 211680000
mywidth = 1024*2
dir_path = r'./input'

#for file in glob.glob(dir_path+"*.jpg"):
for root, dirs, files in os.walk(dir_path, topdown=False):
 for name in files:
### check is image file
  if filetype.is_image(os.path.join(root, name)):
    print(os.path.join(root, name) + ' ==> \n')
    output_png = 'out/'+pathlib.Path(name).stem + '.png'
    output_jpg = 'out/'+pathlib.Path(name).stem + '.jpg'
    output_resize = 'out_r/'+name
    img = Image.open(os.path.join(root, name))
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.Resampling.LANCZOS)
#    img.save(output_resize)
#    os.system(" backgroundremover -i " + output_resize + " -o " + output_path)
    img = img.convert('RGB')

# Removing the background from the given Image
    output = remove(img)

#Saving the image in the given path
#output.save(output_png)
    print('Add BG White '+output_jpg+'\n')
    im=output
    fill_color = (255,255,255)  # your new background color

    im = output.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
    im.convert("RGB").save(output_jpg)