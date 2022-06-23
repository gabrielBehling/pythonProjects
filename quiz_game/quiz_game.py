import random

points = list()
played = list()
used = list()
def pergunta():
    perguntas = open('projects\quiz_game\perguntas.txt')
    x = 0
    questnum = random.randrange(1, 11)
    while x == 0:
        if questnum not in used:
            for l in perguntas:
                if l.startswith(str(questnum)+' '):
                    questLine = l.split("'")
                    quest = questLine[1]
                    answer = questLine[3]
                    pAnswer = input(quest)
                    played.append(questnum)

                    if pAnswer.lower() == answer:
                        print('Correto! (+1)\n')
                        points.append(questnum)
                    else:
                        print('Errado! \n')
                    used.append(questnum)
            x = -1
        else:
            questnum = random.randrange(1, 11)

print('\nBem vindo ao Quiz sobre computadores!\n')

playing = input('Você deseja jogar? ')
if playing.lower() != "sim":
    quit()

print('\nSelecione a dificildade do quiz:')
print('A) Fácil (3 questões)')
print('B) Médio (5 questões)')
print('C) Difícil (10 questões)')
while True:
    try:
        mode = input()

        if mode.lower() == 'a':
            noq = 3
            break
        elif mode.lower() == 'b':
            noq = 5
            break
        elif mode.lower() == 'c':
            noq = 10
            break
        noq = int(noq)
    except:
        print('Resposta invalida!')
print('\nCerto, vamos jogar! :)')

while noq != 0:
    pergunta()
    noq = noq -1

p = (100/len(played))*len(points)
print(f'Você acertou {len(points)} pontos ou {str(int(p))}%.')