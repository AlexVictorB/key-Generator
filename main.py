from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import clipboard
import random

from PyQt5.uic.properties import QtGui


def gerar_chave(size):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    simbols = ['@', '#', '!', '$', '&', '*']

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    if (tela.letters.isChecked()):
        key = letter

    if (tela.numbers.isChecked()):
        key = numbers

    if (tela.simbol.isChecked()):
        key = simbols

    if (tela.letters.isChecked()) and (tela.numbers.isChecked()):
        key = letter + numbers

    if (tela.letters.isChecked()) and (tela.simbol.isChecked()):
        key = letter + simbols

    if (tela.numbers.isChecked()) and (tela.simbol.isChecked()):
        key = numbers + simbols

    if (tela.letters.isChecked()) and (tela.numbers.isChecked()) and (tela.simbol.isChecked()):
        key = numbers + letter + simbols


    random.shuffle(key)

    choice_size = size - 1
    list_size = len(key)

    if list_size > choice_size:
        chave = (key[:choice_size])
        final = str(chave).strip('[]')
        final = final.replace(" ", "")
        final = final.replace(",", "")
        final = final.replace("'", "")
        print(final)

        file = open("chave.txt", 'w')
        file.write(final)


def slider():
    value = str(tela.size.value())
    tela.size_display.setText(value)
    return value


def principal():
    valor: int = int(slider())
    senha = (gerar_chave(valor))
    file = open("chave.txt", 'r')
    tela.display.setText(file.read())

def copiar():
    clipboard.paste()
    with open('chave.txt', 'r') as f:
        conteudo = f.read()
        clipboard.copy(conteudo)

app = QtWidgets.QApplication([])
tela = uic.loadUi("main.ui")
tela.setWindowTitle("Key Generator")
tela.setWindowIcon(QIcon("src/icon/icon.png"))
tela.copiar.setIcon(QIcon('src/png/copy.png'))
tela.copiar.setIconSize(QSize(30, 30))
tela.copiar.clicked.connect(copiar)
tela.size.valueChanged.connect(slider)
tela.gen.clicked.connect(principal)

tela.show()
app.exec()
