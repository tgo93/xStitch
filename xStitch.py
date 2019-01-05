"""
xStitch.py - an image to Cross Stitch colour helper

"""

from tkinter import filedialog
import tkinter as tk
from PIL import Image

# Creates Tk object, and prompt to open an image file
# Needs validation for image files
root = tk.Tk()
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

# filters white from the list
w = False
for c in colorsForDict:
    if c[0] == 255 and c[1] == 255 and c[2] == 255:
        colorsForDict = colorsForDict[1:11]
        w = True
        break
    else:
        colorsForDict = colorsForDict[0:10]
        w = False

# find the percentage of each of top ten colours
colorPercents = []
count.sort(reverse=True)

if w == False:
    colorRange = count[0:10]
elif w == True:
    colorRange = count[1:11]

colorSum = sum(colorRange)
for c in colorRange:
    percentage = (c / colorSum) * 100
    percentage = round(percentage, 2)
    colorPercents.append(percentage)
colorPercents.sort(reverse=True)

# creates/prints a dictionary containing percentages and hex code for each colour
colorDict = dict(zip(colorPercents, colorsForDict))
for k, v in colorDict.items():
    print(k, end=': ')
    print('#{:02x}{:02x}{:02x}'.format(v[0], v[1], v[2]))
