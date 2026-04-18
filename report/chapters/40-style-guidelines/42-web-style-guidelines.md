### Web Style Guidelines

1. **Grid System**
    
    Para mantener la consistencia en el diseño de paneles complejos y dashboards de monitoreo, implementamos un sistema de rejilla estructurado.

    - **Sustento de diseño:** Se utiliza una rejilla de 12 columnas flexible. Este estándar permite que los widgets de datos (gráficos de temperatura, humedad y alertas de plagas) se reorganicen de forma fluida según el ancho de la pantalla. Los márgenes y espacios entre columnas están definidos para evitar la saturación visual, permitiendo que el usuario se concentre en las métricas clave del cultivo de olivo.

  <br>

\begin{figure}[H]
    \caption{Sistema de retícula y grilla responsiva para Viora.}
    \centering
    \includegraphics[width=0.8\textwidth]{report/assets/style-guidelines/01-Grid-System.jpg}
    \caption*{\textit{Nota.} Configuración de columnas, márgenes y canales para Desktop HD, Desktop y Mobile. Elaboración propia.}
\end{figure}
    
<br>

2. **Textfields**
   
   La entrada de datos precisa es vital para la configuración de sensores y parámetros de cultivo.

   - **Sustento de diseño:** Los campos de texto están diseñados con un enfoque en la claridad y la prevención de errores. Incluyen etiquetas flotantes o superiores permanentes, estados de interacción claros (reposo, enfoque, error y éxito) y micro-textos de ayuda. Esto es especialmente importante cuando se debe ingresar coordenadas o umbrales de alerta para la Xylella fastidiosa.

  <br>

\begin{figure}[H]
    \caption{Especificaciones de campos de entrada de texto de Viora.}
    \centering
    \includegraphics[width=0.8\textwidth]{report/assets/style-guidelines/02-Textfields.jpg}
    \caption*{\textit{Nota.} Definición de variantes (con iconos, etiquetas) y estados del sistema (Focus, Error, Disabled). Elaboración propia.}
\end{figure}
    
<br>

3. **Button & Link**

    Los elementos de acción son el puente entre el análisis de datos y la ejecución de tareas.

   - **Sustento de diseño:** Hemos establecido una jerarquía visual estricta para las acciones:
     - Botones Primarios: Con colores sólidos y contrastantes para acciones definitivas.
     - Botones Secundarios: Con bordes definidos para acciones alternativas.
     - Enlaces: Con estilos sutiles para navegación profunda.

  <br>

\begin{figure}[H]
    \caption{Estilos de botones, enlaces y acciones interactivas de Viora.}
    \centering
    \includegraphics[width=0.8\textwidth]{report/assets/style-guidelines/03-Button-&-Link.jpg}
    \caption*{\textit{Nota.} Jerarquía de botones por tamaño (Small, Medium, Large) y estilos aplicados a dispositivos móviles. Elaboración propia.}
\end{figure}
    
<br>

4. **Shadows & Blurs**

    Utilizamos la profundidad visual para organizar la información en capas lógicas.

   - **Sustento de diseño:** Se aplican sombras suaves (soft shadows) para dar elevación a elementos interactivos como tarjetas de resumen de sensores o cuadros de mando. Los efectos de desenfoque (blurs) se reservan para fondos de ventanas modales o menús desplegables, lo que ayuda a mantener la atención del usuario en la tarea activa (como la confirmación de un riego) sin perder el contexto de la pantalla principal.

  <br>

\begin{figure}[H]
    \caption{Guía de elevación, sombras y efectos de transparencia de Viora.}
    \centering
    \includegraphics[width=0.8\textwidth]{report/assets/style-guidelines/04-Shadows-&-Blurs.jpg}
    \caption*{\textit{Nota.} Parámetros técnicos de Drop Shadows y efectos de Glassmorphism para la profundidad visual. Elaboración propia.}
\end{figure}
    
<br>

5. **Components**
   
   La consistencia se logra a través de la reutilización de elementos de interfaz probados.

   - **Sustento de diseño:** La biblioteca de componentes web integra elementos esenciales de interacción y estado, como selectores (checkboxes, radios y toggles) y sistemas de identificación visual mediante avatares. Al estandarizar estos componentes de control, reducimos la carga cognitiva del usuario y aseguramos una respuesta visual consistente en todos los módulos de gestión de la plataforma.

  <br>

\begin{figure}[H]
    \caption{Componentes de selección y elementos de identidad de usuario de Viora.}
    \centering
    \includegraphics[width=0.8\textwidth]{report/assets/style-guidelines/05-Components.jpg}
    \caption*{\textit{Nota.} Definición de estilos para herramientas de selección (Checkbox, Radio, Toggle) y variantes de avatares con estados activos. Elaboración propia.}
\end{figure}
    
<br>

\newpage