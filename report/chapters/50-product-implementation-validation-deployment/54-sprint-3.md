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

Durante el Sprint 3, el equipo ArcadiaDevs consolidó la primera versión operativa del servicio web de Viora en el repositorio backend `viora-platform`. Este incremento permitió integrar las bases técnicas para los contextos Shared, Agronomic, Surveillance, Intervention y PAM, alineados con la construcción de servicios para monitoreo inteligente de parcelas, gestión de alertas, trazabilidad agronómica, coordinación de intervenciones y administración de perfiles y activos.

Para asegurar la trazabilidad del desarrollo, las contribuciones fueron integradas mediante ramas de trabajo, ramas de release y la rama principal `main`. La evidencia de despliegue se sustenta en los commits registrados en el repositorio, donde se observa la incorporación progresiva de configuración del proyecto, modelos de dominio, controladores REST, servicios de aplicación, persistencia, documentación OpenAPI, autenticación JWT, ajustes de endpoints y merges de integración hacia las ramas principales.

A continuación, se presenta la matriz de control de versiones correspondiente al Sprint 3, la cual detalla el historial de commits realizados en el repositorio del servicio web.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on (Date) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | def3076 | chore: initial commit. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1032751 | feat(result): add result test java file. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2f69a10 | feat(dependencies-build): add pluralize library to pom.xml. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 88b96c3 | build(dependencies): remove pluralize library from pom.xml. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 11122a9 | feat(shared): add global exception handler. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | dda4523 | build(dependencies): add springdoc-openapi and pluralize libraries to pom.xml. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 32bda4c | feat(shared): add generic result wrapper for use case responses. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 66dc7cf | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3f1ebfe | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3f54ad9 | feat(shared): convert catalog name, the shema name and the table name to snake case. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d545a98 | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 71f8894 | build: update pluralize dependency. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6095243 | build(Sanke): adding class to change capital letters and singular phrases. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0d34508 | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 49bd80e | ci(docker): add dockerfile for building and running viora-platform. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | cf7fb47 | docs(shared): add javadoc comments to snake case physical strategy. |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | dc306fa | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1a44dc0 | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 202366a | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 26/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f2a8831 | feat(shared): add the function physical sequence name. |  | 30/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 510cb98 | build(pom): adding dependeces to use boot and engine. |  | 30/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5baae45 | feat(shared):  add messages properties. |  | 30/05/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 405ccda | docs: add comments for methods. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 412baec | feat(i18n): update message properties. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | ace34b0 | build: update gitignore. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0a4fcd7 | feat(i18n): create localResolver method to manage default locale and supported locales. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 034b638 | feat(i18n): update messages properties for errors and validations. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c492cb6 | feat(shared): enhance result generic contract. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | edeec25 | feat(i18n): create locale-resolver method to manage default locale and supported locales. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 87c27c1 | feat(i18n): update messages properties for errors and validations. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 406b025 | feat(shared): add application-error record for standardized error handling. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 489c7c1 | feat(shared): add error-resource for standardized error responses. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 69b4a33 | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8ecabd2 | feat(shared): add message-resource for success and informational rest responses. |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6724dce | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 02/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 22ec9fe | feat(shared): add openapi configuration with jwt authentication. |  | 05/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 411fc5f | refactor(shared): rename SnakeCasePhysicalNamingStrategy package for clarity. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6295972 | feat(shared): add abstract-domain-aggregate-root for domain event handling. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | cef4dd1 | feat(shared): add auditable-abstract-persistence-entity for auditing support. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bb2ff54 | feat(shared): add error response assembler and response entity assembler. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 35ef832 | fix(shared): correction of global exception handler. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0e65e99 | feat(shared): add open-api configuration for api documentation and jwt authentication. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 197effd | Merge remote-tracking branch 'origin/feature/shared' into feature/shared |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 686b2b6 | Merge branch 'feature/shared' into develop. |  | 06/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | abc7feb | chore(agronomic): initialize plots backend structure. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 278e372 | feat(agronomic): add area-size value object to represent plot area in hectares. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 779eb62 | feat(agronomic): add geo-point value object to represent geographic coordinates. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 82fd61b | feat(agronomic): implement plot aggregate. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 750180b | feat(agronomic): add plot-id value object to represent unique plot identifiers. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | ec186ca | feat(agronomic): add plot-name value object to represent business names for plots. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 08992df | feat(agronomic): add polygon-coordinates value object to represent closed geographic polygons for plots. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f1a360e | feat(agronomic): add user-id value object to represent user identifiers for plot ownership. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b157dd1 | feat(agronomic): add plot-repository interface for plot persistence operations. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 18c876d | feat(agronomic): add plot-not-found-exception for handling missing plots. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | cf90d0d | feat(agronomic): add plot-deletion-conflict-exception for handling deletion conflicts. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b591c81 | feat(agronomic): add invalid-polygon-coordinates-exception for handling invalid plot polygon coordinates. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3b810b4 | feat(agronomic): add iotdevicerepository and plotrepository interfaces. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b55da4f | feat(agronomic): add value objects for iot device, plot, and user identifiers. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | e136245 | feat(agronomic): add iotdevice aggregate root with validation rules. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3cffed5 | feat(agronomic): add spring data jpa repositories for iotdevice and plot entities. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 78ac8d8 | feat(agronomic): add jpa entities for iotdevice and plot persistence. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2a495a3 | feat(agronomic): add get-plot-by-id-query for retrieving plots by unique identifier. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a7c05ed | feat(agronomic): add plot-query-service for handling plot read operations. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a760b1c | feat(agronomic): add query for retrieving iot devices by plot id with ownership validation. |  | 08/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a785b1e | feat(agronomic): implement iotdevice1ueryservice for retrieving devices by plot id with ownership validation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3fc53f1 | feat(agronomic): add iotdeviceResource for rest response of iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2e3341d | feat(agronomic): add jpa adapters for iotdevice and plot repositories. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 54c6e7a | feat(agronomic): add iotdevicescontroller for managing iot devices by plot. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | fefbf74 | feat(agronomic): add assembler for converting iotDevice to iotdeviceresource dto. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 18a3429 | feat(agronomic): add geo-point-attribute-convert for converting GeoPoint to database format. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b0f1020 | feat(agronomic): add jpa-plot-repository-adapter for jpa-based plot data access. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2d91ae4 | fix(agronomic): correct formatting in plot.java documentation for deactivate method. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 89fe6fd | feat(agronomic): add assembler for converting plot-persistence-entity to plot aggregate. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | e3a3550 | feat(agronomic): add jpa persistence entity for plots. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 02ec205 | feat(agronomic): add assembler for converting plot aggregate to plot-persistence-entity. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5ef5f82 | feat(agronomic): add jpa attribute converter for polygon-coordinates. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a56d348 | feat(agronomic): add spring sata jpa repository for plot-persistence-entity. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0397c48 | feat(agronomic): add createiotdevicecommand for registering new iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 268e6cb | feat(agronomic): add iotdevicecommandservice for handling iot device creation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 15de491 | feat(agronomic): add resource and assembler for creating iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0b4494c | feat(agronomic): enhance iotdevicescontroller with create and list device endpoints. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bc8058a | feat(agronomic): add plot-resource class for rest api representation of plot data. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1679990 | feat(agronomic): add assembler for converting plot aggregate to plot-resource. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9d5cd42 | feat(agronomic): add plots-controller for managing agricultural plots. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 59dc256 | fix(agronomic): enhance error handling. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f15144a | feat(agronomic): add detele plot command for deleting agricultural plots. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 523f30d | feat(agronomic): implement plot-command-service for handling plot updates and deletions. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c32177e | feat(agronomic): add plot-deletion-policy for managing plot deletion logic. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | aa49d48 | feat(agronomic): add update plot command for updating agricultural plot details. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 48e497a | feat(agronomic): add assembler for converting update plot resource to update plot command. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 95cf850 | feat(agronomic): add update plot resource for handling plot update requests. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8acaa5d | fix(agronomic): harden plot operations and project configuration. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 7588a4e | feat(agronomic): add environment configuration files for local and production setups. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3740cc2 | feat(agronomic): definition of aggregate root |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | aa4d97a | feat(agronomic):add valueobjects |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3c5dbf1 | feat(agronomic): implement iotdevicecommandservice and enhance result class. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d5f4bca | feat(agronomic): add command, event for create a plot. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9f06e92 | feat(agronomic): add query to find plots by user id. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2c3b0a6 | feat(agronomic): configure application properties for development and production environments. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | ef616cb | feat(agronomic): add spring data repository for agronomic statistics. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3d5ddfb | feat(agronomic): implement repository and query for agronomic statistics. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9a864db | refactor(agronomic): change estate boolean to string again. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d5b8afb | Merge branch 'feature/agronomic/plots' into develop. Related to TS010. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8471c47 | feat(agronomic): add agronomicstatisticqueryService for retrieving agronomic statistics. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 59e152f | Merge branch 'feature/agronomic/list-iot-device' into feature/agronomic/plots |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 380c06d | feat(agronomic): add assemblers for converting between iotdevice and iotdeviceentity. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1761748 | feat(agronomic): add iotdevicenotfoundexception for handling missing iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c4fa671 | refactor(agronomic): simplify iotdevice constructor and remove default constructor. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | e743782 | feat(agronomic): enhance iotdevice1ueryservice to validate plot ownership using plotid and userid. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | fdd3a2f | feat(agronomic): update iotdevicescontroller to enhance response handling and improve api documentation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 56192f9 | feat(agronomic): refactor jpaiotdevicerepositoryadapter to use assemblers for entity conversion. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 58dfaaa | Merge branch 'feature/agronomic/list-iot-devices' into develop. Related to TS012. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f00d08a | feat(agronomic): add iotdevicerepository and plotrepository interface.# Conflicts: |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1bbea60 | feat(agronomic): add value objects for iot device, plot, and user identifiers. | # Conflicts: #	src/main/java/com/arcadiadevs/viora/platform/agronomic/domain/model/valueobjects/PlotId.java #	src/main/java/com/arcadiadevs/viora/platform/agronomic/domain/model/valueobjects/UserId.java | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8bfe3f8 | feat(agronomic): add iotdevice aggregate root with validation rules. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1f91601 | feat(agronomic): add spring data jpa repositories for iotdevice and plot entities. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | aa39af8 | feat(agronomic): add jpa entities for iotdevice and plot persistence. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a899f75 | feat(agronomic): add query for retrieving iot devices by plot id with ownership validation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 61fbdd9 | feat(agronomic): implement iotdevice1ueryservice for retrieving devices by plot id with ownership validation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | aba2ad9 | feat(agronomic): add iotdeviceResource for rest response of iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 728fc39 | feat(agronomic): add jpa adapters for iotdevice and plot repositories. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a2c1398 | feat(agronomic): add iotdevicescontroller for managing iot devices by plot. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 48b1157 | feat(agronomic): add assembler for converting iotDevice to iotdeviceresource dto. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | cc20e9f | feat(agronomic): configure application properties for development and production environments. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | be6d5ca | feat(agronomic): add assemblers for converting between iotdevice and iotdeviceentity. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 44d57c4 | feat(agronomic): add iotdevicenotfoundexception for handling missing iot devices. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a7b9788 | refactor(agronomic): simplify iotdevice constructor and remove default constructor. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a6ce149 | feat(agronomic): enhance iotdevice1ueryservice to validate plot ownership using plotid and userid. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 542fbba | feat(agronomic): update iotdevicescontroller to enhance response handling and improve api documentation. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 523807b | feat(agronomic): refactor jpaiotdevicerepositoryadapter to use assemblers for entity conversion. |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5edcd4f | Merge branch 'release/0.3.0' into main |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bc5b06d | Merge branch 'main' into feature/agronomic/create-iot-device |  | 09/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1c9cd24 | feat(agronomic): implement iot device registration with ownership validation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 240101a | feat(agronomic): simplify createiotdeviceCommand by removing authenticateduserId parameter. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | e799a31 | feat(agronomic): remove userid from createiotdevicecommand assembly. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3752da8 | feat(agronomic): remove userid parameter from createiotdeviceresource. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 95dc7a6 | feat(agronomic): update iot device registration to remove user ownership check. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 7bea2c5 | Merge branch 'feature/agronomic/create-iot-device' into develop. Related to TS013. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 016458e | feat(agronomic): add createiotdevicecommand for registering new iot devices. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1e24c97 | feat(agronomic): add iotdevicecommandservice for handling iot device creation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 36c2a79 | feat(agronomic): add resource and assembler for creating iot devices. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 80e3636 | feat(agronomic): implement iotdevicecommandservice and enhance result class. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3652406 | feat(agronomic): implement iot device registration with ownership validation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bb0789f | feat(agronomic): simplify createiotdeviceCommand by removing authenticateduserId parameter. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d502ff9 | feat(agronomic): remove userid from createiotdevicecommand assembly. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b2af714 | feat(agronomic): remove userid parameter from createiotdeviceresource. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c3e3e9d | feat(agronomic): update iot device registration to remove user ownership check. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 4efbc0b | Merge branch 'release/0.4.0' into main |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5f7c088 | chore: update gitignore. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5044b3c | feat(agronomic): add IoT device update command infrastructure. | # Conflicts: #	src/main/java/com/arcadiadevs/viora/platform/agronomic/application/commandservices/IoTDeviceCommandService.java | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f68a14c | feat(agronomic): add patch endpoint for iot device update. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 15f68f5 | fix(shared): add plot_ownership_violation error mapping. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 858d323 | feat(agronomic): introduce value objects for agronomic metrics including accumulatedchillHours, chillportions, ndvivalue, timerange, daterange,measuremntdate. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c1a6939 | refactor(agronomic): refactor agronomicstatistic to use accumulatedchillhours and improve validation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 85b501d | feat(agronomic): add assemblers for converting between agronomicstatistic and agronomicstatisticentity. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 395f752 | feat(agronomic): enhance agronomicstatisticqueryservice with plot validation and introduce jpaagronomicstatisticrepositoryadapter. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b834596 | feat(agronomic): add agronomicstatisticentity for jpa persistence with relevant fields and indexes. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d50c28d | refactor(agronomic): align iot device update with ddd guide. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 96fb85d | feat(agronomic): update springdataagronomicstatisticrepository to use agronomicstatisticentity for jpa queries. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1a84257 | feat(agronomic): add agronomicstatisticresource for exposing agronomic metrics to the frontend. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 922ea36 | feat(agronomic): add assembler for converting agronomicstatistic aggregate to agronomicstatisticresource |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f082fc9 | feat(agronomic): add agronomicstatisticscontroller for retrieving agronomic statistics. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0f6f38f | feat(agronomic): refine getagronomicstatisticsquery for improved validation and clarity. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 07b9831 | feat(agronomic): add invalidagronomicmetricexception for handling metric validation errors. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 40486eb | refactor(agronomic): align iot device update with ddd guide and develop patterns |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9c77724 | Merge branch 'feature/agronomic/update-iot-device' into develop. | Related to TS014 | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 806263f | Merge branch 'release/0.5.0' |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9672521 | feat(agronomic): add IoT device update command infrastructure. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 948d943 | feat(agronomic): add deleteiotdevicecommand record. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8741989 | feat(agronomic): add delete endpoint for iot device. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0184cf6 | feat(agronomic): add iot device delete endpoint. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0d2856d | Merge branch 'feature/agronomic/delete-iot-device' into develop. | Related to TS015. | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6c28785 | Merge branch 'release/0.6.0' |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 7599c8b | chore(agronomic): implement agronomic statistics domain model and persistence layer. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 31c641e | Merge branch 'release/0.7.0' |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d05f21b | feat(agronomic): add resource for plot creation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 403469c | feat(agronomic): add assembler for plot creation command. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c85abff | test(agronomic): add integration and unit tests for plot management features. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | e2fac87 | chore(shared): ignore local environment configuration files. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2e7116c | fix(agronomic): enforce active plots in IoT device commands. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0a150f9 | feat(agronomic): implement plot creation command handling. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2cea5c8 | fix(agronomic): validate plot availability and ownership in IoT device queries. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5113c15 | feat(agronomic): add query handling for plots by user. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5f98313 | fix(agronomic): validate plot identifier when creating IoT devices. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 965e0d4 | fix(agronomic): validate identifiers when updating IoT devices. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b295270 | fix(agronomic): validate and normalize IoT device status values. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2251a1a | refactor(agronomic): remove obsolete plot persistence entity. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f00975e | refactor(agronomic): remove obsolete agronomic statistic repository adapter. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 7ac7005 | docs(agronomic): update IoT device endpoint documentation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5cbfccf | feat(agronomic): add plot creation and retrieval endpoints. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a6bbc4e | feat(shared): add forbidden application error factory. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3a569fd | fix(shared): conditionally load OpenAPI configuration. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 659d89c | fix(shared): map forbidden application errors to http status. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6e458d2 | feat(shared): enable test profile for application context tests. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9dccaf9 | feat(shared): replace duplicated result implementation with unit tests. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a342ddf | Merge branch 'feature/agronomic/create-plot' into develop. | Related to TS008. | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1c7cf9e | Merge branch 'release/0.8.0' |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | a0b69ef | feat(agronomic): add tests for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1ae7042 | feat(agronomic): add tests for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | f3785c3 | chore(shared): document postgre sql and agro-monitoring environment variables. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 3fd600a | fix(agronomic): parse plot coordinates in geo json order. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | db276db | feat(agronomic): enrich plot queries with current satellite imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c493bcf | feat(agronomic): expose current imagery in the plot listing endpoint. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 4b655db | docs(agronomic): document geo json coordinate order for plot creation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 6834cc7 | fix(agronomic): serialize plot coordinates in geo json order. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 89fd1fd | docs(agronomic): document geo json coordinate order for plot updates. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 42bd7a7 | feat(agronomic): configure agro monitoring satellite imagery integration. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 543b94a | feat(agronomic): add outbound service for satellite imagery retrieval. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 007d8d6 | feat(agronomic): add read model for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c5529e0 | feat(agronomic): add outbound service for satellite imagery retrieval. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 8180304 | feat(agronomic): add query for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 5f35d6d | feat(agronomic): add satellite imagery value object. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 321cdc8 | feat(agronomic): configure the AgroMonitoring rest client. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c455020 | feat(agronomic): add persistence entity for agro monitoring plot integrations. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 98c8a10 | feat(agronomic): add typed properties for agro monitoring | integration. | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bbc2002 | feat(agronomic): add repository for agro monitoring plot integrations. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 0013462 | feat(agronomic): add rest resource for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | bb7e9fc | feat(agronomic): add assembler for plots with current imagery. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 43b0668 | feat(agronomic): add resource for satellite imagery representation. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c187b8f | Merge branch 'feature/agronomic/list-plots-with-imagery' into develop. | Related to TS009. | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 1f77a3e | Merge branch 'release/0.9.0' |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 2071170 | feat(agronomic): add monitoringsummaryid value object. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 487dfd7 | feat(agronomic): add general health status value object. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d62199c | feat(agronomic): add yield forecast value object. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c939d5f | feat(agronomic): add monitoring summary aggregate root. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 4ca5fee | feat(agronomic): add invalid weather snapshot exception in domain exceptions. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 28b6bca | feat(agronomic): add weather status in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 9974c06 | feat(agronomic): add climate risk level in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | ed2d7b7 | feat(agronomic): add weather snapshot in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 79dd816 | feat(agronomic): add mitigation action type in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 7e08f3f | feat(agronomic): add nutrition input recommendation in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 08b4d9d | feat(agronomic): add mitigation recommendation in value objects. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 344b1fd | feat(agronomic): add climate risk evaluators service. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 08ae677 | feat(agronomic): add monitoring summary entity. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 91aaa8c | feat(agronomic): add get current monitoring summary query. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | d1b94ab | feat(agronomic): add mitigation recommendation generator service. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | 54189bd | feat(agronomic): add monitoring summary entity assembler. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | b2059c1 | feat(agronomic): add monitoring summary from monitoring summary entity assembler. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | c7c9130 | feat(agronomic): add weather data service. |  | 10/06/2026 |
| upc-pre-1asi0729-11848-arcadiadevs/viora-platform | main | acb0484 | feat(agronomic): add spring data monitoring summary repository. |  | 10/06/2026 |



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