resultado=""
anterior=""
historial=[]
funciones=["suma", "resta", "resto", "multi", "div", "neg", "fact", "pot", "AYUDA", "save", "igual", "memoria", "restart", "mostrar"]
hist_res=[]
saved=[]
n2=int(input("Numero: "))
operacion=""
hist_res.append(n2)
l=len(saved)




def suma():
    resultado=hist_res[-1]+n2
    anterior=resultado
    historial.append("suma")
    hist_res.append(resultado)
    print(resultado)
    return 1

def resta():
    resultado=hist_res[-1]-n2
    anterior=resultado
    historial.append("resta")
    hist_res.append(resultado)
    print(resultado)
    return 1

def multi():
    resultado=hist_res[-1]*n2
    anterior=resultado
    historial.append("multi")
    hist_res.append(resultado)
    print(resultado)
    return 1

def div():
    (resultado)=hist_res[-1]/n2
    anterior=resultado
    historial.append("div")
    hist_res.append(resultado)
    print(resultado)
    return 1

def resto():
    resultado=hist_res[-1]%n2
    anterior=resultado
    historial.append("resto")
    hist_res.append(resultado)
    print(resultado)
    return 1

def neg():
    resultado=hist_res[-1]*(-1)
    anterior=resultado
    historial.append("neg")
    hist_res.append(resultado)
    print(resultado)
    return 1

def fact():
    n1=hist_res[-1]
    f=n1-1
    for i in range(n1-1):
        resultado=n1*f
        f=f-1
    print(resultado)

def pot():
    resultado=hist_res[-1]**n2
    anterior=resultado
    historial.append("pot")
    hist_res.append(resultado)
    print(resultado)
    return 1
    
def AYUDA():
    for funcion in funciones:
        print(funcion)

def igual():
    if historial[-1]=="suma":
        suma()
    elif historial[-1]=="resta":
        resta()
    elif historial[-1]=="multi":
        multi()
    elif historial[-1]=="div":
        div()
    elif historial[-1]=="resto":
        resto()
    elif historial[-1]=="neg":
        neg()
    elif historial[-1]=="fact":
        fact()
    elif historial[-1]=="pot":
        pot()


def guardar():
    saved.append(hist_res[-1])
    if l>10:
        saved.pop(saved[0])
    else:
        pass
    print(saved)

def memoria():
    m=int(input("Memoria: "))
    n2=saved[m]
    print(saved)

def restart():
    resultado=""
    anterior=""
    historial=[]
    hist_res=[]
    saved=[]
    n2=int(input("Numero: "))
    hist_res.append(n2)
    operacion=input("Operacion: ")

def mostrar_m():
    print(saved)


while operacion!="salir":
    operacion=input("Operacion: ")
    if operacion=="+" or operacion=="suma":
        n2=int(input("Escribe un numero: "))
        if n2=="memoria":
            memoria()
        else:
            pass
        suma()
    elif operacion=="-" or operacion=="resta":
        n2=int(input("Escribe un numero: "))
        if n2=="memoria":
            memoria()
        resta()
    elif operacion=="*" or operacion=="multi":
        n2=int(input("Escribe un numero: "))
        if n2=="memoria":
            memoria()
        else:
            pass
        multi()
    elif operacion=="/" or operacion=="div":
        n2=int(input("Escribe un numero: "))
        if n2=="memoria":
            memoria()
        else:
            pass
        div()
    elif operacion=="%" or operacion=="resto":
        n2=int(input("Escribe un numero: "))
        if n2=="memoria":
            memoria()
        else:
            pass
        resto()
    elif operacion=="--" or operacion=="neg":
        neg()
    elif operacion=="!" or operacion=="fact":
        fact()
    elif operacion=="pot":
        n2=int(input("Escribe un numero: "))
        if n2==memoria:
            memoria()
        else:
            pass
        pot()
    elif operacion=="=" or operacion=="igual":
        igual()
    elif operacion=="guardar":
        guardar()
    elif operacion=="memoria":
        memoria()
    elif operacion=="restart":
        restart()
    elif operacion=="AYUDA":
        AYUDA()
    elif operacion=="mostrar":
        mostrar_m()
    else:
        break
    

