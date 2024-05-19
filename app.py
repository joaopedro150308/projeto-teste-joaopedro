print('Estamos no nosso primeiro projeto!')
while True:
    while True:
        sei_la = str(input('Você quer começar à aprender a automatizar???? [S/N] ')).upper().strip()[0]
        if sei_la in 'SN':
            break
    if sei_la == 'S':
        print('Puxa! Eu também!!!')
    else:
        print('Problema seu! Eu quero.')