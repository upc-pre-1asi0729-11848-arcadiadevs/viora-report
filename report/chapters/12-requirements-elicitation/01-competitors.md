# Capítulo II: Requirements Elicitation & Analysis

## Competidores.

| Tipo | Competidor | Descripción | Características | Website |
|---|---|---|---|---|
| Directo | ![Metos](report/assets/competitors/metos.png){width=80px} | Plataforma global que integra datos de sensores de suelo y clima (IoT) con modelos matemáticos predictivos de enfermedades. | - Integración directa con hardware propio (estaciones meteorológicas)<br>- Modelos de enfermedades para múltiples cultivos<br>- Pronóstico hiperlocal. | [metos.global](https://metos.global/es/) |
| Directo | ![Agroptima](report/assets/competitors/agroptima.png){width=80px} | Software de gestión agrícola muy popular en España y LATAM, fuertemente utilizado en el sector olivarero para la trazabilidad. | - Cuaderno de campo digital<br>- Registro geolocalizado de aplicación de fitosanitarios<br>- Control de costos<br>- App funcional en modo offline | [agroptima.com](https://www.agroptima.com) |
| Directo | ![Xarvio](report/assets/competitors/xarvio.png){width=80px} | Plataforma de agricultura digital de BASF especializada en modelos de riesgo de enfermedades y apoyo a decisiones fitosanitarias. | - Mapas de riesgo sanitario en tiempo real<br>- Alertas de protección de cultivos<br>- Recomendaciones precisas de fungicidas e insecticidas. | [xarvio.com](https://www.xarvio.com) |
| Indirecto | ![OneSoil](report/assets/competitors/onesoil.png){width=80px} | Aplicación gratuita de agricultura de precisión basada en el análisis de imágenes satelitales e índices de vegetación. | - Monitoreo remoto del vigor del cultivo (NDVI)<br>- Notas de campo (scouting) geolocalizadas<br>- Pronóstico del clima. | [onesoil.com](https://onesoil.ai) |
| Indirecto | ![Auravant](report/assets/competitors/auravant.png){width=80px} | Plataforma "todo en uno" para agricultura digital enfocada en agrónomos y empresas tecnificadas, con fuerte presencia en LATAM. | - Creación de zonas de manejo<br>- Prescripciones de insumos variables<br>- Análisis de capas de información (suelo, clima, rendimiento). | [auravant.com](https://www.auravant.com) |
| Indirecto | ![SENASA](report/assets/competitors/senasa.png){width=80px} | Sistema público oficial del Estado Peruano encargado de monitorear, alertar y contener plagas cuarentenarias (ej. Xylella fastidiosa). | - Emisión de alertas epidemiológicas regionales<br>- Normativas de control oficial<br>- Red de inspectores en campo<br>- Acceso gratuito pero no personalizado. | [gob.pe/senasa](https://www.gob.pe/senasa) |

### Análisis competitivo

Análisis competitivo para competidores **directos**

**¿Por qué llevar a cabo este análisis?**
¿Qué soluciones AgTech de gestión y prevención de plagas existen a nivel global, y cómo Viora puede penetrar en el mercado sur peruano aprovechando las barreras de entrada (como altos costos de hardware o falta de enfoque local) de los líderes internacionales?

| Criterio | Viora ![Viora](report/assets/logos/viora.png){width=60px} | Metos ![Metos](report/assets/competitors/metos.png){width=60px} | Agroptima ![Agroptima](report/assets/competitors/agroptima.png){width=60px} | Xarvio ![Xarvio](report/assets/competitors/xarvio.png){width=60px} |
|---|---|---|---|---|
| **PERFIL** | | | | |
| Overview | Plataforma SaaS B2B hiper-especializada en el ciclo de producción del olivo, que integra datos ambientales para emitir alertas y conecta a productores con agrónomos. | Plataforma global que integra hardware IoT (estaciones meteorológicas) con software predictivo de enfermedades (FieldClimate). | Software líder de gestión agrícola enfocado en el cuaderno de campo, trazabilidad de operaciones y control de costos. | Plataforma de agricultura digital de BASF especializada en modelos de riesgo sanitario y apoyo a decisiones fitosanitarias. |
| Ventaja competitiva | Alertas predictivas hiper-locales exclusivas para la fenología del olivo y un marketplace integrado para contratar la solución inmediata. | Precisión extrema al basar sus predicciones en datos extraídos por sus propios sensores físicos instalados en la parcela del cliente. | Usabilidad superior para el agricultor en el campo (funciona 100% offline) y simplificación del cumplimiento legal. | Algoritmos respaldados por años de I+D de BASF, con alta precisión en la recomendación del momento exacto para aplicar fungicidas. |
| **MARKETING** | | | | |
| Mercado Objetivo | Pequeños/medianos productores de olivo y especialistas técnicos en control de plagas agrícolas del sur del Perú (ej. Tacna). | Grandes corporaciones agroindustriales y fundos de cultivos de alto valor que pueden permitirse invertir en infraestructura (hardware). | Agricultores profesionales, cooperativas y gerentes de fundos de todos los tamaños, principalmente en España y LATAM. | Productores agrícolas que buscan optimizar su inversión en agroquímicos y proteger el rendimiento de sus cultivos intensivos/extensivos. |
| Estrategias de Marketing | Growth Loop basado en referidos/afiliados, alianzas estratégicas con cooperativas locales y asociaciones de productores. | Venta consultiva corporativa B2B y asociaciones con distribuidores locales de maquinaria y hardware agrícola. | Fuerte Content Marketing, prueba gratuita (Trial) de 15 días, embajadores de marca y presencia en ferias agrícolas. | Inbound Marketing, Product-Led Growth (versión freemium) e integraciones con productos químicos de su empresa matriz (BASF). |
| **PRODUCTO** | | | | |
| Servicios | - Dashboard de finca<br>- Motor predictivo de vecería/clima<br>- Alertas fitosanitarias<br>- Directorio de especialistas | - Hardware meteorológico<br>- FieldClimate app<br>- Suscripciones matemáticas | - Cuaderno de campo digital<br>- Registro geolocalizado<br>- Reportes de costos | - Mapas de riesgo de enfermedades<br>- Alertas de protección de cultivos |
| Precios | Modelo SaaS puro con periodo de prueba de riesgo cero. | Alto costo de entrada (hardware) + suscripción anual al software. | Modelo SaaS con suscripción anual basada en módulos según tamaño. | Modelo Freemium; funciones gratuitas y versiones PRO de pago. |
| Distribución | Web App responsiva y Landing Page orientada a conversión. | Distribuidores físicos exclusivos, Web App y App Móvil. | Web Application y App Móvil nativa. | Web Application y App Móvil nativa. |
| **SWOT** | | | | |
| Fortalezas | Especialización en el olivo. Resuelve el problema completo conectando la alerta con el técnico. | Datos hiper-precisos reales. Modelos matemáticos de enfermedades muy maduros. | Interfaz offline a prueba de fallos. Liderazgo en registro de costos operativos. | Fuerte respaldo corporativo. Modelos ampliamente entrenados. |
| Debilidades | Nueva sin base histórica propia. Depende de adopción de dos frentes. | Costo inaccesible para pequeño agricultor. Requiere mantenimiento físico. | Es un ERP, no un sistema predictivo especializado en alertas de plagas. | Sus modelos pueden no estar finamente calibrados para el microclima sur. |
| Oportunidades | Mercado olivarero fuertemente golpeado por anomalías y ENOS. | Integrar APIs con startups locales para vender acceso a sus datos. | Desarrollar módulos predictivos complementarios a su cuaderno. | Localizar modelos predictivos para plagas peruanas evaluando severidad. |
| Amenazas | Competidores gigantes que adapten marketplaces en sus sistemas. | Hardware físico vulnerable. Llegada de sensores IoT de bajo costo. | Otras alternativas locales adaptadas normativamente a Perú. | Desconfianza de productores hacia un conglomerado químico recomendando químicos. |

<br>

Análisis competitivo para competidores **indirectos**

**¿Por qué llevar a cabo este análisis?**
¿Qué alternativas públicas o plataformas satelitales globales utilizan actualmente los productores olivareros para informarse sobre su campo, y cómo Viora puede diferenciarse en la mitigación específica de riesgos fitosanitarios y climáticos en la región sur?

| Criterio | Viora ![Viora](report/assets/logos/viora.png){width=60px} | SENASA ![SENASA](report/assets/competitors/senasa.png){width=60px} | OneSoil ![OneSoil](report/assets/competitors/onesoil.png){width=60px} | Auravant ![Auravant](report/assets/competitors/auravant.png){width=60px} |
|---|---|---|---|---|
| **PERFIL** | | | | |
| Overview | Plataforma SaaS B2B hiper-especializada en el ciclo de producción del olivo... | Sistema público oficial del Estado Peruano encargado de monitorear y alertar plagas... | App global gratuita de agricultura de precisión basada en imágenes satelitales (NDVI). | Plataforma integral "todo en uno" para agricultura digital enfocada en rendimiento. |
| Ventaja competitiva | Alertas predictivas hiper-locales específicas para la fenología del olivo y conexión con marketplace... | Autoridad normativa oficial, respaldo estatal e infraestructura física ante emergencias... | Acceso masivo, gratuito y muy simple a mapas de vigor (NDVI) actualizados por satélite. | Ecosistema robusto y sumamente escalable con fuertes algoritmos para agrónomos. |
| **MARKETING** | | | | |
| Mercado Objetivo | Pequeños/medianos productores olivareros y especialistas del sur del Perú... | Todo el sector agropecuario nacional. | Agricultores y técnicos de todo el mundo en cultivos de áreas extensivas. | Ingenieros agrónomos, asesores técnicos y empresas agrícolas en LATAM. |
| Estrategias de Marketing | Growth Loop basado en referidos/afiliados, alianzas estratégicas... | Resoluciones públicas, campañas de prensa del Estado, capacitaciones físicas... | PLG (Product-Led Growth), SEO y redes sociales para expansión orgánica. | Ventas B2B consultivas (Outbound), webinars especializados, certificaciones. |
| **PRODUCTO** | | | | |
| Servicios | - Dashboard de finca<br>- Motor predictivo de vecería<br>- Alertas de plagas<br>- Marketplace | - Alertas epidemiológicas regionales<br>- Inspecciones de campo<br>- Certificados fitosanitarios | - Mapas de vigor del cultivo<br>- Notas de campo geolocalizadas<br>- Análisis de parcelas | - Mapas de productividad<br>- Pescripciones de insumos<br>- Reportes de ambientación |
| Precios | SaaS (Suscripciones mensuales/anuales escalonadas) con Trial gratuito. | Gratuito (servicio público gubernamental). | 100% gratuito al usuario final (monetiza por datos agregados a macro nivel). | Modelo freemium; planes premium cobrados por la cantidad de hectáreas totales. |
| Distribución | Web App y Landing Page. | Portal gob.pe, oficinas presenciales y atención telefónica. | App Móvil robusta y Web App. | Web App (Core) y App Móvil como soporte. |
| **SWOT** | | | | |
| Fortalezas | Fuerte hiper-especialización. Solución End-to-End. | Poder coercitivo estatal y legal. Alcance masivo sin requerimientos. | UX impecable y uso gratuito para mapas satelitales en tiempo real. | Integración y análisis científico de extrema profundidad técnica e IoT. |
| Debilidades | Plataforma de dos mercados (requiere agricultores y expertos a la par). | Alertas a nivel macro-regional. Lentitud en la gestión altamente reactiva. | NDVI genérico (muestra un síntoma pero no emite el diagnóstico específico in-situ). | Curva de aprendizaje alta e interfaz muy compleja ("Overkill"). |
| Oportunidades | Sector en necesidad de mitigación ante ENOS y El Niño. | Colaboración externa con el sector AgTech para masificar normativas. | Fomentación e inducción para enseñar agricultura a productores conservadores. | Expansión en la base de pirámide de agricultura si simplifica drásticamente su interfaz. |
| Amenazas | Reticencia tecnológica y brecha digital en el entorno rural agrícola regional. | Limitaciones de capacidad operativa y posibles recortes presupuestales de acción. | Viora u otra AgTech hiper-especializada que dé mapas pero añada el factor climático. | Competidores de uso gratuito que adiestran al mercado restándoles clientes base. |

<br>

### Estrategias y tácticas frente a competidores

| Competidor | Táctica diferenciadora | Fortaleza del rival que enfrentamos | Debilidad del rival que aprovechamos |
|---|---|---|---|
| ![Metos](report/assets/competitors/metos.png){width=60px} | **"Software-only escalable y predictivo"**: Ingesta de datos ambientales mediante APIs y algoritmos sin obligar al productor a comprar infraestructura. | Gran precisión de datos de campo y modelos matemáticos de enfermedades. Extraen datos de estaciones propias. | Altos costos de entrada y mantenimiento de hardware para el pequeño productor, así como exposición a vandalismo en campo. |
| ![Agroptima](report/assets/competitors/agroptima.png){width=60px} | **"Motor predictivo vs. Registro pasivo"**: Viora procesa el clima y advierte automáticamente; no es solo una libreta digital de data-entry. | Usabilidad en campo líder europea y potente registro de costos operativos y trazabilidad. | Es un sistema pasivo; sin registro del agricultor, no emite alertas epidemiológicas predictivas autónomas ante crisis climáticas. |
| ![Xarvio](report/assets/competitors/xarvio.png){width=60px} | **"Hiper-nicho olivarero + Marketplace humano"**: Foco en la vecería y enlace físico-tecnológico para la aplicación agronómica inmediata con un experto humano. | Profundidad técnica corporativa, excelente análisis algorítmico y UX simple (mapas de colores intuitivos). | Aislamiento corporativo: Solo te alertan y derivan a químicos propios sin asistencia técnica humana. Riesgo de mala calibración. |

<br>

### Matriz F.O.D.A y C.A.M.E

| Análisis | Factores Externos e Internos |
|---|---|
| **Oportunidades (O)** | - Urgencia por mitigar daños por la variabilidad climática ENOS. (Andina, 2024).<br>- Reacción lenta estatal frente a problemas fitosanitarios (SENASA, 2024).<br>- Startups de AgTech inaccesibles, cediendo todo el ecosistema (Osco-Mamani et al., 2025). |
| **Amenazas (A)** | - Brecha tecnológica en el sistema agrario tradicional.<br>- Conectividad intermitente e inestable en zonas rurales y de frontera (Casanova Núñez-Melgar, 2022).<br>- Competencia con presupuestos internacionales imponentes y modelos consolidados.<br>- Cambios repentinos en el microclima invalidando porciones generadas (Calvo et al., 2024). |
| **Fortalezas (F)** | - Especialización regional única (fenología del olivo).<br>- Fuerte sinergia end-to-end con una red de expertos.<br>- Costo accesible sin requerir estaciones climáticas y una alta flexibilidad frente al problema de infraestructura.<br>- Capacidad de generar pronósticos individualizados a niveles micro-locales. |
| **Debilidades (D)** | - Marca joven sin historial de predicciones de campo.<br>- Fuerte dependencia inicial a servicios de climatología internacionales de terceros en vez de fuentes internas in-situ.<br>- Riesgo frente a la baja adopción simultánea del productor rural y el agrónomo comercial. |
| **Estrategia Ofensiva** | **FO1** Vender por volumen mediante paquetes B2B con las cooperativas olivareras priorizando bajo costo sin hardware.<br>**FO2** Convertirse en la alternativa de respuesta en menos tiempo ante la lentitud en la comunicación desde el sistema estatal.<br>**FO3** Potenciar el "Brazo Ejecutor" mediante el marketplace. |
| **Estrategia Defensiva** | **FA1** Valor Humano frente al corporativo: Enfatizar que Viora llama al especialista humano versus solo emitir la alerta digital.<br>**FA2** Desarrollar la optimización de App de red con bajo consumo de red rural y alta eficacia.<br>**FA3** Reforzar periódicamente el sistema climático previendo los cambios imprevistos de la variabilidad biológica endémica. |
| **Estrat. Reorientación** | **DO1** Dar de baja planes costosos realizando pilotos de adopción gratis locales iniciales levantando una biblioteca de uso sólida de campo.<br>**DO2** Motivar adopción mediante referidos y beneficios de la primera campaña entre colegas.<br>**DO3** Usar a los mismos técnicos como principales agentes comerciales (afiliados). |
| **Estrat. Supervivencia** | **DA1** Mantener un enfoque local rígido e invulnerable sin escalar prematuramente.<br>**DA2** Facilitar al máximo la curva de aprendizaje UX/UI organizando presenciales y talleres.<br>**DA3** Mantener a mano las líneas secundarias directas o "fallbacks" comunicacionales como contingencia extra. |
