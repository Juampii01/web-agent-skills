#!/usr/bin/env python3
"""Arma un zip por skill en claude-ai/ para subir en claude.ai (Personalizar → Skills).

Antes de armar revisa que cada skill tenga SKILL.md con el mismo nombre que su
carpeta, que los archivos compartidos estén sincronizados y que no viaje ningún
secreto.

Uso:  python3 scripts/armar_zips.py
"""
import filecmp
import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = RAIZ / "plugins" / "web" / "skills"
SALIDA = RAIZ / "claude-ai"
IGNORAR = {"__pycache__", ".DS_Store"}
SOSPECHOSOS = [
    re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]
COMPARTIDOS = {
    "scripts/revisar.py": ["web-nota", "web-cambios", "web-versiones", "web-competencia"],
    "references/anti-ia.md": ["web-nota", "web-versiones"],
}


def archivos(base):
    for p in sorted(base.rglob("*")):
        if p.is_file() and not (set(p.parts) & IGNORAR) and p.suffix != ".pyc":
            yield p


def problemas():
    lista = []
    for carpeta in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        md = carpeta / "SKILL.md"
        if not md.exists():
            lista.append(f"{carpeta.name}: falta SKILL.md")
            continue
        m = re.search(r"^name:\s*(\S+)", md.read_text(encoding="utf-8"), re.M)
        if not m or m.group(1) != carpeta.name:
            lista.append(f"{carpeta.name}: el 'name' del frontmatter no coincide con la carpeta")
        for f in archivos(carpeta):
            try:
                texto = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for patron in SOSPECHOSOS:
                if patron.search(texto):
                    lista.append(f"{f.relative_to(RAIZ)}: parece un secreto ({patron.pattern})")
    for archivo, skills in COMPARTIDOS.items():
        for s in skills:
            if not filecmp.cmp(SKILLS / "web-crear" / archivo, SKILLS / s / archivo, shallow=False):
                lista.append(f"{s}/{archivo} está desactualizado: corré scripts/sincronizar.py")
    return lista


def main():
    errores = problemas()
    if errores:
        print("No se armaron los zips. Revisá esto:")
        for e in errores:
            print("  -", e)
        return 1
    SALIDA.mkdir(exist_ok=True)
    for viejo in SALIDA.glob("*.zip"):
        viejo.unlink()
    total = 0
    for carpeta in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        with zipfile.ZipFile(SALIDA / f"{carpeta.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in archivos(carpeta):
                z.write(f, f"{carpeta.name}/{f.relative_to(carpeta)}")
            z.write(RAIZ / "LICENCIA.md", f"{carpeta.name}/LICENCIA.md")
        total += 1
    print(f"Listo: {total} zips en claude-ai/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
