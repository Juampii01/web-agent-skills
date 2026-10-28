---
name: web-versiones
description: >-
  Genera 3 direcciones de diseño distintas para la misma web (paleta,
  tipografía, layout y momento memorable diferentes) y una página para
  compararlas lado a lado y elegir. Usala cuando el usuario diga "mostrame
  opciones", "haceme varias versiones", "no me convence el diseño", "probá
  otro estilo", "/web-versiones", o no sepa qué estilo quiere para su web.
---

# web-versiones

Tres versiones que se parecen entre sí no son tres versiones. Cada una tiene
que ser una apuesta distinta, con el mismo contenido.

## Qué pedir

1. La web actual o el contenido (si no hay web, corré primero el paso 1 de
   `web-crear` para juntar el contenido).
2. Si hay algo fijo: logo, un color de marca, una foto obligatoria.

## Las 3 direcciones

Variá al menos tres de estos cuatro ejes entre versión y versión:

| Eje | Ejemplos de opuestos |
|---|---|
| Paleta | oscura y dramática · clara y luminosa · un color de marca saturado como fondo |
| Tipografía | serif de alto contraste · grotesca ancha · una sola familia con carácter |
| Layout | editorial asimétrico · grilla rigurosa · una columna con imágenes a sangre |
| Momento memorable | entrada orquestada · recorrido por scroll · interacción (arrastrar, elegir) |

Antes de programar, escribí las tres direcciones en una línea cada una y
revisá que ninguna caiga en las estéticas gastadas de
`references/anti-ia.md` (crema con terracota, negro con un acento
ácido, estilo diario, kit de tarjetas, hero violeta). Si dos se parecen,
cambiá una.

Nombrá cada versión por su idea, no por número: "Taller nocturno", "Catálogo
de museo", "Vidriera de calle".

## Construir

- Tres archivos: `version-a.html`, `version-b.html`, `version-c.html`, con el
  mismo contenido y las mismas fotos.
- Una página `comparar.html` con las tres en recuadros lado a lado (iframes a
  los archivos locales), el nombre de cada una y una línea de qué la hace distinta.
- Corré `scripts/revisar.py` en las tres; todas tienen que dar 90 o más.

## Entregar

Las tres versiones, la página para comparar y tu recomendación en una línea
según el negocio y su cliente. Cuando el usuario elija, ofrecé mezclar
("la tipografía de A con los colores de C") usando `web-cambios`.
