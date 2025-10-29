#!/usr/bin/env python3
"""
Script to copy generated CV PDFs to the todas-mis-aplicaciones repository.
Organizes PDFs by application date in /aplicaciones/YYYY-MM-DD folders.

This script is designed to be called from GitHub Actions after PDF generation.
It clones the target repository, creates date-based folder structure,
copies the PDF, and commits/pushes the changes.

Author: GitHub Actions Bot
"""

import os
import sys
import subprocess
import shutil
from datetime import datetime
from pathlib import Path


def run_command(cmd, cwd=None, capture_output=False):
    """Execute a shell command and handle errors."""
    try:
        if capture_output:
            result = subprocess.run(
                cmd, 
                cwd=cwd, 
                check=True, 
                capture_output=True, 
                text=True
            )
            return result.stdout.strip()
        else:
            subprocess.run(cmd, cwd=cwd, check=True)
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando comando: {' '.join(cmd)}")
        print(f"Error: {e}")
        if capture_output and e.stderr:
            print(f"Stderr: {e.stderr}")
        raise


def extract_date_from_folder_name(folder_name):
    """
    Extract date from folder name format: Cargo_Empresa_YYYY-MM-DD
    
    Args:
        folder_name: String like "DataAnalyst_Adoreal_2025-10-13"
    
    Returns:
        Date string in YYYY-MM-DD format
    """
    parts = folder_name.split('_')
    if len(parts) >= 2:
        # The date should be the last part
        date_str = parts[-1]
        # Validate date format
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print(f"⚠️  Warning: Could not parse date from folder name: {folder_name}")
            # Fallback to today's date
            return datetime.now().strftime('%Y-%m-%d')
    else:
        print(f"⚠️  Warning: Unexpected folder name format: {folder_name}")
        return datetime.now().strftime('%Y-%m-%d')


def copy_pdf_to_documents_repo(pdf_path, application_date, empresa, cargo):
    """
    Copy PDF to todas-mis-aplicaciones repository organized by date.
    
    Args:
        pdf_path: Path to the generated PDF file
        application_date: Date of application in YYYY-MM-DD format
        empresa: Company name (for commit message)
        cargo: Job title (for commit message)
    """
    # Get GitHub token (prefer PAT_APLICACION_LABORAL for cross-repo access)
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("❌ Error: GITHUB_TOKEN not available")
        print("   This script requires GITHUB_TOKEN (or PAT_APLICACION_LABORAL) to push to todas-mis-aplicaciones")
        print("   For private repos, configure PAT_APLICACION_LABORAL secret with 'repo' permissions")
        return False
    
    # Configuration
    target_repo = "angra8410/todas-mis-aplicaciones"
    target_repo_url = f"https://x-access-token:{github_token}@github.com/{target_repo}.git"
    
    # Create temporary directory for cloning
    temp_dir = "/tmp/todas-mis-aplicaciones-clone"
    
    # Clean up if directory exists
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    
    print("\n" + "="*60)
    print("📂 Copiando PDF al repositorio todas-mis-aplicaciones")
    print("="*60)
    print(f"📍 Repositorio destino: {target_repo}")
    print(f"📅 Fecha de aplicación: {application_date}")
    print(f"🏢 Empresa: {empresa}")
    print(f"💼 Cargo: {cargo}")
    print("="*60)
    
    try:
        # Clone the target repository
        print(f"\n📥 Clonando repositorio {target_repo}...")
        print(f"🔍 Intentando clonar con credenciales proporcionadas...")
        try:
            run_command([
                "git", "clone", 
                "--depth=1",  # Shallow clone for efficiency
                target_repo_url, 
                temp_dir
            ])
            print(f"✅ Repositorio clonado exitosamente")
        except subprocess.CalledProcessError as e:
            # Check if it's a "repository not found" error
            print("\n" + "="*60)
            print("❌ ERROR: No se pudo clonar el repositorio destino")
            print("="*60)
            print(f"\nRepositorio: {target_repo}")
            print(f"Error: El repositorio no existe o no es accesible con el token proporcionado")
            print("\n🔍 DIAGNÓSTICO:")
            print("   Este error ocurre cuando:")
            print("   1. El repositorio no existe (poco probable según evidencia)")
            print("   2. El repositorio es PRIVADO y el token no tiene permisos")
            print("   3. El token usado es GITHUB_TOKEN en lugar de PAT_APLICACION_LABORAL")
            print("\n📋 SOLUCIÓN PARA REPOSITORIOS PRIVADOS:")
            print("   El GITHUB_TOKEN por defecto NO puede acceder a otros repos privados.")
            print("   Debes configurar un Personal Access Token (PAT):")
            print("")
            print("   Paso 1: Crear PAT")
            print("   ├─ Ve a: https://github.com/settings/tokens/new")
            print("   ├─ Token name: 'CI/CD PDF Copy'")
            print("   ├─ Expiration: 90 días (o sin expiración si prefieres)")
            print("   ├─ Scopes: Marca ☑️  'repo' (Full control of private repositories)")
            print("   └─ Click 'Generate token' y COPIA el token (solo se muestra una vez)")
            print("")
            print("   Paso 2: Configurar Secret en GitHub")
            print(f"   ├─ Ve a: https://github.com/angra8410/aplicaciones_laborales/settings/secrets/actions")
            print("   ├─ Click 'New repository secret'")
            print("   ├─ Name: PAT_APLICACION_LABORAL")
            print("   ├─ Secret: Pega el token que copiaste en Paso 1")
            print("   └─ Click 'Add secret'")
            print("")
            print("   Paso 3: Verificar permisos en todas-mis-aplicaciones")
            print(f"   ├─ Ve a: https://github.com/{target_repo}/settings/actions")
            print("   ├─ En 'Workflow permissions', selecciona:")
            print("   └─ ☑️  'Read and write permissions'")
            print("")
            print("   Paso 4: Re-ejecutar el workflow")
            print("   └─ El workflow automáticamente usará PAT_APLICACION_LABORAL si está configurado")
            print("\n📖 Documentación completa: Ver SETUP_REQUIRED.md en este repositorio")
            print("="*60 + "\n")
            raise
        
        # Create aplicaciones folder if it doesn't exist
        aplicaciones_folder = os.path.join(temp_dir, "aplicaciones")
        os.makedirs(aplicaciones_folder, exist_ok=True)
        print(f"📁 Carpeta base creada/verificada: aplicaciones/")
        
        # Create date-based folder structure inside aplicaciones/
        date_folder = os.path.join(aplicaciones_folder, application_date)
        os.makedirs(date_folder, exist_ok=True)
        print(f"📁 Carpeta por fecha creada/verificada: aplicaciones/{application_date}/")
        
        # Copy PDF to the date folder
        pdf_filename = os.path.basename(pdf_path)
        dest_pdf_path = os.path.join(date_folder, pdf_filename)
        
        # Check if file already exists
        if os.path.exists(dest_pdf_path):
            print(f"⚠️  El archivo {pdf_filename} ya existe en aplicaciones/{application_date}/")
            print(f"   Sobrescribiendo con la nueva versión...")
        
        shutil.copy2(pdf_path, dest_pdf_path)
        print(f"✅ PDF copiado: aplicaciones/{application_date}/{pdf_filename}")
        
        # Configure git in the cloned repo
        run_command([
            "git", "config", "user.email", 
            "github-actions[bot]@users.noreply.github.com"
        ], cwd=temp_dir)
        
        run_command([
            "git", "config", "user.name", 
            "github-actions[bot]"
        ], cwd=temp_dir)
        
        # Add the PDF file
        run_command(["git", "add", dest_pdf_path], cwd=temp_dir)
        
        # Check if there are changes to commit
        status_output = run_command(
            ["git", "status", "--porcelain"],
            cwd=temp_dir,
            capture_output=True
        )
        
        if not status_output:
            print("ℹ️  No hay cambios para commitear (archivo idéntico ya existe)")
            return True
        
        # Commit the changes
        commit_message = f"📄 CV generado: {cargo} - {empresa} ({application_date})"
        run_command([
            "git", "commit", "-m", commit_message
        ], cwd=temp_dir)
        print(f"💾 Commit creado: {commit_message}")
        
        # Push to remote
        print("🚀 Enviando cambios al repositorio remoto...")
        run_command(["git", "push"], cwd=temp_dir)
        print("✅ PDF copiado exitosamente al repositorio todas-mis-aplicaciones")
        
        # Print summary
        print("\n" + "="*60)
        print("📊 Resumen de la operación:")
        print("="*60)
        print(f"   Repositorio destino: {target_repo}")
        print(f"   Carpeta: aplicaciones/{application_date}/")
        print(f"   Archivo: {pdf_filename}")
        print(f"   Empresa: {empresa}")
        print(f"   Cargo: {cargo}")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al copiar PDF al repositorio: {e}")
        return False
    
    finally:
        # Clean up temporary directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print("🧹 Limpieza: directorio temporal eliminado")


