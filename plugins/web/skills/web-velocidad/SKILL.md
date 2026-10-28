---
name: web-velocidad
description: >-
  Optimiza una web para que cargue rápido en el celular: convierte y achica
  las imágenes, agrega carga diferida, ordena fuentes y scripts, y entrega el
  antes y después en kilobytes. Usala cuando el usuario diga "mi web es
  lenta", "optimizá las imágenes", "que cargue más rápido", "mejorá la
  velocidad", "PageSpeed me da mal", "/web-velocidad".
---

# web-velocidad

La mayoría de las webs lentas de negocios chicos tienen el mismo problema:
fotos enormes. Arreglar eso solo suele ser el 80 % de la mejora.

## Qué pedir

La carpeta de la web (HTML + imágenes). Si solo hay un link, podés
diagnosticar leyendo el HTML, pero para optimizar necesitás los archivos.

## 1. Medir el antes

```bash
python3 scripts/optimizar.py carpeta-de-la-web --solo-medir
```

Lista cada imagen con su peso, sus dimensiones y el peso total de la página.
Si el usuario puede, que corra también https://pagespeed.web.dev con su link y
te pase el resultado del celular. No inventes puntajes de PageSpeed.

## 2. Imágenes

```bash
python3 scripts/optimizar.py carpeta-de-la-web
```

Para cada JPG o PNG crea un `.webp` (calidad 80) y versiones de 640, 1024 y
1600 px de ancho, sin agrandar nunca la original. No borra nada: los originales
quedan donde estaban. Necesita Pillow (`pip install Pillow`).

Después actualizá el HTML:

```html
<img src="img/foto-1024.webp"
     srcset="img/foto-640.webp 640w, img/foto-1024.webp 1024w, img/foto-1600.webp 1600w"
     sizes="(max-width: 900px) 100vw, 50vw"
     width="1600" height="1067" alt="..." loading="lazy" decoding="async">
```

- `width` y `height` reales siempre (evita saltos al cargar).
- `loading="lazy"` en todo lo que no se ve al abrir. La foto de portada, al
  revés: `fetchpriority="high"` y sin lazy.

## 3. Fuentes

- Máximo 2 familias y solo los pesos que se usan.
- `&display=swap` en el link de Google Fonts y `preconnect` a fonts.gstatic.com.

## 4. Scripts

- Librerías con versión fija desde un CDN, al final del body o con `defer`.
- Sacá lo que no se usa (sliders, jQuery para dos efectos, píxeles duplicados).
- Videos de fondo: `muted playsinline preload="none"` y un póster liviano.

## 5. Entregar

Tabla de antes y después: peso total de la página, peso de imágenes, cantidad
de archivos. Y la lista de cambios hechos en el HTML.
