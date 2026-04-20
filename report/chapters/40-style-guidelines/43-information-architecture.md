## Information Architecture

### Labeling Systems

### SEO Tags and Meta Tags

Para la arquitectura informacional de Viora, los metadatos se organizan con una lógica dual. La Landing Page concentra la visibilidad orgánica y funciona como una única URL indexable que articula sus secciones internas de la taxonomía: Homepage, Problem & Solution, Segment Benefits, Access Model, Trust & Social, About Us y Footer. En la Web Application, en cambio, la prioridad es operativa; por ello sus rutas deben permanecer fuera del índice público y conservar una intención estrictamente transaccional.

En la experiencia pública, las secciones de la Landing Page no requieren metadatos independientes porque forman parte del mismo documento HTML. Su función SEO se resuelve desde un único conjunto de tags, reforzado por encabezados, anclas y jerarquía semántica. En la experiencia privada sí se definen valores por flujo principal, especialmente para inicio de sesión, prueba gratuita, registro por rol y paneles de trabajo.

| Capa            | Página o flujo             | Title | Meta Description                                                                                         | Meta Keywords                                                                                                        | Author      | Robots            |
| --------------- | -------------------------- | ----- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| Landing Page    | Homepage                   | Viora | Plataforma digital para monitoreo del olivo, alerta temprana y conexión con especialistas agrícolas.     | viora, monitoreo del olivo, alerta fitosanitaria, agricultura de precisión, especialistas agrícolas, prueba gratuita | ArcadiaDevs | index, follow     |
| Web Application | Log In                     | Viora | Accede de forma segura al panel privado de Viora según tu perfil de usuario.                             | viora, inicio de sesión, acceso seguro, panel privado, productor, especialista                                       | ArcadiaDevs | noindex, nofollow |
| Web Application | Start Free Trial           | Viora | Activa tu prueba gratuita y completa el registro inicial para entrar al ecosistema Viora.                | viora, prueba gratuita, trial, onboarding, registro de usuario, agricultura digital                                  | ArcadiaDevs | noindex, nofollow |
| Web Application | Registro de Productor      | Viora | Crea tu cuenta como Productor y accede a las herramientas de monitoreo, trazabilidad y alertas de Viora. | registro productor, productor olivarero, monitoreo satelital, trazabilidad, alertas climáticas                       | ArcadiaDevs | noindex, nofollow |
| Web Application | Registro de Especialista   | Viora | Crea tu cuenta como Especialista y habilita tu perfil profesional dentro del ecosistema Viora.           | registro especialista, especialista agrícola, marketplace agrícola, perfil profesional, cotización                   | ArcadiaDevs | noindex, nofollow |
| Web Application | Dashboard del Productor    | Viora | Consulta el estado de tu parcela, el vigor vegetal y las alertas de riesgo desde tu panel de productor.  | dashboard productor, ndvi, vigor vegetal, riesgo fenológico, trazabilidad agronómica                                 | ArcadiaDevs | noindex, nofollow |
| Web Application | Dashboard del Especialista | Viora | Gestiona solicitudes, disponibilidad operativa y cotizaciones desde tu panel profesional.                | dashboard especialista, marketplace agrícola, disponibilidad operativa, cotización, intervención técnica             | ArcadiaDevs | noindex, nofollow |
| Web Application | Panel de intervención      | Viora | Revisa alertas activas, evaluación de parcela, receta digital y confirmación de aplicación en campo.     | intervención fitosanitaria, receta digital, evaluación de parcela, aplicación técnica, trazabilidad                  | ArcadiaDevs | noindex, nofollow |

### Navigation Systems
El sistema de navegación garantiza la orientación constante del usuario y la finalización exitosa de sus tareas operativas a través de tres niveles:

Navegación Global: Se centraliza en una Navbar para la Landing Page y una Sidebar para la Web App. Estos elementos permiten el acceso permanente a los módulos principales desde cualquier nivel de la plataforma.

Navegación Local y Contextual: Se emplean Tabs para organizar métricas específicas (clima y vigor vegetal) en una sola vista. Además, se integran enlaces contextuales que guían al usuario a través de la Choreography de conversión y registro.

Sistemas de Orientación: Se utilizan Breadcrumbs y botones de retroceso claros. Esto permite que el usuario identifique su ubicación jerárquica y pueda retornar a estados anteriores sin perder el progreso de su trabajo


### Searching Systems
Para resolver las necesidades de localización de expertos y detección de riesgos detectadas en el modelo de negocio, Viora implementa mecanismos de búsqueda que transforman los datos del entorno en conexiones operativas:

Specialist Selection System: Este motor permite al productor obtener una terna de candidatos idóneos mediante el cruce de variables de cercanía geográfica y el Availability status de los asesores. Los resultados se priorizan según la afinidad técnica y las credenciales registradas en el Technical portfolio, facilitando una respuesta rápida ante emergencias.

Zonal Prospecting Radar: Es una herramienta de búsqueda visual y territorial diseñada para que los especialistas localicen Epidemiological alerts y unidades productivas con anomalías de vigor vegetal (NDVI). Este sistema permite aplicar filtros avanzados por nivel de Severity (High/Medium) y tipo de patógeno probable, optimizando la identificación de oportunidades de intervención.

Traceability & History Queries: La plataforma permite realizar búsquedas precisas dentro del historial acumulado de la cuenta. Los usuarios pueden filtrar registros de su Plot traceability y consultar Application logs previos para auditar la ejecución de recetas agrícolas, el control de gastos y la efectividad de campañas pasadas.

\newpage
