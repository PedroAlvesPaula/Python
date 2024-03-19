palavra_secreta = "paralelepipedo"
cont = 0
stop = True
digitado_pelo_usuario =''

while stop:
    letra_digitada_pelo_usuario = input('Tente adivinhar a palavra, digite uma letra: ')

    letra_digitada_pelo_usuario = letra_digitada_pelo_usuario.lower()

    if len(letra_digitada_pelo_usuario) > 1:
        print('Entrada inválida, digite apenas uma letra!!')
        continue
    elif  letra_digitada_pelo_usuario.isdigit():
        print('São aceitas somente letras')
        continue
    
    palavra_formada_pelo_usuario =''

    if letra_digitada_pelo_usuario in palavra_secreta:

        digitado_pelo_usuario += letra_digitada_pelo_usuario

        for letra_secreta in palavra_secreta:

            if letra_secreta in digitado_pelo_usuario:
                palavra_formada_pelo_usuario += letra_secreta
            else:
                palavra_formada_pelo_usuario += '*'
    else:
        print('*')
        continue

    print(palavra_formada_pelo_usuario)

    cont += 1
    
    if palavra_formada_pelo_usuario in palavra_secreta:
        print(f'Parabéns, você acertou a palavra "cavalo" após {cont} tentativas. ')
        stop = False
    
   