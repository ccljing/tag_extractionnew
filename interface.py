import sys
import Pmw
import Tkinter
class Demo:
    phone_1 = "sunsumg"
    phone_2 = 'sunsumg'
    parent = None
    t = None
    def __init__(self, parent):
        self.parent = parent
        parent.configure(background = "white")
        self.target = Tkinter.Label(parent, relief ="sunken", padx= 20, pady = 20)
        self.target.pack(fill ="x" , padx = 8, pady =8)
        phones=('sumsung', 'nokia')
        dropdown = Pmw.ComboBox(parent, label_text = 'the left_phone:', labelpos = 'nw',
                selectioncommand = self.get_phone,
                scrolledlist_items = phones)
        dropdown.pack(side = 'left', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)
        dropdown2 = Pmw.ComboBox(parent, label_text = 'the left_phone:', labelpos = 'nw',
                selectioncommand = self.get_phone2,
                scrolledlist_items = phones)
        dropdown2.pack(side = 'right', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)
        first = phones[0]
        dropdown.selectitem(first)
        first_right = phones[0]
        dropdown2.selectitem(first_right)
        botton = Tkinter.Button(parent, text='compare', command=self.compare_phone)
        botton.pack()
        self.t = Tkinter.Text(parent)

    def get_phone(self, phone):
        self.phone_1 = phone
    def get_phone2(self, phone):
        self.phone_2 = phone

    def compare_phone(self):
        self.t.delete(0.0, Tkinter.END)
        self.t.tag_config('a', foreground = 'red')
        self.t.insert(1.0, self.phone_1, 'a')
        self.t.insert(2.0, self.phone_2, 'a')
        self.t.pack()
if __name__ == "__main__":
    root = Tkinter.Tk()
    Pmw.initialise(root)
    widget = Demo(root)
    root.mainloop()
