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


    def to_html(self):
        """
        """
        pass


    def to_html_lbl(self, tbl_format=False):
        """
            Formatea como HTML y agrega la Etiqueta label
        """
        if self.label == None:
            self.label = self.name

        if tbl_format: #si desea formatear como tabla
            out = """\t<tr>
\t\t<td><label>%s</label></td>
\t\t<td>%s</td>
\t</tr>""" %(self.label, self.to_html())
        else:
            out = "<label>%s</label>%s<br />" %(self.label, self.to_html())
        return out


    def __str__(self):
        return "DefaultField"


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


    def __str__(self):
        return "TextField"


class PasswordField(TextField):
    """
        Solo varia respecto al tipo pero contiene los mismo campos q un
        TextField
    """
    def __init__(self):
        TextField.__init__(self)
        

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

        return "<input type=\"password\" %s/>" %argvs


    def __str__(self):
        return "PasswordField"


class RadioField(DefaultField):
    """
    """
    def __init__(self):
        DefaultField.__init__(self)
        self.value = None


    def set_values(self, dict={}):
        """
            Carga los valores a partir de un Diccionario
        """
        self._set_values(dict)
        self.value = dict.get("value", "")


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if self.value != "":
            argvs += "value=\"%s\"" %self.value

        return "<input type=\"radio\" %s/>" %argvs


    def __str__(self):
        return "RadioField"


class CheckBoxField(RadioField):
    """
    """
    def __init__(self):
        RadioField.__init__(self)


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if self.value != "":
            argvs += "value=\"%s\"" %self.value

        return "<input type=\"checkbox\" %s/>" %argvs


    def __str__(self):
        return "CheckBoxField"

        
#---#
class HiddenField(RadioField):
    """
    """
    def __init__(self):
        RadioField.__init__(self)


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if self.value != "":
            argvs += "value=\"%s\"" %self.value

        return "<input type=\"hidden\" %s/>" %argvs


    def to_html_lbl(self, tbl_format=False):
        """
            Metodo rescrito solo para mantener compatibilidad, este campo
            no requiere una etiqueta identificatoria
        """
        #if self.label == None:
        #    self.label = self.name

        if tbl_format: #si desea formatear como tabla
            out = """\t<tr>
\t\t<td colspan="2">%s</td>
\t</tr>""" %self.to_html()
        else:
            out = "%s<br />" %self.to_html()
        return out


    def __str__(self):
        return "HiddenField"


class ButtonField(HiddenField):
    def __init__(self, type=""):
        HiddenField.__init__(self)
        self.type = type


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if not(self.type in ("submit", "reset")):
            self.type = "button"

        if self.value != "":
            argvs += "value=\"%s\"" %self.value

        return "<input type=\"%s\" %s/>" %(self.type, argvs)


class ImageField(DefaultField):
    """
    """
    def __init__(self):
        DefaultField.__init__(self)


    def __str__(self):
        return "ImageField"


class TextAreaField(DefaultField):
    """
    """
    def __init__(self):
        DefaultField.__init__(self)
        self.rows = None
        self.cols = None
        self.text = None
        self.tabindex = None
        self.wrap = None


    def set_values(self, dict={}):
        """
            Carga los valores a partir de un Diccionario
        """
        self._set_values(dict)
        self.text = dict.get("text", "")
        self.rows = dict.get("rows", "")
        self.cols = dict.get("cols", "")
        self.tabindex = dict.get("tabindex", "")
        if dict.get("wrap", "") in ("off", "virtual", "physical"):
            self.wrap = dict.get("wrap", "")
        else:
            self.wrap = ""
            

    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if self.rows != "":
            argvs += "rows=\"%s\" " %self.rows

        if self.cols != "":
            argvs += "cols=\"%s\" " %self.cols

        if self.tabindex != "":
            argvs += "value=\"%s\" " %self.tabindex

        if self.wrap != "":
            argvs += "wrap=\"%s\" " %self.wrap

        return "<textarea %s/>%s</textarea>" %(argvs, self.text)


    def __str__(self):
        return "TextAreaField"


class SelectField(DefaultField):
    """
    """
    def __init__(self, opt_list={}):
        DefaultField.__init__(self)
        self.size = None
        self.multiple = None
        self.opt_list = opt_list


    def set_values(self, dict={}):
        """
            Carga los valores a partir de un Diccionario
        """
        self._set_values(dict)
        self.size = dict.get("size", "")
        if dict.get("multiple", "") in ("yes", "no"):
            self.multiple = dict.get("multiple", "")
        else:
            self.multiple = ""


    def to_html(self):
        """
            Formatea como HTML
        """
        argvs = self.to_str() #cargar argumentos por defecto

        if self.size != "":
            argvs += "size=\"%s\" " %self.size

        if self.multiple != "":
            argvs += "multiple=\"%s\" " %self.multiple

        txt ="\n<select %s>\n" %argvs
        for key in self.opt_list:
            txt += "\t\t<option value=\"%s\">%s</option>\n"  %(key, self.opt_list[key])
        txt += "<\select>\n"
        return txt
    

    def __str__(self):
        return "SelectField"