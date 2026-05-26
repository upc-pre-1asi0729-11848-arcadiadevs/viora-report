### Sprint 3

#### Sprint Planning 3

&nbsp;

En esta sección se consolidan los acuerdos fundamentales alcanzados por el equipo ArcadiaDevs durante la sesión de planificación del Sprint 3, realizada de manera virtual a través de la plataforma Discord. Tras el despliegue exitoso de la primera versión de la aplicación web, considerando funcionalidades que son importantes para el usuario del segmento objetivo de productores y la mejora de la presencia digital de Viora, el propósito central de esta reunión fue evolucionar hacia la segunda versión de la Aplicación Web y la construcción de la primera versión operativa del Servicio Web de Viora. Para ello, el equipo priorizó el desarrollo de los subdominios core y support vinculados al monitoreo inteligente de parcelas, la gestión fitosanitaria, la coordinación entre productores y especialistas, y la automatización de procesos de trazabilidad y validación. Asimismo, se consideró la corrección y refinamiento de funcionalidades implementadas en el Sprint 2, alineando el esfuerzo de ingeniería con la necesidad de reducir los principales pain points identificados en ambos segmentos de usuarios.

Para esta iteración, el equipo ha definido un compromiso de trabajo de 76 puntos de esfuerzo sobre una velocidad proyectada de 120 puntos. Dentro de esta estimación, se ha asignado 1 punto a actividades de corrección y mejora incremental relacionadas con la Landing Page y la Web Application previamente desplegadas, mientras que los 72 puntos restantes corresponden al desarrollo de nuevas capacidades funcionales y servicios backend asociados al ecosistema Viora. Esta planificación busca no solo incrementar el valor funcional de la plataforma mediante capacidades de analítica predictiva, monitoreo climático y sensoramiento remoto satelital, sino también establecer las bases del Servicio Web encargado de orquestar la sincronización de datos externos, gestión de alertas, matchmaking técnico y trazabilidad de intervenciones. Además, se incorporan activamente las lecciones aprendidas durante la retrospectiva anterior, ampliando el margen temporal de coordinación y validación técnica para garantizar un Sprint Planning más sólido, realista y alineado con los objetivos estratégicos del producto.

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
| **Sprint 3 Velocity** | 76 |
| **Sum of Story Points** | 120 |

#### Aspect Leaders and Collaborators

&nbsp;

En esta sección se presenta la matriz Leadership-and-Collaboration Matrix (LACX) correspondiente al Sprint 3, diseñada para fortalecer la coordinación estratégica y la especialización técnica dentro del ecosistema Viora durante el desarrollo de la segunda versión de la aplicación web y la primera versión operativa del Servicio Web. Para este incremento, el alcance se ha reorganizado en torno a bounded contexts alineados con los principales procesos del negocio y los pain points identificados en los segmentos de productores olivareros y especialistas fitosanitarios. En consecuencia, el equipo ha distribuido las responsabilidades entre los contextos Shared, Agronomic, Surveillance, Intervention, Community y PAM (Profile & Asset Management), además de considerar la evolución y refinamiento de la Landing Page.

| Team Member (Last Name, First Name) | GitHub Username | Shared Context Leader (L) / Collab (C) | Agronomic Context Leader (L) / Collab (C) | Surveillance Context Leader (L) / Collab (C) | Intervention Context Leader (L) / Collab (C) | Community Context Leader (L) / Collab (C) | PAM Context Leader (L) / Collab (C) | Landing Page Leader (L) / Collab (C) |
|---|---|---|---|---|---|---|---|---|
| Carpio, Josue   | josf17                           | C | C | C | C | C | L | C |
| Espada, Piero   | espadita2510 / pieroedeveloper25 | C | C | L | C | C | C | C |
| Li, Diana       | peruvianMiau                     | C | C | C | L | C | C | C |
| Paredes, Victor | DaronCameloft                    | C | C | C | C | C | C | L |
| Santi, Fabrizio | Santi2007939                     | C | L | C | C | C | C | C |
| Trinidad, Jahat | trinity-bytes                    | L | C | C | C | L | C | C |

#### Sprint Backlog 3

&nbsp;

