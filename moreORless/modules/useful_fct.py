import tkinter

# resize and position the window
def set_geometry(self:tkinter.Tk|tkinter.Toplevel, margin_EW:int=100, margin_NS:int=20, center:bool=True):
    self.update_idletasks()
    width = self.winfo_reqwidth() + margin_EW  # margin E-W
    height = self.winfo_reqheight() + margin_NS  # margin N-S

    x = (self.winfo_screenwidth() // 2) - (width // 2)
    y = (self.winfo_screenheight() // 2) - (height // 2)
    if center:
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    else:
        self.geometry('{}x{}'.format(width, height))

# destroy all widget in the given window
def clear(self:tkinter.Tk|tkinter.Frame|tkinter.Toplevel):
    for widget in self.winfo_children():
            widget.destroy()

# undisplay all widget in the given window without destroy it
def undisplay(self:tkinter.Tk|tkinter.Frame|tkinter.Toplevel):
     for widget in self.winfo_children():
            widget.pack_forget()

