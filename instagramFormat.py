# Python program to change the aspect ratio and resolution of image as per instagram doc
# https://help.instagram.com/1631821640426723

from PIL import Image
import os

# Taking image as input
path = "E:\\images\\"
dir_list = os.listdir(path)


for file in dir_list:
    img = Image.open(path + file)

    # Getting height and width of the image
    width = img.size[0]
    height = img.size[1]
    ar = width / height

    if(ar>0.8 and ar<1.9): 
        # resize 
        width = 1080 
        height = int(width // ar)
        final = img.resize((width, height), Image.Resampling.LANCZOS)
                 
    else:
        
        if(ar>1.9): 
            # resize and modify width
            height = 1350
            width = int(height * ar)
            resized = img.resize((width, height), Image.Resampling.LANCZOS)

            newAR = 1.9
            newwidth = height * newAR
            # crop
            left = (width - newwidth) // 2
            right = left + newwidth - 1
            final = resized.crop((left, 0, right, height))

        else: 
            # resize and modify height
            width = 1080 
            height = int(width // ar)
            resized = img.resize((width, height), Image.Resampling.LANCZOS)

            newAR = 0.8
            newheight = int(width // newAR)
            # crop
            upper = (height - newheight) // 2
            lower = upper + newheight - 1
            final = resized.crop((0, upper, width, lower))
    
    final.save(file)
    print("done " + file )

f.close()