El objetivo principal de este Sprint 3 es desarrollar la segunda versión de la aplicación web y la primera versión operativa del Servicio Web de Viora, mediante la incorporación de capacidades de autenticación segura, monitoreo fitosanitario inteligente, sincronización climática y satelital, gestión de alertas epidemiológicas y coordinación de intervenciones técnicas entre productores olivareros y especialistas fitosanitarios. Asimismo, el sprint contempla la consolidación de procesos de trazabilidad agronómica, reputación comunitaria y administración de perfiles y activos agrícolas, junto con el refinamiento incremental de la Landing Page y funcionalidades implementadas en iteraciones anteriores.

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

% US56
US56 & Exploración de beneficios para el Productor & TK01 & Presentación de todos los beneficios del segmento de productores & Implementación de cards con todos los beneficios ofrecidos para el segmento de productores & 1.0 & Paredes, Victor & To-do \\ \hline

% US57
US57 & Exploración de beneficios para el Especialista & TK02 & Presentación de todos los beneficios del segmento de especialistas & Implementación de cards con todos los beneficios ofrecidos para el segmento de especialistas fitosanitarios & 1.0 & Paredes, Victor & To-do \\ \hline

% US60
US60 & Exploración del equipo detrás de la plataforma & TK03 & Video e imágenes del equipo & Implementación de placeholder para imágenes del equipo trabajo y el video About the team & 1.0 & Paredes, Victor & To-do \\ \hline

% US08
US08 & Monitoreo de telemetría IoT para decisiones hídricas & TK04 & Datos inválidos mostrados & Corregir que aparezcan elementos no existenten en la lista de dispositivos IoT & 1.0 & Santi, Fabrizio & To-do \\ \hline

% US15
US15 & Alerta por frío insuficiente & TK05 & Componente de alerta de frío & Implementación de tipo de alerta fenológica de frío y filtro & 0.5 & Espada, Piero & To-do \\ \hline

% US19
US19 & Reporte de sintomatología y evaluación automática & TK06 & Creación manual de alerta & Implementación de formulario con selector de Parcela y multiselección de síntomas vistos & 1.0 & Espada, Piero & To-do \\ \cline{3-8}
& & TK07 & Visualización de alertas por parcela & Implementación de filtro de alerta de acuerdo según parcela & 1.0 & Espada, Piero & To-do \\ \cline{3-8}
& & TK08 & Mensaje de confirmación & Implementación de pop-up de alerta validada o archivada & 1.0 & Espada, Piero & To-do \\ \hline

% US20
US20 & Difusión de alerta preventiva comunitaria & TK09 & Componente de alerta comunitaria & Implementación de tipo de alerta comunitaria y filtro & 1.0 & Espada, Piero & To-do \\ \hline

% US21
US21 & Prospección zonal de intervenciones técnicas & TK10 & Listado de parcelas con alertas & Implementación de lista de parcelas con cantidad de alertas presentadas y peligro & 2.0 & Espada, Piero & To-do \\ \hline

% US22
US22 & Priorización de prospección por severidad estimada & TK11 & Mapbox SDK con marcadores de alertas & Configuración de marcadores de alertas en Mapbox SDK relacionado a alertas. & 2.0 & Espada, Piero & To-do \\ \cline{3-8}
& & TK12 & Filtro de plaga y severidad & Implementación de filtro de plagas y severidad mostrados en el mapa. & 1.0 & Espada, Piero & To-do \\ \hline

% US24
US24 & Identificación de especialistas zonales & TK13 & Lista de especialistas disponibles & Implementación de lista de técnicos con datos de disponibilidad. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK14 & Indisposición de especialistas & Implementación de componente de especialistas no disponibles & 0.5 & Li, Diana & To-do \\ \hline

% US25
US25 & Solicitud formal de intervención & TK15 & Solicitud de invervención & Implementación de creación de solicitud con estado en espera. & 1.0 & Li, Diana & To-do \\ \hline

% US26
US26 & Evaluación de disponibilidad operativa & TK16 & Lista de solicitudes en espera & Implementación de lista de solicitudes sin respuesta. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK17 & Información de solicitud & Implementación de popup con datos de la unidad productiva y alerta. & 1.5 & Li, Diana & To-do \\ \hline

