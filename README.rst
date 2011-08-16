
Form Generator
==============

Sencillo generador de formularios HTML que permite generar formularios HTML a partir de
informacion simple


Sintaxis
--------
    la primera linea deve contener la definicion del formulario, junto con
    los parametros del mismo un ejemplo sencillo:

    form;action=parse.php;method=post;


    las lineas sucesivas son referentes a los campos del formulario,
    el primer valor es el tipo de campo los tipos de campo soportados
    por el momento son:

    - text
    - password
    - checkbox
    - radio
    - submit
    - reset
    - image
    - hidden
    - textarea
    - select

    Su sintasis es similar:

    >>> tipo;parametro1=val1;parametro2=val2;...

    ejemplo:

    >>> text;label=Nombre Usuario;name=nombre;class=edt;
    -> <label>Nombre Usuario</label><imput type="text" name="nombre" class="edt" />

    Es posible agregar lineas de comentarios anteponiendo al principio

    %exc%

    ejemplo:
        >>> %exc% Esto es un comentario, esta linea se obiara


    Parametros que comparten todos los Elementos
    ---------------------------------------------
    -name
    -id
    -class (**)
    -label (*)

    (*) Exepto los elementos hidden, sibmit y reset
    (**) Exepto los elementos hidden


    Parametros Elementos text
    -------------------------
    - value
    - size
    - maxlenght

