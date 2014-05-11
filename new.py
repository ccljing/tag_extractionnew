# -*- coding: utf-8 -*-
from Tkinter import *
import Pmw
root = Tk()
Pmw.initialise()
phone_1 = ""
phone_2 = ""
score_1 = {}
score_2 = {}
parent = None
t = None
root.configure(background = "white")
target = Tkinter.Label(parent, text = "Mobile Phone Analysis", relief ="sunken", padx= 20, pady = 20)
target.pack(fill ="x" , padx = 8, pady =8)
phone_list = []
# load phone name
f = open('data/valid_index')
for line in f:
    line = line.strip()
    fields = line.split("\t")
    phone_list.append(fields[0])
f.close()
 # load phone score dict
phone_score = {}
g = open('phone_score')
for line in g:
    line = line.strip()
    fields = line.split("\t")
    key = fields[0]
    if phone_score.get(key,None) == None:
        phone_score[key] = []
        for i in range(1,len(fields)):
            phone_score[key].append(fields[i])
        else:
            continue
g.close()
 # create scroll list box 
phone_list.sort();
phone_name = tuple(phone_list)  
buttonleft = Tkinter.Button(parent, relief = "flat", bg = 'green')
buttonright = Tkinter.Button(parent, relief = "flat", bg = 'blue')
buttonlist = []
for i in range(0,9):
    buttonname = "%s"%("button")+"%d"%(i+1)
    print buttonname
    buttonname = Tkinter.Button(parent, relief = "flat")
    buttonlist.append(buttonname)
def selectionCommand1():
    global phone_1
    phone_1 = dropdown1.getcurselection()[0]
    print type(phone_1)
    if len(phone_1) == 0:
        print "No SELECTION"
    else:
        print "selection left phone:", phone_1
def selectionCommand2():
    global phone_2
    phone_2 = dropdown2.getcurselection()[0]
    if len(phone_2) == 0:
        print "NO SELECTION"
    else:
        print "selection right phone:", phone_2
        
def compare_phone():
    global phone_1,phone_2
    print phone_1,phone_2
    if phone_1 in phone_score.keys():
        attribute1 = phone_score[phone_1]
        for i in range(0,len(attribute1)):
            value = attribute1[i].split(":")
            key = value[0]
            score = value[1]
            score_1[key] = score
    else:
        attribute1 = "not found"
        print "not found"
    if phone_2 in phone_score.keys():
        attribute2 = phone_score[phone_2]
        for i in range(0,len(attribute2)):
            value = attribute2[i].split(":")
            key = value[0]
            score = value[1]
            score_2[key] = score
    else:
        attribute2 = "not found"
        print "not found"
    buttonleft['text'] = phone_1
    buttonright['text'] = phone_2
    buttonleft.pack(side = "left",padx = 8,pady =8, anchor = "n")
 #  button2 = Tkinter.Button(self.parent,text = phone_2, relief = "flat", bg = 'blue')
    buttonright.pack(expand = 1 ,side = "right", anchor = "n")
    index = 0
    for key in score_1.keys():
        score1 = score_1[key]
        score2 = score_2[key]
        print key,score1,score2
        message = key + ":"+"customers' score is:" + "\t"+score1+"\t"+"vs"+"\t"+score2
#       button = Tkinter.Button(parent, text = message, relief = "flat")
        buttonlist[index]['text'] = message
        buttonlist[index].pack(expand = 1,side = "top", anchor = "w", padx = 8, pady = 8)
        index +=1
      
dropdown1 = Pmw.ScrolledListBox(parent, listbox_selectmode=SINGLE,
              items= phone_name,
              labelpos=NW, label_text='The left phone',
              listbox_height=5, vscrollmode='static',
              selectioncommand=selectionCommand1,
              dblclickcommand=selectionCommand1,
              usehullsize=1, hull_width=200, hull_height=200,)
dropdown1.pack(side = 'left', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)
dropdown2 = Pmw.ScrolledListBox(parent, listbox_selectmode=SINGLE,
              items= phone_name,
              labelpos=NW, label_text='The right phone',
              listbox_height=5, vscrollmode='static',
              selectioncommand=selectionCommand2,
              dblclickcommand=selectionCommand2,
              usehullsize=1, hull_width=200, hull_height=200,)
dropdown2.pack(side = 'right', anchor = 'n', fill = 'x', expand =1, padx =8, pady = 8)

button_compare = Tkinter.Button(parent, text='compare', command=compare_phone)
button_compare.pack()
      
           
root.mainloop()
