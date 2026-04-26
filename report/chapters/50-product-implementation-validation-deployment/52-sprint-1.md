## Landing Page, Services & Applications Implementation

### Sprint 1

#### Sprint Planning 1

En esta sección se detallan los acuerdos fundamentales alcanzados por el equipo Turistas durante la sesión de planificación del Sprint 1, llevada a cabo de manera virtual mediante la plataforma Discord. El propósito central de esta reunión fue alinear los esfuerzos técnicos con la estrategia de captación de la marca Viora, definiendo un compromiso de trabajo basado en una velocidad de 20 puntos para abordar un conjunto de historias de usuario que suman 18 puntos de esfuerzo.

A continuación, se presenta el cuadro resumen del Sprint Planning Meeting, el cual integra la logística de la sesión, los responsables de la documentación y el Sprint Goal diseñado para garantizar que este primer incremento de software entregue valor real a los productores y especialistas del sector olivarero.

\begin{tabular}{p{0.30\textwidth} p{0.65\textwidth}}
\hline
\textbf{Sprint \#} & Sprint 1 \\ \hline
\multicolumn{2}{l}{\textbf{Sprint Planning Background}} \\ \hline
\textbf{Date} & 2026-04-24 \\
\textbf{Time} & 07:10 PM \\
\textbf{Location} & Discord (Virtual) \\
\textbf{Prepared By} & Trinidad Leon, Jahat Jassiel \\
\textbf{Attendees} & Espada Lazo, Piero Anthony / Li Gayoso, Diana Carolina / Paredes Maza, Juan de Dios / Santi Guerrero Fabrizio Alonso / Trinidad Leon, Jahat Jassiel \\ \hline
\multicolumn{2}{l}{\textbf{Sprint Goal \& User Stories}} \\ \hline
\textbf{Sprint 1 Goal} & Nuestro enfoque está en proporcionar una experiencia informativa y persuasiva mediante la Landing Page oficial, destacando la conexión entre datos climáticos y acción en campo; creemos que entrega claridad inmediata sobre la propuesta de valor, confianza institucional y una ruta directa de conversión hacia el periodo de prueba a los visitantes productores y especialistas fitosanitarios; esto se confirmará cuando los usuarios puedan navegar los beneficios segmentados, validar la eficacia mediante testimonios y completar la transición hacia el flujo de registro o contacto comercial sin fricciones. \\
\textbf{Sprint 1 Velocity} & 20 \\
\textbf{Sum of Story Points} & 18 \\ \hline
\end{tabular}

#### Aspect Leaders and Collaborators 

En esta sección se presenta la matriz Leadership-and-Collaboration Matrix (LACX) del Sprint 1, diseñada para optimizar la coordinación interna y asegurar la calidad técnica de la plataforma Viora. Para este primer incremento, el alcance de desarrollo se ha segmentado en cinco ejes: la estructuración de la interfaz y navegación base, la comunicación de la propuesta de valor segmentada, el desarrollo lógico del modelo de acceso, la consolidación de la credibilidad corporativa, y la implementación técnica de la conversión y contacto.

\begin{tabular}{|p{0.16\textwidth}|p{0.12\textwidth}|p{0.12\textwidth}|p{0.12\textwidth}|p{0.12\textwidth}|p{0.12\textwidth}|p{0.12\textwidth}|}
\hline
\textbf{Team Member (Last Name, First Name)} & \textbf{GitHub Username} & \textbf{Core UI Leader (L) / Collab (C)} & \textbf{Value \& Seg Leader (L) / Collab (C)} & \textbf{Access Model Leader (L) / Collab (C)} & \textbf{Corp Trust Leader (L) / Collab (C)} & \textbf{Conversion Leader (L) / Collab (C)} \\ \hline
Espada, Piero & espadita2510 & C & C & C & C & L \\ \hline
Li, Diana & peruvianMiau & L & C & C & C & C \\ \hline
Paredes, Victor & DaronCameloft & C & C & C & L & C \\ \hline
Santi, Fabrizio & Santi2007939 & C & L & C & C & C \\ \hline
Trinidad, Jahat & trinity-bytes & C & C & L & C & C \\ \hline
\end{tabular}

#### Sprint Backlog 1

El objetivo principal de este Sprint es establecer la presencia digital estratégica de Viora mediante la construcción de una Landing Page funcional y persuasiva, diseñada para comunicar la propuesta de valor y facilitar la conversión directa de productores y especialistas hacia el ecosistema transaccional.

\begin{figure}[H]
\caption{Vista General del Sprint Backlog 1}
\centering
\includegraphics[width=0.8\textwidth]{report/assets/sprint-backlog/sb1.png}
\caption*{\textit{Nota.} Elaboración propia a partir del tablero en Trello: https://trello.com/invite/b/69ee3364a0402cb22cd14dec/ATTI41e197d9a1a090a8630eda1d8f3252f33AB6B10F/1asi0729-viora-sb1}
\end{figure}

\begin{tabular}{|p{0.05\textwidth}|p{0.14\textwidth}|p{0.05\textwidth}|p{0.14\textwidth}|p{0.24\textwidth}|p{0.08\textwidth}|p{0.12\textwidth}|p{0.07\textwidth}|}
\hline
\multicolumn{2}{|l|}{\textbf{Sprint \#}} & \multicolumn{6}{l|}{Sprint 1} \\ \hline
\multicolumn{2}{|l|}{\textbf{User Story}} & \multicolumn{6}{l|}{\textbf{Work-Item / Task}} \\ \hline
\textbf{Id} & \textbf{Title} & \textbf{Id} & \textbf{Title} & \textbf{Description} & \textbf{Estimation (Hours)} & \textbf{Assigned To} & \textbf{Status (To-do / In-Process / To-Review / Done)} \\ \hline

% US54
\multirow{3}{*}{US54} & \multirow{3}{*}{\parbox{0.14\textwidth}{Presentación de la propuesta de valor central}} 
& TK01 & Header UI \& Navigation & Maquetación, estilos y programación del comportamiento de navegación responsiva del encabezado principal. & 0.75 & Li, Diana & Done \\ \cline{3-8}
& & TK02 & Hero Section Layout & Estructuración semántica y diseño visual de la sección principal de inicio. & 0.5 & Santi, Fabrizio & Done \\ \cline{3-8}
& & TK03 & Hero Ambient Audio Logic & Implementación del comportamiento interactivo y control del reproductor de audio ambiental. & 0.5 & Santi, Fabrizio & Done \\ \hline

% US55
\multirow{2}{*}{US55} & \multirow{2}{*}{\parbox{0.14\textwidth}{Redirección hacia el ecosistema transaccional}} 
& TK04 & Problem \& Solution Layout & Diseño estructural visual de la sección persuasiva enfocada en los retos del rubro olivarero. & 0.5 & Santi, Fabrizio & Done \\ \cline{3-8}
& & TK05 & Persuasive CTAs Behavior & Programación de interacciones y animaciones para los botones de llamado a la acción (CTA). & 0.5 & Santi, Fabrizio & Done \\ \hline

% US56
\multirow{1}{*}{US56} & \multirow{1}{*}{\parbox{0.14\textwidth}{Exploración de beneficios para el Productor}} 
& TK06 & Producer Segment Interface & Maquetación y estilos de la vista de beneficios orientada exclusivamente a productores. & 0.5 & Santi, Fabrizio & Done \\ \hline

% US57
\multirow{2}{*}{US57} & \multirow{2}{*}{\parbox{0.14\textwidth}{Exploración de beneficios para el Especialista}} 
& TK07 & Specialist Segment Interface & Maquetación y estilos de la vista de beneficios orientada a especialistas fitosanitarios. & 0.5 & Santi, Fabrizio & Done \\ \cline{3-8}
& & TK08 & Segment Toggle Behavior & Programación del comportamiento dinámico para alternar la interfaz entre perfiles de usuario. & 0.5 & Santi, Fabrizio & Done \\ \hline

% US58
\multirow{2}{*}{US58} & \multirow{2}{*}{\parbox{0.14\textwidth}{Presentación del modelo de acceso}} 
& TK09 & Pricing Layout \& Parallax & Implementación visual de los planes de suscripción junto con el efecto de fondo parallax. & 0.75 & Trinidad, Jahat & Done \\ \cline{3-8}
& & TK10 & Referrals Logic \& UI & Desarrollo de la interfaz e interactividad de la tarjeta del programa de referidos. & 0.5 & Trinidad, Jahat & Done \\ \hline

% US59
\multirow{1}{*}{US59} & \multirow{1}{*}{\parbox{0.14\textwidth}{Validación de eficacia mediante experiencias de usuarios}} 
& TK11 & Testimonials Carousel & Diseño de tarjetas de reseña e implementación de la lógica del carrusel interactivo. & 0.75 & Espada, Piero & Done \\ \hline

% US60
\multirow{2}{*}{US60} & \multirow{2}{*}{\parbox{0.14\textwidth}{Exploración del respaldo corporativo y humano}} 
& TK12 & Mission \& Vision Intro & Creación de la interfaz para la sección introductoria y panel descriptivo de la misión. & 0.5 & Paredes, Victor & Done \\ \cline{3-8}
& & TK13 & Team \& Partners Displays & Maquetación y efectos visuales de los perfiles del equipo de desarrollo y grilla de socios. & 0.5 & Paredes, Victor & Done \\ \hline

% US61
\multirow{2}{*}{US61} & \multirow{2}{*}{\parbox{0.14\textwidth}{Consulta de normativas / Contacto}} 
& TK14 & Contact UI & Maquetación y estilos de los datos de contacto. & 0.75 & Espada, Piero & Done \\ \cline{3-8}
& & TK15 & Footer Semantic Layout & Estructuración semántica y diseño responsivo del pie de página. & 0.5 & Santi, Fabrizio & Done \\ \hline

\end{tabular}


