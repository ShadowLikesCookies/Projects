import customtkinter as ctk
import darkdetect
from settings import *
from Buttons import *
from PIL import Image
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass

class calc(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color= (WHITE, BLACK))

        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')

        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)

        self.iconbitmap('empty.ico')
        self.title('')

        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform= 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')

        self.result_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')

        self.create_widgets()

        self.mainloop()
    def create_widgets(self):

        main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family = FONT, size = OUTPUT_FONT_SIZE )


        out_label(self, 0, 'Se', main_font, self.formula_string)
        out_label(self, 1, 'e', result_font, self.result_string)

        Button(self,
               text = OPERATORS['clear']['text'],
               col =OPERATORS['clear']['col'],
               row = OPERATORS['clear']['row'],
               font = main_font,
               func = self.clear)
        Button(self,
               text = OPERATORS['percent']['text'],
               col =OPERATORS['percent']['col'],
               row = OPERATORS['percent']['row'],
               font = main_font,
               func = self.percent)
        invert_image = ctk.CTkImage(
            light_image= Image.open(OPERATORS['invert']['image path']['dark']),
            dark_image=Image.open(OPERATORS['invert']['image path']['light']))
        ImageButton(self,
                    func = self.invert,
                    image = invert_image,
                    col=OPERATORS['invert']['col'],
                    row=OPERATORS['invert']['row']
                    )
        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text=num,
                func=self.num_press,
                col=data['col'],
                row=data['row'],
                font=main_font,
                span=data['span'])
        for operator, data in MATH_POSITIONS.items():
            if data['image path']:
                divi = ctk.CTkImage(
                    light_image= Image.open(data['image path']['dark']),
                    dark_image = Image.open(data['image path']['light'])
                )
                mathimagebutton(self,
                                operator = operator,
                                func = self.mathpress,
                                col = data['col'],
                                row = data['row'],
                                image = divi)
            else:
                MathButton(self,
                        font = main_font,
                        text = data['character'],
                        operator = operator,
                        func = self.mathpress,
                        col = data['col'],
                        row = data['row'])
    def num_press(self, value):
        print(value)
    def clear(self):
        print('clear')
    def percent(self):
        print('percent')
    def invert(self):
        print("invert")
    def mathpress(self, value):
        print(value)
class out_label(ctk.CTkLabel):
    def __init__(self, parent, row, sticky, font, string_var):
        super().__init__(parent, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = sticky,padx = 10)


if __name__ == '__main__':
    calc(darkdetect.isDark())

