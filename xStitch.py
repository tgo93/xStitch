"""
xStitch.py - an image to Cross Stitch colour helper, so Kendra can make overwatch sprays, basically :)
Travis O'Brien
"""

from tkinter import filedialog
from tkinter import *
from PIL import Image

# Creates Tk object, and prompt to open an image file
# Needs validation for image files
root = Tk()
root.file = filedialog.askopenfile(parent=root, mode='rb', title="choose an image")
openFile = Image.open(root.file)
openFileRGB = openFile.convert("RGB")

colors = openFileRGB.getcolors(openFileRGB.size[0]*openFileRGB.size[1])  # list of tuples, count of each color
count = []  # list of the count of colours
for i in range(len(colors)):
    new = list(colors[i])
    count.append(new[0])

# find the percentage of each of top ten colours
colorPercents = []
count.sort()
colorRange = count[-11:-1]

colorSum = sum(colorRange)
for c in colorRange:
    percentage = (c / colorSum) * 100
    colorPercents.append(percentage)

print(colorPercents)
