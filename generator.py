#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Interprete via comando
    uso:

    $> python generador.py [-t|-n] [-nav|-txt] entrada

    Nota: por defecto la salida es en formato txt, sin tablas
"""

from sys import argv
from os import system

from form_parser import Form



def main():
    print """
        -------------
        FormGenerator
        -------------
    """
    use_tbl = False
    open_with = EDITOR

    #si se formateara como tabla
    if len(argv) == 4:
        if argv[1] == "-t":
            use_tbl = True

        elif argv[1] == "-n":
            use_tbl = False

        else:
            print "ERROR: use $> generador.py [-t|-n] [-nav|-txt] entrada"
            print argv
            return -1

        #como se mostrara la salida
        if argv[2] == "-nav":
            open_with = NAVEGADOR

        elif argv[2] == "-txt":
            open_with = EDITOR

        else:
            print "ERROR: use $> generador.py [-t|-n] [-nav|-txt] entrada"
            print argv
            return -1

    if len(argv) == 3:
        if argv[1] == "-t":
            use_tbl = True

        elif argv[1] == "-n":
            use_tbl = False

        elif argv[1] == "-nav":
            open_with = NAVEGADOR

        elif argv[1] == "-txt":
            open_with = EDITOR

        else:
            print "ERROR: use $> generador.py [-t|-n] [-nav|-txt] entrada"
            print argv
            return -1
    
    if len(argv) < 2:
        print "ERROR: use $> generador.py [-t|-n] [-nav|-txt] entrada"
        print argv
        return -1

    form = Form()
    data = open(argv[-1], "r").readlines()
    form.parse_data(data)
    text = form.generate(use_tbl)
    out_name = argv[-1] + ".html" #nombre de archivo de salida
    out = open(out_name, "w")
    out.write(text)
    out.close()
    print "Salida:", out_name
    system("%s %s" %(open_with, out_name))


if __name__ == "__main__":
    main()
