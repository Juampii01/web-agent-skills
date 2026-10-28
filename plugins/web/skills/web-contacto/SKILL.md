---
name: web-contacto
description: >-
  Conecta el formulario de una web con WhatsApp (y opcionalmente con el correo)
  para que cada visita termine en un mensaje: arma el formulario, el botón
  flotante y el mensaje ya escrito con los datos del cliente. Usala cuando el
  usuario diga "conectá el formulario", "que me lleguen los mensajes por
  WhatsApp", "agregá un botón de WhatsApp", "el formulario no manda nada",
  "/web-contacto", o pida captar clientes desde su web.
---

# web-contacto

El objetivo: que nadie se vaya de la web sin una forma de escribir en un toque,
y que el mensaje que llega ya diga quién es, qué quiere y para cuándo, así el
dueño puede contestar sin preguntar nada.

## Qué pedir

1. El número de WhatsApp con código de país, sin espacios ni signos
   (Argentina: `549` + característica sin 0 + número sin 15, por ejemplo
   `5491123456789`).
2. Qué datos necesita para contestar bien (servicio, fecha, presupuesto,
   zona). Máximo 4 campos además del nombre: cada campo extra baja las consultas.
3. Si quiere también recibir copia por correo (opcional, ver abajo).

## Qué hacer

1. Copiá el bloque de `assets/contacto.html` dentro de la web: tiene el
   formulario, el botón flotante y el script.
2. Ajustá los campos al negocio y escribí la plantilla del mensaje en
   `data-plantilla`, con los nombres de los campos entre llaves:
   `Hola, soy {nombre}. Quiero {servicio} para el {fecha}.`
3. Cambiá `data-numero` por el número del usuario.
4. Revisá el texto del botón: dice qué pasa ("Escribinos por WhatsApp"), no "Enviar".
5. Probalo: completá el formulario y verificá que abre WhatsApp con el
   mensaje bien armado, en el celular y en la computadora.

## Cómo funciona

Al enviar, el script valida los campos, arma el texto con la plantilla y abre
`https://wa.me/NUMERO?text=MENSAJE`. En el celular abre la app; en la
computadora, WhatsApp Web. La persona solo toca "Enviar" en WhatsApp.

No hay servidor de por medio, así que funciona en cualquier hosting gratis
(Netlify, Vercel, GitHub Pages).

## Copia por correo (opcional)

Si el usuario quiere además un registro por correo, usá un servicio de
formularios sin servidor (por ejemplo Formspree o Web3Forms, ambos con plan
gratis): el usuario crea su cuenta, te pasa el endpoint y se agrega como
`data-correo="https://..."`. El script lo manda en segundo plano antes de abrir
WhatsApp. No crees cuentas a nombre del usuario.

## Reglas

- El número también va escrito visible en la web (como texto que se puede
  copiar), por si WhatsApp no abre.
- Nada de pop-ups que tapan la web a los 3 segundos.
- El botón flotante no tapa otros botones en el celular.
- Los mensajes de error dicen qué falta: "Falta tu nombre para saber cómo saludarte."
