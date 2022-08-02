#import serial
import time
import os
apps = {'Bloc de notas':'Notepad.exe', 
        'Word':'Word.exe', 
        'Calculadora':'Calculator.exe', 
        'Whatsapp':'Whatsapp.exe'} # Aplicaciones

#port = "COM4"
#v = 9600
#set = serial.Serial(puerto = port,baudrate = v)

#int = int(set.readline())
#Funciones
def menu() -> None:
    print('Escoger aplicacion'.center(30,'-'))
    print(f'\t1 >> Bloc de notas\n\t2 >> Word\n\t3 >> Calculadora\n\t4 >> Whatsapp\n\t5 >> Salir\n\n\n')

def aplicacion(app) -> None:
    os.system(app)

#Bucle infinito que sigue hasta que se genere el break
while(True):
    time.sleep(1)
    menu()
    #respuesta_bytes = set.read()
    var = int(input('Escoger aplicacion: '))
    #print('Escoger aplicacion: ')
    #int = int(set.readline())
    #Relacionado con la seleccion
    if var == 1:
        print(f'Usted ha seleccionado la aplicacion "Bloc de notas"')
        aplicacion(apps.get('Bloc de notas'))
    elif var == 2:
        print(f'Usted ha seleccionado la aplicacion "Word"')
        aplicacion(apps.get('Word'))
    elif var == 3:
        print(f'Usted ha seleccionado la aplicacion Calculadora')
        aplicacion(apps.get('Calculadora'))
    elif var == 4:
        print(f'Usted ha seleccionado la aplicacion Whatsapp')
        aplicacion(apps.get('Whatsapp'))
    elif var == 5:
        print('Gracias por usar')
        break
    else:
        print('Valor invalido')

#set.close()
