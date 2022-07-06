from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def back():
    window.destroy()
    import gui

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg="#1E1E1E")


canvas = Canvas(
    window,
    bg="#1E1E1E",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_i.png"))
image_1 = canvas.create_image(
    500.0,
    300.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Back_Button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_2.place(
    x=20,
    y=530.0,
    width=171.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
