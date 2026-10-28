# Cómo instalar Web Agent Skills

Elegí un camino según cómo usás Claude:

| | Camino A · Claude Code | Camino B · claude.ai (web, escritorio o app) |
|---|---|---|
| Plan de Claude | Pro, Max, Team o Enterprise | Cualquiera con skills habilitadas |
| Cuánto tarda | 2 minutos | 5 minutos |
| Qué instalás | Las 10 de una vez | Las que elijas, una por una |
| Scripts (detector, optimizador de imágenes) | Corren en tu computadora | Corren en el entorno de Claude |

---

## Camino A · Claude Code

**1.** Si no tenés Claude Code, instalalo:

Mac o Linux:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
Windows (PowerShell):
```powershell
irm https://claude.ai/install.ps1 | iex
```

**2.** Agregá el repositorio e instalá el plugin:

```bash
claude plugin marketplace add Juampii01/web-agent-skills
claude plugin install web@web-agent-skills
```

También podés hacerlo desde adentro de una sesión de Claude Code con
`/plugin marketplace add Juampii01/web-agent-skills` y después `/plugin`.

**3.** Probala. Abrí `claude` en una carpeta vacía y escribí:

```
/web:web-crear
```

O pedilo con tus palabras ("armame una web para mi negocio"): Claude elige la
skill sola.

**Actualizar:** `claude plugin marketplace update web-agent-skills`.

Para los scripts necesitás Python 3 (`python3 --version`). El optimizador de
imágenes usa Pillow: `pip install Pillow`.

---

## Camino B · claude.ai

**1. Activá la ejecución de código.** Las skills la necesitan para correr sus
scripts y crear archivos.
- Planes individuales: **Configuración → Capacidades** (*Settings → Capabilities*) y activá la creación y edición de archivos.
- Planes Team o Enterprise: lo activa quien administra la cuenta.

**2. Descargá los zips.** Están en la carpeta [`claude-ai/`](claude-ai) de este
repositorio, uno por skill. **No los descomprimas.**

**3. Subí cada skill.**
1. En Claude, andá a **Personalizar → Skills** (*Customize → Skills*).
2. Tocá **"+"** y elegí **subir una skill** (*Upload a skill*).
3. Seleccioná el `.zip` (por ejemplo `web-crear.zip`).
4. Repetí con las que quieras. Cada una se prende y apaga desde esa lista.

**¿Por cuáles empiezo?** `web-crear`, `web-contacto` y `web-nota`. Con esas
tres armás la web, la conectás a WhatsApp y la revisás.

**4. Probala.** Abrí un chat nuevo y escribí: *"Armame una web para mi
negocio"*. Si Claude arranca preguntando qué vendés y a quién, está funcionando.

---

## Problemas comunes

- **La skill no aparece (claude.ai):** subiste el `.zip` sin descomprimir y la
  ejecución de código está activada.
- **"python3 no se reconoce" (Windows):** reinstalá Python marcando "Add Python
  to PATH", o usá `python` en lugar de `python3`.
- **"claude no se reconoce":** cerrá y abrí la terminal. Si sigue, repetí el paso 1.
- **La web se parece a una plantilla:** pedile a Claude que corra el detector
  (`revisar.py`) y arregle todo lo que marque hasta llegar a 90.
