import linecache,os,pyperclip,re,fileinput
from tempfile import mkstemp
from shutil import move
from os import remove, close
Pasta = "C:\\Users\\sustu\\OneDrive\\Documentos\\MUGEN\\chars"
PastaORIGINAL = "C:\\Users\\sustu\\OneDrive\\Documentos\\MUGEN\\data\\select.def"
texto = "./Texto.txt"
def find_word_line_number(filename, target_word):
    line_number = 0
 
    with open(filename, 'r') as file:
        for line in file:
            line_number += 1
            if target_word in line:
                return line_number
 
    return None


file = open(PastaORIGINAL)
content = file.readlines()
ListArq = []
files = os.listdir(Pasta)
for file in files:
    ListArq.append(file)

Personagens = str(ListArq).replace("'","").replace("[","").replace("]","").replace(",","\n")

String = open(texto).read()
new_String = re.sub(str(ListArq),'',String)

 
filename = "Texto.txt"
word_to_find = "[Characters]"    
line_number = find_word_line_number(filename, word_to_find) + 1


file_path = "Texto.txt"

fh_r = open(file_path)
fh, abs_path = mkstemp()
fh_w = open(abs_path, 'w')

for i, line in enumerate(fh_r):
    if i == line_number - 1:
        fh_w.write(Personagens + line)
    else:
        fh_w.write(line)

fh_r.close()
close(fh)
fh_w.close()

remove(file_path)
move(abs_path, file_path)


pyperclip.copy(Personagens)