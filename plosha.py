#підключення бібліотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*


#створення елементів інтерфейсу
app = QApplication([])


#головне вікно меню
my_win1 = QWidget()
my_win1.setWindowTitle("Меню")
my_win1.resize(300, 300)
my_win1.setStyleSheet("background-color:lightblue;")


#Елементи інтерфейсу
question = QLabel("⭑🟊  Вибери  🟊⭑")
question.setStyleSheet("font-size:23px;")

button1 = QPushButton("🟊 Площа 🟊")
button1.setStyleSheet("font-size:16px;")

button2 = QPushButton("🟊 Периметр 🟊")
button2.setStyleSheet("font-size:16px;")

line1 = QHBoxLayout()
line1.addWidget(question, alignment= Qt.AlignCenter)

line2 = QHBoxLayout()
line2.addWidget(button1, alignment= Qt.AlignCenter)
line2.addWidget(button2, alignment= Qt.AlignCenter)

line = QVBoxLayout()
line.addLayout(line1)
line.addLayout(line2)
my_win1.setLayout(line)


#Главное окно площі
my_win = QWidget()
my_win.setWindowTitle("Площа")
my_win.resize(300, 300)
my_win.setStyleSheet("background-color:lightblue;")


#Елементи інтерфейсу
question = QLabel("⭑🟊  Знайти площу ⎕ 🟊⭑")
question.setStyleSheet("font-size:23px;")

a1 = QLabel("🟆 ⇨ Довжина:")
a1.setStyleSheet("font-size:19px;")

a = QLineEdit()

b1 = QLabel("🟆 ⇧ Висота:")
b1.setStyleSheet("font-size:19px;")
b = QLineEdit()

button = QPushButton("🟊 Вичислити 🟊")
button.setStyleSheet("font-size:15px;")

line1 = QHBoxLayout()
line1.addWidget(question, alignment= Qt.AlignCenter)

line2 = QHBoxLayout()
line2.addWidget(a1, alignment= Qt.AlignLeft)
line2.addWidget(a, alignment= Qt.AlignCenter)

line3 = QHBoxLayout()
line3.addWidget(b1, alignment= Qt.AlignLeft)
line3.addWidget(b, alignment= Qt.AlignCenter)

line4 = QHBoxLayout()
line4.addWidget(button, alignment= Qt.AlignCenter)

line = QVBoxLayout()
line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
line.addLayout(line4)
my_win.setLayout(line)


#Главное окно периметра
my_win2 = QWidget()
my_win2.setWindowTitle("Периметр")
my_win2.resize(300, 300)
my_win2.setStyleSheet("background-color:lightblue;")


#Елементи інтерфейсу
question0 = QLabel("⭑🟊  Знайти периметр  🟊⭑")
question0.setStyleSheet("font-size:23px;")

a10 = QLabel("🟆  1 сторона:")
a10.setStyleSheet("font-size:19px;")

a0 = QLineEdit()
b10 = QLabel("🟆  2 сторона:")
b10.setStyleSheet("font-size:19px;")
b0 = QLineEdit()

button3 = QPushButton("🟊 Вичислити 🟊")
button3.setStyleSheet("font-size:15px;")

line1 = QHBoxLayout()
line1.addWidget(question0, alignment= Qt.AlignCenter)

line2 = QHBoxLayout()
line2.addWidget(a10, alignment= Qt.AlignLeft)
line2.addWidget(a0, alignment= Qt.AlignCenter)

line3 = QHBoxLayout()
line3.addWidget(b10, alignment= Qt.AlignLeft)
line3.addWidget(b0, alignment= Qt.AlignCenter)

line4 = QHBoxLayout()
line4.addWidget(button3, alignment= Qt.AlignCenter)

line = QVBoxLayout()
line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
line.addLayout(line4)
my_win2.setLayout(line)


#Функція кнопки площі
def button_OK():
    c = float(a.text())*float(b.text())
    c = str(c)
    win_1 = QMessageBox()
    win_1.setText(c)
    win_1.setStyleSheet("font-size:19px;")
    win_1.exec_()


#Функція кнопки периметра
def button_200():
    c = 2*(float(a0.text())*float(b0.text()))
    c = str(c)
    win_1 = QMessageBox()
    win_1.setText(c)
    win_1.setStyleSheet("font-size:19px;")
    win_1.exec_()


#Функція для зміни вікна меню на вікно площі
def button_10():
    my_win1.close()
    my_win2.close()
    my_win.show()


#Функція для зміни вікна меню на вікно периметра
def button_20():
    my_win1.close()
    my_win.close()
    my_win2.show()


#Прив'язення функцій до кнопок
button.clicked.connect(button_OK)
button1.clicked.connect(button_10)
button2.clicked.connect(button_20)
button3.clicked.connect(button_200)


my_win2.hide()
my_win.hide()
my_win1.show()
app.exec_()
