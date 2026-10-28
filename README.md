# Web Agent Skills

**10 skills en español para que Claude te arme la web de tu negocio, y que no se note que la hizo una IA.**

Le contás qué vendés y te devuelve la web completa: textos, secciones, diseño propio, animaciones y un formulario que termina en un mensaje de WhatsApp. Después la revisa, le pone nota, la compara con tu competencia y la mejora.

Gratis. Funcionan en claude.ai y en Claude Code.

## Las 10 skills

| Skill | Qué hace |
|---|---|
| `web-crear` | Le describís tu negocio y te devuelve la web completa, en un archivo listo para publicar. Trae 8 estructuras de landing por rubro y las reglas para que no parezca hecha con IA. |
| `web-contacto` | Conecta el formulario y el botón de WhatsApp: cada visita termina en un mensaje ya escrito. |
| `web-competencia` | Analiza las webs de tu competencia y te dice qué copiar, qué evitar y qué hueco nadie ocupa. |
| `web-nota` | Le pone nota de 0 a 100 a tu web actual, con los 5 arreglos que más la suben. |
| `web-titular` | Reescribe tu titular para que en 3 segundos se entienda qué vendés. 5 opciones puntuadas. |
| `web-seo` | Plan SEO de 12 semanas, un artículo por semana, con el primero escrito y los ajustes de la página. |
| `web-velocidad` | Optimiza imágenes, fuentes y scripts para que cargue rápido en el celular. |
| `web-conversion` | Revisa sección por sección y te marca cuál no empuja a la gente a escribirte. |
| `web-cambios` | Le escribís qué querés cambiar y lo cambia sin romper el diseño. |
| `web-versiones` | Te genera 3 versiones de diseño distintas para que elijas. |

## Instalar

Seguí [INSTALAR.md](INSTALAR.md). Resumen:

- **Claude Code** (2 comandos):
  ```bash
  claude plugin marketplace add Juampii01/web-agent-skills
  claude plugin install web@web-agent-skills
  ```
- **claude.ai:** subís los `.zip` de la carpeta [`claude-ai/`](claude-ai) en *Personalizar → Skills*.

## Probala

Después de instalar, escribile a Claude:

> Armame una web para mi taller mecánico en Junín. Hacemos service y diagnóstico, atendemos de lunes a sábado y quiero que me escriban por WhatsApp.

O pasale tu web actual:

> Ponele nota a mi web: https://...

## El detector de "olor a IA"

`web-crear`, `web-nota`, `web-cambios` y `web-versiones` traen `revisar.py`, un script que lee una web y le pone puntaje de 0 a 100 según cuántas señales de plantilla tiene: tipografías gastadas, degradados violetas, todo en tarjetas iguales, frases hechas, emojis en los títulos y más. Cada hallazgo viene con la línea, por qué delata y cómo arreglarlo.

```bash
python3 revisar.py index.html
```

## Ejemplo

En [`ejemplos/vauren/`](ejemplos/vauren) está la web de Vauren, una relojería inventada hecha con estas reglas: la hora real del visitante girando como un reloj en la portada, la colección con scroll horizontal y un zoom por scroll que recorre el reloj pieza por pieza. Saca 100/100 en el detector.

## Lo que no hace

Las skills escriben, diseñan y revisan. **No publican tu web solas**, no compran dominios, no se conectan a tus cuentas y **no inventan reseñas, cifras ni clientes**: si falta un dato tuyo, queda marcado como `{{dato}}` para que lo completes.

Para publicarla gratis: arrastrá la carpeta a [Netlify Drop](https://app.netlify.com/drop) o subila a Vercel.

---

Hecho por [Juan Pablo Acosta](https://github.com/Juampii01) · Nova Softwares. Ver [LICENCIA.md](LICENCIA.md).
