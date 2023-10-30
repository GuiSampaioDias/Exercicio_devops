def soma(a,b):
    try:
        return a + b
    except:
        return "Erro"
    
def multiplicacao(a,b):
    try:
        return a * b
    except:
        return "Erro"

def main():
    print(soma(10,5))
    pri = int(input('pri: '))
    seg = int(input('seg: '))
    print(multiplicacao(pri, seg))
main()