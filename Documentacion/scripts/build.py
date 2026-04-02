import os

# --- DETECCIÓN DE RUTAS ---
# Obtenemos la ruta de ESTE script (dentro de la carpeta 'scripts')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# La raíz de la documentación es una carpeta hacia atrás (..)
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
# La raíz principal (fuera de Documentacion) es otra carpeta hacia atrás
OUT_DIR = os.path.dirname(PROJECT_ROOT)

# Obtenemos el nombre exacto de la carpeta (probablemente "Documentacion")
DOCS_FOLDER_NAME = os.path.basename(PROJECT_ROOT)

# --- CONFIGURACIÓN ---
# Ahora el archivo final se guarda en OUT_DIR (fuera de Documentacion)
OUTPUT_FILE = os.path.join(OUT_DIR, 'README.md')
CONTENT_DIR = os.path.join(PROJECT_ROOT, 'content')

# Lista de archivos en orden (solo el nombre)
FRONT_MATTER_FILES = [
    'cover.md',
    'version-register.md',
    'collaboration-insights.md',
    'table-of-content.md',
    'student-outcome.md'
]

BACK_MATTER_FILES = [
    'bibliography.md'
]

PAGE_BREAK = '\n\n<div style="page-break-before: always;"></div>\n\n'

def process_file_content(filepath):
    """Lee el archivo y ajusta las rutas de las imágenes para que funcionen desde el directorio padre."""
    if not os.path.exists(filepath):
        print(f"Advertencia: No se encontró: {os.path.basename(filepath)}")
        return ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # AJUSTE DE RUTAS:
        # Como el archivo final ahora está un nivel ARRIBA de 'Documentacion',
        # cambiamos "../" (ej. ../assets/...) por "./Documentacion/" (ej. ./Documentacion/assets/...)
        content = content.replace('../', f'./{DOCS_FOLDER_NAME}/')
        
        return content

def main():
    final_content = []
    
    print(f"Carpeta de documentación detectada en: {PROJECT_ROOT}")
    print(f"El archivo final se guardará en: {OUT_DIR}")

    # 1. Procesar Front-Matter
    print("Procesando Front-Matter...")
    for filename in FRONT_MATTER_FILES:
        full_path = os.path.join(PROJECT_ROOT, 'front-matter', filename)
        final_content.append(process_file_content(full_path))
        final_content.append(PAGE_BREAK)

    # 2. Procesar Contenido Principal (Documento.md)
    print("Procesando Contenido Principal...")
    if os.path.exists(CONTENT_DIR):
        content_files = sorted([f for f in os.listdir(CONTENT_DIR) if f.endswith('.md')])
            
        for filename in content_files:
            print(f"   -> Agregando: {filename}")
            full_path = os.path.join(CONTENT_DIR, filename)
            final_content.append(process_file_content(full_path))
            final_content.append(PAGE_BREAK)
    else:
        print(f"Error: No existe la carpeta {CONTENT_DIR}")
    
    # 3. Procesar Back-Matter
    if BACK_MATTER_FILES:
        print("Procesando Back-Matter...")
        for filename in BACK_MATTER_FILES:
            full_path = os.path.join(PROJECT_ROOT, 'back-matter', filename)
            final_content.append(process_file_content(full_path))
            final_content.append(PAGE_BREAK)

    # Eliminar el último salto de página extra si existe
    if final_content and final_content[-1] == PAGE_BREAK:
        final_content.pop()

    # 4. Guardar el archivo final fuera de Documentacion
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("".join(final_content))
        print(f"\n¡Éxito! Archivo generado correctamente en: {os.path.abspath(OUTPUT_FILE)}")
    except Exception as e:
        print(f"\nError al escribir el archivo: {e}")

if __name__ == '__main__':
    main()