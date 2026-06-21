### Sprint 3

#### Sprint Planning 3

&nbsp;

En esta sección se consolidan los acuerdos fundamentales alcanzados por el equipo ArcadiaDevs durante la sesión de planificación del Sprint 3, realizada de manera virtual a través de la plataforma Discord. Tras el despliegue exitoso de la primera versión de la aplicación web, considerando funcionalidades que son importantes para el usuario del segmento objetivo de productores y la mejora de la presencia digital de Viora, el propósito central de esta reunión fue evolucionar hacia la segunda versión de la Aplicación Web y la construcción de la primera versión operativa del Servicio Web de Viora. Para ello, el equipo priorizó el desarrollo de los subdominios core y support vinculados al monitoreo inteligente de parcelas, la gestión fitosanitaria, la coordinación entre productores y especialistas, y la automatización de procesos de trazabilidad y validación. Asimismo, se consideró la corrección y refinamiento de funcionalidades implementadas en el Sprint 2, alineando el esfuerzo de ingeniería con la necesidad de reducir los principales pain points identificados en ambos segmentos de usuarios.

Para esta iteración, el equipo ha definido un compromiso de trabajo de 97 puntos de esfuerzo sobre una velocidad proyectada de 100 puntos. Dentro de esta estimación, se ha asignado 1 punto a actividades de corrección y mejora incremental relacionadas con la Landing Page y la Web Application previamente desplegadas, mientras que los 93 puntos restantes corresponden al desarrollo de nuevas capacidades funcionales y servicios backend asociados al ecosistema Viora. Esta planificación busca no solo incrementar el valor funcional de la plataforma mediante capacidades de analítica predictiva, monitoreo climático y sensoramiento remoto satelital, sino también establecer las bases del Servicio Web encargado de orquestar la sincronización de datos externos, gestión de alertas, matchmaking técnico y trazabilidad de intervenciones. Además, se incorporan activamente las lecciones aprendidas durante la retrospectiva anterior, ampliando el margen temporal de coordinación y validación técnica para garantizar un Sprint Planning más sólido, realista y alineado con los objetivos estratégicos del producto.

A continuación, se presenta el cuadro resumen del Sprint Planning Meeting, el cual detalla la logística de la sesión, la revisión de los resultados del sprint previo y el Sprint Goal diseñado para transformar datos climáticos y satelitales en decisiones agronómicas de alto impacto.

| **Sprint #** | Sprint 3 |
| :--- | :--------------- |
| **Date** | 2026-05-20 |
| **Time** | 08:00 AM |
| **Location** | Discord (Virtual) |
| **Prepared By** | Trinidad Leon, Jahat Jassiel |
| **Attendees (to planning meeting)** | Carpio Peña, Josue Francisco / Espada Lazo, Piero Anthony / Li Gayoso, Diana Carolina / Paredes Maza, Juan de Dios / Santi Guerrero Fabrizio Alonso / Trinidad Leon, Jahat Jassiel |
| **Sprint 2 Review Summary** | Durante el Sprint 2, se cumplió satisfactoriamente con el 100% de los objetivos mediante la implementación de las mejoras del Landing Page y la primera versión de la aplicación web, logrando entregar 32 story points distribuidos en 6 historias de usuario implementadas, y las correciones de las historias de usuario del Landing Page. El incremento fue desplegado con éxito en Firebase bajo una arquitectura responsiva, respaldada por un flujo de trabajo colaborativo de 161 commits. Por su parte, el Product Owner validó que el producto cumple con el Sprint Goal al consolidar que la primera versión muestra información relevante para uno de los principales segmentos objetivo,aprobando la entrega sin observaciones técnicas pendientes. A pesar de ello, aún se deben realizar correciones al Landing Page. |
| **Sprint 2 Retrospective Summary** | Durante el sprint 2, el equipo indentificó que el tiempo designado para la documentación e implementación era corto, por lo que al haber contratiempos la calidad de la entrega y alcance del sprint planning podría ser afectado; por ello, se acordó en definir deadlines definitivas y posibles, para que se pueda identificar las razones de sobreestimaciones. De esta manera, cada integrante podrá determinar sus puntos de mejora personales y el equipo podrá desarrollarse, además, en este sprint se ha designado más tiempo para su elaboración. |
| **Sprint 3 Goal** | Nuestro enfoque está en proporcionar un ecosistema colaborativo de respuesta fitosanitaria y monitoreo inteligente que conecte a productores olivareros y especialistas fitosanitarios mediante alertas predictivas, diagnóstico territorial y coordinación de intervenciones técnicas; creemos que entrega una reducción del tiempo de reacción frente a amenazas biológicas y climáticas, una mayor capacidad de prevención operativa y una trazabilidad integral de las acciones ejecutadas tanto para productores como para especialistas dentro del ecosistema Viora; esto se confirmará cuando los productores puedan identificar riesgos activos en sus parcelas, solicitar asistencia técnica y dar seguimiento a las intervenciones realizadas, mientras los especialistas puedan prospectar zonas críticas, gestionar solicitudes de servicio y validar tratamientos sobre la base de información climática, satelital y agronómica consolidada. |
| **Sprint 3 Velocity** | 100 |
| **Sum of Story Points** | 97 |