% US27
US27 & Resolución de la solicitud de intervención & TK18 & Aceptación de solicitud & Implementación de aceptación del especialista y visualización del productor. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK19 & Lista de solicitudes rechazadas & Implementación de lista de solicitudes rechazadas. & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK20 & Lista de solicitudes en proceso & Implementación de lista de solicitudes recientemente aceptadas preeliminarmente. & 0.5 & Li, Diana & To-do \\ \hline

% US28
US28 & Evaluación preliminar de la unidad productiva & TK21 & Información consolidada de la parcela & Implementación de resumen de últimos datos de trazabilidad de la parcela y últimas alertas recibidas & 2.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK22 & Visualización del mapa de la parcela & Configurar Mapbox SDK para mostrar la parcela. & 1.0 & Li, Diana & To-do \\ \hline

% US29
US29 & Emisión de propuesta de servicio & TK23 & Creación de presupuesto & Implementación de formulario relacionado con la parcela asignada. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK24 & Muestra de presupuesto & Implementación de cambio de estado de solicitud en aceptada & 0.5 & Li, Diana & To-do \\ \hline

% US30
US30 & Resolución de la propuesta de servicio & TK25 & Resolución de propuesta & Implementación de visualización del formulario para solo leer con opciones de aceptar o rechazar. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK26 & Repetición del ciclo de búsqueda & Implementación de cambio de estado y retomar actividad de búsqueda de especialistas & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK27 & Lista de propuestas rechazadas & Implementación de lista de propuestas rechazadas del especialista & 1.0 & Li, Diana & To-do \\ \hline

% US31
US31 & Habilitación de canal de comunicación directo & TK28 & Botón de contacto habilitado & Implementación de popup con datos de correo y whatsapp. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK29 & Botón de contacto deshabilitado & Implementación de tooltip para comunicar que se habilirá al aceptar una propuesta. & 0.5 & Li, Diana & To-do \\ \hline

% US36
US36 & Revisión de antecedentes agronómicos en campo & TK30 & Información de trazabilidad de la parcela & Implementación de resumen de últimos datos de trazabilidad de la parcela & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK31 & Información de últimas alertas similares & Implementación de lista de alertas similares & 1.0 & Li, Diana & To-do \\ \hline

% US37
US37 & Registro de datos de inspección física & TK32 & Formulario de inspección física & Implementación de formulario para registrar observaciones biológicas y daños detectados. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK33 & Registro de evidencias de inspección & Implementación de carga de imágenes y notas técnicas relacionadas a la parcela. & 1.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK34 & Resumen de hallazgos de campo & Implementación de componente con resumen de observaciones registradas. & 0.5 & Paredes, Victor & To-do \\ \hline

% US38
US38 & Validación algorítmica de ventana de aplicación & TK35 & Validación climática de aplicación & Implementación de validación de fecha de tratamiento según pronóstico climático. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK36 & Alerta de condiciones adversas & Implementación de mensaje de advertencia por lluvias o vientos fuertes. & 0.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK37 & Recomendación de nueva ventana & Implementación de sugerencia de reprogramación de aplicación fitosanitaria. & 0.5 & Paredes, Victor & To-do \\ \hline

% US39
US39 & Emisión de prescripción de agrofármacos & TK38 & Formulario de receta técnica & Implementación de formulario para registrar agrofármacos, dosis y método de aplicación. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK39 & Resumen de prescripción emitida & Implementación de componente de visualización de receta técnica generada. & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK40 & Notificación de nueva receta & Implementación de mensaje de disponibilidad de plan de tratamiento para el productor. & 0.5 & Li, Diana & To-do \\ \hline

% US07
US07 & Delimitación de área productiva & TK41 & Configuración de Mapbox SDK & Implementación de mapa interactivo para delimitación de parcelas. & 2.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK42 & Herramienta de dibujo de polígonos & Implementación de selección de puntos y cierre de área geográfica. & 2.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK43 & Validación de polígono incompleto & Implementación de validación para impedir parcelas sin cierre correcto. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK44 & Visualización de parcela registrada & Implementación de componente de visualización de límites geográficos registrados. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK45 & Vinculación climática automática & Implementación de asociación automática entre parcela y datos climáticos zonales. & 0.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK46 & Lista de parcelas & Implementación de lista de parcelas, con selección para ver el detalle de cada una y botón para la creación de una nueva. & 1.0 & Santi, Fabrizio & To-do \\ \hline

