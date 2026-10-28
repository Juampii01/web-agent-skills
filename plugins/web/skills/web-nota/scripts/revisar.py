#!/usr/bin/env python3
"""
revisar.py — detecta las señales que delatan una web hecha con IA o con plantilla.

Uso:
    python3 revisar.py index.html            # informe legible
    python3 revisar.py index.html --json     # para que otra skill lo lea

Lee un archivo HTML (con su CSS y JS embebidos) y devuelve:
  - puntaje "sin olor a IA" de 0 a 100
  - cada hallazgo con la línea, por qué delata y cómo arreglarlo
  - chequeos básicos de calidad (idioma, viewport, alt, foco, movimiento reducido)

No usa librerías externas. Python 3.8 o más nuevo.
"""
import json
import re
import sys
from collections import Counter

FUENTES_GASTADAS = [
    "Inter", "Roboto", "Open Sans", "Poppins", "Montserrat", "Lato",
    "Space Grotesk", "Nunito", "Raleway", "Plus Jakarta Sans", "DM Sans",
    "Instrument Serif", "Playfair Display",
]

FRASES_HECHAS = [
    # español
    "lleva tu negocio al siguiente nivel", "llevá tu negocio al siguiente nivel",
    "al siguiente nivel", "soluciones innovadoras", "solución integral",
    "potenciá tu", "potencia tu", "desbloqueá", "desbloquea tu",
    "revolucioná", "revoluciona tu", "de clase mundial", "experiencia única",
    "transformá tu", "transforma tu", "sin complicaciones", "todo en un solo lugar",
    "impulsá tu", "impulsa tu", "a otro nivel", "calidad premium",
    "tu socio estratégico", "comprometidos con la excelencia",
    "en la era digital", "en el mundo actual", "descubrí más", "descubre más",
    # inglés
    "take your business to the next level", "unlock", "seamless", "cutting-edge",
    "empower", "supercharge", "elevate your", "game-changer", "world-class",
    "all-in-one", "revolutionize", "next-gen", "lorem ipsum",
]

COLORES_IA = {
    "violeta/índigo de plantilla": ["#6366f1", "#8b5cf6", "#a855f7", "#7c3aed", "#4f46e5", "#9333ea"],
    "terracota de Claude": ["#d97757", "#da7756", "#cc785c"],
    "crema de Claude": ["#f4f1ea", "#f5f0e8", "#faf9f5"],
    "verde ácido": ["#c6ff00", "#b6ff00", "#d4ff00", "#ccff00"],
}

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")


def linea(texto, pos):
    return texto.count("\n", 0, pos) + 1


