# Parejas tipográficas por rubro

Todas están en Google Fonts, son gratis y no son las que eligen las IA por
defecto. Cargalas con:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=FAMILIA:wght@400;600&display=swap" rel="stylesheet">
```

Siempre con una fuente de respaldo real: `font-family: "Bodoni Moda", "Didot", serif;`

| Rubro | Títulos | Texto | Por qué |
|---|---|---|---|
| Lujo, relojería, joyería | Bodoni Moda | Schibsted Grotesk | Contraste alto de relojería, texto limpio y moderno |
| Moda, perfumería | Italiana | Hanken Grotesk | Elegante y fina sin ser Playfair |
| Gastronomía de autor | Young Serif | Figtree | Cálida, de carta impresa |
| Café, panadería | Gloock | Albert Sans | Redonda y artesanal |
| Bar, cervecería | Bricolage Grotesque | Bricolage Grotesque | Una sola familia con carácter, varios anchos |
| Abogado, contador, consultor | Newsreader | Public Sans | Seria y confiable, nada de corporativo frío |
| Salud, consultorio | Literata | Atkinson Hyperlegible | Legibilidad máxima, tono humano |
| Arquitectura, diseño | Syne | Manrope | Geométrica, de estudio |
| Tecnología, software | Familjen Grotesk | IBM Plex Sans | Técnica sin ser la de siempre |
| Deporte, gimnasio | Anton | Barlow | Condensada y con fuerza |
| Inmobiliaria | Libre Caslon Display | Instrument Sans | Editorial, de revista de arquitectura |
| Educación, cursos | Gelasio | Nunito Sans | Amable, se lee fácil |
| Infantil, juguetes | Fredoka | Lexend | Redondeada sin ser caricatura |
| Construcción, industria | Archivo (ancho expandido) | Archivo | Robusta, de cartel de obra |
| Belleza, estética | Cormorant (solo títulos grandes) | Karla | Delicada; Cormorant nunca en texto chico |

## Reglas

- Títulos: interlineado 0.95 a 1.1, tracking levemente negativo en tamaños grandes.
- Texto: 16 a 18 px, interlineado 1.5 a 1.6, líneas de hasta 70 caracteres.
- Una escala fija (por ejemplo 14 · 17 · 22 · 34 · 56 · 96) y no salirse.
- Números alineados en tablas y precios: `font-variant-numeric: tabular-nums`.
