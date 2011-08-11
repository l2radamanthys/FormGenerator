#!/usr/bin/env python
# -*- coding: utf-8 -*-


#tags
html_ini = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>formulario generado</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <meta name="generator" content="FormGenerator" />
</head>

<body>
"""

html_end = "\n</body>\n</html>"



form_ini = "<form {tags} >"
form_end = "</form>"

#form definition
form = {
    "action": "#",
    "method": "post",
    "enctype": "",
    "name": "",
    "class": "",
    "id": "",
}

base_input = {
    "type": "text",
    "value": "",
    "size": "",
    "name": "",
    "label": "",
    "maxlength": "",
    "class": "",
    "id": "",
}

text = {
    "type": "text",
    "value": "",
    "size": "",
    "name": "",
    "label": "",
    "maxlength": "",
    "class": "",
    "id": "",
}

password = {
    "type": "password",
    "value": "",
    "size": "",
    "maxlength": "",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

checkbox = {
    "type": "checkbox",
    "value": "",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

radio = {
    "type": "checkbox",
    "value": "",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

image = {
    "type": "image",
    "src": "",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

submit = {
    "type": "submit",
    "value": "Submit",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

reset = {
    "type": "reset",
    "value": "Reset",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
}

hidden = {
    "type": "hidden",
    "value": "",
    "name": "",
    "class": "",
    "id": "",
}

textarea = {
    "type": "textarea",
    "name": "",
    "class": "",
    "id": "",
    "cols": "",
    "rows": "",
}

select = {
    "type": "select",
    "size": "",
    "name": "",
    "label": "",
    "class": "",
    "id": "",
    tags: {},
}

key_dict = {
    "form": form,
    "text": text,
    "password": password,
    "checkbox": checkbox,
    "radio": radio,
    "submit": submit,
    "reset": reset,
    "hidden": hidden,
    "image": image,
    "textarea": textarea,
    "select": select,
}





