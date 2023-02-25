import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import *
from PIL import Image, ImageTk
import os

# Create a window
window = tk.Tk()

# Set the title of the window
window.title("Image Compression using Tkinter Library in Python")

# Create two empty boxes with black borders to display images
image_box1 = tk.Label(window, width=40, height=20, bg="white", bd=2, relief="solid")
image_box2 = tk.Label(window, width=40, height=20, bg="white", bd=2, relief="solid")


compressed = None
# Create a button to choose an image
def choose_image():
    # Open a file dialog to choose an image file
    file_path = filedialog.askopenfilename()
    # Load the chosen image and resize it to fit the image box
    imageOriginal = Image.open(file_path)

    myheight, mywidth = imageOriginal.size
    image = imageOriginal.resize((myheight,mywidth),Image.LANCZOS)
    global compressed 
    compressed = image

    image = imageOriginal
    
    # Convert the image to Tk format and display it in the image box
    image = image.resize((int(myheight/10),int(mywidth/10)),Image.LANCZOS)
    image_box1.config(width=int(mywidth/10)+150, height=int(myheight/10)-50)
    image_box2.config(width=int(mywidth/10)+150, height=int(myheight/10)-50)
    

    photo = ImageTk.PhotoImage(image)
    globalPhoto = photo
    image_box1.configure(image=photo)
    image_box1.image = photo

    image_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    print("Image size Before Compression: {:.2f} MB".format(image_size_mb))

    image_box2.configure(image=globalPhoto)
    image_box2.image = globalPhoto

    window.update()

def display():
    save_path = asksaveasfilename()
    compressed.save(save_path+"_compressed.JPG")
    image_size_mb = os.path.getsize(save_path+"_compressed.JPG") / (1024 * 1024)
    print("Image size After Compression: {:.2f} MB".format(image_size_mb))
    

# Create a button to trigger image display
choose_button  = tk.Button(window, text="Choose Image", command=choose_image, width=15, height=2)
display_button = tk.Button(window, text="Save Compressed Image",command=display, width=20, height=2)

# Position the boxes and buttons using grid layout
image_box1.grid(row=0, column=0, padx=5, pady=5)
image_box2.grid(row=0, column=1, padx=5, pady=5)
choose_button.grid(row=1, column=0, padx=5, pady=5)
display_button.grid(row=1, column=1, padx=5, pady=5)

# Run the window
window.mainloop()
