from reportlab.pdfgen import canvas    
import pandas as pd
from xlsxwriter import Workbook
from janela import Ui_MainWindow
from login import Ui_login
from mysql.connector import connect
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem, QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Minha_janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela = Ui_MainWindow()
        self.janela.setupUi(self)

        #Mudar para janela insercao de cadastro
        self.janela.bt_cadastrar.clicked.connect(self.janela_cadastrar)
        #Mudar para janela dos cadastros
        self.janela.bt_cadastros.clicked.connect(self.janela_relatorio)
        self.janela.bt_cadastros.clicked.connect(self.janela_resumo)
        #sair da janela
        self.janela.bt_sair.clicked.connect(self.sair_janela)
        #botao para gerar pdf
        self.janela.bt_pdf.clicked.connect(self.gerar_pdf)
        #botao para gerar excel
        self.janela.bt_excel.clicked.connect(self.gerar_excel)
        #botao para excluir dados
        self.janela.bt_deletar.clicked.connect(self.excluir_dados)
        #botao para salvar os dados
        self.janela.bt_salvar.clicked.connect(self.salvar_dados)
        self.janela.line_tel.clearFocus()
        #botao para pesquisar e filtrar os dados da tabela
        self.janela.line_pesquisar.textChanged.connect(self.filtra_pesquisar)
        #botao para voltar a janela principal
        self.janela.bt_voltar.clicked.connect(self.janela_principal)
        self.janela.bt_editar.clicked.connect(self.editar)
        self.janela.btt_salvar_1.clicked.connect(self.salvar_alteracoes)
        # validando as entradas de dados
        reg_ex = QRegExp("[1-9][0-9]{1,}")
        validar_apart = QRegExpValidator(reg_ex, self)
        self.janela.line_apart.setValidator(validar_apart)
        self.janela.line_3.setValidator(validar_apart)
        self.janela.line_4.setValidator(validar_apart)
        #validar tlefone
        reg_ex = QRegExp("^[1-9]{2}(?:[9]{1}[1-9])[0-9]{1,}$")
        validar_telefone = QRegExpValidator(reg_ex, self)
        self.janela.line_tel.setValidator(validar_telefone)
        self.janela.line_pesquisar.setValidator(validar_telefone)
        self.janela.line_2.setValidator(validar_telefone)
        #validar somente letras
        reg_ex = QRegExp("[a-zA-Z]+[a-zA-Z]+")
        val_letras = QRegExpValidator(reg_ex, self)
        self.janela.line_nome.setValidator(val_letras)
        self.janela.line.setValidator(val_letras)
        
        
    # deleta os botoes de excluir e editar quando o usuario acessar   
    def deletar_botoes(self):
        self.janela.bt_deletar.hide()
        self.janela.bt_editar.hide() 
                    
    #abre a jenala de cadastro
    def janela_cadastrar(self):
        self.janela.pages.setCurrentIndex(2)

    #abre a janela principal
    def janela_principal(self):
        self.janela.pages.setCurrentIndex(0)

    #abre a janela de cadastros
    def janela_relatorio(self):
        self.janela.pages.setCurrentIndex(1)

    def janela_editar(self):
        self.janela.pages.setCurrentIndex(3)
        
    #sair da janela principal e volta para a janela de login
    def sair_janela(self):
        self.login = bt_login()
        self.login.show()
        Minha_janela.close(self)

    #filtra os dados da tabela
    def filtra_pesquisar(self):
        pes = self.janela.line_pesquisar.text()
        self.db = db()
        self.db.cursor.execute(' SELECT * FROM cadastro_moradores WHERE TELEFONE LIKE"%{}%" '.format(pes))
        relatorio = self.db.cursor.fetchall()
        
        self.janela.tableWidget.setRowCount(len(relatorio))
        self.janela.tableWidget.setColumnCount(5)
        for l in range(0, len(relatorio)):
            for c in range(0, 5):
                self.janela.tableWidget.setItem(l, c,QTableWidgetItem(str(relatorio[l][c])))
        
    #salva os dados do cadastro no banco
    def salvar_dados(self):
        #lista dos DDDs do Brasil
        lista_dds = ['11' , '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
        
        #Pegando Nome Cliente
        nome = self.janela.line_nome.text()
        tel = self.janela.line_tel.text()
        apart = self.janela.line_apart.text()
        andar = self.janela.comboBox.currentText()
        
        #Abrir Conexao
        self.db = db()
        self.db.cursor.execute("SELECT TELEFONE FROM cadastro_moradores WHERE TELEFONE = '{}'".format(tel))
        resltado = self.db.cursor.fetchall()
        self.db.cursor.execute("SELECT APARTAMENTO FROM cadastro_moradores WHERE APARTAMENTO = '{}'".format(apart))
        rs_apart = self.db.cursor.fetchall()
        
        if not len(resltado) == 0:
            return self.Qmessagem('Já existe um cadastro com esse número de telefone')
           
        elif not len(rs_apart) == 0:
            return self.Qmessagem('Já existe um cadastro com esse número de apartamento.')
        
        elif nome == '' or tel == '' or apart == '':
            return self.Qmessagem('Por favor insira preencha os campos.')
            

        elif not len(tel) == 11:
            return self.Qmessagem('Número de telefone deve conter 11 digitos.')
            
        
        elif not tel[:2] in lista_dds:
            return self.Qmessagem('DDD invalido.')
            
        
        else:
            pass
        try:
            self.db.cursor.execute(''' INSERT INTO cadastro_moradores (NOME, TELEFONE, APARTAMENTO, ANDAR)
                                    VALUES('%s','%s','%s','%s') ''' % (nome.upper(),
                                                                                    tel,
                                                                                    apart,
                                                                                    andar ))
            self.db.con.commit()
            self.infom('Cadastro realizado')
            self.janela.line_nome.clear()
            self.janela.line_tel.clear()
            self.janela.line_apart.clear()
        except:
           return self.Qmessagem('Ocorreu um problema na hora de salvar os dados.')
    
    #editar dados   
    def editar(self):
        p = self.janela.line_pesquisar.text()
        if not len(p) == 11:
            return self.Qmessagem('Preencha com número de telefone')
        try:
            self.db = db()
            
            self.db.cursor.execute("SELECT * FROM cadastro_moradores WHERE TELEFONE ="+ str(p) )
            valor = self.db.cursor.fetchall()
            
            self.janela_editar()
            self.janela.line.setText(str(valor[0][1]))
            self.janela.line_2.setText(str(valor[0][2]))
            self.janela.line_3.setText(str(valor[0][3]))
            self.janela.line_4.setText(str(valor[0][4]))
            print(str(valor[0][0]))
            self.id = str(valor[0][0])
        except:
            pass
        
    def infom(self, v):
        
        ms = QMessageBox()
        ms.setText(f"{v}")
        ms.setWindowTitle("SUCESSO")
        ms.setIcon(QMessageBox.Information)
        ms.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);font-size: 14px;")
        ms.exec_()
        
    #abrir caixa de menssagem de erro
    def Qmessagem(self, V):
        msg = QMessageBox()
        msg.setText(f"{V}")
        msg.setWindowTitle("ERRO")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);font-size: 14px;")
        msg.exec_()
        
    #salvar alteracoes
    def salvar_alteracoes (self):
         #lista dos DDDs do Brasil
        lista_dds = ['11' , '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
        
        nome = self.janela.line.text()
        tel = self.janela.line_2.text()
        apart = self.janela.line_3.text()
        andar = self.janela.line_4.text()
        id = self.id
        self.db = db()
        
        self.db.cursor.execute('SELECT TELEFONE, APARTAMENTO FROM _moradores_moradores WHERE ID != {} AND TELEFONE = {}'.format(id,tel))
        relatorio = self.db.cursor.fetchall()
        self.db.cursor.execute('SELECT TELEFONE, APARTAMENTO FROM cadastro_moradores WHERE ID != {} AND TELEFONE = {}'.format(id,tel))
        res_apart = self.db.cursor.fetchall()
        print(res_apart)
        print(relatorio)
        
        if not len(relatorio) == 0:
            return self.Qmessagem('Já existe um cadastro com esse número de telefone')
           
        elif not len(res_apart) == 0:
            return self.Qmessagem('Já existe um cadastro com esse número de apartamento.')
        
        elif nome == '' or tel == '' or apart == '' or andar == '':
            return self.Qmessagem('Por favor insira preencha os campos.')
            

        elif not len(tel) == 11:
            return self.Qmessagem('Número de telefone deve conter 11 digitos.')
            
        
        elif not tel[:2] in lista_dds:
            return self.Qmessagem('DDD invalido.')
        
        else:
            pass
        try:
            self.db.cursor.execute("UPDATE cadastro_moradores SET NOME = '{}', TELEFONE = '{}', APARTAMENTO = '{}', ANDAR ='{}' WHERE ID = {}".format(nome.upper() ,tel, apart, andar, id))
            self.db.con.commit()
            self.infom('Alteração realizada')
            self.janela_relatorio()
            self.janela.line_pesquisar.clear()
        except:
            return self.Qmessagem('Ocorreu um problema na hora de salvar os dados.')
    #gera pdf
    def gerar_pdf(self):
        self.db = db()
        self.db.cursor.execute(' SELECT * FROM cadastro_moradores')
        relatorio = self.db.cursor.fetchall()
        
        y = 0
        pdf = canvas.Canvas('cadastro_moradores.pdf')
        pdf.setFont('Times-Bold',25)
        pdf.drawString(200, 800, 'Cadastros Moradores:')
        pdf.setFont('Times-Bold', 10)
        
        pdf.drawString(10, 750, 'ID')
        pdf.drawString(50, 750, 'NOME')
        pdf.drawString(210, 750, 'TELEFONE')
        pdf.drawString(310, 750, 'APARTAMENTO')
        pdf.drawString(480, 750, 'ANDAR')
        
        for i in range(0, len(relatorio)):
            y+= 50
            pdf.drawString(10, 750 - y, str(relatorio[i][0]))
            pdf.drawString(50, 750 - y, str(relatorio[i][1]))
            pdf.drawString(210, 750 - y, str(relatorio[i][2]))
            pdf.drawString(350, 750 - y, str(relatorio[i][3]))
            pdf.drawString(510, 750 - y, str(relatorio[i][4]))
        
        pdf.save()
        self.infom('PDF gerado')
   
    #gerar excel
    def gerar_excel(self):
        self.workbook = Workbook('cadastro_moradores.xlsx')
        self.worksheet = self.workbook.add_worksheet('Rel.User')
        self.db = db()
        self.db.cursor.execute (" SELECT ID, NOME, TELEFONE, APARTAMENTO, ANDAR FROM cadastro_moradores")
        rs = self.db.cursor.fetchall()   
        
        self.worksheet.write(0,0, u'ID')
        self.worksheet.write(0,1, u'Nome')
        self.worksheet.write(0,2, u'Telefone')
        self.worksheet.write(0,3, u'Apartamento')
        self.worksheet.write(0,4, u'Andar')
        for i,user in enumerate(rs):
            self.worksheet.write(i + 1, 0, user[0])
            self.worksheet.write(i + 1, 1, user[1])
            self.worksheet.write(i + 1, 2, user[2])
            self.worksheet.write(i + 1, 3, user[3])
            self.worksheet.write(i + 1, 4, user[4])
        self.workbook.close()
        self.infom('EXCEL gerado')
    
    
    #excluir cadastros da tabela
    def excluir_dados(self):
        pes = self.janela.line_pesquisar.text()
        if not len(pes) == 11:
            return self.Qmessagem('Preencha com número de telefone.')
        else:
            pass
        try:
            self.db = db()
            self.db.cursor.execute("DELETE FROM cadastro_moradores WHERE TELEFONE =" +str(pes))
            self.db.con.commit()
            self.infom('Cadastro deletado')
            self.janela.line_pesquisar.clear()
        except:
            pass
   
    #joga todos os cadastros na tabela
    def janela_resumo(self):
        self.db = db()
        self.db.cursor.execute(''' SELECT ID, NOME, TELEFONE, APARTAMENTO, ANDAR FROM cadastro_moradores ''')
        relatorio = self.db.cursor.fetchall()
        
        self.janela.tableWidget.setRowCount(len(relatorio))
        self.janela.tableWidget.setColumnCount(5)
        for l in range(0, len(relatorio)):
            for c in range(0, 5):
                self.janela.tableWidget.setItem(l, c,QTableWidgetItem(str(relatorio[l][c])))
                
#janela de login              
class bt_login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_login()
        self.login.setupUi(self)
        self.login.bt_sair.clicked.connect(self.sair)
        self.login.pushButton.clicked.connect(self.janela_principal)
        
      
    def sair(self):
        bt_login.close(self)
        
        
    def limpar_janela_login(self):
        self.login.lineEdit.close()
        self.login.lineEdit_2.close()
        
    def Qmessagem(self, V):
        msg = QMessageBox()
        msg.setText(f"{V}")
        msg.setWindowTitle("ERRO")
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);font-size: 14px;")
        msg.exec_()
        
    def janela_principal(self):
        user = self.login.lineEdit.text()
        senha = self.login.lineEdit_2.text()
        adm = self.login.r_adm.isChecked()
        usuarios = self.login.r_usuario.isChecked()
        if user == '' or senha == '' or adm == '' or usuarios == '':
            self.Qmessagem('Prencha os campos para logar.')

        else:
            if user == 'admin' and senha == '123':
                # se o radiobutton do administrador for marcado
                if adm:
                    #limpar dados do login
                    self.limpar_janela_login()
                    #fechar a janela login
                    self.sair()
                    #abrir a janela principal
                    self.janela = Minha_janela()
                    self.janela.janela_principal()
                    self.janela.show()
                else:
                    self.Qmessagem('Selecione administrador para logar.')
                
            
            elif user == 'usuario' and senha == '1562':
                
                if usuarios:
                    #limpar os dados do login
                    self.limpar_janela_login()
                    #sair da tela de login
                    self.sair()
                    #abre a janela principal
                    self.janela = Minha_janela()
                    self.janela.janela_principal()
                    #se o login for do usuario deleta os botoes de alterar e exclir
                    self.janela.deletar_botoes()
                    self.janela.show()
                else:
                    #mensagem caso o radiobutton nao seja marcado
                    self.Qmessagem('Selecione usuario para logar.')
            else:
                self.Qmessagem('Usuario ou senha invalidos.')
            
        
#banco de dados
class db():
    def __init__(self, host = '185.212.70.154', database ='u121785755_Redes_social', user = 'u121785755_Rede_info_db',password = 'Pinha@Wellington@963147258'):
        self.con = connect(host=host, database=database, user=user, password=password)
        self.cursor = self.con.cursor()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = bt_login()
    window.show()
    sys.exit(app.exec_())