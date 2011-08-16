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
        "text;name=slug;label=SLUG;class=edt_m;",
    ]

    form = parser.Form()
    form.parse_data(data)
    print form.generate(True)
    print form.generate(False)
    print form.generate(False, False)
    raw_input("fin")

if __name__ == "__main__":
    main()