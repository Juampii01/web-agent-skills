---
name: web-nota
description: >-
  Le pone nota de 0 a 100 a una web con una rúbrica de 8 categorías (claridad,
  conversión, confianza, diseño sin olor a IA, celular, velocidad, SEO y
  accesibilidad) y devuelve los arreglos ordenados por impacto. Usala cuando
  el usuario diga "ponele nota a mi web", "auditá mi página", "qué le falta a
  mi web", "por qué mi web no vende", "/web-nota", o pegue un link o un
  archivo HTML y pregunte cómo está.
---

# web-nota

## Qué pedir

El link de la web, o el archivo HTML si todavía no está publicada. Con el link,
leela con la herramienta web que tengas. Si además el usuario puede pasar el
HTML (Ctrl+U en el navegador, guardar como), mejor: el detector automático
necesita el código.

## Cómo puntuar

Usá `rubric.json`: 8 categorías, cada una con su peso y sus criterios. Para
cada criterio decidí si se cumple (puntos completos), a medias (la mitad) o no
(cero), y anotá la evidencia (qué viste y dónde).

La categoría **Diseño sin olor a IA** sale del detector:

```bash
python3 scripts/revisar.py index.html
```

Convertí su puntaje (0 a 100) al peso de la categoría (por ejemplo, 80/100 en
una categoría de 15 puntos = 12 puntos). Si no hay HTML, puntuá esa categoría a
ojo con `references/anti-ia.md` y aclaralo.

Si no pudiste medir algo (por ejemplo la velocidad real sin acceso a
PageSpeed), decilo y dejá ese criterio fuera del total, recalculando sobre lo
que sí mediste. Nunca inventes un número.

## Qué entregar

1. **La nota:** `72/100` grande, con una línea de veredicto.
2. **Tabla por categoría:** puntos obtenidos sobre puntos posibles.
3. **Los 5 arreglos que más suben la nota**, ordenados por impacto/esfuerzo:
   qué cambiar, dónde, y cuántos puntos suma. El primero tiene que poder
   hacerse hoy.
4. **Lo que está bien** (2 o 3 cosas), para no romperlas.
5. Ofrecé el siguiente paso: `web-titular` si falla claridad, `web-conversion`
   si falla conversión, `web-velocidad` si falla velocidad.

## Escala

| Nota | Qué significa |
|---|---|
| 90-100 | Nivel estudio. Pulir detalles. |
| 75-89 | Buena, con fugas concretas. |
| 55-74 | Funciona, pero pierde clientes en el camino. |
| 0-54 | Rehacer: la web juega en contra. |
