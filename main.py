from professor import Professor
from disciplina import Disciplina
from atividade import Atividade

disc = Disciplina()
prof = Professor()

print('Seja bem vindo! ')
while True: 
  print('')
  print('Escolha uma das opções abaixo: ')
  print('1 - Adicinar nova disciplina')
  print('2 - Adicionar nova atividade')
  print('3 - Marcar atividade como concluída')
  print('4 - Ver as atividades concluídas')
  print('5 - Ver as atividades em aberto')
  print('6 - Sair do programa')
  print('')
  opcao = int(input('O que você deseja fazer? '))
  print('')

  if opcao == 1:
    nome_disc = input('Nome da disciplina: ')
    prof.add_disc(nome_disc)
    
  elif opcao == 2:
    nome_disc = input('Nome da disciplina: ')
    atividade = input('Nome da atividade: ')
    data = input('Data de entrega(DDMMAAAA): ')
    for disciplinas in prof.disciplinas:
      if prof.nome_disc == nome_disc:
        disc.add_atividade(atividade, data)
  elif opcao == 3: 
    atividade = input('Nome da atividade: ')
    data = input('Data de entrega: ')
    for atividade in disc.atividades: 
      if atividade.nome == atividade and atividade.data == data:
        atividade.marcar_concluida()

  elif opcao == 4: 
    disc.atv_concluidas()
  
  elif opcao == 5: 
    disc.atv_em_aberto()

  elif opcao == 6:
    print('Saindo do programa...')
    break

  else: 
    print('ERRO! Por favor, insira uma das opções acima!')
