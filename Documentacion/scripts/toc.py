import os
import re

# --- CONFIGURACIÓN DE RUTAS ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Ruta de la carpeta de contenido
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# Archivo de salida
OUTPUT_FILE = os.path.join(PROJECT_ROOT, 'front-matter', 'table-of-content.md')

# --- DEFINICIÓN DEL ORDEN DE LECTURA ---
# 1. Front-Matter (EXCLUYENDO cover.md y el propio table-of-content.md)
FRONT_MATTER_FILES = [
    'version-register.md',
    'collaboration-insights.md',
    'student-outcome.md'
]

# 3. Back-Matter
BACK_MATTER_FILES = [
    'bibliography.md'
]

# Lista maestra en orden de aparición
ALL_FILES = []
# Agregamos rutas completas a la lista maestra
for f in FRONT_MATTER_FILES:
    ALL_FILES.append(os.path.join(PROJECT_ROOT, 'front-matter', f))
    
if os.path.exists(CONTENT_DIR):
    # Obtenemos archivos .md y los ordenamos alfabéticamente
    # Esto asegura que chapter-1 vaya antes que chapter-2
    content_files = sorted([f for f in os.listdir(CONTENT_DIR) if f.endswith('.md')])
    
    for f in content_files:
        ALL_FILES.append(os.path.join(CONTENT_DIR, f))
else:
    print(f"Advertencia: No se encontró la carpeta {CONTENT_DIR}")

for f in BACK_MATTER_FILES:
    ALL_FILES.append(os.path.join(PROJECT_ROOT, 'back-matter', f))

def slugify(text):
    """
    Convierte un título en un enlace ancla compatible con Markdown estándar.
    Ej: "1.1. Descripción de la Startup" -> "11-descripción-de-la-startup"
    """
    slug = text.lower().strip()
    # 1. Reemplazar espacios con guiones
    slug = slug.replace(' ', '-')
    # 2. Eliminar caracteres que no sean alfanuméricos o guiones (ej: puntos, paréntesis)
    # Nota: Mantenemos tildes/ñ porque muchos visores de MD modernos las soportan,
    # pero eliminamos puntuación como . , : ?
    slug = re.sub(r'[^\w\-áéíóúñü]', '', slug)
    # 3. Eliminar guiones múltiples seguidos
    slug = re.sub(r'\-+', '-', slug)
    return slug

def parse_headings(file_path):
    """Lee un archivo y extrae las líneas que empiezan con #"""
    headings = []
    if not os.path.exists(file_path):
        print(f"Saltando (no encontrado): {file_path}")
        return headings

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Detectar líneas que son títulos (ej: "## Título")
            match = re.match(r'^(#+)\s+(.*)', line)
            if match:
                level = len(match.group(1)) # Número de hashtags (#)
                title = match.group(2).strip()
                headings.append((level, title))
    return headings

def generate_toc():
    print("Escaneando archivos para generar el índice...")
    toc_lines = ["## Contenido\n"]

    for file_path in ALL_FILES:
        headings = parse_headings(file_path)
        for level, title in headings:
            # Lógica de indentación:
            # H1 (#) -> sin identación (o bullet simple)
            # H2 (##) -> 2 espacios
            # H3 (###) -> 4 espacios, etc.
            # Ajustamos 'level - 1' si quieres que H1 sea el nivel base.
            indent = "  " * (max(0, level - 1))
            
            # Crear el link (slug)
            anchor = slugify(title)
            
            # Formato: - [Título](#link)
            line = f"{indent}- [{title}](#{anchor})"
            toc_lines.append(line)
        
        if "collaboration-insights.md" in file_path:
            toc_lines.append("  - [Contenido](#contenido)")

    # Guardar el archivo
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(toc_lines))
        print(f"Índice generado exitosamente en: front-matter/table-of-content.md")
    except Exception as e:
        print(f"Error al guardar el índice: {e}")

if __name__ == '__main__':
    generate_toc()