% US16
US16 & Prescripción automatizada de nutrición dinámica & TK47 & Generación de plan nutricional & Implementación de recomendación de fertilización según riesgo fenológico. & 1.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK48 & Resumen de tratamiento compensatorio & Implementación de visualización de agrofármacos y dosis recomendadas. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK49 & Ajuste de ventana de aplicación & Implementación de actualización de recomendación según cambios climáticos. & 0.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK50 & Alerta de modificación climática & Implementación de mensaje de cambio de ventana óptima de aplicación. & 0.5 & Paredes, Victor & To-do \\ \hline

% US40
US40 & Certificación de aplicación de receta técnica & TK51 & Formulario de certificación de aplicación & Implementación de registro de fecha y dosificación aplicada en campo. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK52 & Actualización de historial de parcela & Implementación de consolidación de trazabilidad posterior a intervención. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK53 & Advertencia de aplicación fuera de ventana & Implementación de mensaje de posible reducción de eficacia climática. & 0.5 & Li, Diana & To-do \\ \hline

% US17
US17 & Certificación de aplicación del plan nutricional & TK54 & Formulario de certificación nutricional & Implementación de registro de fecha y agrofármacos aplicados en campo. & 1.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK55 & Validación de datos obligatorios & Implementación de validación de insumos químicos y fecha de intervención. & 0.5 & Santi, Fabrizio & To-do \\ \hline

% US41
US41 & Consolidación del gasto de intervención & TK56 & Formulario de registro de gastos & Implementación de ingreso de costos operativos y agrofármacos utilizados. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK57 & Actualización de métricas financieras & Implementación de recálculo de rentabilidad asociado a la parcela. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK58 & Resumen económico de intervención & Implementación de visualización consolidada de gastos registrados. & 0.5 & Li, Diana & To-do \\ \hline

% US18
US18 & Consolidación del gasto de mitigación climática & TK59 & Formulario de gasto de mitigación climática & Implementación de ingreso de costos asociados al plan nutricional. & 1.0 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK60 & Validación de declaración financiera & Implementación de bloqueo de cierre sin registro de costos. & 0.5 & Santi, Fabrizio & To-do \\ \cline{3-8}
& & TK61 & Actualización de rentabilidad productiva & Implementación de recálculo financiero posterior a la mitigación climática. & 1.0 & Santi, Fabrizio & To-do \\ \hline

% US43
US43 & Evaluación post-intervención del vigor vegetal & TK62 & Monitoreo NDVI post-intervención & Implementación de comparación de vigor vegetal antes y después del tratamiento. & 1.5 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK63 & Visualización de recuperación de parcela & Implementación de componente con estado epidemiológico actualizado. & 1.0 & Paredes, Victor & To-do \\ \cline{3-8}
& & TK64 & Detección de rebrotes & Implementación de alerta de persistencia de estrés vegetal posterior a intervención. & 1.0 & Paredes, Victor & To-do \\ \hline

% US44
US44 & Reporte de impacto fitosanitario post-intervención & TK65 & Formulario de reporte post-tratamiento & Implementación de confirmación de control o persistencia de plaga. & 1.0 & Li, Diana & To-do \\ \cline{3-8}
& & TK66 & Registro de eficacia fitosanitaria & Implementación de almacenamiento de resultado positivo o negativo del tratamiento. & 0.5 & Li, Diana & To-do \\ \cline{3-8}
& & TK67 & Resumen de impacto clínico & Implementación de visualización de estado posterior al periodo de gracia. & 0.5 & Li, Diana & To-do \\ \hline

% US42
US42 & Cierre formal del servicio y evaluación de calidad & TK68 & Formulario de cierre de servicio & Implementación de vista para confirmar la finalización de la intervención técnica. & 1.0 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK69 & Calificación de especialista & Implementación de componente de evaluación cualitativa del Asesor Técnico mediante puntuación y comentario. & 1.0 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK70 & Visualización de reputación actualizada & Implementación de actualización del puntaje y estado reputacional del especialista en el perfil público. & 1.0 & Carpio, Josue & To-do \\ \hline

