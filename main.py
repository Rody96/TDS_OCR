import tkinter as tk
from tkinter import filedialog, PhotoImage, Canvas, font


def UploadAction(event=None):
    filename = filedialog.askopenfilename(initialdir="/",
                                          filetypes=(
                                              ("PNG File", "*.png"), ("BMP File", "*.bmp"), ("JPEG File", "*.jpeg")),
                                          title="Choose a file.")
    pathTextBox.delete("1.0", "end")
    pathTextBox.insert("1.0", filename)


def ReadAction(event=None):
    resultData = [1, 2, 3, 4, 5, 6, 7]

    Canvas.create_text(canvas, 175, 330, text=resultData[0], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 215, 330, text=resultData[1], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 255, 330, text=resultData[2], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 295, 330, text=resultData[3], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 340, 330, text=resultData[4], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 380, 330, text=resultData[5], fill="#FFFFFF", font=helv36)
    Canvas.create_text(canvas, 420, 330, text=resultData[6], fill="#FFFFFF", font=helv36)


# Création fenètre
window = tk.Tk()

# Personalisation de la fenetre
window.title("OCR Compteurs - groupe 4")
window.geometry("600x720")
window.minsize(480, 360)
window.iconbitmap("OCR-logo.ico")
window.config(background="#91BEDC")
# Font
title1 = font.Font(family='Helvetica', size=36, weight='bold')
title2 = font.Font(family='Helvetica', size=26, weight='bold')

uploadButton = tk.Button(window, text='Parcourir', font=title2, relief="raised",pady="5",padx="5", command=UploadAction)
uploadButton.pack()

pathLabel = tk.Label(window, text="Path:", font=title1,bg="#91BEDC")
pathLabel.pack()

pathTextBox = tk.Text(window, height=2)
pathTextBox.pack()

readImButton = tk.Button(window, text='Lire image', font=title2,pady="5",padx="5", command=ReadAction)
readImButton.pack()

# Création image

w = 600
h = 600

helv36 = font.Font(family='Helvetica', size=36, weight='bold')
image = PhotoImage(file='img/OCR-logo.png').zoom(35).subsample(32)
canvas = Canvas(window, width=w, height=h, bg="#91BEDC", bd=0, highlightthickness=0)
canvas.create_image(w / 2, h / 2, image=image)
Canvas.create_text(canvas, w / 2, 50, text="Résultat :", fill="#FFFFFF", font=title1)
canvas.pack()

window.mainloop()
