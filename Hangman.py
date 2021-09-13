import random
import os
from time import sleep

def chamar_nome():
    print('----====>>>>HaNgMaN<<<<====----\n')

board = [
'''
 +-----+
 |     |
       |
       |
       |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
       |
       |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
 |     |
       |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
/|     |
       |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
/|\    |
       |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
/|\    |
/      |
       |
==============
''',
'''
 +-----+
 |     |
 O     |
/|\    |
/ \    |
       |
==============
''']

letras_e = []
letras_c = []
palavra_lista = []

class Hangman():
    def __init__(self, aPalavra):
        self.palavra = aPalavra
        for i in self.palavra:
            palavra_lista.append('_')

    def adivinha(self):
        self.status_do_jogo()
        resp = str(input('Coloque uma letra: ')).upper()
        rec = self.verifica(resp)
        if rec == True:
            if resp in self.palavra:
                print('Opa, acertou. Essa letra existe em nossa palavra!\n')
                letras_c.append(resp)
                for j, i in enumerate(self.palavra):
                    if i == resp:
                        palavra_lista.insert(j, resp)
                        palavra_lista.pop(j+1)
            else:
                print('ERROU, na nossa palavra misteriosa não existe essa letra!\n')
                letras_e.append(resp)
        sleep(1.5)
        os.system('cls')

        self.adivinha_palavra()

    def adivinha_palavra(self):
        self.status_do_jogo()
        if len(letras_e) != 6:
            pergunta = str(input('Quer arriscar a palavra? [S para SIM / Qualquer tecla para NÃO]')).strip().upper()
            if pergunta == 'S':
                pergunta = str(input('Digite: ')).strip().upper()
                if pergunta == self.palavra:
                    palavra_lista.clear()
                    for i in self.palavra:
                        palavra_lista.append(i)
                else:
                    print('Não é essa a palavra ainda!')
        sleep(1.5)
        os.system('cls')

    def status_do_jogo(self):
        print('STATUS:', end=' ')
        print(board[len(letras_e)])
        print('PALAVRA: ', end='')
        for i in palavra_lista:
            print(i, end=' ')
        print()
        print(f'Letras erradas:', end=' ')
        for i in letras_e:
            print(i, end='  ')
        print()
        print(f'Letras certas:', end=' ')
        for i in letras_c:
            print(i, end='  ')
        print('\n')

    def fim_de_jogo(self):
        if '_' not in palavra_lista:
            print('PARABÉNS, VOCÊ VENCEU!!!')
        elif len(letras_e) == 6:
            print('ENFORCADO!!! Você perdeu...')

    def verifica(self, letra):
        if letra in letras_e or letra in letras_c:
            print('Você já digitou essa letra, digite outra!')
            return False
        else:
            return True


def palavra_ra():
    with open('palavras.txt', 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip().upper()

def main():
    jogar_novamente = 'S'
    while jogar_novamente == 'S':
        game = Hangman(palavra_ra())
        while True:
            chamar_nome()
            game.adivinha()

            if '_' not in palavra_lista or len(letras_e) == 6:
                break
        game.status_do_jogo()
        game.fim_de_jogo()

        print(f'A palavra é: {game.palavra}')
        sleep(5)
        jogar_novamente = str(input('Deseja jogar novamente [S para sim]\n')).strip().upper()
        letras_c.clear()
        letras_e.clear()
        palavra_lista.clear()

if __name__ == '__main__':
    main()
