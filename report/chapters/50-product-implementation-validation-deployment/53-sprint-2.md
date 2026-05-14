### Sprint 2

#### Sprint Planning 2

&nbsp;

En esta sección se consolidan los acuerdos fundamentales alcanzados por el equipo ArcadiaDevs durante la sesión de planificación del Sprint 2, realizada de manera virtual a través de la plataforma Discord. Tras el despliegue exitoso de la presencia digital de Viora, el propósito central de esta reunión fue pivotar hacia el desarrollo del núcleo técnico de la plataforma, alineando el esfuerzo de ingeniería con la necesidad de reducir la incertidumbre operativa en el sector olivarero.

Para esta iteración, el equipo ha definido un compromiso de trabajo de 32 puntos de esfuerzo sobre una velocidad proyectada de 32 puntos. En esta estimación de puntos se considerará a todas las historias de usuario del Landing Page para realizar las modificaciones necesarias y respectiva refactorización. El contenido será el mismo, solo que la arquitectura cambiará. Esta planificación no solo busca la entrega de valor funcional mediante analítica predictiva y sensoramiento remoto, sino que también integra activamente las lecciones aprendidas en la retrospectiva anterior, estableciendo un flujo de trabajo más holgado que garantice la solvencia técnica frente a los plazos de entrega.

A continuación, se presenta el cuadro resumen del Sprint Planning Meeting, el cual detalla la logística de la sesión, la revisión de los resultados del sprint previo y el Sprint Goal diseñado para transformar datos climáticos y satelitales en decisiones agronómicas de alto impacto.

| **Sprint #** | Sprint 2 |
| :--- | :--------------- |
| **Date** | 2026-04-29 |
| **Time** | 10:40 PM |
| **Location** | Discord (Virtual) |
| **Prepared By** | Trinidad Leon, Jahat Jassiel |
| **Attendees (to planning meeting)** | Carpio Peña, Josue Francisco / Espada Lazo, Piero Anthony / Li Gayoso, Diana Carolina / Paredes Maza, Juan de Dios / Santi Guerrero Fabrizio Alonso / Trinidad Leon, Jahat Jassiel |
| **Sprint n – 1 Review Summary** | Durante el Sprint 1, se cumplió satisfactoriamente con el 100% de los objetivos mediante la implementación de la Landing Page oficial de Viora, logrando entregar 18 story points distribuidos en 8 historias de usuario que abarcan desde la segmentación dinámica para productores y especialistas hasta la integración de modelos de suscripción y testimonios. El incremento fue desplegado con éxito en Vercel bajo una arquitectura responsiva, respaldada por un flujo de trabajo colaborativo de 43 commits. Por su parte, el Product Owner validó que el producto cumple con el Sprint Goal al comunicar eficazmente la propuesta de valor para los segmentos de usuario, aprobando la entrega sin observaciones técnicas pendientes y confirmando una base sólida para el desarrollo de futuros servicios. A pesar de ello, se tendrá que realizar correciones para la arquitectura de la Landing Page y la integración de redirecciones correctas en los CTAs del Landing Page. |
| **Sprint n – 1 Retrospective Summary** | Durante el Sprint 1, el equipo identificó como principal oportunidad de mejora la gestión del cronograma, señalando que el margen de tiempo para el cierre de actividades frente a la fecha límite fue excesivamente estrecho; por ello, se acordó para las próximas iteraciones establecer una planificación de tiempos más holgada que permita completar los entregables con mayor solvencia y sin comprometer el ritmo de trabajo del equipo. |
| **Sprint 2 Goal** | Nuestro enfoque está en proporcionar un núcleo unificado de monitoreo diagnóstico y capacidad predictiva que integre la muestra de datos generales de interés para los productores, datos climáticos y sensoramiento remoto satelital; creemos que entrega una reducción crítica de la incertidumbre operativa y una mayor capacidad de respuesta técnica para los productores olivareros, permitiéndoles anticipar factores que merman la cosecha, como la vecería (alternancia productiva) y el estrés biológico; esto se confirmará cuando los productores puedan visualizar un estado de salud consolidado de sus parcelas, reciban alertas epidemiológicas o relacionadas al vigor vegetal (NDVI) y logren proyectar el rendimiento de su campaña mediante el seguimiento de acumulación de frío y trazabilidad de manejo, todo sin necesidad de intervención manual constante. |
| **Sprint 2 Velocity** | 32 |
| **Sum of Story Points** | 32 |

