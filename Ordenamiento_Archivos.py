import os
import glob
import shutil


def organizar(ruta):
    os.chdir(ruta)
    listaCarpetas = ["pdf", "Imagenes", "Documentos", "Videos", "Programas", "Aplicaciones", "Comprimidos" ]
    for i in listaCarpetas:
        while(True):
            if os.path.exists(i) == True:
                pass
            else:
                os.mkdir(i)
            break
    
    #Fotos
    png = glob.glob("*.png")
    jpg = glob.glob("*.jpg")
    
    #archivos
    pdf = glob.glob("*.pdf")
    docx = glob.glob("*.docx")
    txt = glob.glob("*.txt")
    
    #Aplicaciones Fedora
    rpm = glob.glob("*.rpm")

    #videos 
    mp4 = glob.glob("*.mp42")
    flv = glob.glob("*.flv")
    mkv = glob.glob("*.mkv")

    #programas
    py = glob.glob("*.py")
    c = glob.glob("*.c")
    cpp = glob.glob("*.cpp")
    html = glob.glob("*.html")

    rar = glob.glob("*.rar")
    tar = glob.glob("*.tar*")
    

    for i in (png):
        shutil.move(i, "Imagenes")
    for i in (jpg):
        shutil.move(i, "Imagenes")
    for i in (pdf):
        shutil.move(i, "pdf")
    for i in (docx):
        shutil.move(i, "Documentos")
    for i in (txt):
        shutil.move(i, "Documentos")
    for i in (rpm):
        shutil.move(i, "Aplicaciones")
    for i in (mp4):
        shutil.move(i, "Videos")
    for i in (flv):
        shutil.move(i, "Videos")
    for i in (mkv):
        shutil.move(i, "Videos")
    for i in (py):
        shutil.move(i, "programas")
    for i in (c):
        shutil.move(i, "Videos")
    for i in (cpp):
        shutil.move(i, "Videos")    
    for i in (html):
        shutil.move(i, "Videos")    
    for i in (rar):
        shutil.move(i, "Comprimidos")    
    for i in (tar):
        shutil.move(i, "Comprimidos")

"""def OrdenamientoDocumentos():
    os.chdir("/home/Al3xmm14/Descargas/Documentos")
    docx = glob.glob("*.docx")
    if os.path.exists("Word"):
        pass
    else:
        os.mkdir("Word")
    for i in (docx):
        shutil.move(i, "Word")
    os.chdir("/home/Al3xmm14/Descargas/Documentos")
    txt = glob.glob("*.txt")

    if os.path.exists("txt"):
        pass
    else:
        os.mkdir("txt")

    for i in (txt):
        shutil.move(i, "txt")
    os.chdir("/home/Al3xmm14/Descargas")
   """ 
def MENU ():
    ruta = None 
    listaCarpetas = ["pdf", "Imagenes", "Documentos", "Videos", "Programas", "Aplicaciones", "Comprimidos" ]
    a = True
    while(a == True):

        print("                 MENU ORDENAMIENTO (Linux)             \n\n")
        print("1.- Ver carpetas que se crearan                                       \n")
        print("2.- Colocar ruta de ordenamiento                                       \n")
        print("3.- Ver ruta de ordenamiento                                            \n")
        print("4.- Ordenar                                                              \n")
        print("5.- Salir                                                                 \n")
    
        opcion = int(input("Digite una opción: "))

        """if opcion == 1:
            os.system ("clear")
            carpetas = input("Digite el nombre de la carpeta: ")
            if carpetas in listaCarpetas:
                os.system ("clear")
                print("Este nombre ya estra registrado")
                os.system ("clear")
            else:
                os.system ("clear")  
                listaCarpetas.append(carpetas)
                print("Se registro: ", carpetas)
                input()
                os.system ("clear")"""
        if opcion == 1:   
            os.system ("clear")
            print(listaCarpetas)
            input()
            os.system ("clear")
        elif opcion == 2:
            ruta = input("Colocar ruta de ordenamiento: \n")
        elif opcion == 3:
            if ruta == None:
                os.system("clear")
                print("No se le a asignado una ruta:c")
                input("")
                os.system("clear")
            else:
                os.system("clear")
                print(ruta)
                input("")
                os.system("clear")
        elif opcion == 4:
            if ruta == None:
                os.system("clear")
                print("Primero asigne una ruta donde va a ordenar")
                input("")
                os.system("clear")
            else:
                os.system("clear")
                organizar(ruta)
                print("Se han organizado sus archivos correctamente...")
                input("")
                os.system("clear")  
        elif opcion == 5:
            break
        else:
            print("Error, Opcion no valida")



MENU()
    