#### Aspect Leaders and Collaborators

&nbsp;

En esta sección se presenta la matriz Leadership-and-Collaboration Matrix (LACX) correspondiente al Sprint 3, diseñada para fortalecer la coordinación estratégica y la especialización técnica dentro del ecosistema Viora durante el desarrollo de la segunda versión de la aplicación web y la primera versión operativa del Servicio Web. Para este incremento, el alcance se ha reorganizado en torno a bounded contexts alineados con los principales procesos del negocio y los pain points identificados en los segmentos de productores olivareros y especialistas fitosanitarios. En consecuencia, el equipo ha distribuido las responsabilidades entre los contextos Shared, Agronomic, Surveillance, Intervention, y PAM (Profile & Asset Management), además de considerar la evolución y refinamiento de la Landing Page.

| Team Member (Last Name, First Name) | GitHub Username | Shared Context Leader (L) / Collab (C) | Agronomic Context Leader (L) / Collab (C) | Surveillance Context Leader (L) / Collab (C) | Intervention Context Leader (L) / Collab (C) | PAM Context Leader (L) / Collab (C) | Brand & Communication Leader (L) / Collab (C) |
|---|---|---|---|---|---|---|---|---|
| Carpio, Josue   | josf17                           | C | C | C | C | L | C |
| Espada, Piero   | espadita2510 / pieroedeveloper25 | C | C | L | C | C | C |
| Li, Diana       | peruvianMiau                     | C | C | C | L | C | C |
| Paredes, Victor | DaronCameloft                    | C | C | C | C | C | L |
| Santi, Fabrizio | Santi2007939                     | C | L | C | C | C | C |
| Trinidad, Jahat | trinity-bytes                    | L | C | C | C | C | C |

#### Sprint Backlog 3

&nbsp;

El objetivo principal de este Sprint 3 es desarrollar la segunda versión de la aplicación web y la primera versión operativa del Servicio Web de Viora, mediante la incorporación de capacidades de autenticación segura, monitoreo fitosanitario inteligente, sincronización climática y satelital, gestión de alertas epidemiológicas y coordinación de intervenciones técnicas entre productores olivareros y especialistas fitosanitarios. Asimismo, el sprint contempla la consolidación de procesos de trazabilidad agronómica, reputación comunitaria y administración de perfiles y activos agrícolas, junto con el refinamiento incremental de la Landing Page y funcionalidades implementadas en iteraciones anteriores.

