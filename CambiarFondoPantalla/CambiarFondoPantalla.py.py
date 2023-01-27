import ctypes
"""rutaImagen = "C:\\Users\\Alejandro Molina\\Downloads\\8-bitCity_1920x1080.jpg"""""
rutaImagen= "C:\\Users\\Alejandro Molina\\OneDrive\\Fotos\\CSC_0542.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, rutaImagen, 3)