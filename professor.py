from disciplina import Disciplina

class Professor(Disciplina):
  def __init__(self):
    self.disciplinas = []
    
  def add_disc(self, nome_disc):
    self.nome_disc = nome_disc
    self.disciplinas.append(nome_disc)
    print(f'A disciplina {nome_disc} foi adicionada')
