from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("720x431")
window.configure(bg = "#eeeeee")
canvas = Canvas(
    window,
    bg = "#eeeeee",
    height = 431,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    359.5, 215.5,
    image=background_img)

canvas.create_text(
    182.5, 61.5,
    text = "Personal Manager",
    fill = "#6c63ff",
    font = ("Raleway-Bold", int(16.0)))

canvas.create_text(
    81.0, 116.5,
    text = "SIGN IN",
    fill = "#000000",
    font = ("None", int(16.0)))

canvas.create_text(
    168.0, 150.0,
    text = "Sign in to continue to our application",
    fill = "#464040",
    font = ("arial", int(11.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    185.0, 280.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 79.0, y = 262,
    width = 212.0,
    height = 35)

canvas.create_text(
    101.0, 250.0,
    text = "Password",
    fill = "#0c8686",
    font = ("helvetica", int(11.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    185.5, 221.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 79.0, y = 204,
    width = 213.0,
    height = 32)

canvas.create_text(
    102.0, 194.0,
    text = "Username",
    fill = "#0f7d7d",
    font = ("helvetica", int(11.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 113, y = 305,
    width = 148,
    height = 34)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 288, y = 47,
    width = 58,
    height = 22)

window.resizable(False, False)
window.mainloop()
