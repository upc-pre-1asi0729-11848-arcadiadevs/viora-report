## Software Configuration Management

### Software Development Environment Configuration

- Project Management
Para la gestión del proyecto y la administración de las necesidades del producto, el equipo utiliza las siguientes plataformas:

    - Discord: Se utiliza como centro de comunicación principal para las sesiones síncronas y coordinación. Integra Webhooks con GitHub para notificar en tiempo real las actividades de los repositorios. (https://discord.com/)

    - Trello: Plataforma utilizada para la priorización de tareas mediante tableros Kanban. (https://trello.com/)

- Requirements Management
Para la gestión de requisitos el se dividió en tres herramientas que permitieran conceptualizar las ideas del Lean UX Process y la información obtenida mediante las entrevistas.

    - UXPressia: Se utilizó para elaborar los artefactos de investigación, tales como los User Personas, Empathy Maps, Journey Maps e Impact Maps, centrando el diseño en las necesidades del usuario. (https://uxpressia.com/)

    - Miro: Se utilizó para la elaboración del Big Picture Event Storming, permitiendo explorar el dominio del negocio de forma visual. (https://miro.com/)

    - Trello: Se utilizó para la gestión y mantenimiento del Product Backlog, asegurando que los requerimientos estén priorizados según el valor de negocio.(https://trello.com/)

- Product UX/UI Design
De acuerdo a la sección con relación al diseño del producto, se utilizaron 5 herramientas:

    - Figma: Para el diseño visual y de la interfaz, se centralizó el trabajo en Figma. Esta herramienta se usó para desarrollar los Wireframes y Mock-ups de la Landing Page; los Wireframes, Mock-ups y Prototypes de la aplicación web, asegurando el uso de Material Design como lenguaje de diseño. (https://www.figma.com/)

    - LucidChart: Se empleó LucidChart para realizar las conexiones en los Wireflows y User Flows. Adicionalmente, se utilizó para los diagramas UML. (https://www.lucidchart.com/)

    - Structurizr: Se empleó para la representación gráfica y estructuración de la Arquitectura de Software utilizando el C4 Model. (https://structurizr.com/)

    - Vertabelo: Herramienta especializada para el diseño físico de la base de datos relacional, facilitando la integridad del esquema para cada Bounded Context. (https://vertabelo.com/)

    - Miro: Se empleó para el desarrollo del Design-Level Event Storming, profundizando en la identificación de comandos, eventos y agregados. (https://miro.com/)

- Software Development
El entorno de desarrollo para la solución web distribuida se basará en un stack de tecnologías open-source, gestionado con las siguientes herramientas:

    - GitHub: Para el almacenamiento, hosteo y control de versiones del código fuente, facilitando el trabajo colaborativo de todo el equipo. (https://github.com/)

    - WebStorm: Entorno de desarrollo integrado (IDE) principal para el Frontend Web Application. Se utilizará para programar de manera eficiente con Angular Framework, gestionando la lógica en TypeScript bajo el estándar de documentación TSDoc, la estructura en HTML5, los estilos en CSS3 y se crearán directivas en base al Web Design. (https://www.jetbrains.com/webstorm/download/)

    - IntelliJ IDEA: Entorno de desarrollo integrado (IDE) principal para el Backend. Se empleará para la codificación y despliegue de los Web Services bajo una arquitectura RESTful API, utilizando Java como lenguaje de programación, documentado bajo el estándar Javadoc y el framework Spring Boot. (https://www.jetbrains.com/idea/download/)

    - Visual Studio Code: Entorno de desarrollo integrado (IDE) principal para el desarrollo de la Landing Page. Se utilizará para la maquetación semántica en HTML5, el diseño visual y responsivo mediante CSS3, y la interactividad con JavaScript bajo el estándar de documentación JSDoc, asegurando un código limpio, organizado y fácil de escalar. (https://code.visualstudio.com/Download)

- Software Deployment
Para cumplir con el ciclo de desarrollo y despliegue de una solución distribuida en la nube, se ha implementará una estrategia híbrida que separa la captación comercial de la lógica transaccional:

    - Microsoft Azure: Proveedor de servicios Cloud principal para la infraestructura operativa. (https://azure.microsoft.com/)

        - Azure App Service: Hosteo del Web Service (Backend) de Spring Boot. Permite la ejecución de servicios Server-Side de Java en un entorno seguro y escalable. (https://azure.microsoft.com/es-es/products/app-service/)

        - Azure Static Web Apps: Se utilizará para el despliegue de la aplicación de Angular, optimizando la entrega del frontend mediante una red de distribución de contenido (CDN) global. (https://azure.microsoft.com/es-es/products/app-service/static/) 

        - Azure Database for PostgreSQL: Servicio gestionado para la persistencia de datos. Se utilizará para el almacenamiento de polígonos de parcelas y datos agronómicos, aprovechando la extensión PostGIS para el procesamiento geográfico necesario en el proyecto. (https://azure.microsoft.com/es-es/products/postgresql/)

    - Hostinger: Hosting para la Landing Page estática y gestor oficial del dominio y registros DNS del ecosistema

    - GitHub Actions: Motor de CI/CD que automatiza la compilación y despliegue hacia Azure en cada push a las ramas principales.

- Software Documentation
Para la documentación de la solución se considerará lo siguiente:

    - Visual Studio Code: Herramienta para la redacción modular del informe en Markdown, siguiendo una arquitectura de directorios organizada en Kebab-case para facilitar el enfoque "Docs-as-Code". (https://code.visualstudio.com/Download)

    - GitHub (Docs-as-Code): Aplicación de GitFlow, Conventional Commits y Semantic Versioning para el control de versiones de la documentación técnica y entregables. (https://github.com/)

    - Swagger (OpenAPI): Para la generación automática de la documentación de los Web Services, permitiendo visualizar claramente los parámetros, esquemas y respuestas de los endpoints (https://swagger.io/).


### Source Code Management

### Source Code Style Guide & Conventions

### Software Deployment Configuration

\newpage