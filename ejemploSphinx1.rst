=====================
Esto é unha cabeceira
=====================

Cabecera h1
***********

Título h2
=========

Título h3
---------

Título h4
+++++++++


Marcado dentro do texto
+++++++++++++++++++++++
Escribimos texto en varias lineas y esto forma un párrafo.
Lembrade que o tabulado é importante para que o entenda sphinx. Dentro do texto podemos
resañtar mediante *cursiva* ou **negriña** e ``dobres comillas para o código``.


Listas no numeradas
+++++++++++++++++++
* Podemos facer listas.
* De distintos elementos.
  Utilizando o * .

Listas numeradas
++++++++++++++++
1. Otra lista numerada
2. Utilizando o número seguido do punto.


#. Seguimos numerando listas
#. Neste caso utilizamos #.

Cun novo paragrafo no medio comeza a numeracion ?

#. Nova lista

Sublistas
+++++++++
* Lista
* con elementos

    * En novas sublistas
    * Con niveis

* E subniveis

Definicions
+++++++++++
Termino
    Definicion do término, mediante tabulacion


Outro termino.
    Coa súa definición


Saltos de liña
++++++++++++++

| Estas liñas se mostraran
| cos saltos de liña marcados
| se adaptarán ao tamaño da pantalla

Bloques de texto literales
++++++++++++++++++++++++++

O texto normal de paragrafo. O texto qe se mostra a
continuación serñia un bloque literal ::

    import sys

    class MinhaClase:
        #Por facer

Continuamos o texto o mesmo nivel de paragrafo a continuación.

>>> 2 + 2
4

Taboas
++++++

+---------------------------+---------------+--------------+------------+
| Cabeceira fila, columna 1 | cabecera 2    | cabecera 3   | cabecera 4 |
| Pode usar varias liñas    |               |              |            |
+===========================+===============+==============+============+
| Fila1, columna 1          | Fila 1, col 2 | aaaa         |  aaaa      |
+---------------------------+---------------+--------------+------------+
|         a                 |      a        |       a      |     a      |
+---------------------------+---------------+--------------+------------+


Listas
++++++
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======


Enlaces
+++++++

.. _cfr Daniel Castelao : http://www.danielcastelao.org/

Os enlaces non é necesario marcalos http://www.danielcastelao.org salvo que queiramos
a etiqueta para o enlace o `cole <http://www.danielcastelao.org/>`_


Outra forma de facelo é `cfr Daniel Castelao`_.



#doc en https://www.sphinx-doc.org/es/stable/rest.html

.. _Daniel Castelao:
.. figure:: _static/312523.png
  :align: center

Este é o texto de pé da imaxe

:download: `Baixa o exemplo.rst <_static/exemplo.rst>`_

.. note::
    Esta é unha advertencia

.. warning::
    Ollo con utilizar esta etiqueta!

.. versionchanged::
   0.0.1

.. versionadded::
   0.0.2


Para meter codigo no medio da páxina::

    def minhafuncion(variable,variable2=True):
        """Esta é unha funcion
            exempolo """
            return variable2

Si queremos introducir codigo dentreo dunha liña para mostrar
un comando como ``sphinix-quickstart``

podemos falar de módulos como :mod:  `threading` ou de clases como
:class:`threading.Thread` . Tamén podemos facer referencia a
funcions como :func: `time.time`

















