# Investigación sobre Metodologías Ágiles

## Ágil: qué es y por qué surge

Ágil surge a partir del **Manifesto for Agile Software Development** (2001), creado por 17 profesionales del desarrollo de software. El manifiesto señala que buscaban "mejores formas de desarrollar software" y prioriza individuos e interacciones, software funcionando, colaboración con el cliente y respuesta al cambio.

Según el Project Management Institute (PMI), el movimiento surgió porque muchos enfoques tradicionales estaban fuertemente orientados a la planificación y documentación, perdiendo de vista la satisfacción del cliente y la capacidad de responder a cambios.

Este archivo cubrira, además de el concepto general de ágil, conceptos de scrum, kanban, y design thinking.

---

## Valores y principios clave de Ágil

### Los 4 valores del Manifiesto Ágil

| Valor | Explicación breve | Impacto en la gestión del trabajo |
|---------|---------|---------|
| Individuos e interacciones sobre procesos y herramientas | Las personas y la colaboración son más importantes que seguir procedimientos rígidos. | Favorece la comunicación, la colaboración y la toma rápida de decisiones. |
| Software funcionando sobre documentación exhaustiva | Se prioriza entregar resultados funcionales. | Permite validar avances mediante entregables reales. |
| Colaboración con el cliente sobre negociación contractual | El cliente participa activamente durante el desarrollo. | Facilita ajustar prioridades según necesidades reales. |
| Responder al cambio sobre seguir un plan | Los cambios pueden incorporarse durante el trabajo. | Incrementa la capacidad de adaptación frente a nuevas necesidades. |

### Los 12 principios

- Satisfacer al cliente mediante entregas tempranas y continuas de valor.
- Aceptar cambios en los requisitos, incluso en etapas tardías.
- Entregar software funcional frecuentemente.
- Colaboración diaria entre negocio y desarrollo.
- Construir proyectos alrededor de personas motivadas.
- Utilizar la conversación directa como medio efectivo de comunicación.
- Medir el progreso mediante resultados funcionales.
- Mantener un ritmo de trabajo sostenible.
- Promover la excelencia técnica y el buen diseño.
- Favorecer la simplicidad.
- Impulsar equipos autoorganizados.
- Reflexionar regularmente para mejorar continuamente.

**Impacto general en la gestión del trabajo:** estos principios fomentan la entrega continua de valor, la colaboración constante, la adaptación al cambio y la mejora continua.

---

## Marcos ágiles

### Scrum

Scrum es un marco ligero que ayuda a personas, equipos y organizaciones a generar valor mediante soluciones adaptativas para problemas complejos. Trabaja de forma iterativa e incremental mediante ciclos llamados Sprints.

**Cuándo elegirlo:** cuando existe trabajo complejo, se requiere planificación iterativa y se desean entregas periódicas con roles y eventos bien definidos.

### Kanban

Kanban es un método para gestionar trabajo y servicios profesionales mediante la visualización del flujo de trabajo y la mejora continua. Busca ayudar a las organizaciones a responder de forma adaptativa a los cambios.

**Cuándo elegirlo:** cuando se necesita visualizar el trabajo, gestionar el flujo de tareas y mejorar progresivamente procesos existentes sin reemplazarlos.

### Design Thinking

Design Thinking es un enfoque centrado en las personas para resolver problemas complejos. Integra las necesidades de las personas, las posibilidades de la tecnología y los requisitos de negocio para generar soluciones innovadoras.

**Cuándo elegirlo:** cuando el objetivo principal es comprender a los usuarios, explorar problemas poco definidos o generar ideas innovadoras antes de desarrollar una solución.

---

## Comparación entre Scrum, Kanban y Design Thinking

| Marco | Beneficios | Limitaciones | Trade-offs típicos |
|---------|---------|---------|---------|
| Scrum | Proporciona estructura clara, fomenta la inspección y adaptación continua, y permite entregas incrementales. | Requiere disciplina en roles y eventos; puede resultar rígido para algunos equipos. | Mayor estructura y previsibilidad a cambio de más ceremonias y coordinación. |
| Kanban | Fácil de adoptar sobre procesos existentes, alta visibilidad del trabajo y mejora continua basada en flujo. | No define roles ni eventos específicos; puede existir menor predictibilidad si no se gestiona adecuadamente. | Mayor flexibilidad a cambio de menor estructura formal. |
| Design Thinking | Favorece la comprensión profunda de los usuarios, la creatividad y la innovación. | No está orientado a gestionar la ejecución completa de proyectos. | Mayor exploración e innovación a cambio de menor enfoque en la gestión operativa continua. |

