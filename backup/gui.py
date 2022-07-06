from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from subprocess import call
from detect_mask_video import run

def instruct():
    window.destroy()
    import guiInstruction
def about():
    window.destroy()
    guiabout()
    
def start():
    window.destroy()
    run()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#1E1E1E")


canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    457.0,
    300.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start,
    relief="flat"
)
button_1.place(
    x=421.0,
    y=52.0,
    width=158.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=instruct,
    relief="flat"
)
button_2.place(
    x=612.0,
    y=52.0,
    width=181.0,
    height=39.0
)


def guiabout():
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
    window.configure(bg = "#1E1E1E")

    canvas = Canvas(
        window,
        bg = "#1E1E1E",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_a.png"))
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


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=about,
    relief="flat"
)
button_3.place(
    x=826.0,
    y=52.0,
    width=162.0,
    height=34.0
)


window.resizable(False, False)
window.mainloop()