\begin{figure}[H]
\caption{Vista General del Sprint Backlog 3}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-backlog/sb3.png}
\caption*{\textit{Nota.} Elaboración propia a partir del tablero en Trello: https://trello.com/invite/b/6a1b2ed803a5bfcd16c6439c/ATTIf0554d374fee985e464bf104446c8676C57DDFD2/1asi0729-viora-sb3}
\end{figure}

\begin{longtable}{|p{0.05\textwidth}|p{0.14\textwidth}|p{0.05\textwidth}|p{0.14\textwidth}|p{0.24\textwidth}|p{0.08\textwidth}|p{0.12\textwidth}|p{0.07\textwidth}|}
\hline
\multicolumn{2}{|l|}{\textbf{Sprint \#}} & \multicolumn{6}{l|}{Sprint 3} \\ \hline
\multicolumn{2}{|l|}{\textbf{User Story}} & \multicolumn{6}{l|}{\textbf{Work-Item / Task}} \\ \hline
\textbf{Id} & \textbf{Title} & \textbf{Id} & \textbf{Title} & \textbf{Description} & \textbf{Estimation (Hours)} & \textbf{Assigned To} & \textbf{Status} \\ \hline
\endfirsthead

\hline
\multicolumn{2}{|l|}{\textbf{User Story}} & \multicolumn{6}{l|}{\textbf{Work-Item / Task (Continuación)}} \\ \hline
\textbf{Id} & \textbf{Title} & \textbf{Id} & \textbf{Title} & \textbf{Description} & \textbf{Estimation} & \textbf{Assigned To} & \textbf{Status} \\ \hline
\endhead

% US47
US47 & Exploración de beneficios para el Productor & TK01 & Presentación de todos los beneficios del segmento de productores & Implementación de cards con todos los beneficios ofrecidos para el segmento de productores & 1.0 & Paredes, Victor & To-do \\ \hline

% US48
US48 & Exploración de beneficios para el Especialista & TK01 & Presentación de todos los beneficios del segmento de especialistas & Implementación de cards con todos los beneficios ofrecidos para el segmento de especialistas fitosanitarios & 1.0 & Paredes, Victor & To-do \\ \hline

% US51
US51 & Exploración del equipo detrás de la plataforma & TK01 & Sección de video e imágenes del equipo & Implementación de placeholder para imágenes del equipo trabajo y el video About the team & 1.0 & Paredes, Victor & To-do \\ \hline

% US08
US08 & Monitoreo de telemetría IoT para decisiones hídricas & TK01 & Datos inválidos mostrados & Corregir que aparezcan elementos no existenten en la lista de dispositivos IoT & 1.0 & Santi, Fabrizio & To-do \\ \hline

% US15
US15 & Alerta por frío insuficiente & TK01 & Componente de alerta de frío & Implementación de tipo de alerta fenológica de frío y filtro & 0.5 & Espada, Piero & To-do \\ \hline

% US21
US21 & Consulta de zonas con alerta & TK01 & Radar fitosanitario con Mapbox & Implementación de mapa interactivo con marcadores georreferenciados de alertas epidemiológicas. & 2.0 & Espada, Piero & To-do \\ \hline

% US22
US22 & Filtrado de alertas por gravedad & TK01 & Filtro de severidad y tipo de plaga & Implementación de filtros dinámicos para alertas de plagas. & 1.0 & Espada, Piero & To-do \\ \cline{3-8}
& & TK02 & Panel de alertas filtradas & Implementación de listado sincronizado con las alertas visibles en el mapa. & 2.0 & Espada, Piero & To-do \\ \hline

% US24
US24 & Identificación de especialistas cercanos & TK01 & Lista de especialistas disponibles & Implementación de lista de técnicos con datos de disponibilidad. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Indisposición de especialistas & Implementación de componente de especialistas no disponibles & 0.5 & Li, Diana & To-do \\ \hline

% US25
US25 & Solicitud formal de intervención & TK01 & Solicitud de invervención & Implementación de creación de solicitud con estado en espera. & 1.0 & Li, Diana & To-do \\ \hline

% US26
US26 & Evaluación de disponibilidad operativa & TK01 & Lista de solicitudes en espera & Implementación de lista de solicitudes sin respuesta. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Información de solicitud & Implementación de popup con datos de la unidad productiva y alerta. & 1.5 & Li, Diana & To-do \\ \hline

% US27
US27 & Resolución de la solicitud de intervención & TK01 & Aceptación de solicitud & Implementación de aceptación del especialista y visualización del productor. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Lista de solicitudes rechazadas & Implementación de lista de solicitudes rechazadas. & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK03 & Lista de solicitudes en proceso & Implementación de lista de solicitudes recientemente aceptadas preeliminarmente. & 0.5 & Li, Diana & To-do \\ \hline

% US43
US43 & Evaluación preliminar de la unidad productiva & TK01 & Información consolidada de la parcela & Implementación de resumen de últimos datos de trazabilidad de la parcela y últimas alertas recibidas & 2.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Visualización del mapa de la parcela & Configurar Mapbox SDK para mostrar la parcela. & 1.0 & Li, Diana & To-do \\ \hline

% US29
US29 & Emisión de propuesta de servicio & TK01 & Creación de presupuesto & Implementación de formulario relacionado con la parcela asignada. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Muestra de presupuesto & Implementación de cambio de estado de solicitud en aceptada & 0.5 & Li, Diana & To-do \\ \hline

% US30
US30 & Resolución de la propuesta de servicio & TK01 & Resolución de propuesta & Implementación de visualización del formulario para solo leer con opciones de aceptar o rechazar. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Repetición del ciclo de búsqueda & Implementación de cambio de estado y retomar actividad de búsqueda de especialistas & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK03 & Lista de propuestas rechazadas & Implementación de lista de propuestas rechazadas del especialista & 1.0 & Li, Diana & To-do \\ \hline

% US31
US31 & Habilitación de canal de comunicación directo & TK01 & Botón de contacto habilitado & Implementación de popup con datos de correo y whatsapp. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Botón de contacto deshabilitado & Implementación de tooltip para comunicar que se habilirá al aceptar una propuesta. & 0.5 & Li, Diana & To-do \\ \hline

% US32
US32 & Revisión de antecedentes agronómicos en campo & TK01 & Información de trazabilidad de la parcela & Implementación de resumen de últimos datos de trazabilidad de la parcela & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Información de últimas alertas similares & Implementación de lista de alertas similares & 1.0 & Li, Diana & To-do \\ \hline

% US33
US33 & Registro de datos de inspección física & TK01 & Formulario de inspección física & Implementación de formulario para registrar observaciones biológicas y daños detectados. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK02 & Registro de evidencias de inspección & Implementación de carga de imágenes y notas técnicas relacionadas a la parcela. & 1.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK03 & Resumen de hallazgos de campo & Implementación de componente con resumen de observaciones registradas. & 0.5 & Paredes, Victor & To-do \\ \hline

% US34
US34 & Emisión de prescripción de agrofármacos & TK01 & Formulario de receta técnica & Implementación de formulario para registrar agrofármacos, dosis y método de aplicación. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Resumen de prescripción emitida & Implementación de componente de visualización de receta técnica generada. & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK03 & Notificación de nueva receta & Implementación de mensaje de disponibilidad de plan de tratamiento para el productor. & 0.5 & Li, Diana & To-do \\ \hline

% US07
US07 & Delimitación de área productiva & TK01 & Configuración de Mapbox SDK & Implementación de mapa interactivo para delimitación de parcelas. & 2.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK02 & Herramienta de dibujo de polígonos & Implementación de selección de puntos y cierre de área geográfica. & 2.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK03 & Validación de polígono incompleto & Implementación de validación para impedir parcelas sin cierre correcto. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK44 & Visualización de parcela registrada & Implementación de componente de visualización de límites geográficos registrados. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK05 & Vinculación climática automática & Implementación de asociación automática entre parcela y datos climáticos zonales. & 0.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK06 & Lista de parcelas & Implementación de lista de parcelas, con selección para ver el detalle de cada una y botón para la creación de una nueva. & 1.0 & Santi, Fabrizio & To-do \\ \hline

% US16
US16 & Plan de fertilización ajustado al clima & TK01 & Generación de recomendación agronómica & Implementación de estrategia compensatoria según riesgo climático o fenológico. & 1.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK02 & Resumen de tratamiento recomendado & Implementación de visualización de insumos y dosis sugeridas para mitigación. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK03 & Ajuste de ventana de aplicación & Implementación de actualización de recomendación según cambios climáticos. & 0.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK04 & Alerta de modificación climática & Implementación de notificación sobre cambio de ventana óptima de aplicación. & 0.5 & Paredes, Victor & To-do \\ \hline

% US35
US35 & Certificación de aplicación de receta técnica & TK01 & Formulario de certificación de aplicación & Implementación de registro de fecha y dosificación aplicada en campo. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Actualización de historial de parcela & Implementación de consolidación de trazabilidad posterior a intervención. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK03 & Advertencia de aplicación fuera de ventana & Implementación de mensaje de posible reducción de eficacia climática. & 0.5 & Li, Diana & To-do \\ \hline

% US17
US17 & Certificación de aplicación del plan de mitigación & TK01 & Formulario de certificación de intervención & Implementación de registro de fecha e insumos aplicados en campo. & 1.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK02 & Validación de datos obligatorios & Implementación de validación de insumos utilizados y fecha de intervención. & 0.5 & Santi, Fabrizio & To-do \\ \hline

% US36
US36 & Consolidación del gasto de intervención & TK01 & Formulario de registro de gastos & Implementación de ingreso de costos operativos y agrofármacos utilizados. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK02 & Actualización de métricas financieras & Implementación de recálculo de rentabilidad asociado a la parcela. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK03 & Resumen económico de intervención & Implementación de visualización consolidada de gastos registrados. & 0.5 & Li, Diana & To-do \\ \hline

% US18
US18 & Consolidación del gasto de mitigación climática & TK01 & Formulario de gasto de mitigación climática & Implementación de ingreso de costos asociados al plan nutricional. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK02 & Validación de declaración financiera & Implementación de bloqueo de cierre sin registro de costos. & 0.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK03 & Actualización de rentabilidad productiva & Implementación de recálculo financiero posterior a la mitigación climática. & 1.0 & Santi, Fabrizio & To-do \\ \hline

\end{longtable}

#### Deployment Evidence for Sprint Review

&nbsp;

#### Execution Evidence for Sprint Review

&nbsp;

Durante el Sprint 3 se implementó con éxito la segunda versión de la aplicación web y la primera versión operativa del servicio web de Viora. En el Landing Page se incorporaron las secciones de beneficios segmentados para productores olivareros y especialistas fitosanitarios, así como la sección del equipo detrás de la plataforma y un video de presentación. En la Web Application se desarrollaron funcionalidades de gestión de parcelas con delimitación poligonal vía Mapbox, visualización de datos de trazabilidad agronómica por parcela, y un panel de control general con resumen del estado de las parcelas.

A continuación, se exponen las capturas de pantalla de las principales vistas implementadas en el entorno de producción. Asimismo, para evidenciar el comportamiento dinámico del sitio, se adjunta un enlace a un video demostrativo que ilustra a detalle la visualización interactiva y la navegación fluida lograda en este Sprint.

\begin{figure}[H]
\caption{Página principal del Landing Page con la propuesta de valor de Viora.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/lp-home.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Sección de beneficios para productores olivareros en el Landing Page.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/lp-benefits-producer.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Sección de beneficios para especialistas fitosanitarios en el Landing Page.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/lp-benefits-specialist.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Sección del equipo detrás de la plataforma Viora.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/lp-about-team-1.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Sección de video About the Team en el Landing Page.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/lp-about-the-team-video.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Vista general del dashboard de la Web Application con resumen de parcelas.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-dashboard-overview-1.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Detalle del dashboard con indicadores de estado de las parcelas.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-dashboard-overview-2.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Listado de parcelas del productor con información de trazabilidad.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-my-plots-1.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Detalle de una parcela con mapa georreferenciado y datos agronómicos.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-plot-detail.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Vista de overview de parcela con imágenes satelitales y estado NDVI.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-plot-overview-1.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Formulario de edición de parcela con herramienta de delimitación poligonal.}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-evidence/sprint-3/wa-edit-plots.jpeg}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

[https://viora-website.vercel.app/](https://viora-website.vercel.app/)

[https://viora-webapp.vercel.app/](https://viora-webapp.vercel.app/)

[https://tinyurl.com/viora-sprint-3](https://tinyurl.com/viora-sprint-3)

&nbsp;

#### Services Documentation Evidence for Sprint Review

&nbsp;

#### Software Deployment Evidence for Sprint Review

&nbsp;

#### Team Collaboration Insights for Sprint Review

&nbsp;

En esta sección se detallan las actividades de implementación llevadas a cabo durante el Sprint 3, orientadas a la construcción y despliegue de la Landing Page, Webapp de Viora y Webservice de Viora. El proceso de desarrollo se ejecutó de manera ágil y estructurada, garantizando que todos los miembros del equipo tuvieran una participación técnica activa. Para respaldar la trazabilidad del trabajo colaborativo, a continuación se presentan las evidencias extraídas directamente de los analíticos de GitHub (Contributors). Estas capturas ilustran el flujo de integración, con la participación de los 6 autores.

\begin{figure}[H]
\caption{Vista de Contributors de Github - Website}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-review/sprint-3/contributors-website.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Vista de Contributors de Github - Webapp}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-review/sprint-3/contributors-webapp.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}

\begin{figure}[H]
\caption{Vista de Contributors de Github - Webservice}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-review/sprint-3/contributors-webservice.png}
\caption*{\textit{Nota.} Elaboración propia.}
\end{figure}


\newpage