---

# Scrum

## Propósito de Scrum y cuándo usarlo

Según la Scrum Guide, Scrum es un marco de trabajo ligero que ayuda a personas, equipos y organizaciones a generar valor mediante soluciones adaptativas para problemas complejos.

### Cuándo usarlo
- Cuando se trabaja sobre problemas complejos o inciertos.
- Cuando es valioso inspeccionar resultados frecuentemente y adaptarse.
- Cuando se requiere entregar valor de forma incremental.
- 
---

## Roles de Scrum

### Product Owner
**Descripción breve:** Responsable de maximizar el valor del producto y gestionar el Product Backlog.

**Responsabilidades:**
- Desarrollar y comunicar el Product Goal.
- Crear y ordenar los Product Backlog Items.
- Garantizar que el Product Backlog sea transparente y comprendido.

**Errores comunes:**
- Actuar como comité en lugar de tomar decisiones.
- Mantener un backlog poco claro o mal priorizado.
- No comunicar adecuadamente el objetivo del producto.

### Scrum Master
**Descripción breve:** Responsable de que Scrum sea comprendido y aplicado eficazmente.

**Responsabilidades:**
- Ayudar al equipo a aplicar Scrum.
- Facilitar eventos productivos.
- Ayudar a eliminar impedimentos.
- Apoyar al Product Owner y a la organización.

**Errores comunes:**
- Actuar como gerente tradicional.
- Dirigir al equipo en lugar de facilitar.
- Convertirse en administrador de reuniones.

### Developers (Development Team)
**Descripción breve:** Personas que crean el Incremento durante cada Sprint.

**Responsabilidades:**
- Crear un plan para el Sprint.
- Adaptar el plan diariamente.
- Mantener la calidad mediante la Definition of Done.
- Entregar un Incremento utilizable.

**Errores comunes:**
- Trabajar en silos.
- No inspeccionar ni adaptar el plan.
- Considerar terminadas tareas que no cumplen la Definition of Done.

---

## Artefactos Scrum

### Product Backlog
Lista ordenada y emergente de lo que se conoce que se necesita para mejorar el producto.

### Sprint Backlog
Plan creado por los Developers para alcanzar el Sprint Goal y entregar el Incremento.

### Increment
Suma de todos los elementos completados durante un Sprint y los incrementos anteriores.

### Criterios de calidad
La Scrum Guide establece la **Definition of Done (DoD)** como el compromiso asociado al Increment.

#### Definition of Done vs Criterios de aceptación

| Aspecto | Definition of Done | Criterios de aceptación |
|----------|----------|----------|
| Alcance | Aplica a todos los Product Backlog Items | Aplica a un elemento específico |
| Objetivo | Garantizar calidad consistente | Verificar requisitos específicos |
| Perspectiva | Calidad global del producto | Comportamiento esperado de una funcionalidad |
| Estabilidad | Normalmente estable entre Sprints | Cambia según cada requisito |

---

## Eventos Scrum

| Evento | Descripción breve | Objetivo | Duración sugerida (máx. Scrum Guide) | Antipatrón típico |
|----------|----------|----------|----------|----------|
| Sprint | Contenedor de todos los eventos Scrum. | Crear un Incremento valioso. | Un mes o menos. | Cambiar constantemente los objetivos del Sprint. |
| Sprint Planning | Inicia el Sprint definiendo qué y cómo se trabajará. | Establecer Sprint Goal y Sprint Backlog. | 8 horas para Sprint de un mes. | Convertirla en una asignación de tareas. |
| Daily Scrum | Evento diario de inspección y adaptación. | Inspeccionar el progreso hacia el Sprint Goal. | 15 minutos. | Convertirlo en reporte de estatus para un jefe. |
| Sprint Review | Inspección del Incremento con stakeholders. | Obtener retroalimentación y adaptar el Product Backlog. | 4 horas para Sprint de un mes. | Tratarla como una demostración informal sin discusión. |
| Sprint Retrospective | Reflexión sobre personas, procesos y herramientas. | Mejorar la efectividad del equipo. | 3 horas para Sprint de un mes. | Generar acciones de mejora que nunca se implementan. |

---

## Métricas Scrum

### Velocity
**Qué mide:** Cantidad de trabajo completado por el equipo en un Sprint.

**Cómo interpretarla:**
- Sirve para planificación y pronóstico.
- Permite estimar capacidad futura basándose en datos históricos.

