#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DefaultField:
    """
        Contenedor Basico con elementos comunes a contenedor
    """
    def __init__(self):
        self.name = None
        self.id = None
        self._class = None
        self.label = None


    def _to_str(self):
        argvs = ""
        if self.name:
            argvs += " %s=\"%s\"" %("name",self.name)
        if self.id:
            argvs += " %s=\"%s\"" %("id",self.id)
        if self._class:
            argvs += " %s=\"%s\"" %("class",self._class)
        return argvs


    def set_values(self, dict={}):
        """
            este metodo se implementara en las clases hijas
            para carga de datos
        """
        pass


    def _set_values(self, dict={}):
        """
            Carga los parametros por defecto de todas las clases
        """
        self.name = dict.get("name", "")
        self.id = dict.get("id", "")
        self._class = dict.get("class", "")
        self.label = dict.get("label", "")


    def to_str(self):
        """
        """
        argvs = ""
        if self.name != "":
            argvs += "name=\"%s\" " %self.name
        if self.id != "":
            argvs += "id=\"%s\" " %self.id
        if self._class != "":
            argvs += "class=\"%s\" " %self._class
        return argvs



class TextField(DefaultField):
    def __init__(self):
        DefaultField.__init__(self)
        self.value = None
        self.size = None
        self.maxlength = None


    def set_values(self, dict={}):
        """
            Carga los valores a partir de un Diccionario
        """
        self._set_values(dict)
        self.value = dict.get("value", "")
        self.size = dict.get("size", "")
        self.maxlenght = dict.get("maxlenght", "")


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto
        
        if self.value != "":
            argvs += "value=\"%s\"" %self.value
        if self.size != "":
            argvs += "size=\"%s\"" %self.size
        if self.maxlenght != "":
            argvs += "maxlenght=\"%s\"" %self.maxlenght
            
        return "<input type=\"text\" %s/>" %argvs


    def to_html_lbl(self, tbl_format=False):
        """
            Formatea como HTML y agrega la Etiqueta label
        """
        if self.label == None:
            self.label = self.name

        if tbl_format: #si desea formatear como tabla
            out = """
\t<tr>
\t\t<td><label>%s</label></td>
\t\t<td>%s</td>
\t</td>""" %(self.label, self.to_html())
        else:
            out = "<label>%s</label>%s" %(self.label, self.to_html())
        return out