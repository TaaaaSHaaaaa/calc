from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout, QPushButton, QVBoxLayout,QLabel
first_number=0
second_number=0
midresult=None
is_it_first=True
app = QApplication ([])
window = QWidget ()

layout = QGridLayout ()
#creating buttons and main label
mainlabel=QLabel('Insert')
layout.addWidget(mainlabel,0,0)
button_0 = QPushButton ('0')
layout.addWidget(button_0,4,1)
button_1 = QPushButton ('1')
layout.addWidget(button_1,1,0)
button_2 = QPushButton ('2')
layout.addWidget(button_2,1,1)
button_3 = QPushButton ('3')
layout.addWidget(button_3,1,2)
button_4 = QPushButton ('4')
layout.addWidget(button_4,2,0)
button_5 = QPushButton ('5')
layout.addWidget(button_5,2,1)
button_6 = QPushButton ('6')
layout.addWidget(button_6,2,2)
button_7 = QPushButton ('7')
layout.addWidget(button_7,3,0)
button_8 = QPushButton ('8')
layout.addWidget(button_8,3,1)
button_9 = QPushButton ('9')
layout.addWidget(button_9,3,2)
button_plus = QPushButton ('+')
layout.addWidget(button_plus,1,3)
button_minus = QPushButton ('-')
layout.addWidget(button_minus,2,3)
button_multiply = QPushButton ('x')
layout.addWidget(button_multiply,3,3)
button_devide = QPushButton (':')
layout.addWidget(button_devide,4,3)
button_result = QPushButton ('=')
layout.addWidget(button_result,4,2)
button_delete = QPushButton ('<')
layout.addWidget(button_delete,4,0)

window.setGeometry(100,100,200,200)
button_1.move(100,100)
#functions
def button_0_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 0
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 0
        mainlabel.setText(str(second_number))
def button_1_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 1
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 1
        mainlabel.setText(str(second_number))
    
def button_2_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 2
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 2
        mainlabel.setText(str(second_number))
def button_3_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 3
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 3
        mainlabel.setText(str(second_number))

def button_4_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 4
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 4
        mainlabel.setText(str(second_number))
def button_5_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 5
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 5
        mainlabel.setText(str(second_number))
def button_6_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 6
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 6
        mainlabel.setText(str(second_number))

        
def button_7_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 7
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 7
        mainlabel.setText(str(second_number))
def button_8_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 8
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 8
        mainlabel.setText(str(second_number))
def button_9_clicked():
    global midresult
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global midresult
    if midresult!=None:
        is_it_first=False
        first_number=midresult
    if is_it_first:
        first_number=first_number*10 + 9
        mainlabel.setText(str(first_number))

        
    else:
        second_number=second_number*10 + 9
        mainlabel.setText(str(second_number))
def plus():
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    is_it_first=False
    operation="+"

    
def minus():
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    is_it_first=False
    operation="-"

def multiply():
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    is_it_first=False
    operation="x"

def devide():
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    is_it_first=False
    operation=":"
def result():
    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    global midresult
    is_it_first=True
    if operation=='+':
        mainlabel.setText(str(first_number+second_number))
        
    if operation=='-':
        mainlabel.setText(str(first_number-second_number))
    if operation=='x':
        mainlabel.setText(str(first_number*second_number))
    if operation==':':
        mainlabel.setText(str(first_number/second_number))
    midresult=first_number+second_number
    first_number=0    
    second_number=0
    
def delete():

    global first_number
    global second_number
    global mainlabel
    global is_it_first
    global operation
    global midresult
    mainlabel.setText('0')
    midresult=None
    first_number=0
    second_number=0
    midresult=None
    is_it_first=True


#moitoring button clicks    
button_0.clicked.connect(button_0_clicked)        
button_1.clicked.connect(button_1_clicked)
button_2.clicked.connect(button_2_clicked)
button_3.clicked.connect(button_3_clicked)
button_4.clicked.connect(button_4_clicked)
button_5.clicked.connect(button_5_clicked)
button_6.clicked.connect(button_6_clicked)
button_7.clicked.connect(button_7_clicked)
button_8.clicked.connect(button_8_clicked)
button_9.clicked.connect(button_9_clicked)
button_plus.clicked.connect(plus)
button_minus.clicked.connect(minus)
button_multiply.clicked.connect(multiply)
button_devide.clicked.connect(devide)
button_result.clicked.connect(result)
button_delete.clicked.connect(delete)
window.setLayout(layout)
window.show ()
app.exec_ ()