**Cómo NO usarla:**
- No comparar equipos.
- No utilizarla como métrica de productividad individual.
- No establecer objetivos para aumentar artificialmente la velocidad.

### Burndown
**Qué mide:** Trabajo restante a lo largo del tiempo dentro de un Sprint.

**Cómo interpretarla:**
- Permite visualizar el avance y detectar desviaciones.
- Facilita conversaciones de inspección y adaptación.

**Cómo NO usarla:**
- No asumir que una línea perfecta implica éxito.
- No usarla para controlar individualmente a las personas.

### Work in Progress (WIP)
**Qué mide:** Número de elementos iniciados pero no terminados.

**Cómo interpretarla:**
- Ayuda a entender el flujo de trabajo.
- Un WIP elevado puede indicar cuellos de botella o exceso de trabajo simultáneo.

**Cómo NO usarla:**
- No utilizarla para medir productividad individual.
- No confundir WIP con WIP Limit.

---

# Kanban

## Principios y prácticas de Kanban

### Principios

- **Comienza con lo que haces actualmente**

 Enfoque en lo que la organización ya esta haciendo, no cambies el proceso de inmediato, haz mejoras.

- **Los cambios ocurren organicamente con el tiempo y no deben apresurarse**

 Mejora continua, pequeños cambios graduales basados en observación cuidadosa de los flujos de
 trabajo.

- **Respeta los roles y responsabilidades actuales**

 Los cambios de roles y responsabilidades pueden surgir a medida que avanza el proceso de mejora
 continua, pero no forman parte de la metodologia.

- **Fomenta el liderazgo de todos**

 Promueve un entorno colaborativo donde los miembros pueden sugerir oportunidades de mejora.

### Practicas

| Práctica | Descripción breve |
|----------|----------|
| Visualizar el trabajo | Hacer visible el trabajo y cómo fluye a través del sistema mediante un tablero. |
| Limitar WIP (Work In Progress) | Restringir la cantidad de trabajo en curso para favorecer la finalización antes de iniciar nuevas tareas. |
| Gestionar el flujo | Supervisar cómo avanza el trabajo para identificar bloqueos y mejorar la entrega. |
| Hacer explícitas las políticas | Definir reglas claras sobre cómo se procesa el trabajo. |
| Implementar bucles de retroalimentación | Utilizar revisiones periódicas para inspeccionar y mejorar el sistema. |
| Mejorar evolutivamente | Introducir cambios incrementales y colaborativos basados en observaciones y experimentos. |

---

## Tablero Kanban para un equipo de desarrollo

### Propuesta de columnas

| Columna | Propósito |
|----------|----------|
| Backlog | Trabajo pendiente de iniciar. |
| Analysis | Refinamiento o análisis del requerimiento. |
| Development | Implementación activa. |
| Code Review | Revisión técnica del código. |
| Testing | Validación funcional y técnica. |
| Deployment | Preparación o liberación. |
| Done | Trabajo completado. |

### Ejemplo de límites WIP

| Columna | WIP sugerido | Razón |
|----------|----------|----------|
| Analysis | 2 | Evitar acumulación de requisitos sin implementar. |
| Development | 3 a 5 | Mantener foco y reducir multitarea. |
| Code Review | 2 | Evitar cuellos de botella en revisiones. |
| Testing | 2 | Mantener flujo constante hacia entrega. |

Estos límites deberian ajustarse según la capacidad real del equipo.

---

## Métricas de flujo Kanban

### Lead Time
Tiempo total desde que un elemento entra al flujo hasta que está terminado.

**Cómo leerla:** valores menores y más predecibles suelen indicar un flujo más eficiente.

### Cycle Time
Tiempo desde que el equipo comienza activamente un elemento hasta que lo termina.

**Cómo leerla:** ayuda a entender la velocidad real de ejecución del equipo.

### Throughput
Número de elementos completados durante un período determinado.

**Cómo leerla:** muestra la capacidad real del sistema y ayuda a realizar pronósticos.

### Diagrama de Flujo Acumulado (CFD)
Gráfico que muestra la acumulación de trabajo en cada estado del flujo.

**Cómo leerlo:**
- La distancia vertical entre bandas muestra el WIP.
- La pendiente de la banda de elementos completados muestra el throughput.
- El ensanchamiento de una banda suele indicar un cuello de botella.

---

## Políticas y clases de servicio Kanban

