# Tutorial WEB

馃毃 Este material fue creado por Ana Julia Velez Rueda y como todo el repositorio se encuentra bajo licencia 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

>
> En este recorrido:
> - se basa en el material [http-tutorial](https://github.com/AJVelezRueda/http-tutorial/tree/master/tutorial/es) de los autores Franco Leonardo Bulgarelli y Ana Julia Velez Rueda
>
> - Retoma el material te贸rico [Introducci贸n a la arquitectura Web](https://docs.google.com/document/d/1LBqAhXPzn-aeN5BIRZBmIrU5RKiYvySyWH-2Jkn-kJw/edit#heading=h.kx1xmbyu1do6) generado por Franco Leonardo Bulgarelli
>

## 脥ndice
[Contenido del recorrido](#1-Web)
  * [1. Internet](#1-interntet)
  * [2. La Web](#2-web)
  * [3. Introducci贸n al concepto de Cloud Computing](#3-Cloud-computing)
  * [4. Arquitectura Web](#4-arquitectura-web)
  * [5. Protocolos de comunicaci贸n](#5-protocolos)
  * [6. Presentacion](#6-presentacion)

## [1. Internet](#1-interntet)

Internet se podr铆a definir como la red de redes de computadoras, conectadas por medio de un cableado f铆sico que permite intercambiar informaci贸n entre todos sus usuarios. 

Para acceder al servicio que ofrece la informaci贸n, debemos tener dos programas que se ejecutan en dos computadoras diferentes y que nos permiten compartir recursos. 

A la computadora que ejecuta el programa que proporciona el recurso o informaci贸n se la denomina **servidor** y a la computadora que consume un recurso o informaci贸n se la denomina **cliente**. En la computadora del cliente se ejecutar谩 entonces el programa que le permite utilizar el recurso o leer la informaci贸n.

Pero 驴Qu茅 tipo de recursos pueden brindarse o consimirse a trav茅s de internet? Por medio de Internet podemos enviar mensajes, programas ejecutables, archivos de texto, consultar bases de datos, etc.

## [2. La Web](#2-web)
La Web en particular, diminutivo de World Wide Web, es un conjunto de p谩ginas interconectadas por las cuales podemos navegar.

Estas p谩ginas web est谩n pensadas para consumir contenido hipertextual, es decir  contenido que contiene v铆nculos o enlaces a otros contenidos.

## [3. Introducci贸n al concepto de Cloud Computing](#2-Cloud-computing)

La computaci贸n en la nube o Cloud Computing es el consumo o prestaci贸n bajo demanda de recursos tecnologicos a trav茅s de Internet. 

En lugar de comprar y mantener servidores y centros de datos f铆sicos(es decir una super duper m谩quina en tu casa), pod茅s consumir los servicios tecnol贸gicos, como potencia inform谩tica, almacenamiento y bases de datos, seg煤n te sea necesario, en el momento que te sea necesario, de un proveedor.

## [4. Arquitectura Web](#4-arquitectura-web)

Los sistemas Web hoy en d铆a presentan en genarl una arquitectura distribuida, es decir que sus componentes est谩n distribuidos en dos tipos de nodos: **clientes** (muchos) y **servidores** (uno). En esta arquitectura, llamada `cliente-servidor`, los clientes se comunican con el servidor siguiendo un protocolo de pedido-respuesta en el que: 

* Un cliente hace un pedido, 
* El servidor procesa el pedido y responde.
* El cliente se encarga de presentar (renderizar) la respuesta al usuario final

Esta comunicaci贸n ocurre a trav茅s de redes Intranets o la misma Internet, empleando un protocolo llamado HTTP, sobre el cu谩l hablaremos en el punto siguiente.

Entonces en la arquitectura web `cliente-servidor`, los servidores son quienes almacenan y proveen la informaci贸n o recursos dados, y los clientes son responsables de presentar la informaci贸n al usuario, empleando tecnolog铆as espec铆ficas de la Web. 


>
> 馃 Para pensar: 驴qu茅 tecnolog铆as se usan en la Web? 驴En qu茅 se desarrolla un cliente? 驴Y un servidor?
>

## [5. Protocolos de comunicaci贸n](#5-protocolos)

驴Alguna vez te preguntaste c贸mo es que logramos comunicarnos los seres humanos? 驴C贸mo es que las palabras pueden estructurarse en conversaciones ordenadas? Bueno tal y como explica el Dr. Juan Eduardo Bonnin, <a href="https://www.youtube.com/watch?v=jrA70HwWnts&t=9s">en su video</a>, los seres humanos somos capaces de estructurar las palabras, y estas en oraciones que devienen en conversaciones. En este proceso se pone en juego no solo cuestiones ficiol贸gicas, sino tambi茅n cuestiones culturales y personales, como: la lengua, las normas sociales, los valores culturales, los intereses y prop贸sitos individuales. Por tanto, lo que pensamos como un simple intercambio de palabras, se convierte en una actividad compleja, matizada con el ritmo de todo esta informaci贸n extra...o meta 馃槤

Los protocolos, como ver谩s, forman parte de nuestras vidas m谩s de lo que pens谩bamos. Y estos pueden variar seg煤n el entorno en el que nos movemos. Cada 谩mbito posee sus propias reglas para la comunicaci贸n. No nos expresamos de igual modo cuando estamos en un recital, que cuando estamos en la facultad 驴No? 馃檹

Este conjunto de reglas de comunicaci贸n, impl铆citas o expl铆citas, se denomina protocolo y en Internet hay uno espec铆fico para establecer la comunicaci贸n entre servidores y clientes. Este protocolo fue creado para la transferencia de archivos hipertextuales y se llama justamente HTTP, por las siglas en ingl茅s de protocolo de transferencia de hipertexto (HyperText Transfer Protocol).

Este protocolo de comunicaci贸n empleado en la Web tiene ciertas caracter铆sticas que debemos tener en cuenta:
\
- **Pedido-Respuesta**: se abre una conexi贸n por cada pedido, que surge del cliente, y el servidor la cierra cuando ha enviado la respuesta

- **Stateless**: el protocolo per-s茅 no maneja ninguna noci贸n de memoria de pedidos anteriores

- **Textual**: se intercambian mensajes de **s贸lo texto**

- **Basado en c贸digos de respuesta**: incluso para los flujos de error; no hay memoria compartida, continuaciones, excepciones ni eventos

馃摑 [NOTA] Sobre esto hablaremos en el recorrido de [HTTTP y REST](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/HTTP_%26_REST.md)

## [6. Presentacion](#6-presentacion)

De lo que dijimos anteriormente se desprende que la presentaci贸n o representaci贸n de los datos por el servidor corren por parte del cliente. Seg煤n lo vivenciado navegando en internet sabemos que las presentaciones son mucho m谩s ricas e interactivas que simple texto. 隆Con el texto enviado por el servidor plano no nos alcanza!

Lo que el servidor responde normalmente es el c贸digo fuente de una p谩gina escrita usando una combinaci贸n de lenguajes, que es interpretado por un programa del cliente, el mismo programa que tambi茅n es responsable de crear las conexiones HTTP. 

驴Saben c贸mo se llama esta aplicaci贸n? Adivinaron, 隆es **el navegador** (browser)!

Los navegadores modernos son capaces de entender algunos lenguajes sin necesidad de ning煤n complemento (plugin), que son los que constituyen como el est谩ndar la Web:

* HTML: lenguajes basado en etiquetas, emparentado con XML, dise帽ado para estructurar informaci贸n

* CSS: lenguaje para formatear informaci贸n (estructurada en HTML)

* JS: lenguaje de prop贸sito general, que en los navegadores es utilizado para desarrollar cualquier l贸gica de aplicaci贸n. Este 煤ltimo nos permite entre otras cosas: 
  - Mutar, acceder a, y observar eventos del DOM (la representaci贸n del contenido HTML)
  - Implementar efectos visuales complejos; Realizar pedidos al servidor en segundo plano
  - Implementar navegabilidad del lado del cliente

馃摑 [NOTA]  En este curso vamos a hackear lo standard y omitir el uso JS, echando mano de una biblioteca de Python, que nos ayuda a recrear nuestras aplicaciones web de forma sencilla.  De ello vamos a hablar m谩s en el material sobre [maquetado web](https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/ipywidgets_y_maquetado.md)