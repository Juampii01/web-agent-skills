#!/usr/bin/env python3
"""
optimizar.py — achica las imágenes de una web para que cargue rápido en el celular.

Uso:
    python3 optimizar.py carpeta/              # crea .webp en 640, 1024 y 1600 px
    python3 optimizar.py carpeta/ --solo-medir # solo informa pesos y tamaños

No borra ni pisa los originales. Necesita Pillow:  pip install Pillow
"""
import os
import sys

ANCHOS = (640, 1024, 1600)
EXT = (".jpg", ".jpeg", ".png")


def kb(n):
    return f"{n / 1024:,.0f} KB".replace(",", ".")


def imagenes(carpeta):
    for raiz, _, archivos in os.walk(carpeta):
        for a in sorted(archivos):
            if a.lower().endswith(EXT) and not any(f"-{w}." in a for w in ANCHOS):
                yield os.path.join(raiz, a)


def medir(carpeta):
    total_img = 0
    total = 0
    for raiz, _, archivos in os.walk(carpeta):
        for a in archivos:
            total += os.path.getsize(os.path.join(raiz, a))
    filas = []
    try:
        from PIL import Image
    except ImportError:
        Image = None
    for ruta in imagenes(carpeta):
        peso = os.path.getsize(ruta)
        total_img += peso
        dim = ""
        if Image:
            with Image.open(ruta) as im:
                dim = f"{im.width}×{im.height}"
        alerta = "  ← pesada" if peso > 300 * 1024 else ""
        filas.append(f"  {kb(peso):>10}  {dim:>11}  {os.path.relpath(ruta, carpeta)}{alerta}")
    print(f"\nImágenes JPG/PNG en {carpeta}:")
    print("\n".join(filas) or "  (ninguna)")
    print(f"\nPeso de imágenes: {kb(total_img)}   Peso total de la carpeta: {kb(total)}\n")
    return total_img


def optimizar(carpeta):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Falta Pillow. Instalalo con:  pip install Pillow")
    antes = medir(carpeta)
    despues = 0
    for ruta in imagenes(carpeta):
        base, _ = os.path.splitext(ruta)
        with Image.open(ruta) as im:
            im = im.convert("RGBA") if im.mode in ("P", "LA", "RGBA") else im.convert("RGB")
            for w in ANCHOS:
                if w > im.width and w != ANCHOS[0]:
                    continue  # nunca agrandar
                ancho = min(w, im.width)
                alto = round(im.height * ancho / im.width)
                destino = f"{base}-{w}.webp"
                im.resize((ancho, alto), Image.LANCZOS).save(destino, "WEBP", quality=80, method=6)
                if w == 1024 or (w == ANCHOS[0] and im.width < 1024):
                    despues += os.path.getsize(destino)
                print(f"  {os.path.relpath(destino, carpeta)}  {ancho}×{alto}  {kb(os.path.getsize(destino))}")
    if antes:
        print(f"\nAntes (originales): {kb(antes)}   Después (versión de 1024 px): {kb(despues)}"
              f"   Ahorro: {100 - despues * 100 // antes} %\n")
    print("Ahora actualizá el HTML con srcset, width, height y loading=lazy (ver SKILL.md).")


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print(__doc__)
        sys.exit(1)
    if "--solo-medir" in sys.argv:
        medir(sys.argv[1])
    else:
        optimizar(sys.argv[1])


if __name__ == "__main__":
    main()