def revisar(html):
    hallazgos = []
    bajo = html.lower()

    def agregar(peso, que, por_que, arreglo, pos=None):
        hallazgos.append({
            "peso": peso, "que": que, "por_que": por_que, "arreglo": arreglo,
            "linea": linea(html, pos) if pos is not None else None,
        })

    # 1. tipografía
    familias = set(re.findall(r"family=([A-Za-z+]+)", html))
    familias |= {f.strip().strip("'\"") for f in re.findall(r"font-family\s*:\s*([^;}{]+)", html) for f in f.split(",")}
    familias = {f.replace("+", " ").strip() for f in familias}
    gastadas = sorted(f for f in familias if f in FUENTES_GASTADAS)
    if gastadas:
        pos = bajo.find(gastadas[0].lower())
        agregar(14, f"Tipografía gastada: {', '.join(gastadas)}",
                "Son las fuentes que eligen por defecto las IA y las plantillas; la web se ve igual a mil otras.",
                "Elegí una pareja de references/tipografias.md según el rubro.", pos)
    solo_sistema = not any(f for f in familias if f and f.lower() not in
                          {"system-ui", "-apple-system", "sans-serif", "serif", "monospace",
                           "blinkmacsystemfont", "segoe ui", "helvetica", "arial", "inherit"})
    if solo_sistema:
        agregar(10, "Sin tipografía propia",
                "Solo fuentes del sistema: no hay personalidad tipográfica.",
                "Sumá una display con carácter y una de texto (Google Fonts).")

    # 2. colores de plantilla
    for nombre, hexes in COLORES_IA.items():
        for h in hexes:
            p = bajo.find(h)
            if p >= 0:
                agregar(8, f"Color típico de IA ({nombre}): {h}",
                        "Es una de las paletas que más repiten las webs generadas.",
                        "Sacá la paleta del rubro: materiales, fotos y objetos del negocio.", p)
                break
    grad = re.search(r"linear-gradient\([^)]*(purple|violet|indigo|#6366f1|#8b5cf6|#a855f7)", bajo)
    if grad:
        agregar(10, "Degradado violeta/azul",
                "El hero con degradado violeta es la marca registrada de las landings de IA.",
                "Usá una foto real del producto o un fondo plano del color del rubro.", grad.start())

    # 3. layout de plantilla
    radios = Counter(re.findall(r"border-radius\s*:\s*([^;}{]+)", bajo))
    if radios:
        valor, veces = radios.most_common(1)[0]
        if veces >= 6 and len(radios) <= 2:
            agregar(8, f"Mismo border-radius en todo ({valor.strip()}, {veces} veces)",
                    "Todas las cajas iguales aplanan la jerarquía: kit de tarjetas SaaS.",
                    "Redondeá solo lo que se toca (botones, campos) y dejá rectas las secciones.")
    sombras = re.findall(r"box-shadow\s*:\s*[^;]*rgba\(0,\s*0,\s*0,\s*0?\.(0?[5-9]|1|15)\)", bajo)
    if len(sombras) >= 4:
        agregar(6, f"Sombra gris suave repetida ({len(sombras)} veces)",
                "La misma sombra debajo de cada tarjeta es el default de los generadores.",
                "Separá con espacio, color o tamaño; sombra solo para lo que flota.")
    centrados = len(re.findall(r"text-align\s*:\s*center", bajo))
    if centrados >= 6:
        agregar(6, f"Todo centrado ({centrados} reglas text-align:center)",
                "Centrar todo es la salida fácil; nada guía la lectura.",
                "Alineá a la izquierda el texto largo y centrá solo piezas sueltas.")
    mayus = len(re.findall(r"text-transform\s*:\s*uppercase", bajo))
    if mayus >= 3:
        agregar(6, f"Etiquetas en mayúsculas encima de los títulos ({mayus})",
                "La 'eyebrow' en mayúsculas espaciadas sobre cada título es plantilla pura.",
                "Sacalas; si la info importa, que esté en el título.")
    numeros = re.findall(r">\s*0[1-9]\s*<", html)
    if len(numeros) >= 3:
        agregar(5, "Numeración 01 / 02 / 03 decorativa",
                "Numerar cosas que no son pasos es adorno de plantilla.",
                "Numerá solo procesos reales con orden.")
    flechas = re.search(r"(→|-&gt;|&rarr;)\s*</(a|button)>", html)
    if flechas:
        agregar(4, "Flecha → pegada al texto de los botones",
                "Detalle repetidísimo en webs generadas.",
                "El botón dice qué pasa al tocarlo; no necesita flecha.", flechas.start())
    stats = re.findall(r">\s*\d+(\.\d+)?\s*(k\+|m\+|\+|%)\s*<", bajo)
    if len(stats) >= 3:
        agregar(4, "Fila de numeritos (10k+, 99%, 24/7)",
                "La franja de estadísticas inventadas es relleno típico.",
                "Poné un dato real con su fuente, o nada.")

    # 4. emojis en títulos
    for m in re.finditer(r"<h[1-3][^>]*>(.*?)</h[1-3]>", html, re.S):
        if EMOJI.search(m.group(1)):
            agregar(6, "Emoji en un título",
                    "Emojis como marcadores de sección delatan generación automática.",
                    "Sacalo; si hace falta un ícono, que sea uno diseñado.", m.start())
            break

    # 5. copy
    for frase in FRASES_HECHAS:
        p = bajo.find(frase)
        if p >= 0:
            agregar(5, f"Frase hecha: “{frase}”",
                    "Nadie habla así; suena a texto de IA o de agencia genérica.",
                    "Decí qué hace el negocio, para quién y con un dato concreto.", p)

    # 6. calidad básica (pesa menos, pero se informa)
    if not re.search(r"<html[^>]*\blang=", bajo) and "<title" in bajo and "<html" in bajo:
        agregar(3, "Falta lang en <html>", "Lectores de pantalla y Google no saben el idioma.", 'Agregá lang="es".')
    if "name=\"viewport\"" not in bajo and "<head" in bajo:
        agregar(3, "Falta meta viewport", "En el celular se ve chiquito.", "Agregá la meta viewport.")
    sin_alt = [m for m in re.finditer(r"<img(?![^>]*\balt=)[^>]*>", bajo)]
    if sin_alt:
        agregar(3, f"{len(sin_alt)} imagen(es) sin alt", "Accesibilidad y SEO.", "Describí cada foto en su alt.", sin_alt[0].start())
    if "prefers-reduced-motion" not in bajo and ("@keyframes" in bajo or "gsap" in bajo or "transition" in bajo):
        agregar(3, "No respeta 'reducir movimiento'", "Hay gente que se marea con animaciones.",
                "Agregá @media (prefers-reduced-motion: reduce).")
    if ":focus-visible" not in bajo and ":focus" not in bajo:
        agregar(2, "Sin estilo de foco para teclado", "Quien navega con teclado no ve dónde está.",
                "Agregá :focus-visible con un contorno visible.")

    descuento = sum(h["peso"] for h in hallazgos)
    puntaje = max(0, 100 - descuento)
    return puntaje, sorted(hallazgos, key=lambda h: -h["peso"])


def veredicto(p):
    if p >= 90: return "Parece hecha a mano por un estudio."
    if p >= 75: return "Bien, con detalles que delatan plantilla."
    if p >= 55: return "Se nota que es plantilla o IA."
    return "Grita 'hecha con IA'. Rehacer la dirección de diseño."


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    ruta = sys.argv[1]
    with open(ruta, encoding="utf-8", errors="replace") as f:
        html = f.read()
    puntaje, hallazgos = revisar(html)
    if "--json" in sys.argv:
        print(json.dumps({"archivo": ruta, "puntaje": puntaje, "veredicto": veredicto(puntaje),
                          "hallazgos": hallazgos}, ensure_ascii=False, indent=2))
        return
    print(f"\n{ruta}\nSin olor a IA: {puntaje}/100. {veredicto(puntaje)}\n")
    if not hallazgos:
        print("No encontré señales de plantilla.")
    for h in hallazgos:
        donde = f" (línea {h['linea']})" if h["linea"] else ""
        print(f"-{h['peso']:>2}  {h['que']}{donde}\n     Por qué: {h['por_que']}\n     Arreglo: {h['arreglo']}\n")


if __name__ == "__main__":
    main()
