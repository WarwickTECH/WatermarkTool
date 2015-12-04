from PIL import Image, ExifTags
from time import gmtime, strftime
import os, sys

path = "/Users/alex/Desktop/marked/"
dirs = os.listdir( path )
watermark = Image.open("warwick.png")
W1, H1 = watermark.size

def mark():
    counter = 0
    for item in dirs:
        if item.endswith('.jpg') or item.endswith('.png'):
            im = Image.open(path+item)
            try:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation]=='Orientation':
                        break
                exif=dict(im._getexif().items())
                if exif[orientation] == 3:
                    im=im.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    im=im.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    im=im.rotate(90, expand=True)
            except (AttributeError, KeyError, IndexError):
                pass
            f, e = os.path.splitext(path+item)
            W2, H2 = im.size
            im.paste(watermark, (0, H2-H1), watermark)
            current = strftime("%Y-%m-%d-", gmtime())
            im.save(path+current+str(counter)+'.png', 'PNG', quality=90)
            counter+=1
            if path+item != path+current+str(counter)+'.png':
                os.remove(path+item)
mark()
