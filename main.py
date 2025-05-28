import sys
import re

from PyQt5 import uic
from PyQt5 import QtWidgets

ultima_operacao = ''
buffer_value = 0




class Calculadora(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora-2.ui", self)
        for button in self.frame.findChildren(QPushButton):
            button.clicked.connect(lambda _, b=button: self._digitar(b.text()))
        self.btMais.clicked.connect(lambda: self._digitar("+"))
        self.btMenos.clicked.connect(lambda: self._digitar("-"))
        self.btMult.clicked.connect(lambda: self._digitar("*"))
        self.btDiv.clicked.connect(lambda: self._digitar("/"))
        self.btIgual.clicked.connect(self._calcular)
        self.btClear.clicked.connect(self._clear)

    def _carregar_operacao(self, op:str):
        global buffer_value
        buffer_value = op

    def _digitar(self, valor):
        global ultima_operacao, buffer_value
        texto_atual = self.display.text()
        if valor in "+-*/":
            if texto_atual:
                buffer_value = float(texto_atual)
                ultima_operacao = valor
                self.display.setText("")
            return
        if valor == "." and "." in texto_atual:
            return
        if texto_atual == "" and valor == ".":
            return
        novo_texto = texto_atual + str(valor)
        self.display.setText(novo_texto)

    def _clear(self):
        self.display.setText("")

    def _calcular(self):
        global ultima_operacao, buffer_value
        try:
            expressao = f"{buffer_value}" + ultima_operacao + self.display.text()
            expressao = re.sub(r'\b0+(\d)', r'\1', expressao)
            resultado = eval(expressao)
            buffer_value = self.display.text()
            self.display.setText(str(resultado))
        except Exception as e:
            self.display.setText("Erro")



if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QPushButton

    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())