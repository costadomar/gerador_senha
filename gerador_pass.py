import random
import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow

from g_senha import *


class ger_senha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #adicionando os botões
        self.ui.Botgerar.clicked.connect(self.senha)
        self.ui.Botcopy.clicked.connect(self.copiar)

#gerando a senha
    @QtCore.pyqtSlot()
    def senha(self):
        abc = ''
        for i in range (ord ('a'), ord ('z') + 1) : abc += (chr (i))
        ABC = abc.upper ()
        num = ''
        for i in range (0, 10) : num += str (i)
        simbolo = '!@#$%¨&*/<>§'
        selecao_argu=''
        if self.ui.checkBox_abc.isChecked() == True: selecao_argu += abc
        if self.ui.checkBox_ABC.isChecked () == True : selecao_argu += ABC
        if self.ui.checkBox_num.isChecked () == True : selecao_argu += num
        if self.ui.checkBox_simb.isChecked () == True : selecao_argu += simbolo

        tam_senha = int(self.ui.line_tamanho.text())
        senha_gerada =''
        for i in range(tam_senha): senha_gerada += random.choice(selecao_argu)
        self.ui.label.setText(senha_gerada)

    def copiar(self):
        cop = self.ui.label.text()
        pyperclip.copy(cop)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ger_senha()
    w.show()
    sys.exit(app.exec_())