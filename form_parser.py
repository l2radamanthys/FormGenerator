#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constantes import *
from elementos import *


class Form:
    """
        Clase base generador de formularios
    """
    def __init__(self):
        self.header = {} #form.copy()
        self.fields = []


    def remove_blank(self, data=[]):
        """
            Elimina espacios en blancos y comentarios
        """
        _data = []
        for line in data:
            if len(line) > 5 and not("%exc%" in line):
                _data.append(line)
        return _data


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
                if data[0][0] == "$":
                    line = data.pop(0)[1:]
                    options = line.split(";")
                field = self.parse_select(parametros, options)

            elif type == "text":
                field = self.parse_text(parametros)

            elif type == "image":
                field = self.parse_image(parametros)

            elif type == "password":
                field = self.parse_password(parametros)

            elif type == "checkbox":
                field = self.parse_checkbox(parametros)

            elif type == "radio":
                field = self.parse_radio(parametros)

            elif type == "textarea":
                field = self.parse_textarea(parametros)

            elif type == "hidden":
                field = self.parse_hidden(parametros)

            elif type == "submit":
                field = self.parse_button(parametros, "submit")

            elif type == "reset":
                field = self.parse_button(parametros, "reset")

            elif type == "button":
                field = self.parse_button(parametros, "button")

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


    def headers_to_str(self):
        """
        """
        argvs = ""
        for key in self.header:
            argvs += " %s=%s" %(key, self.header[key])
        return "<form %s >"  %argvs


    #demaciado codigo repetido -.-
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
        dict = {}
        field = PasswordField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def parse_checkbox(self, parametros):
        """
        """
        dict = {}
        field = CheckBoxField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def parse_radio(self, parametros):
        """
        """
        dict = {}
        field = RadioField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def parse_hidden(self, parametros):
        """
        """
        dict = {}
        field = HiddenField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def parse_button(self, parametros, type=""):
        """
        """
        dict = {}
        field = ButtonField(type)
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def parse_select(self, parametros, options):
        """
        """
        dict = {}
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value

        opt_list = {}
        for opt in options:
            if len(opt.split("=")) == 2:
                key,value = opt.split("=")
                opt_list[key] = value


        field = SelectField(opt_list)
        field.set_values(dict)
        return field


    def parse_textarea(self, parametros):
        """
        """
        dict = {}
        field = TextAreaField()
        for param in parametros:
            if len(param.split("=")) == 2:
                key,value = param.split("=")
                dict[key.lower()] = value
        field.set_values(dict)
        return field


    def generate(self, with_table=False, labels=True):
        """
        """
        txt = ""
        if with_table:
            txt += "<table>\n"
            #print self.fields
            for field in self.fields:
                #print field #para debug
                txt += "%s\n" %field.to_html_lbl(True)
            txt += "</table>\n"
        else:
            if labels:
                for field in self.fields:
                    txt += "%s\n" %field.to_html_lbl()
            else:
                for field in self.fields:
                    txt += "%s\n" %field.to_html()

        return html_ini + self.headers_to_str() + "\n" + txt + "</form>" +  html_end


