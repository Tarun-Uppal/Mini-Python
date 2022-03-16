from PIL import Image

def newImg():
    r = 0
    g = 0
    b = 0
    
    x = 500
    y = 500
    img = Image.new('RGB', (x, y))
    for i in range(x):
        for j in range(y):
            img.putpixel((i,j), (r,g,b))
        if (r<255):
            r+=1
        elif(g<255):
            g+=1
        else:
            b+=1
						
     
    img.save('F:\Mini-Python\colour_detection\sqr.png')

    return img

wallpaper = newImg()
wallpaper.show()