#### Aspect Leaders and Collaborators

&nbsp;

En esta sección se presenta la matriz Leadership-and-Collaboration Matrix (LACX) del Sprint 2, diseñada para optimizar la coordinación interna y asegurar la integridad técnica de la plataforma Viora. Para este segundo incremento, el alcance se ha segmentado en los tres ejes fundamentales definidos por los contextos delimitados: Shared, Agronomic y Surveillance. Además, se considerará a la refactorización como un aspecto clave.


| Team Member (Last Name, First Name) | GitHub Username | Shared Context Leader (L) / Collab (C) | Agronomic Context Leader (L) / Collab (C) | Surveillance Context Leader (L) / Collab (C) | Landing Page refactor Leader (L) / Collab (C) |
|---|---|---|---|---|---|
| Carpio, Josue | josf17 | C | C | C | C |
| Espada, Piero | espadita2510 | C | C | L | C |
| Li, Diana | peruvianMiau | C | C | C | C |
| Paredes, Victor | DaronCameloft | C | L | C | C |
| Santi, Fabrizio | Santi2007939 | C | C | C | L |
| Trinidad, Jahat | trinity-bytes | L | C | C | C |

#### Sprint Backlog 2

&nbsp;

El objetivo principal de este Sprint 2 es desarrollar el, mediante la integración de datos de telemetría IoT, análisis geoespacial de parcelas y visualización de indicadores agronómicos críticos, diseñado para centralizar la toma de decisiones y optimizar la gestión de riesgos biológicos e hídricos para el productor. También, se refactorizará la arquitectura del Landing Page.

