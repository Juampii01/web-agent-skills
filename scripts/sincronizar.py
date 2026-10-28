#!/usr/bin/env python3
"""Copia los archivos compartidos de web-crear a las skills que los usan.
Cada skill tiene que funcionar sola (en claude.ai se suben por separado).
Correlo después de editar revisar.py o anti-ia.md:  python3 scripts/sincronizar.py"""
import filecmp, os, shutil
RAIZ = os.path.join(os.path.dirname(__file__), "..", "plugins", "web", "skills")
ORIGEN = os.path.join(RAIZ, "web-crear")
COMPARTIDOS = {
    "scripts/revisar.py": ["web-nota", "web-cambios", "web-versiones", "web-competencia"],
    "references/anti-ia.md": ["web-nota", "web-versiones"],
}
for archivo, skills in COMPARTIDOS.items():
    for s in skills:
        destino = os.path.join(RAIZ, s, archivo)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        if not os.path.exists(destino) or not filecmp.cmp(os.path.join(ORIGEN, archivo), destino, shallow=False):
            shutil.copy2(os.path.join(ORIGEN, archivo), destino)
            print("actualizado", os.path.relpath(destino, RAIZ))
print("listo")
