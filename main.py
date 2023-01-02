
x = 1
def sumador(**kwargs):
    inicial =  kwargs['incial'] if  'inicial' in kwargs else 0  
    final = kwargs['final'] if 'final' in kwargs else inicial
    
    resultado = 0
    for x in range(inicial,final + 1):
        resultado += x
        
        return resultado 
    
    print(sumador(inicial = 5))
    
    