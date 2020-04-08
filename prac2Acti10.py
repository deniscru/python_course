imagenes=['im1','im2','im3']

cantIngresadas=0

cantAIngresar=int(len(imagenes))

todas=[]

unaCoor=()

imagenes1=[]

sigue=True
while sigue:

    agregar=True                  #controlo de agregar las coordenadas a las imagenes

    x=int(input('ingrese una coordenada x: '))
    y=int(input('ingrese una coordenada y: '))
    for d in range(len(todas)):
        t=todas[d]                             #controla que no hay coordenadas repetidas
        if t[0]==x and t[1]==y:
            agregar=False

    if agregar:                                 #agrego las coordenadas a la imagenen de la lista
        if cantIngresadas>0:
            print('coordenada valida ')
        unaCoor=(x,y)
        todas.extend([unaCoor])
        imagenes1.extend([imagenes[cantIngresadas],unaCoor])
        cantIngresadas+=1
    else:
        print ('vuelve a ingresar otra coordenada, ya existe esta ')

    if cantIngresadas==cantAIngresar:
        sigue=False
print ('imagenes: ', imagenes1)
