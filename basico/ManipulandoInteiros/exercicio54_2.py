hour = input('Digite a apenas a hora (ex 17, 18 ou 13): ')

hour_int = int(hour)

if hour_int > 24 or hour_int < 0:
    print('Digite uma hora válida')
elif hour_int >= 0 and hour_int < 12:
    print('Bom dia')
elif hour_int >= 12 and hour_int < 18:
    print('Boa tarde')
else:
    print('Boa noite')