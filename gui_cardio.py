import tkinter as tk
from tkinter import filedialog
from app import SiriusCardio


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    input_filename = filedialog.askopenfilename()
    output_filename = filedialog.asksaveasfilename()

    app: SiriusCardio = SiriusCardio(
        input_filename=input_filename,
        output_filename=output_filename
    )
    app.run()


