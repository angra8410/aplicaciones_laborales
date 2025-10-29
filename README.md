# aplicaciones_laborales

En este repo yacen todas las aplicaciones laborales realizadas

## 🚀 Mejoras Recientes: Sistema de Personalización Inteligente + Scoring Automático

Este repositorio incluye un **motor de personalización avanzado** y un **sistema de scoring multi-dimensional** que genera hojas de vida verdaderamente adaptadas a cada vacante y evalúa objetivamente el match del candidato con los requerimientos del puesto.

### 📊 Mejoras Implementadas

#### Fase 1-3: Sistema de Personalización (COMPLETADO ✅)
- ✅ **Professional Summary Personalizado:** Se genera dinámicamente según los requisitos de cada vacante
- ✅ **Job Alignment Inteligente:** Mapea requisitos a logros reales con evidencia cuantificable
- ✅ **Sin Errores Gramaticales:** Corrección completa de problemas de redacción
- ✅ **Evidencia Concreta:** En lugar de "Demonstrated experience in...", muestra logros específicos con métricas
- ✅ **Nivel de Personalización:** Incrementado de 5% a 65%

#### Fase 4: Sistema de Scoring Automático (NUEVO ✅)
- ✅ **Análisis Multi-dimensional:** Evalúa el match en 5 dimensiones clave
  - Technical Skills Match (30% peso)
  - Experience Depth & Relevance (25% peso)
  - Domain Knowledge (20% peso)
  - Soft Skills & Cultural Fit (15% peso)
  - Achievement Quality (10% peso)
- ✅ **Reporte de Scoring Detallado:** Genera automáticamente un informe completo con:
  - Puntuación global y recomendación (EXCELLENT/STRONG/GOOD/MODERATE/WEAK FIT)
  - Desglose por dimensión con visualización de barras
  - Identificación de fortalezas y gaps
  - Estrategias de mitigación para gaps
  - Recomendaciones accionables priorizadas
  - Análisis detallado requisito por requisito
- ✅ **Transparencia Total:** Cada puntuación explica cómo se calculó y qué evidencia la respalda
- ✅ **Integración Automática:** Se ejecuta automáticamente en el flujo de GitHub Actions

#### Fase 5: Formato Profesional ATS-Friendly en PDF (NUEVO ✅)
- ✅ **Header Centrado y Profesional:** Nombre destacado, información de contacto centrada
- ✅ **Compatible con ATS:** Sin enlaces azules, fuentes estándar, formato limpio
- ✅ **Tipografía Mejorada:** LaTeX/XeTeX para apariencia profesional
- ✅ **Líneas Horizontales Rectas:** Separadores limpios y consistentes
- ✅ **Márgenes Optimizados:** 0.75 pulgadas, formato estándar
- ✅ **Enlaces en Negro:** Todos los enlaces en color negro para ATS
- ✅ **Documentación Completa:** Guías de uso y personalización incluidas

#### Fase 6: Prevención de Conflictos en Ejecuciones Concurrentes (NUEVO ✅)
- ✅ **Nombres de Archivo Únicos:** Todos los archivos generados incluyen timestamp para evitar colisiones
  - Formato: `ANTONIO_GUTIERREZ_RESUME_{empresa}_{fecha}_{timestamp}.pdf`
  - Ejemplo: `ANTONIO_GUTIERREZ_RESUME_TruelogicSoftware_2025-10-27_2025-10-27T01-30-45.pdf`
- ✅ **Estrategia de Merge:** El workflow usa `git merge` en lugar de `git rebase` para evitar conflictos add/add
- ✅ **Resolución Automática de Conflictos:** Si ocurren conflictos en archivos generados, se resuelven automáticamente
- ✅ **Robustez en Concurrencia:** El sistema puede manejar múltiples aplicaciones al mismo puesto/fecha sin errores
- ✅ **Compatibilidad Completa:** Los cambios son transparentes para el usuario final

### 📁 Documentación Completa

#### ⚡ Inicio Rápido
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md):** 🚀 **NUEVO** - Referencia rápida de configuración (3 minutos) - **EMPEZAR AQUÍ**
- **[RESUMEN_SOLUCION_PUSH_CI_CD.md](RESUMEN_SOLUCION_PUSH_CI_CD.md):** ⭐ **NUEVO** - Resumen ejecutivo de la solución non-fast-forward en CI/CD

#### 🔧 Configuración Inicial (⚠️ REQUERIDO para copia automática de PDFs)
- **[CONFIGURACION_INICIAL.md](CONFIGURACION_INICIAL.md):** 🚀 **NUEVO** - Guía paso a paso para configurar el repositorio destino (5 minutos)
- **[SETUP_REQUIRED.md](SETUP_REQUIRED.md):** ⚠️ **IMPORTANTE** - Instrucciones detalladas de configuración requerida