def main():
    """Main function to process command line arguments and copy PDF."""
    if len(sys.argv) != 2:
        print("Uso: python copy_pdf_to_documents_repo.py <folder_name>")
        print("Ejemplo: python copy_pdf_to_documents_repo.py DataAnalyst_Adoreal_2025-10-13")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    
    # Extract date from folder name
    application_date = extract_date_from_folder_name(folder_name)
    
    # Parse folder name to extract empresa and cargo
    parts = folder_name.split('_')
    if len(parts) >= 2:
        # Remove date from parts
        cargo = parts[0]
        empresa = '_'.join(parts[1:-1])  # Handle multi-part company names
    else:
        cargo = "Unknown"
        empresa = "Unknown"
    
    # Find the PDF file
    output_dir = os.path.join("to_process_procesados", folder_name)
    
    if not os.path.exists(output_dir):
        print(f"❌ Error: Carpeta no encontrada: {output_dir}")
        sys.exit(1)
    
    # Look for CV PDF (not scoring report)
    # Updated to support timestamped filenames: ANTONIO_GUTIERREZ_RESUME_{empresa}_{fecha}_{timestamp}.pdf
    pdf_files = [f for f in os.listdir(output_dir) 
                 if f.startswith("ANTONIO_GUTIERREZ_RESUME_") and f.endswith(".pdf") and "SCORING_REPORT" not in f]
    
    if not pdf_files:
        print(f"❌ Error: No se encontró PDF del CV en {output_dir}")
        sys.exit(1)
    
    pdf_path = os.path.join(output_dir, pdf_files[0])
    
    if not os.path.exists(pdf_path):
        print(f"❌ Error: Archivo PDF no encontrado: {pdf_path}")
        sys.exit(1)
    
    print(f"📄 PDF encontrado: {pdf_path}")
    
    # Copy PDF to documents repository
    success = copy_pdf_to_documents_repo(pdf_path, application_date, empresa, cargo)
    
    if success:
        print("✅ Proceso completado exitosamente")
        sys.exit(0)
    else:
        print("❌ Proceso falló")
        sys.exit(1)


if __name__ == "__main__":
    main()
