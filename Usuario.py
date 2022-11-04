import os
import time

usuarios = {}
#Classe
class Usuario:
#Construtor
  print("""MENU
  ===================================
  [1]CADASTRAR-SE
  [2]LOGIN
  [3]DELETAR CONTA""")
  def __init__(self, nome,email,senha,telefone):
#Atributos
    self.nome = nome
    self._email = email
    self.__senha= senha
    self.telefone = telefone


#Método get  
  def getemail (self):
    return self._email

    
  def getsenha(self):
    return self.__senha
#Método de modificar a senha

  def setsenha(self):
    novasen = str(input('Digite a nova senha: '))
    if novasen == self.__senha:
      print("\033[30mA senha não pode ser igual a anterior\033[3m")
      novasen = input(' Digite a nova senha: ')
    else:
       novasen=self.__senha
       print("Senha registrada com sucesso")

  #Método de cadastrar o usuário
  def cadastrarUser(self):
    print('\033[34m-=\033[m' * 10)
    print('\033[1;46m  REALIZAR CADASTRO\033[m')
    print('\033[34m-=\033[m' * 10)
    self.nome = input('Digite seu nome: ')
    self.data_de_nasc = input('Digite sua data de nascimento: ')
    self.telefone = int(input('Digite seu telefone: '))
    self._email = input ('Digite seu email: ')
    while '@' not in self._email:
      self._email = input('Digite um email válido: ')
    while self._email in usuarios:
      self._email = input('Email já existe. Digite um email válido: ')
    self.__senha = input('Digite sua senha: ')
    email = self._email
    email = Usuario(self.nome, self.telefone, self._email, self.__senha)
    usuarios[email.getemail()] = email
    file = open ('cadastros.txt', 'a+')
    file.write ("%s, %s, %s, %s\n" %(self.nome, self.telefone, self._email, self.__senha))
    os.system('clear')
    
#Método de dados
  def dice(self):
    esc = input(f'Olá {self.nome}, deseja visualizar seus dados cadastrados?\nResposta: ')
    os.system('clear')
    if esc == 'sim':
      print('\033[1;93mSeus Dados\033[0;0m')
      print('-'*40)
      print(f'Nome: {self.nome}')
      print('-'*40)
      print(f'Email: {self._email}')
      print('-'*40)
      print(f'Número de telefone: {self.telefone}')
      print('-'*40)
      print(f'Data de nascimento: {self.data_de_nasc}')
      print('-'*40)
      print('Senha: -----------')
      print('-'*40)
    else:
      pass
    
      
#Método de login   
  def login(  self):
    print('\033[35m-=\033[m' * 10)
    print('\033[1;46m   EFETUAR LOGIN\033[m')
    print('\033[35m-=\033[m' * 10)
    email = input('Insira seu email:')
    senha = input('Insira sua senha:')
    if email == self._email and senha == self.__senha:
        print('\n\033[32mLOGIN EFETUADO COM SUCESSO!\033[m')
    while senha != self.__senha:
      esqueceuASenha=input('Esqueceu a senha?')
      if esqueceuASenha == 'não':
         senha = input('Insira sua senha:')
      elif esqueceuASenha =='sim':
        seguranca=str(input('Por segurança informe seu email de login: '))
        if seguranca == self._email:
          usuario.setsenha()
          break
        else:
          print('Email inválido!')
          
        
    
      #loop
#    while email!=self._email or senha!= self.__senha:
        print('\n\033[31mOpa! E-mail ou Senha incorretos. Por favor, tente novamente\033[m')
        email = input('Insira seu email:')
        senha = input('Insira sua senha:')
        if email == self._email and senha == self.__senha:
            print('\n\033[32mLOGIN EFETUADO COM SUCESSO!\033[m')

#Método de deletar o cadastro do usuário
  def deletarCadastro(self):
    self.nome = None
    self._email = None
    self.__senha= None
    self.telefone = None
    print('Sua conta foi deletada. Até logo! :) ')
  

#invocando métodos
usuario = Usuario("","","","")
usuario.cadastrarUser()
usuario.login()