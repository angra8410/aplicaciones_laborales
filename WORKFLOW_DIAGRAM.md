# 🔄 Diagrama de Flujo: Automatización Completa

## Flujo de Trabajo End-to-End

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     USUARIO CREA APLICACIÓN                              │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
                   ┌──────────────────────────┐
                   │  to_process/             │
                   │  nueva_aplicacion.yaml   │
                   │                          │
                   │  cargo: "Data Analyst"   │
                   │  empresa: "TechCorp"     │
                   │  fecha: "2025-10-15"     │
                   └────────────┬─────────────┘
                                │
                                │ git push
                                ▼
          ┌─────────────────────────────────────────┐
          │   GitHub Actions Workflow Triggered     │
          │   (.github/workflows/crear_aplicacion)  │
          └──────────────────┬──────────────────────┘
                             │
          ┌──────────────────┴─────────────────┐
          │                                     │
          ▼                                     ▼
┌──────────────────┐                  ┌─────────────────────┐
│ Setup            │                  │ Install Tools       │
│ - Checkout       │                  │ - Python 3.11       │
│ - Config Git     │                  │ - Pandoc            │
└────────┬─────────┘                  │ - LaTeX/XeTeX       │
         │                            └──────────┬──────────┘
         │                                       │
         └───────────────────┬───────────────────┘
                             │
                             ▼
            ┌─────────────────────────────────────┐
            │  PASO 1: Procesar Aplicación        │
            │  (procesar_aplicacion.py)           │
            └─────────────────┬───────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Genera       │  │ Personaliza  │  │ Crea Scoring │
    │ Carpeta      │  │ CV con       │  │ Report       │
    │ en           │  │ Motor AI     │  │              │
    │ to_process_  │  │              │  │              │
    │ procesados/  │  │              │  │              │
    └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
           │                 │                 │
           └────────┬────────┴─────────┬───────┘
                    │                  │
                    ▼                  ▼
        ┌────────────────────┐  ┌─────────────────┐
        │ ANTONIO_GUTIERREZ_ │  │ SCORING_REPORT  │
        │ RESUME_TechCorp.pdf│  │ .pdf            │
        └────────────────────┘  └─────────────────┘
                    │
                    ▼
            ┌──────────────────────────────────┐
            │  PASO 2: Crear Issue             │
            │  (create_issue_and_add_to_       │
            │   project.py)                    │
            └─────────────────┬────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Crea Issue   │  │ Añade Labels │  │ Agrega a     │
    │ en GitHub    │  │ - aplicacion │  │ Proyecto     │
    │              │  │   -procesada │  │ "aplicacion  │
    │ Título:      │  │ - Aplicados  │  │  -estados"   │
    │ "Aplicación: │  │              │  │              │
    │  Data Analyst│  │              │  │              │
    │  en TechCorp"│  │              │  │              │
    └──────────────┘  └──────────────┘  └──────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────┐
            │  ⭐ PASO 3: Copiar PDF               │
            │  ⭐ (copy_pdf_to_documents_repo.py)  │
            │  ⭐ NUEVA FUNCIONALIDAD              │
            └─────────────────┬───────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Clone Repo   │  │ Crea Carpeta │  │ Copia PDF    │
    │ todos-mis-   │  │ 2025-10-15/  │  │ a Carpeta    │
    │ documentos   │  │ (si no       │  │              │
    │ (temporal)   │  │  existe)     │  │              │
    └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
           │                 │                 │
           └────────┬────────┴─────────┬───────┘
                    │                  │
                    ▼                  ▼
        ┌────────────────────┐  ┌─────────────────────┐
        │ Git Commit         │  │ Git Push            │
        │ "📄 CV generado:   │  │ to todos-mis-       │
        │  DataAnalyst -     │  │ documentos          │
        │  TechCorp          │  │                     │
        │  (2025-10-15)"     │  │                     │
        └────────────────────┘  └─────────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────┐
            │  PASO 4: Commit Local               │
            │  (en aplicaciones_laborales)        │
            └─────────────────┬───────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────┐
            │  Git commit y push                  │
            │  "Automatización: Nueva aplicación  │
            │   laboral creada por workflow"      │
            └─────────────────┬───────────────────┘
                              │
                              ▼
          ┌───────────────────────────────────────────┐
          │         ✅ PROCESO COMPLETO                │
          └───────────────────┬───────────────────────┘
                              │
                              │
          ┌───────────────────┼──────────────────┐
          │                   │                  │
          ▼                   ▼                  ▼
┌────────────────────┐  ┌───────────────┐  ┌─────────────────┐
│ aplicaciones_      │  │ Issue creada  │  │ todos-mis-      │
│ laborales/         │  │ en GitHub     │  │ documentos/     │
│                    │  │               │  │                 │
│ to_process_        │  │ #42           │  │ 2025-10-15/     │
│ procesados/        │  │ "Aplicación:  │  │ ANTONIO_        │
│ DataAnalyst_       │  │  Data Analyst │  │ GUTIERREZ_      │
│ TechCorp_          │  │  en TechCorp" │  │ RESUME_         │
│ 2025-10-15/        │  │               │  │ TechCorp.pdf    │
│ ├── CV.pdf         │  │ Project:      │  │                 │
│ ├── SCORING.pdf    │  │ aplicacion-   │  │ Commit:         │
│ └── ...            │  │ estados       │  │ "📄 CV gener..."│
└────────────────────┘  └───────────────┘  └─────────────────┘
```

## Resumen del Flujo

1. **Usuario:** Crea archivo YAML y hace push
2. **GitHub Actions:** Detecta cambio y ejecuta workflow
3. **Procesamiento:** Genera CV personalizado y scoring report
4. **Issue Creation:** Crea issue y la agrega al proyecto
5. **⭐ PDF Copy:** Copia PDF a `todos-mis-documentos` organizado por fecha
6. **Commit:** Guarda cambios en ambos repositorios

## Ventajas del Flujo

- ✅ **Automatización Completa:** Sin intervención manual
- ✅ **Trazabilidad Total:** Cada paso registrado
- ✅ **Organización:** CVs ordenados por fecha
- ✅ **Respaldo:** PDF en 2 repositorios
- ✅ **Gestión:** Issue tracking automático
- ✅ **Auditable:** Commits descriptivos en ambos repos

## Tiempos de Ejecución

- Procesamiento de aplicación: ~30-45 segundos
- Creación de issue: ~5-10 segundos
- Copia de PDF: ~10-15 segundos
- **Total:** ~1-2 minutos por aplicación

## Recursos Utilizados

- **GitHub Actions:** ~2 minutos de compute time
- **Storage:** Mínimo (solo PDFs, ~100-200KB cada uno)
- **API Calls:** ~5-8 por aplicación (GitHub REST + GraphQL)
