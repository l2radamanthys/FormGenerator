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



class TextField(DefaultField):
    def __init__(self):
        DefaultField.__init__()
        self.vale = None
        self.size = None
        self.maxlength = None


    def to_str(self):
        """
            Formatea como HTML
        """
        argvs = ""
        
        return "<input type=\"text\" %s />" %argvs


    def to_html(self, tbl_format=False):
        """
        """
        if tbl_format:
            out = """
\t<tr>
\t\t<td><label>%s</label></td>
\t\t<td>%s</td>
\t</td>""" %(self.label, self.to_str())
        else:
            out = "<label>%s</label>%s" %(self.label, self.to_str())
        return out