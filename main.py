import tkinter as tk
from tkinter import filedialog,PhotoImage,Canvas


def UploadAction(event=None):
    filename = filedialog.askopenfilename(initialdir="/",
                                          filetypes=(
                                          ("PNG File", "*.png"), ("BMP File", "*.bmp"), ("JPEG File", "*.jpeg")),
                                          title="Choose a file.")
    pathTextBox.delete("1.0", "end")
    pathTextBox.insert("1.0", filename)


# Création fenètre
window = tk.Tk()

# Personalisation de la fenetre
window.title("OCR Compteurs - groupe 4")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("OCR-logo.ico")

uploadButton = tk.Button(window, text='Parcourir', command=UploadAction)
uploadButton.pack()

pathLabel = tk.Label(window, text="Path:")
pathLabel.pack()

pathTextBox = tk.Text(window, height=2)
pathTextBox.pack()

readImButton = tk.Button(window, text='Lire image')
readImButton.pack()

resultLabel = tk.Label(window, text="Données:")
resultLabel.pack()

resultTextBox = tk.Text(window, height=6, bg="#AAAAAA")
resultTextBox.pack(side='top', padx=2, pady=0)

# Création image

w = 600
h = 600
image = PhotoImage(file='img/OCR-logo.png').zoom(35).subsample(32)
canvas = Canvas(window, width=w, height=h, bg="#FFFFFF", bd=0, highlightthickness=0)
canvas.create_image(w/2, h/2, image=image)
Canvas.create_text(canvas,175,330, text="1", fill="#FFFFFF")
Canvas.create_text(canvas,215,330, text="2", fill="#FFFFFF")
Canvas.create_text(canvas,255,330, text="3", fill="#FFFFFF")
Canvas.create_text(canvas,295,330, text="4", fill="#FFFFFF")
Canvas.create_text(canvas,340,330, text="5", fill="#FFFFFF")
Canvas.create_text(canvas,380,330, text="6", fill="#FFFFFF")
Canvas.create_text(canvas,420,330, text="7", fill="#FFFFFF")
canvas.pack()

window.mainloop()
