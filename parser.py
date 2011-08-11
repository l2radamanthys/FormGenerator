#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constantes import *


class Form:
    """
        Clase base generador de formularios
    """
    def __init__(self):
        self.header = form.copy()
        self.fields = []


    def parse_data(self, data=[]):
        """
        """
        if "form" in data[0].lower():
            self.parse_headers(data.pop(0))

        while len(data) > 0:
            line = data.pop(0)
            if line[0] != '#': #preg si no es comentario
                parametros = line.lower().split(";")
                type = parametros.pop(0)

                if type == "select":
                    options = []
                    if data[0][0] == "%":
                         line = data.pop(0)[1:]
                         options = line.lower().split(";")
                    self.parse_select(parametros, options)

                else:
                    self.parse_field(parametros)




    def parse_headers(self, line):
        """
            Parsea las cabecera del formulario
        """
        parametros = line.lower().split(";")[1:]
        for param in parametros:
            key,value = param.split("=")
            self.header[key] = value



    def parse_field(self, parametros):
        """
        """
        type = parametros.pop(0)
        if type == "text":
            pass

        elif type == "img":
            pass

        elif type == "password":
            pass

        elif type == "checkbox":
            pass

        elif type == "radio":
            pass

        elif type == "textarea":
            pass

        elif type == "hidden":
            pass

        elif type == "submit":
            pass

        elif type == "reset":
            pass


    def parse_select(self, parametros, options):
        """
        """
        pass


    def parse_textarea(self, parametros):
        """
        """
        pass

        
    def generate(self):
        """
        """
        pass

    
    def generate_with_table(self):
        """
        """
        pass




