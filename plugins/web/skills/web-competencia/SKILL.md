---
name: web-competencia
description: >-
  Analiza las webs de la competencia y devuelve qué copiar, qué evitar y dónde
  hay un hueco que nadie está ocupando, con evidencia de cada página. Usala
  cuando el usuario diga "mirá la web de mi competencia", "analizá estas
  webs", "qué hacen mis competidores", "espiá a la competencia",
  "/web-competencia", o pegue varios links de negocios parecidos al suyo.
---

# web-competencia

No es un resumen de cada web. Es una decisión: qué tomar, qué evitar y por
dónde diferenciarse.

## Qué pedir

1. Entre 3 y 5 links de competidores (si el usuario no sabe cuáles, buscá en
   la web "[rubro] en [ciudad]" y proponé 5 para que confirme).
2. Su propia web, si tiene.
3. A quién le vende (para juzgar con los ojos de ese cliente).

## Cómo analizar cada web

Abrí cada link (con la herramienta de lectura web que tengas). Si una página
no se puede leer, decilo y seguí con las demás; no inventes lo que no viste.
Para cada una anotá, con citas textuales cortas como evidencia:

| Punto | Qué mirar |
|---|---|
| Titular | ¿Se entiende en 3 segundos qué venden y para quién? Citalo. |
| Oferta | Precios visibles, planes, garantía, qué incluye |
| Prueba | Reseñas, casos, cifras, logos: ¿reales y verificables? |
| Acción principal | Qué botón empujan, cuántos clics hasta contactar |
| Contacto | WhatsApp, formulario, teléfono, horarios |
| Diseño | ¿Plantilla o propio? Corré `scripts/revisar.py` si tenés el HTML |
| Tono | Cómo le hablan al cliente (formal, cercano, técnico) |
| Huecos | Preguntas obvias del cliente que la web no responde |

## Qué entregar

1. **Tabla comparativa** de todas las webs con los puntos de arriba (una fila
   por punto, una columna por competidor, más la del usuario si tiene web).
2. **Copiar (3 cosas):** lo que funciona en más de una web y el usuario no
   tiene. Cada una con el ejemplo concreto.
3. **Evitar (3 cosas):** errores que se repiten, con la cita.
4. **El hueco:** lo que ningún competidor dice o muestra y el cliente
   necesita saber. Es el ángulo para el titular del usuario.
5. **Próximo paso:** si el usuario quiere aplicar esto, ofrecé correr
   `web-titular` (con el hueco como ángulo) o `web-crear`.

## Reglas

- Solo lo que viste. Si algo no se pudo verificar, va como "no visible en la web".
- No copies textos ni imágenes de la competencia: se toma la idea, no el material.
- No completes formularios ni contactes a los competidores.
