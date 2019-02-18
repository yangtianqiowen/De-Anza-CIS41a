'''
Tianqi Yang
Lab3
'''
from ezgraphics import GraphicsImage, GraphicsWindow
from math import sqrt

filename = "jellyfish.gif"
#load the orignal Image
origImage = GraphicsImage(filename)
# Create an empty image that will contain the new flipped image.
width = origImage.width()
height = origImage.height()
newImage = GraphicsImage(width, height)
#locate the center of the new image
if width > height:
    radius = height // 2 
else: 
    radius = width // 2 
#set up the effect color to white(255,255,255)
newRed=255
newBlue=255
newGreen=255
# newRow is row number of new image
newRow = 0
for row in range(height):     #go through every row
    # outer loop is top-down
    for col in range(width):         #go through column
    #inner loop is left-to-right
        newCol = col
        if sqrt((width/2-col)**2+(height/2-row)**2) <= radius:   
            green = int(0.7152*origImage.getGreen(row,col))
            red = int(0.2126*origImage.getRed(row,col))
            blue = int(0.0722*origImage.getBlue(row,col) )  
            gray = green + red + blue
            newImage.setPixel(newRow, newCol, gray, gray, gray)  #paste to new image
        else :
            newImage.setPixel(newRow, newCol, newRed, newGreen, newBlue)  # paste to new image
    newRow = newRow + 1
# Save the new image with "Black".
newImage.save("black-" + filename)

# Draw the telescoped image
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newImage)
win.wait()