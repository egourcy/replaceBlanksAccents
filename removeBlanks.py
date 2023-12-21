import os
import sys

# Replace blank spaces with "-" character & remove accents
def split(path):
  folder = os.listdir(path)
  counter = 0
  for files in folder:
    blank = files.find(' ')
    if (blank != -1):
      replace = files.replace(' ', '-')
      replace = replace.replace('á', 'a')
      replace = replace.replace('é', 'e')
      replace = replace.replace('é', 'i')
      replace = replace.replace('ó', 'o')
      replace = replace.replace('ú', 'u')
      replace = replace.replace('Á', 'A')
      replace = replace.replace('É', 'E')
      replace = replace.replace('Í', 'I')
      replace = replace.replace('Ó', 'O')
      replace = replace.replace('Ú', 'U')
      replace = replace.replace('ñ', 'n')
      replace = replace.replace(',', '')
      #Detect OS
      #Windows
      #os.rename(path+"\\"+files, path+"\\"+replace)
      #Mac
      os.rename(path+files, path+replace)
      print("\n", replace)
      counter += 1
  
  print("\nSe modificaron ", counter , " archivos\n")

# Select path
def setDiectory(directory):
  try:
    if (directory):
     split(directory)
  except:
    question = input("No paso argumentos o el directorio es incorrecto, ¿Desea continuar con el directorio actual? (S/N) ")
    if (question == 'S' or question == 's' or question == 'SI' or question == 'Si' or question == 'si'):
      split(os.getcwd())
#
# __main__
#
if __name__ == '__main__':
  setDiectory(sys.argv[1])