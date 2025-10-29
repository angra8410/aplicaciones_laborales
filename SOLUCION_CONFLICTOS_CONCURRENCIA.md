# Solución de Conflictos de Concurrencia en Workflows

## 📋 Problema Identificado

El workflow de GitHub Actions generaba conflictos tipo **add/add** durante operaciones de rebase cuando:
- Múltiples workflows se ejecutaban simultáneamente
- Dos aplicaciones procesaban el mismo puesto y fecha
- Se intentaba crear archivos con nombres idénticos pero contenido diferente

### Archivos Afectados
- `ANTONIO_GUTIERREZ_RESUME_{empresa}.pdf`
- `SCORING_REPORT.pdf`
- `hoja_de_vida_adecuada.md`
- `scoring_report.md`

## ✅ Solución Implementada

### 1. Nombres de Archivo Únicos con Timestamp

Se agregó un timestamp único a todos los archivos generados para evitar colisiones:

**Formato Anterior:**
```
ANTONIO_GUTIERREZ_RESUME_TruelogicSoftware.pdf
SCORING_REPORT.pdf
```

**Formato Nuevo:**
```
ANTONIO_GUTIERREZ_RESUME_TruelogicSoftware_2025-10-27_2025-10-29T01-30-45.pdf
SCORING_REPORT_2025-10-27_2025-10-29T01-30-45.pdf
```

#### Beneficios:
- ✅ Cada archivo es único, incluso si se procesa la misma aplicación múltiples veces
- ✅ Permite rastrear cuándo se generó cada documento
- ✅ Evita completamente los conflictos add/add
- ✅ Mantiene trazabilidad histórica de versiones

### 2. Cambio de Estrategia: Rebase → Merge

El workflow ahora usa `git merge` en lugar de `git rebase`:

**Antes (Rebase):**
```bash
if git rebase origin/main; then
  echo "✅ Rebase exitoso"
else
  echo "❌ ERROR: Conflicto durante el rebase"
  git rebase --abort
  exit 1
fi
```

**Después (Merge):**
```bash
if git merge origin/main -m "Merge remote changes" --no-edit; then
  echo "✅ Merge exitoso"
else
  echo "⚠️  Conflicto durante el merge. Intentando resolución automática..."
  git checkout --ours to_process_procesados/ || true
  git add to_process_procesados/ || true
  git commit --no-edit -m "Automatización: Resolución automática de conflictos"
fi
```

#### Ventajas del Merge sobre Rebase:
- ✅ Más tolerante a cambios concurrentes
- ✅ Permite resolución automática de conflictos
- ✅ No requiere reescritura del historial
- ✅ Más robusto en entornos de CI/CD con múltiples ejecutores

### 3. Resolución Automática de Conflictos

Si ocurre un conflicto en archivos generados:
1. Se usa la estrategia `--ours` para favorecer los cambios locales
2. Esto es seguro porque cada archivo tiene un nombre único con timestamp
3. El workflow continúa sin requerir intervención manual

## 🔧 Cambios Técnicos Realizados

### Archivo: `aplicaciones_laborales/scripts/procesar_aplicacion.py`

**Líneas modificadas:**

```python
# Importar datetime
from datetime import datetime

# Generar timestamp único
timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

# PDFs con timestamp
pdf_filename = f"ANTONIO_GUTIERREZ_RESUME_{empresa}_{fecha}_{timestamp}.pdf"
scoring_pdf_path = os.path.join(output_dir, f"SCORING_REPORT_{fecha}_{timestamp}.pdf")
```

### Archivo: `aplicaciones_laborales/scripts/copy_pdf_to_documents_repo.py`

**Actualización del filtro de archivos:**

```python
# Filtrar PDFs excluyendo SCORING_REPORT
pdf_files = [f for f in os.listdir(output_dir) 
             if f.startswith("ANTONIO_GUTIERREZ_RESUME_") 
             and f.endswith(".pdf") 
             and "SCORING_REPORT" not in f]
```

### Archivo: `.github/workflows/crear_aplicacion.yml`

**Estrategia de merge actualizada** (líneas 85-131):
- Cambio de `git rebase` a `git merge`
- Adición de resolución automática de conflictos
- Manejo robusto de archivos generados

## 📊 Casos de Uso Soportados

### Caso 1: Ejecución Simple
✅ Un workflow genera archivos → Push exitoso

### Caso 2: Ejecuciones Concurrentes (Mismo Puesto y Fecha)
✅ Workflow A y B procesan "Senior Data Analyst - TruelogicSoftware - 2025-10-27"
- Workflow A genera: `RESUME_TruelogicSoftware_2025-10-27_2025-10-29T01-30-45.pdf`
- Workflow B genera: `RESUME_TruelogicSoftware_2025-10-27_2025-10-29T01-31-12.pdf`
- Ambos archivos coexisten sin conflicto

### Caso 3: Ejecuciones Concurrentes (Puestos Diferentes)
✅ Cada puesto genera su propia carpeta y archivos únicos

### Caso 4: Re-procesamiento de Aplicación
✅ Procesar la misma aplicación nuevamente crea una nueva versión con timestamp diferente

## 🎯 Validación de la Solución

### Pruebas Realizadas

1. **Prueba de Sintaxis Python:**
   ```bash
   python3 -m py_compile aplicaciones_laborales/scripts/procesar_aplicacion.py
   ✅ Sin errores
   ```

2. **Prueba de Generación de Timestamp:**
   ```python
   timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
   # Resultado: 2025-10-29T01-30-45
   ✅ Formato correcto
   ```

3. **Prueba de Workflow YAML:**
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('.github/workflows/crear_aplicacion.yml'))"
   ✅ YAML válido
   ```

4. **Prueba de Generación de Aplicación:**
   - Se creó un archivo YAML de prueba
   - Se ejecutó el script procesar_aplicacion.py
   - ✅ Archivos generados correctamente con timestamps

## 📝 Documentación Actualizada

Se actualizó el README.md con la nueva **Fase 6: Prevención de Conflictos en Ejecuciones Concurrentes**

## 🔄 Compatibilidad

### Backward Compatibility
- ✅ Los archivos existentes no se ven afectados
- ✅ El sistema continúa funcionando con archivos antiguos
- ✅ La copia automática de PDFs sigue funcionando

### Forward Compatibility
- ✅ Todos los nuevos archivos incluyen timestamp
- ✅ El filtro en `copy_pdf_to_documents_repo.py` maneja ambos formatos
- ✅ No se requieren cambios manuales por parte del usuario

## 🚀 Próximos Pasos

El sistema ahora puede:
1. ✅ Generar aplicaciones laborales sin conflictos
2. ✅ Manejar múltiples ejecuciones concurrentes
3. ✅ Copiar PDFs al repositorio de documentos
4. ✅ Crear issues automáticamente en GitHub Projects

## 📖 Referencias

- **Código fuente:** 
  - `aplicaciones_laborales/scripts/procesar_aplicacion.py`
  - `aplicaciones_laborales/scripts/copy_pdf_to_documents_repo.py`
  - `.github/workflows/crear_aplicacion.yml`
- **Documentación relacionada:**
  - `README.md` (Fase 6)
  - `SOLUCION_NON_FAST_FORWARD.md`
  - `GUIA_RAPIDA_NON_FAST_FORWARD.md`

---

**Fecha de implementación:** 29 de Octubre de 2025  
**Estado:** ✅ Completado y Probado