% US45
US45 & Registro de disposición de recontratación & TK71 & Selector de preferencia de recontratación & Implementación de opción favorable o desfavorable sobre futuras colaboraciones. & 0.5 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK72 & Historial privado de especialistas & Implementación de sección privada con preferencias registradas para futuras búsquedas. & 0.5 & Carpio, Josue & To-do \\ \hline

% US46
US46 & Publicación de caso de éxito en portafolio & TK73 & Botón de publicación de caso exitoso & Implementación de acción para agregar intervenciones validadas al portafolio público. & 1.0 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK74 & Mensaje de restricción de publicación & Implementación de alerta para intervenciones con evaluación desfavorable. & 0.5 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK75 & Sección pública de casos de éxito & Implementación de galería de intervenciones destacadas dentro del perfil del especialista. & 1.5 & Carpio, Josue & To-do \\ \hline

% US32
US32 & Emisión de reporte por inconducta profesional & TK76 & Formulario de denuncia & Implementación de formulario para registrar infracción ética o inasistencia. & 1.0 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK77 & Validación visual de campos obligatorios & Implementación de mensajes de error para categoría y sustento incompleto. & 0.5 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK78 & Mensaje de reporte enviado & Implementación de popup de confirmación de denuncia registrada. & 0.5 & Trinidad, Jahat & To-do \\ \hline

% US33
US33 & Evaluación y penalización autónoma (strikes) & TK79 & Indicador de strikes acumulados & Implementación de visualización de cantidad de penalizaciones del usuario. & 1.0 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK80 & Estado disciplinario del perfil & Implementación de badge de estado del usuario dentro del marketplace. & 0.5 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK81 & Alerta de límite de penalizaciones & Implementación de mensaje preventivo por acumulación de strikes. & 0.5 & Trinidad, Jahat & To-do \\ \hline

% US34
US34 & Inhabilitación temporal preventiva & TK82 & Pantalla de suspensión temporal & Implementación de vista de acceso restringido por sanción preventiva. & 1.0 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK83 & Mensaje de suspensión preventiva & Implementación de notificación con motivo y duración de sanción. & 0.5 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK84 & Deshabilitación de acciones del marketplace & Implementación de bloqueo visual de botones y funcionalidades restringidas. & 0.5 & Trinidad, Jahat & To-do \\ \hline

% US35
US35 & Expulsión definitiva del marketplace & TK85 & Pantalla de expulsión definitiva & Implementación de vista de bloqueo permanente de acceso. & 1.0 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK86 & Ocultamiento de perfil sancionado & Implementación de invisibilización de perfil dentro de búsquedas y marketplace. & 0.5 & Trinidad, Jahat & To-do \\ \cline{3-8}
& & TK87 & Mensaje de revocación permanente & Implementación de notificación de expulsión definitiva del ecosistema. & 0.5 & Trinidad, Jahat & To-do \\ \hline

% US10
US10 & Gestión de estado de disponibilidad & TK88 & Selector de disponibilidad operativa & Implementación de interruptor visual para activar o pausar recepción de solicitudes. & 0.5 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK89 & Estado visible de disponibilidad & Implementación de badge de estado operativo mostrado en el perfil profesional. & 0.5 & Carpio, Josue & To-do \\ \hline

% US09
US09 & Establecimiento de perfil profesional & TK90 & Formulario de perfil profesional & Implementación de vista para registrar experiencia, especialidades y datos de contacto. & 1.0 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK91 & Ubicación geográfica del especialista & Implementación de selección y visualización de zona operativa mediante mapa interactivo. & 1.5 & Carpio, Josue & To-do \\ \cline{3-8}
& & TK92 & Visualización pública del portafolio & Implementación de perfil público mostrado en terna de especialistas. & 0.5 & Carpio, Josue & To-do \\ \hline

\end{longtable}

#### Deployment Evidence for Sprint Review

&nbsp;

#### Execution Evidence for Sprint Review

&nbsp;

#### Services Documentation Evidence for Sprint Review

&nbsp;

#### Software Deployment Evidence for Sprint Review

&nbsp;

#### Team Collaboration Insights for Sprint Review

&nbsp;

\newpage