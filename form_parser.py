#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constantes import *
from elementos import *


class Form:
    """
        Clase base generador de formularios
    """
    def __init__(self):
        self.header = form.copy()
        self.fields = []


    def remove_blank(self, data=[]):
        """
            Elimina espacios en blancos y comentarios
        """
        pass


    def parse_data(self, data=[]):
        """

        """
        self.remove_blank(data)
        if "form" in data[0].lower():
            self.parse_headers(data.pop(0))

        while len(data) > 0:
            line = data.pop(0)
            
            #parametros = line.lower().split(";")
            parametros = line.split(";")
            type = parametros.pop(0)
            if type == "select":
                options = []
                line = data.pop(0)[1:]
                options = line.lower().split(";")
                self.parse_select(parametros, options)

            if type == "text":
                field = self.parse_text(parametros)

            elif type == "image":
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

            self.fields.append(field)


    def parse_headers(self, line):
        """
            Parsea las cabecera del formulario
        """
        #parametros = line.lower().split(";")[1:]
        parametros = line.split(";")[1:]
        #print parametros #debug line
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                self.header[key.lower()] = value


    def parse_text(self, parametros):
        """
        """
        #parametros = line.lower().split(";")[1:]
        dict = {}
        field = TextField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field



    def parse_password(self, parametros):
        """
        """
        pass


    def parse_checkbox(self, parametros):
        """
        """
        pass


    def parse_radio(self, parametros):
        """
        """
        pass


    def parse_hidden(self, parametros):
        """
        """
        pass


    def parse_button(self, parametros):
        """
        """
        pass


    def parse_select(self, parametros, options):
        """
        """
        pass


    def parse_textarea(self, parametros):
        """
        """


    def generate(self, with_table=False, labels=True):
        """
        """
        txt = ""
        if with_table:
            for field in self.fields:
                txt += "%s\n" %field.to_html_lbl(True)

        else:
            if labels:
                for field in self.fields:
                    txt += "%s\n" %field.to_html_lbl()
            else:
                for field in self.fields:
                    txt += "%s\n" %field.to_html()
        return txt


