from PIL import Image
import sys, os
from tqdm import tqdm
from tkinter import *
from customtkinter import *
from customtkinter import filedialog


'''
image_directory = input("Enter path to files: ")
output_directory = input("Enter path to ouput directory: ")

if os.path.exists(output_directory) == False:
    os.mkdir(output_directory)

for fl in tqdm(os.listdir(image_directory)):
    
    if fl.endswith(".webp"):
        filename = fl.strip(".webp")
        im = Image.open(os.path.join(image_directory,fl))
        im.convert("RGB")
        im.save(os.path.join(output_directory,f"{filename}.png"))
'''


def open_directory():
    drct = filedialog.askdirectory()
    return drct
    

app = CTk()
app.title("File converter")
app.geometry("600x350")

my_label = CTkLabel(app, text="", font=("Helvetica", 24))
my_label.pack(pady=40)

search_im = PhotoImage(file=r"File Converter\file_search.png").subsample(8,8)
export_im = PhotoImage(file=r"File Converter\file_export.png").subsample(7,7)

source_directory = CTkButton(app, 
	height=50,
	width=500,
    text="Enter Source Directory",
	font=("Helvetica", 18),
	corner_radius=30,
	text_color="white",
	state="normal",
    image=search_im,
    compound=RIGHT,
    command = open_directory
)
source_directory.pack(pady=20)

save_directory = CTkButton(app, 
	
	height=50,
	width=500,
    text="Enter Save Directory",
	font=("Helvetica", 18),
	corner_radius=30,
	text_color="white",
	state="normal",
    image=export_im,
    compound=RIGHT,
    command = open_directory
)
save_directory.pack(pady=20)

filetype = CTkComboBox(master=app,values=["jpeg", "png", "svg", "webp"], font=("Helvetica", 18))
filetype.pack(pady=20)

app.mainloop()