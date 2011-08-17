#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Prueba del modulo
"""

import form_parser as parser


def main():
    data = [
        "form;action=#;method=post;",
        "text;name=categoria;label=Categoria;class=edt_m;",
        "password;name=slug;label=SLUG;class=edt_m;",
        "radio;name=opcion;label=Si;class=edt;",
        "radio;name=opcion;label=No;class=edt;",
        "checkbox;name=reenviar;label=Reenviar:;class=edt;",
        "hidden;name=query;value=1;",
        "select;label=Sexo;name=nombre;class=edt;",
        "$M=Masculino;F=Femenino;N=No Definido;",
        "textarea;rows=10;cols=80;",
        "submit;value=Crear;",
        "reset;value=Limpiar;",
    ]

    form = parser.Form()
    form.parse_data(data)
    print form.generate(True) #genera formateado como tabla
    #print form.generate(False) #genera campo con etiquetas
    #print form.generate(False, False) #solo genera los campos
    raw_input("Enter para terminar..")

if __name__ == "__main__":
    main()