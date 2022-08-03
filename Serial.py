import serial, time, os
apps = {'Bloc de notas':'Notepad.exe', 
        'Chrome':'"C:\Program Files\Google\Chrome\Application\Chrome.exe"', 
        'Proteus 7':'"C:\Program Files (x86)\Labcenter Electronics\Proteus 7 Professional\BIN\ISIS.exe"', 
        'Whatsapp':'Whatsapp.exe'} # Aplicaciones
#Alistando puerto serial
port = "COM1"
v = 1200
bs = 8
pr = 'N'
tout = 1
set = serial.Serial(puerto = port,baudrate = v, bytesize = bs,parity = pr,timeout = tout)

#Funciones
def menu() -> None:
    print('Escoger aplicacion'.center(30,'-'))
    print(f'\t1 >> Bloc de notas\n\t2 >> Word\n\t3 >> Calculadora\n\t4 >> Whatsapp\n\t5 >> Salir\n\n\n')

def aplicacion(app) -> None:
    os.system(app)

#Bucle infinito que sigue hasta que se genere el break
while(True):
    time.sleep(2)
    menu()
    #var = int(input('Escoger aplicacion: '))
    print('Escoger aplicacion: ')
    var = set.read()
    #Relacionado con la seleccion
    if (var == b'1'):
        print(f'Usted ha seleccionado la aplicacion "Bloc de notas"')
        aplicacion(apps.get('Bloc de notas'))
    elif (var == b'2'):
        print(f'Usted ha seleccionado la aplicacion "Word"')
        aplicacion(apps.get('Word'))
    elif (var == b'3'):
        print(f'Usted ha seleccionado la aplicacion "Proteus 7"')
        aplicacion(apps.get('Proteus 7'))
    elif (var == b'4'):
        print(f'Usted ha seleccionado la aplicacion "Whatsapp"')
        aplicacion(apps.get('Whatsapp'))
    #elif var == 5:
        #print('Gracias por usar')
        #break
    else:
        print('Valor invalido')

set.close()
