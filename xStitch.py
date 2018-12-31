"""
xStitch.py - an image to Cross Stitch colour helper

"""

from tkinter import filedialog
from tkinter import *
from PIL import Image

# Creates Tk object, and prompt to open an image file
# Needs validation for image files
root = Tk()
root.file = filedialog.askopenfile(parent=root, mode='rb', title="Choose Image")
openFile = Image.open(root.file)
openFileRGB = openFile.convert("RGB")

# list of tuples, count of each color
colors = openFileRGB.getcolors(openFileRGB.size[0]*openFileRGB.size[1])  
count = []  # list of the count of colours
colorsForDict = []
for i in range(len(colors)):
    new = list(colors[i])
    count.append(new[0])
    colorsForDict.append(new[1])

colorsForDict = colorsForDict[-11:-1]

# find the percentage of each of top ten colours
colorPercents = []
count.sort()
colorRange = count[-11:-1]

colorSum = sum(colorRange)
for c in colorRange:
    percentage = (c / colorSum) * 100
    percentage = round(percentage, 2)
    colorPercents.append(percentage)

# creates/prints a dictionary containing percentages and hex code for each colour
colorDict = dict(zip(colorPercents, colorsForDict))
for k, v in colorDict.items():
    print(k, end=': ')
    print('#{:02x}{:02x}{:02x}'.format(v[0], v[1], v[2]))