\begin{longtable}{|p{0.05\textwidth}|p{0.14\textwidth}|p{0.05\textwidth}|p{0.14\textwidth}|p{0.24\textwidth}|p{0.08\textwidth}|p{0.12\textwidth}|p{0.07\textwidth}|} 
\hline 
\multicolumn{2}{|l|}{\textbf{Sprint \#}} & \multicolumn{6}{l|}{Sprint 2} \\ \hline 
\multicolumn{2}{|l|}{\textbf{User Story}} & \multicolumn{6}{l|}{\textbf{Work-Item / Task}} \\ \hline 
\textbf{Id} & \textbf{Title} & \textbf{Id} & \textbf{Title} & \textbf{Description} & \textbf{Estimation (Hours)} & \textbf{Assigned To} & \textbf{Status} \\ \hline 
\endfirsthead

\hline 
\multicolumn{2}{|l|}{\textbf{User Story}} & \multicolumn{6}{l|}{\textbf{Work-Item / Task (Continuación)}} \\ \hline 
\textbf{Id} & \textbf{Title} & \textbf{Id} & \textbf{Title} & \textbf{Description} & \textbf{Estimation} & \textbf{Assigned To} & \textbf{Status} \\ \hline 
\endhead

% REFACTORIZACIÓN (EX SPRINT 1)
US54 & Presentación de la propuesta de valor central & TK01 & Refactor Header Nav & Migración del encabezado principal de arquitectura DDD a una estructura estática y simplificada. & 0.75 & Santi, Fabrizio & Done \\ \cline{3-8} 
& & TK02 & Refactor Hero Layout & Eliminación de dependencias de dominio en el Hero Layout para renderizado estático directo. & 0.5 & Santi, Fabrizio & Done \\ \cline{3-8} 
& & TK03 & Refactor Ambient Sound & Adaptación de la lógica del sonido ambiental y Toggle UI para operar sin controladores complejos. & 0.5 & Santi, Fabrizio & Done \\ \hline

US55 & Redirección hacia el ecosistema transaccional & TK04 & Refactor Problem UI & Conversión de las tarjetas de contexto. & 0.5 & Li, Diana & Done \\ \cline{3-8} 
& & TK05 & Webapp Redirect & Desarrollo de redireccionamiento hacia el entorno de la Webapp. & 0.25 & Santi, Fabrizio & Done \\ \hline

US56 & Exploración de beneficios para el Productor & TK06 & Refactor Grower Insights & Traslado de la sección de beneficios (NDVI y preventivos) & 0.25 & Trinidad, Jahat & Done \\ \hline

US57 & Exploración de beneficios para el Especialista & TK07 & Refactor Specialist & Desacoplamiento del apartado de beneficios técnicos. & 0.5 & Paredes, Victor & Done \\ \hline

US58 & Presentación del programa de referidos & TK08 & Refactor Pricing Panel & Simplificación de los paneles de precios para carga estática eliminando repositorios DDD. & 0.75 & Carpio, Josue & Done \\ \cline{3-8} 
& & TK09 & Refactor Referrals & Migración de la sección de referidos a una vista estática. & 0.5 & Li, Diana & Done \\ \hline

US59 & Validación de impacto mediante resultados & TK10 & Refactor Performance & Reescritura de los scripts base de métricas para un entorno puramente estático. & 0.75 & Espada, Piero & Done \\ \hline

US60 & Exploración del respaldo corporativo y humano & TK11 & Refactor Mission \& Vision & Migración del panel "Learning from best" e información del equipo a marcado estático. & 1.0 & Santi, Fabrizio & Done \\ \hline

US61 & Políticas y contacto & TK12 & Refactor Contact \& i18n & Adaptación del sistema de contacto y pie de página eliminando servicios de dominio complejos. & 1.0 & Santi, Fabrizio & Done \\ \hline

US11 & Análisis de Tendencia de Vigor Vegetal & TK13 & Chart.js Integration & Implementación de gráficos comparativos consumiendo datos simulados desde la Fake-API. & 2.5 & Santi, Fabrizio & Done \\ \cline{3-8}
& & TK14 & Trend Analytics Logic & Programación de filtros temporales. & 1.5 & Santi, Fabrizio & Done \\ \hline

US12 & Visualización Satelital de Parcelas & TK15 & Mapbox SDK Setup & Configuración del visor de mapas y renderizado de polígonos mediante el SDK de Mapbox. & 3.0 & Santi, Fabrizio & Done \\ \cline{3-8}
& & TK16 & Fake-API Data Mapping & Vinculación de coordenadas geográficas desde la MockApi para su representación en el mapa. & 1.0 & Santi, Fabrizio & Done \\ \hline

US08 & Gestión de Dispositivos IoT & TK17 & IoT Telemetry View & Maquetación de la tabla de dispositivos y visualización de métricas en Vue. & 1.5 & Carpio, Josue & Done \\ \cline{3-8}
& & TK18 & MockApi CRUD Service & Implementación de servicios de persistencia (creación, edición, eliminación) conectados al MockApi. & 1.5 & Li, Diana & Done \\ \cline{3-8}
& & TK19 & Device Forms & Desarrollo de formularios reactivos para el registro de dispositivos con validaciones. & 1.0 & Li, Diana & Done \\ \hline

US13 & Resumen General y Proyección de Cosecha & TK20 & KPI Cards Layout & Diseño y maquetación de las 4 tarjetas de resumen de medidas agregadas. & 1.5 & Paredes, Victor & Done \\ \cline{3-8}
& & TK21 & Fake-API KPI & Formateo de datos desde MockApi para el despliegue de promedios generales. & 0.5 & Santi, Fabrizio & Done \\ \hline

US14 & Resumen Meteorológico y Evaluación de Riesgo & TK22 & Weather Widget & Implementación del componente de resumen climático y pronósticos. & 1.0 & Espada, Piero & Done \\ \cline{3-8}
& & TK23 & MockApi Weather Service & Conexión con el endpoint de weather-summaries en la Fake-API. & 1.0 & Espada, Piero & Done \\ \hline

US23 & Consulta de Alertas Recientes & TK24 & Alerts Mock Mapping & Mapeo de las alertas más recientes obtenidas desde el endpoint de alerts de la Fake-API. & 1.0 & Trinidad, Jahat & Done \\ \cline{3-8}
& & TK25 & Severity Status Logic & Programación de la lógica de colores y etiquetas basadas en el nivel de severidad. & 1.0 & Trinidad, Jahat & Done \\ \hline

\end{longtable}

\end{longtable}