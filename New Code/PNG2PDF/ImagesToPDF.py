import os
from os import listdir
from os.path import isfile, join
import sys

def process(LOCATION):
    files = [f for f in listdir(LOCATION) if isfile(join(LOCATION, f))]
    stdout = sys.stdout
    sys.stdout = None
    print(files)
    PATH = LOCATION + '/output.tex'
    print(PATH)
    f = open(PATH, 'w')
    text = '''\\documentclass{article}
    \\usepackage{graphicx}
    \\begin{document}\n'''

    for i in files:
        if i[-4:] == '.png':
            text += '\\begin{figure}\n  \\includegraphics[width=\\linewidth]{' + i + '}\n\\end{figure}\n\\newpage\n'
            

    os.chdir(LOCATION)
    text += '\n\\end{document}'
    f.write(text)
    f.close()
    os.system(f'pdflatex output.tex /b') # Make pdf

    os.remove(LOCATION + '\\output.tex') # Remove unwanted files.
    os.remove(LOCATION + '\\output.aux')
    os.remove(LOCATION + '\\output.log')
    os.system('.\\output.pdf')
    sys.stdout = stdout
    
    return None

if __name__ == '__main__':
    LOCATION = input("Please input the directory path of the files you want to convert:\n>")
    process()