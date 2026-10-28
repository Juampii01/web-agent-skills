---
name: web-cambios
description: >-
  Aplica en una web existente los cambios que el usuario pide en palabras
  ("cambiá el color del botón", "agregá una sección de precios", "poné mi
  dirección nueva") sin romper el diseño ni el resto de la página, y muestra
  qué cambió. Usala cuando el usuario diga "cambiá", "agregá", "sacá",
  "movéme", "corregí" algo de su web, "/web-cambios", o pida editar una web
  hecha con web-crear.
---

# web-cambios

El riesgo de editar una web con IA es que en cada cambio se pierda un poco el
diseño: colores que aparecen de la nada, una tipografía nueva, una sección que
no se parece a las demás. Esta skill cambia lo pedido y nada más.

## Antes de tocar nada

1. Leé el archivo completo.
2. Identificá el sistema de diseño: las variables de `:root` (colores,
   fuentes, márgenes), la escala de tamaños y cómo están hechas las secciones
   parecidas a la que vas a tocar.
3. Si el pedido es ambiguo ("hacelo más moderno"), preguntá una sola cosa
   concreta con 2 o 3 opciones. Si es claro, hacelo.

## Al cambiar

- **Cambio mínimo.** Tocá solo las líneas necesarias; no reformatees ni
  reordenes el resto del archivo.
- **Reusá el sistema.** Colores y fuentes salen de las variables existentes.
  Si hace falta un color nuevo, agregalo como variable con nombre y avisá.
- **Secciones nuevas** copian la estructura de una sección hermana (márgenes,
  títulos, ritmo), no inventan otra.
- **Textos nuevos** siguen el tono que ya tiene la web (voseo o tuteo, largo
  de frase). Nada de frases hechas.
- **Datos:** si el pedido necesita un dato que no está (precio, horario), va
  `{{dato}}` y lo decís.

## Después de cambiar

1. Corré el detector para asegurarte de que el cambio no metió señales de plantilla:
   ```bash
   python3 scripts/revisar.py index.html
   ```
   El puntaje no puede bajar respecto de antes del cambio.
2. Si podés, mirá la parte cambiada en escritorio y en celular.
3. Contale al usuario en 2 o 3 líneas qué cambió y dónde, sin pegar el archivo entero.

## Si el pedido rompe el diseño

Si lo pedido va contra la dirección de la web (por ejemplo, "poné todo en
Comic Sans" en una relojería de lujo), hacelo igual si insiste, pero antes
decí en una línea qué se pierde y ofrecé una alternativa que logre lo mismo.
