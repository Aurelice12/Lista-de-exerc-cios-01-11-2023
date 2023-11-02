from atividade import Atividade
class Disciplina(Atividade): 
  def __init__(self):
    self.atividades = []

  def add_atividade(self, nome, data):
    self.nome = nome
    self.data = data
    for atividade in self.atividades:
      if self.data == data:
        print("Não é possível adicionar duas atividades na mesma data!")
    else:
      self.atividades.append(Atividade(nome, data))

  def marcar_concluida(self, nome, data):
    for atividade in self.atividades:
      if atividade.nome == nome and atividade.data == data:
          atividade.concluida = True
          print("Atividade marcada como concluída.")
          return
        
  def atv_concluidas(self):
    print('Lista de atividades concluídas: ')
    for atividade in self.atividades:
      if atividade.concluida:
        print(f'Atividade: {self.nome} | Data de entrega: {self.data}')

  def atv_em_aberto(self):
    print('Lista de atividades em aberto:')
    for atividade in self.atividades:
      if not self.concluida:
        print(f'Atividade: {self.nome} | Data de entrega: {self.data}')
