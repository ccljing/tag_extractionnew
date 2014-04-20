import sys
import Pmw
import Tkinter

class Demo:
    phone_1 = ""
    phone_2 = ""
    parent = None
    t = None
    def __init__(self, parent):
        self.parent = parent
        parent.configure(background = "white")
        self.target = Tkinter.Label(parent, text = "Mobile Phone Analysis", relief ="sunken", padx= 20, pady = 20)
        self.target.pack(fill ="x" , padx = 8, pady =8)
        self.phone_list = []
        # load phone name
        f = open('data/valid_index')
        for line in f:
            line = line.strip()
            fields = line.split("\t")
            self.phone_list.append(fields[0])
        f.close()
        # load phone score dict
        self.phone_score = {}
        g = open('phone_score')
        for line in g:
            line = line.strip()
            fields = line.split("\t")
            key = fields[0]
            if self.phone_score.get(key,None) == None:
                self.phone_score[key] = []
                for i in range(1,len(fields)):
                    self.phone_score[key].append(fields[i])
            else:
                continue
        g.close()
                    
       # create scroll list box 
        self.phone_list.sort();
        self.phone_name = tuple(self.phone_list)  
        self.dropdown1 = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE,
              items= self.phone_name,
              labelpos=NW, label_text='The left phone',
              listbox_height=5, vscrollmode='static',
              selectioncommand=self.selectionCommand1,
              dblclickcommand=self.selectionCommand1,
              usehullsize=1, hull_width=200, hull_height=200,)
        self.dropdown1.pack(side = 'left', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)
        self.dropdown2 = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE,
              items= self.phone_name,
              labelpos=NW, label_text='The right phone',
              listbox_height=5, vscrollmode='static',
              selectioncommand=self.selectionCommand2,
              dblclickcommand=self.selectionCommand2,
              usehullsize=1, hull_width=200, hull_height=200,)
        self.dropdown2.pack(side = 'right', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)
        
        botton = Tkinter.Button(parent, text='compare', command=self.compare_phone)
        botton.pack()
 #       self.t = Tkinter.Text(parent)
 #       self.t.pack()
    def selectionCommand1(self):
        self.phone_1 = self.dropdown1.getcurselection()[0]
        if len(self.phone_1) == 0:
            print "No SELECTION"
        else:
            print "selection left phone:", self.phone_1
    def selectionCommand2(self):
        self.phone_2 = self.dropdown2.getcurselection()[0]
        if len(self.phone_2) == 0:
            print "NO SELECTION"
        else:
            print "selection right phone:", self.phone_2
    def compare_phone(self):
   #     self.t.delete(0.0, Tkinter.END)
     #   self.t.tag_config('a', foreground = 'red')
        if self.phone_1 in self.phone_score.keys():
            attribute1 = self.phone_score[self.phone_1]
            score_1 = {}
            for i in range(0,len(attribute1)):
                value = attribute1[i].split(":")
                key = value[0]
                score = value[1]
                score_1[key] = score
        else:
            attribute1 = "not found"
        if self.phone_2 in self.phone_score.keys():
            attribute2 = self.phone_score[self.phone_2]
            score_2 = {}
            for i in range(0,len(attribute2)):
                value = attribute2[i].split(":")
                key = value[0]
                score = value[1]
                score_2[key] = score
        else:
            attribute2 = "not found"
        button1 = Tkinter.Button(self.parent, text = self.phone_1, relief = "flat", bg = 'green')
        button1.pack(side = "left",padx = 8,pady =8, anchor = "n")
        button2 = Tkinter.Button(self.parent,text = self.phone_2, relief = "flat", bg = 'blue')
        button2.pack(expand = 1 ,side = "right", anchor = "n")
        for key in score_1.keys():
            score1 = score_1[key]
            score2 = score_2[key]
            message = key + ":"+"customers' score is:" + "\t"+score1+"\t"+"vs"+"\t"+score2
            button = Tkinter.Button(self.parent, text = message, relief = "flat")
            button.pack(expand = 1,side = "top", anchor = "w", padx = 8, pady = 8)
            
            
            
       
    #    self.t.insert(1.0, attribute1, 'a')
   #     self.t.insert(3.0, attribute2, 'a')
    #    self.t.pack()
if __name__ == "__main__":
    root = Tkinter.Tk()
    Pmw.initialise(root)
    widget = Demo(root)
    root.mainloop()
