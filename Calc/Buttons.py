from customtkinter import CTkButton
from settings import *
class Button(CTkButton):
    def __init__(self,parent,text, func, col, row, font,span = 1, color = 'dark-gray'):
        super().__init__(parent,
                         text = text,
                         corner_radius= STYLING['corner-radius'],
                         font = font,
                         fg_color= COLORS[color]['fg'],
                         hover_color= COLORS[color]['hover'],
                         text_color=COLORS[color]['text'],
                         command = func)
        self.grid(column = col, columnspan = span, row = row, sticky = 'nesw', padx = STYLING['gap'], pady = STYLING['gap'])

class NumButton(Button):
    def __init__(self,parent,text, func, col, row, span, font, color = 'light-gray'):
        super().__init__(parent,
                         text = text,
                         func = lambda: func(text),
                         col = col,
                         row = row,
                         font = font,
                         color = color,
                         span = span)

class MathButton(Button):
    def __init__(self,parent,text, operator, func, col, row, font, color = 'orange'):
        super().__init__(parent,
                         text = text,
                         func = lambda: func(operator),
                         col = col,
                         row = row,
                         font = font,
                         color = color)


class ImageButton(CTkButton):
    def __init__(self, parent, func, col, row, image,text = '',color = 'dark-gray'):
        super().__init__(
            parent,
            text=text,
            corner_radius=STYLING['corner-radius'],
            image= image,
            fg_color=COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'],
            command=func)
        self.grid(column = col, row = row, sticky = 'nesw', padx = STYLING['gap'], pady = STYLING['gap'])

class mathimagebutton(ImageButton):
    def __init__(self,parent, operator, func, col, row, image, color = 'orange'):
        super().__init__(parent,

                         func = lambda: func(operator),
                         col = col,
                         row = row,
                         image = image,
                         color = color)
