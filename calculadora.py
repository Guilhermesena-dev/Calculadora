
acumulador = 0.0 

def soma(a, b = None  ):
    global acumulador
    if b == None:
        return  acumulador + a 
    else: 
        acumulador = a + b 
    return a + b 

def subtrai(a, b = None ):
    global acumulador
    if b == None:
        return  acumulador -  a 
    else: 
        acumulador = a - b 
    return a + b 
def multiplica(a, b = None ):
    global acumulador
    if b == None:
        return  acumulador * a 
    else: 
        acumulador = a * b 
    return a + b 
def divisão(a, b = None ):
    global acumulador
    if b == None:
        return  acumulador / a 
    else: 
        acumulador = a  / b 
    return a + b 
 