Las clases de servicio permiten tratar distintos tipos de trabajo mediante políticas diferenciadas.

| Clase de servicio | Descripción | Ejemplo | Cuándo aplicarla |
|----------|----------|----------|----------|
| Expedite | Trabajo de máxima urgencia que recibe atención inmediata. | Incidente crítico en producción. | Cuando el costo de demora es extremadamente alto. |
| Fixed Date | Trabajo con fecha límite definida. | Cumplimiento regulatorio o campaña programada. | Cuando existe una fecha de entrega obligatoria. |
| Standard | Trabajo normal sin urgencia especial. | Nueva funcionalidad planificada. | Para la mayoría de las solicitudes habituales. |
| Intangible | Trabajo cuyo beneficio se verá en el futuro. | Reducción de deuda técnica o refactorización. | Cuando se busca mejorar sostenibilidad y calidad futura. |

---

## Cuándo usar Kanban en lugar de otros enfoques

Kanban resulta especialmente adecuado cuando:

- Existe alta variabilidad en la llegada de trabajo.
- Las prioridades cambian frecuentemente.
- Se necesita entrega continua.
- El trabajo llega en forma de tickets o solicitudes continuas.
- Se desea mejorar un proceso existente sin realizar una transformación completa.
- Es importante equilibrar demanda y capacidad mediante un sistema pull.

Ejemplos habituales:
- Mesas de ayuda (Help Desk).
- Equipos de soporte.
- Gestión de incidencias.
- Equipos que trabajan principalmente mediante tickets.
- Equipos con carga de trabajo altamente variable.

---

# Design Thinking

## Principios de Design Thinking y cómo encajan con el desarrollo de software

Design Thinking es descrito por IDEO como un enfoque centrado en las personas para la innovación, que integra las necesidades de las personas, las posibilidades de la tecnología y los requisitos para el éxito del negocio.

### Relación con el desarrollo de software

| Principio | Relación con desarrollo de software |
|------------|------------|
| Enfoque centrado en las personas | Ayuda a comprender necesidades reales de usuarios antes de implementar funcionalidades. |
| Experimentación | Permite validar ideas mediante prototipos antes de invertir en desarrollo completo. |
| Colaboración multidisciplinaria | Facilita la participación de negocio, diseño y desarrollo. |
| Aprendizaje iterativo | Favorece ajustes continuos a medida que se obtiene retroalimentación. |

---

## Fases de Design Thinking

| Fase | Objetivo | Técnicas sugeridas | Entregables mínimos |
|--------|--------|--------|--------|
| Empatizar | Comprender usuarios, necesidades y contexto. | Entrevistas, observación, shadowing, mapas de empatía. | Hallazgos de investigación y necesidades identificadas. |
| Definir | Sintetizar hallazgos y formular el problema. | Point of View (POV), afinidad, análisis de hallazgos. | Declaración clara del problema y necesidades priorizadas. |
| Idear | Generar posibles soluciones. | Brainstorming, Crazy 8s, co-creación. | Lista de ideas o conceptos candidatos. |
| Prototipar | Convertir ideas en representaciones tangibles. | Wireframes, bocetos, mockups, prototipos de papel. | Prototipo de baja o media fidelidad. |
| Probar | Obtener retroalimentación de usuarios. | Pruebas de usabilidad, entrevistas y observación. | Resultados y aprendizajes para iterar. |

---

## Ejemplo de Design Thinking

### Problema hipotético

Los estudiantes universitarios olvidan fechas importantes de entrega de tareas debido a que utilizan múltiples plataformas académicas.

### Empatizar
**Actividades:** entrevistar estudiantes, observar cómo registran tareas y recopilar frustraciones frecuentes.

**Entregable:** necesidades y problemas principales.

### Definir
**Actividades:** sintetizar entrevistas y redactar la necesidad.

**Definición del problema:** Los estudiantes necesitan una forma más simple de visualizar tareas y fechas límite porque la información se encuentra distribuida en varias herramientas.

**Entregable:** declaración del problema.

### Idear
**Actividades:** sesiones de brainstorming para proponer soluciones.

**Ideas generadas:**
- Calendario unificado.
- Recordatorios automáticos.
- Priorización por urgencia.

**Entregable:** conjunto de ideas priorizadas.

### Prototipar
**Actividades:** crear una representación simple de la solución.

**Entregable:** prototipo inicial.

### Probar
**Actividades:** mostrar el prototipo a estudiantes y recopilar comentarios.

**Entregable:** lista de observaciones y mejoras.

