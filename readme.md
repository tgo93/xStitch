# xStitch.py
---
Uses Python 3.6
Requires:
- Pillow (PIL) library
- Tkinter library
---
Program can be run with command 'python xStitch.py' while in correct directory ('python3 xStitch.py' on Linux)

Then, simply select an image, and xStitch will provide a list of each colour, along with it's percentage in overall colours
(Currently top ten colours, percentages shown are those of that top 10) - will be altered to display total percentage
---
Starting with one image (Moira pixel spray), and moving toward identifying many images
And listing the colours of string required to accompany a cross-stitch pattern

---

## Early steps

Take in an image file (think jpg or png) ~~~ DONE ~~~
Take in desired size (with some buffer around stitched image!!!) - hardcoded for Moira

VALIDATION TAKES PLACE
    Throw error message if not valid
    Continue otherwise

Check each pixel of image for colour
Determine each unique colour

Provide a percentage for each colour, matched with the colour code
~ Turn RGB triples into a hex code, and turn into dictionary with percentages

Serve a place to identify each colour

---

### TODO

- Develop a user interface for finding image, handing to program etc
- Provide link to website to identify colours and/or find strings
- Include support for coloured beads - essentially the same process with a different link

---

### Add Ons

Webtool that allows selection of missing colours from provided list
    This will allow user to select a color from the image, and be provided a colour code for additional colours

---