#### 🔧 Troubleshooting y Solución de Problemas
- **[SOLUCION_CONFLICTOS_CONCURRENCIA.md](SOLUCION_CONFLICTOS_CONCURRENCIA.md):** 🚀 **NUEVO** - Solución completa a conflictos de concurrencia en workflows (Fase 6)
- **[DIAGRAMA_SOLUCION_CONFLICTOS.md](DIAGRAMA_SOLUCION_CONFLICTOS.md):** 🚀 **NUEVO** - Diagrama visual antes/después de la solución de conflictos
- **[TROUBLESHOOTING_RAPIDO.md](TROUBLESHOOTING_RAPIDO.md):** 🚀 **NUEVO** - Guía rápida de resolución de problemas (5 minutos)
- **[EJEMPLO_VISUAL_WORKFLOW.md](EJEMPLO_VISUAL_WORKFLOW.md):** 🚀 **NUEVO** - Ejemplos visuales de logs y escenarios
- **[SOLUCION_IMPLEMENTADA.md](SOLUCION_IMPLEMENTADA.md):** 🚀 **NUEVO** - Resumen ejecutivo de la solución implementada
- **[GUIA_RAPIDA_NON_FAST_FORWARD.md](GUIA_RAPIDA_NON_FAST_FORWARD.md):** ⭐ **NUEVO** - Solución a errores de push non-fast-forward (3 minutos)
- **[DIAGRAMA_SOLUCION_PUSH.md](DIAGRAMA_SOLUCION_PUSH.md):** ⭐ **NUEVO** - Diagramas visuales de la solución non-fast-forward

#### 📚 Automatización y Flujos de Trabajo
- **[AUTOMATION_QUICKSTART.md](AUTOMATION_QUICKSTART.md):** ⭐ Inicio rápido para la automatización (5 minutos)
- **[AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md):** ⭐ Guía completa de automatización de issues y proyectos
- **[AUTOMATION_PDF_COPY_QUICKSTART.md](AUTOMATION_PDF_COPY_QUICKSTART.md):** ⭐ Setup rápido de copia automática de PDFs (5 minutos)
- **[AUTOMATION_PDF_COPY_GUIDE.md](AUTOMATION_PDF_COPY_GUIDE.md):** ⭐ Copia automática de CV PDFs al repositorio todos-mis-documentos
- **[WORKFLOW_DIAGRAM.md](WORKFLOW_DIAGRAM.md):** ⭐ **NUEVO** - Diagrama visual del flujo completo de automatización

#### 📖 Documentación Técnica
- **[DIAGNOSTIC_REPORT.md](DIAGNOSTIC_REPORT.md):** Diagnóstico completo del sistema de generación de CVs, identificación de limitaciones y propuestas de mejora
- **[BEFORE_AFTER_COMPARISON.md](BEFORE_AFTER_COMPARISON.md):** Ejemplos comparativos mostrando el antes y después de las mejoras
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md):** Guía técnica de implementación, uso y mantenimiento del sistema
- **[PHASE4_SCORING_SYSTEM_DESIGN.md](PHASE4_SCORING_SYSTEM_DESIGN.md):** Diseño completo del sistema de scoring multi-dimensional (Fase 4)
- **[CV_PDF_FORMATTING.md](CV_PDF_FORMATTING.md):** Documentación técnica del formato profesional de PDF (Fase 5)
- **[GUIA_FORMATO_CV.md](GUIA_FORMATO_CV.md):** Guía de usuario sobre el formato profesional ATS-friendly en PDF
- **[SOLUCION_NON_FAST_FORWARD.md](SOLUCION_NON_FAST_FORWARD.md):** ⭐ **NUEVO** - Solución técnica completa a errores de push non-fast-forward en CI/CD

### 🎯 Ejemplo de Mejora

**ANTES:**
```markdown
- Demonstrated experience in build and maintain custom dashboards..
```

**DESPUÉS (CV Personalizado):**
```markdown
**Build and maintain custom dashboards to support business operations**

Architected consolidated dashboard integrating 8 data sources, cutting data preparation time by 70%
```

**NUEVO (Scoring Report):**
```markdown
## Overall Match Score: 75.5% - STRONG FIT 🟢

### Dimensional Analysis

1. Technical Skills Match: 85% 🟢 (Contribution: 25.5%)
   ✅ Matched: dashboard, sql, etl, automation
   
2. Experience Depth: 90% 🟢 (Contribution: 22.5%)
   5+ years with 6 quantifiable achievements
   
3. Domain Knowledge: 75% 🟢 (Contribution: 15.0%)
   
4. Soft Skills: 70% 🟢 (Contribution: 10.5%)
   
5. Achievement Quality: 75% 🟢 (Contribution: 7.5%)

### Key Strengths
✅ Dashboard Expertise: 8 data sources integrated, 70% time reduction
✅ Automation Track Record: 60-75% time savings demonstrated

### Actionable Recommendations
🔴 [High] Prepare 2-3 stories highlighting dashboard & automation experience
🟡 [Medium] Review Zapier basics (30 minutes)
```

