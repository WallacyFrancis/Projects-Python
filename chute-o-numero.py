# Advinhar o valor aleatório que o programa exibe
import random

class chuteONumero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1
    self.valor_maximo = 10
    self.tentar_novamente = True

  def Iniciar(self):
    self.GerarNumeroAleatorio()
    self.PedirValorAleatorio()
    while self.tentar_novamente == True:
      if int(self.valor_do_chute) > self.valor_aleatorio:
        print('Chute um valor mais baixo')
        self.PedirValorAleatorio()
      elif int(self.valor_do_chute) < self.valor_aleatorio:
        print('Chute um valor mais alto')
        self.GerarNumeroAleatorio()
      if self.valor_do_chute  == self.valor_aleatorio:
        self.tentar_novamente == False
        print('Parabéns, vocÊ acertou!')

  def PedirValorAleatorio(self):
    self.valor_do_chute = input('Chute um numero de 1 a 10: ')

  def GerarNumeroAleatorio(self):
    self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo) 

chute = chuteONumero()
chute.Iniciar()   