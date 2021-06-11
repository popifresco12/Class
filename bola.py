def implista():

    for i in range(10):
        for j in range(10):
            print(lista[i][j], end=" ")
        print()


lista=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
y=0
x=0
lista_instr=[]

contador=0

instrucciones=open("instrucciones.txt", "r")
#posicion x
listax=[]
penx=""
antepx=""
#penx=lista_x[-3]
#antepx=lista_x[-4]

#posicion y
listay=[]
peny=""
antepy=""
#peny=lista_y[-3]
#antepy=lista_y[-4]

    
for i in range(10):
    for j in range(10):
        if lista[i][j]==1:
            x=i
            y=j


for z in instrucciones:
    u=z.split(",")
    for p in u:
        if p=="arriba":
            if x==0:
                lista[9][y]="."
                lista[x][y]="*"
                x=0
                #metemos posicion en listas
                listax.append(x)
                listay.append(y)
                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
            else:
                lista[x-1][y]="."
                lista[x][y]="*"
                x=x-1

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
        if p=="abajo":
            if x==9:
                lista[0][y]="."
                lista[x][y]="*"
                x=9

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
            else:
                lista[x+1][y]="."
                lista[x][y]="o"
                x=x+1

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
        if p=="derecha":
            if y==9:
                lista[x][0]="."
                lista[x][y]="*"
                y=0

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len(listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len(listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
            else:
                lista[x][y+1]="."
                lista[x][y]="*"
                y=y+1

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
        if p=="izquierda":
            if y==0:
                lista[x][9]="."
                lista[x][y]="*"
                y=9

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len (listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len (listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"
            else:
                lista[x][y-1]="."
                lista[x][y]="*"
                y=y-1

                listax.append(x)
                listay.append(y)

                #if len lista > algo entonces rastro
                if len(listax) >= 3:
                    penx=listax[-3]
                    peny=listay[-3]
                    #pasamos a la lista
                    lista[penx][peny]="o"
                    
                if len(listax) >= 4:
                    antepx=listax[-4]
                    antepy=listay[-4]
                    #pasamos a la lista
                    lista[antepx][antepy]="O"



implista()
instrucciones.close()