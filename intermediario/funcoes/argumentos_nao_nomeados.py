def multiplicacao(*args):
    total = 1;
    for num in args:
        total *= num

    return total

def verifica_paridade(num):
    if num % 2 == 0:
        return "par"
    
    return "impar"


num = multiplicacao(1,2,3,4,5,6)
print(num)
print(verifica_paridade(num))
    
