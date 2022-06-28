import os
import glob
import shutil


ruta = input("Ingresa la ruta donde quieres ordenar tus documentos")

#os.chdir("/home/Al3xmm14/Descargas")
os.chdir(ruta)
def crearCarpetas():
    while(True):
        if os.path.exists("pdf") == True:
            pass
        else:
            os.mkdir("pdf")
        if os.path.exists("Imagenes") == True:
            pass
        else:
            os.mkdir("Imagenes")

        if os.path.exists("Documentos") == True:
            pass
        else:
            os.mkdir("Documentos")
    
        if os.path.exists("Videos") == True:
            pass
        else:
            os.mkdir("Videos")
        
        if os.path.exists("programas") == True:
            pass
        else:
            os.mkdir("programas")
        
        if os.path.exists("RPM") == True:
            pass
        else:
            os.mkdir("RPM")
        if os.path.exists("Comprimidos"):
            pass
        else:
            os.mkdir("Comprimidos")
        break
        
    
def organizar():
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
        shutil.move(i, "RPM")
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

def OrdenamientoDocumentos():
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
    
    
    

    


    

crearCarpetas()
organizar()
OrdenamientoDocumentos()

