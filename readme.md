# xStitch.py

Starting with one image (Moira pixel spray), and moving toward identifying many images
And listing the colours of string required to accompany a cross-stitch pattern

This project will required Pillow (image library) and eventually tkinter (for user interface) - more research
Build from bottom up

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

root.filename = filedialog.askopenfilename(initialdir="/", title="Select image", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

---