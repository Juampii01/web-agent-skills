---
name: web-crear
description: >-
  Arma una web completa y lista para publicar a partir de la descripción de un
  negocio: textos, secciones, diseño propio, animaciones y formulario, en un
  solo archivo HTML, sin que se note que la hizo una IA. Usala cuando el
  usuario diga "armame una web", "haceme una landing", "necesito una página
  para mi negocio", "quiero una web como la de [marca]", "/web-crear", o
  describa su negocio y pida una página. También en inglés: "build me a
  website", "make a landing page".
---

# web-crear

Tu trabajo es entregar una web que parezca hecha por un estudio de diseño
caro, no por una IA ni con una plantilla. El cliente ya vio cien landings con
degradado violeta, tarjetas redondeadas y "Llevá tu negocio al siguiente
nivel". Si la tuya se parece a esas, fallaste aunque funcione.

## 1. Entender el negocio (máximo 5 preguntas)

Si el usuario ya contó lo necesario, no preguntes. Si falta, preguntá solo lo
que cambia el resultado, en un único mensaje:

1. ¿Qué vendés y a quién? (una frase)
2. ¿Qué tiene que hacer la persona al terminar de ver la web? (escribir por
   WhatsApp, reservar, comprar, pedir presupuesto)
3. ¿Tenés fotos propias, logo o colores de marca? (si no, se proponen)
4. ¿Hay una web que te guste? (el link sirve de referencia de nivel, no se copia)
5. Datos reales: dirección, horarios, precios, WhatsApp. **Nunca inventes
   números, reseñas, clientes ni premios.** Lo que falte va como
   `{{precio}}`, `{{dirección}}`, para que el usuario lo complete.

## 2. Elegir la estructura

Leé `references/estructuras.md` y elegí la que corresponde al negocio (hay 8).
Cada una trae el orden de secciones y qué trabajo cumple cada una. Adaptala:
podés sacar secciones, nunca agregar relleno.

## 3. Diseñar antes de programar

Escribí un plan corto (no se lo muestres entero al usuario, salvo que lo pida):

- **Paleta:** 4 a 6 colores con nombre, sacados del mundo del negocio
  (materiales, producto, lugar). No de una paleta "linda" genérica.
- **Tipografía:** una pareja de `references/tipografias.md` según el rubro.
  Nunca Inter, Roboto, Poppins, Montserrat, Open Sans, Space Grotesk.
- **El momento memorable:** UNA sola cosa que la gente va a recordar (en una
  relojería, la hora real girando como un reloj; en una cafetería, el vapor de
  la taza siguiendo el scroll). Todo lo demás, sobrio.
- **Layout:** describilo en una línea por sección.

Después revisá el plan contra `references/anti-ia.md`. Si alguna parte se
parece a lo que harías para cualquier otro negocio, cambiala. Recién ahí
programás.

## 4. Construir

- Arrancá de `assets/base.html`: ya trae el andamiaje de scroll suave,
  animaciones, movimiento reducido, foco visible y móvil.
- Un solo archivo `index.html` con CSS y JS adentro, más una carpeta `img/`.
- Copy: leé `references/copy.md`. Frases cortas, voz activa, nada de frases
  hechas. El botón dice exactamente qué pasa ("Escribinos por WhatsApp", no
  "Enviar").
- Movimiento: leé `references/movimiento.md`. Una secuencia de entrada
  orquestada vale más que veinte "fade-in" en cada sección.
- Fotos: si el usuario no tiene, dejá el espacio con un recuadro elegante y
  escribí al lado qué foto va ahí (encuadre, luz, fondo), para que la saque o
  la genere. Nunca uses fotos de personas reales que no sean del negocio.
- Formulario y WhatsApp: seguí la skill `web-contacto` si está instalada; si
  no, un formulario que abra WhatsApp con el mensaje armado.

## 5. Revisar antes de entregar

1. Corré el detector:
   ```bash
   python3 scripts/revisar.py index.html
   ```
   Tiene que dar **90 o más**. Si da menos, arreglá lo que marca y volvé a correr.
2. Si podés, mirá la web en un navegador a 1440 px y a 390 px de ancho
   (captura de pantalla). Revisá: nada se superpone, el texto se lee sobre las
   fotos, el hero entra completo en el celular.
3. Revisá que no quedó ningún dato inventado.

## 6. Entregar

- La carpeta con `index.html` e `img/`.
- Tres líneas: qué estructura usaste, cuál es el momento memorable y qué
  datos `{{...}}` tiene que completar.
- Cómo publicarla gratis: arrastrar la carpeta a https://app.netlify.com/drop
  (no hace falta cuenta para probar) o subirla a Vercel.

## Lo que esta skill no hace

No compra dominios, no publica sola y no se conecta a cuentas del usuario. No
inventa testimonios, cifras ni logos de clientes.
