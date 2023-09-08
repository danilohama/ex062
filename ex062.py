"""Melhore o desafio 062, Perguntando para o usuario se ele quer mostrar mais alguns termos, o programa encerra quando
ele disser que quer mostrar o termos"""
print('\033[032m<>\033[32m' * 10)
print('   \033[031mGerador de PA\033[031m')
print('\033[032m<>\033[32;0m' * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[33m {}\033[33;0m -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('\033[031mPAUSA\033[031m')
    mais = int(input('\033[37mQuantos termos você quer mostrar a mais\033[37;0m? '))
print('\033[32mA Progressão foi finalizada com\033[32;0m \033[33m{}\033[33;0m \033[32mtermos mostrados\033[32m'.format(
    total))