### 🔧 Uso

El sistema funciona automáticamente:

1. Coloca un archivo YAML en `to_process/` con los datos de la vacante
2. GitHub Actions procesa automáticamente el archivo
3. Se genera una carpeta en `to_process_procesados/` con:
   - **CV personalizado** en Markdown y PDF
   - **Reporte de scoring** en Markdown y PDF
   - Descripción de la vacante
   - Lista de requerimientos
4. ⭐ **NUEVO:** Se crea automáticamente una issue en GitHub
5. ⭐ **NUEVO:** La issue se agrega al proyecto "aplicacione-estados"
6. ⭐ **NUEVO:** El CV PDF se copia automáticamente al repositorio `todos-mis-documentos` organizado por fecha

### 🤖 Automatización de Gestión (NUEVO ✅)

El sistema ahora incluye **automatización completa de gestión de aplicaciones**:

- ✅ **Creación Automática de Issues:** Cada aplicación procesada genera automáticamente una issue con:
  - Título descriptivo (Cargo + Empresa)
  - Metadatos completos (fecha, carpeta, archivos generados)
  - Checklist de próximos pasos
  - Labels: `aplicacion-procesada`, `Aplicados`

- ✅ **Integración con GitHub Projects:** Las issues se agregan automáticamente al proyecto "aplicacione-estados"

- ✅ **Prevención de Duplicados:** El sistema verifica y evita crear múltiples issues para la misma aplicación

- ✅ **Trazabilidad Completa:** Cada aplicación tiene su issue dedicada para seguimiento

- ✅ **Copia Automática a todos-mis-documentos:** El CV PDF se copia automáticamente al repositorio `todos-mis-documentos`:
  - Organización por fecha (carpetas YYYY-MM-DD)
  - Commits descriptivos con trazabilidad
  - Agrupación de todas las aplicaciones del mismo día
  - Versionado documental completo
  - ⚠️ **Requiere configuración inicial:** Ver [SETUP_REQUIRED.md](SETUP_REQUIRED.md)

📖 **Documentación:** 
- **Quick Start Issues:** [AUTOMATION_QUICKSTART.md](AUTOMATION_QUICKSTART.md) ⭐ Comienza aquí
- **Quick Start PDFs:** [AUTOMATION_PDF_COPY_QUICKSTART.md](AUTOMATION_PDF_COPY_QUICKSTART.md) ⭐ Setup en 5 minutos
- **Guía completa Issues:** [AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)
- **Guía completa PDFs:** [AUTOMATION_PDF_COPY_GUIDE.md](AUTOMATION_PDF_COPY_GUIDE.md) ⭐ Nueva funcionalidad

### 🛠️ Componentes Técnicos

**Personalización:**
- **Motor de Personalización:** `aplicaciones_laborales/scripts/cv_personalization_engine.py`
- **Script Principal:** `aplicaciones_laborales/scripts/procesar_aplicacion.py`
- **Template:** `aplicaciones_laborales/plantillas/hoja_de_vida_harvard_template.md`

**Scoring (Nuevo):**
- **Motor de Scoring:** `aplicaciones_laborales/scripts/scoring_engine.py`
- **Generador de Reportes:** `aplicaciones_laborales/scripts/scoring_report_generator.py`
- **Tests:** `aplicaciones_laborales/scripts/test_scoring_engine.py`

**Automatización (Nuevo):**
- **Creación de Issues:** `aplicaciones_laborales/scripts/create_issue_and_add_to_project.py`
- **Copia de PDFs:** `aplicaciones_laborales/scripts/copy_pdf_to_documents_repo.py`
- **Workflow:** `.github/workflows/crear_aplicacion.yml`

### 📈 Roadmap Futuro

- **Fase 6:** ⭐ **Automatización de Gestión con Issues y Proyectos** (COMPLETADO ✅)
  - Creación automática de issues para cada aplicación
  - Integración con GitHub Projects
  - Trazabilidad completa del flujo
- **Fase 7:** ⭐ **Copia Automática de CV PDFs a todos-mis-documentos** (COMPLETADO ✅)
  - Organización por fecha (YYYY-MM-DD)
  - Commits descriptivos y auditables
  - Integración en el flujo CI/CD
- **Fase 8:** Análisis semántico avanzado con embeddings (opcional)
- **Fase 9:** Feedback loop y calibración automática de pesos
- **Fase 10:** Dashboard de métricas y tracking de aplicaciones
- **Fase 11:** Integración con APIs externas para benchmarking

---

Para más detalles, consulta la documentación completa en los archivos mencionados arriba.