### Prototipo de baja fidelidad (texto)

```text
+--------------------------------+
| Panel de tareas                |
+--------------------------------+
| Hoy                            |
| - Matemáticas (mañana)         |
| - Física (3 días)              |
+--------------------------------+
| Próximas entregas              |
| - Proyecto final               |
| - Presentación                 |
+--------------------------------+
| [Agregar tarea]                |
+--------------------------------+
```

---

## Relación con SDLC, Scrum y Kanban

### Design Thinking y SDLC

Design Thinking suele emplearse antes o durante las etapas tempranas del desarrollo para comprender necesidades y validar ideas antes de construir soluciones.

### Cómo reduce el riesgo de construir lo incorrecto

- Promueve comprensión profunda del usuario.
- Permite validar hipótesis mediante prototipos.
- Obtiene retroalimentación temprana antes de realizar inversiones significativas en desarrollo.
- Facilita la iteración basada en evidencia observada.

### Relación con Scrum

- Design Thinking ayuda a descubrir problemas y oportunidades.
- Los resultados pueden transformarse en Product Backlog Items.
- Scrum puede utilizarse para construir e iterar sobre las soluciones validadas.

### Relación con Kanban

- Design Thinking aporta descubrimiento y validación.
- Kanban ayuda a gestionar el flujo continuo del trabajo derivado de las ideas validadas.
- Ambos enfoques favorecen la mejora continua y la adaptación.

---

# Conclusiones

### Como aplicaria esto en mi vida academica ó profesiónal?

Veo que estas metodologías, aunque tengan un enfoque en el software, poseen muchos principos que pueden aplicarse en otras areas, ya que discuten el proceso mediante el cual se elabora un producto. En la escuela, nos piden proyectos, o tareas; lo que resulta de que creemos algo a partir de ellas, es un producto, el cual tiene un proceso de creación. Por lo tanto, podriamos usar cosas como la iteración de Scrum para la mejora continua del objeto, como por ejemplo, el robot que nos pidio, ademas de implementar cosas de Kanban para guíar su elaboración junto a elementos de Design Thinking para aseguar que el robot cumpla las funciónes que nos pide.

Y profesionalmente es lo mismo, nos piden que elaboremos objetos, que tambíen poseen un proceso de elaboración, y que por lo tanto también se les pueden aplicar conceptos de las metodologías agiles para realizarlos.

---

# Referencias

### Ágil

- https://agilemanifesto.org/
- https://www.pmi.org/disciplined-agile/agile/theagilemanifesto
- https://scrumguides.org/scrum-guide.html
- https://www.scrum.org/learning-series/what-is-scrum/
- https://kanban.university/kanban-guide/
- https://kanban.university/resources/kanbanmethod/
- https://designthinking.ideo.com/
- https://www.ideo.com/methodologies

### Scrum

- https://www.scrum.org/resources/blog/definition-done-vs-acceptance-criteria-explained
- https://www.scrum.org/resources/blog/what-difference-between-definition-done-and-acceptance-criteria
- https://www.sitepoint.com/scrum-artifacts-velocity-and-burndown-charts/
- https://www.scrum.org/resources/burndown-charts-defined
- https://www.scrum.org/resources/blog/4-key-flow-metrics-and-how-use-them-scrums-events
- https://agileseekers.com/blog/mastering-scrum-metrics-velocity-burndown-flow-based-insights

### Kanban

- https://ones.com/blog/kanban-methodology-explained-visual-guide-streamlining-workflow/
- https://edworking.com/project-management/methodologies/kanban
- https://ones.com/blog/kanban-methodology-example-step-by-step-guide/
- https://www.atlassian.com/agile/project-management/kanban-metrics
- https://www.kanban.global/en/metricas-no-kanban-como-medir-e-interpretar/
- https://www.dev-toolbox.tech/tools/kanban-board/examples/kanban-metrics-and-analytics
- https://teamhood.com/kanban-resources/kanban-classes-of-service/
- https://kanbanzone.com/resources/kanban/classes-of-service/
- https://www.kanban.global/en/aprender/classes-de-servico/
- https://ones.com/blog/when-to-use-kanban-methodology/
- https://allthingsagile.co/post/when-to-use-kanban/
- https://www.sendboard.com/blog/ticketing-workflows-with-kanban

### Design Thinking

- https://www.ideo.com/methodologies/design-thinking
- https://www.interaction-design.org/literature/topics/design-thinking
- https://dschool.stanford.edu/resources