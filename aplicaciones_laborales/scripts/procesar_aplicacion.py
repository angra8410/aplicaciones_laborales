import os
import sys
import shutil
import yaml
import subprocess
from datetime import datetime

# Import the enhanced personalization engine and scoring system
from cv_personalization_engine import CVPersonalizationEngine
from scoring_engine import AdvancedScoringEngine
from scoring_report_generator import ScoringReportGenerator

def sanitize_filename(s):
    return "".join(c for c in s if c.isalnum() or c in (' ', '_', '-')).replace(" ", "")

def generar_job_alignment(requerimientos):
    """
    Generate intelligent job alignment using the personalization engine
    """
    engine = CVPersonalizationEngine()
    return engine.generar_job_alignment_inteligente(requerimientos)

def generar_professional_summary(cargo, requerimientos):
    """
    Generate personalized professional summary
    """
    engine = CVPersonalizationEngine()
    return engine.generar_professional_summary_personalizado(cargo, requerimientos)

def main(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    cargo = sanitize_filename(data['cargo'])
    empresa = sanitize_filename(data['empresa'])
    fecha = data['fecha']
    
    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    
    folder_name = f"{cargo}_{empresa}_{fecha}"

    # Output directory in to_process_procesados
    output_dir = os.path.join("to_process_procesados", folder_name)
    os.makedirs(output_dir, exist_ok=True)

    # descripcion.md
    with open(os.path.join(output_dir, "descripcion.md"), "w", encoding="utf-8") as f:
        f.write(f"# Descripción del Puesto\n\n**Cargo:** {data['cargo']}\n**Empresa:** {data['empresa']}\n**Fecha de aplicación:** {fecha}\n\n## Descripción\n\n{data['descripcion']}\n")

    # requerimientos.md
    with open(os.path.join(output_dir, "requerimientos.md"), "w", encoding="utf-8") as f:
        f.write(f"# Requerimientos del Puesto\n\n")
        for req in data.get('requerimientos', []):
            f.write(f"- {req}\n")

    # hoja_de_vida_adecuada.md (Harvard template con job_alignment_section)
    harvard_cv_path = "aplicaciones_laborales/plantillas/hoja_de_vida_harvard_template.md"
    dest_adaptada_cv = os.path.join(output_dir, "hoja_de_vida_adecuada.md")
    if os.path.exists(harvard_cv_path):
        with open(harvard_cv_path, "r", encoding="utf-8") as src, open(dest_adaptada_cv, "w", encoding="utf-8") as dst:
            content = src.read()
            content = content.replace("{Cargo}", data['cargo']).replace("{Empresa}", data['empresa'])
            
            # Generate intelligent job alignment
            job_alignment_section = generar_job_alignment(data.get('requerimientos', []))
            content = content.replace("{job_alignment_section}", job_alignment_section)
            
            # Generate personalized professional summary
            personalized_summary = generar_professional_summary(data['cargo'], data.get('requerimientos', []))
            # Replace the static summary with personalized one
            # Find and replace the Professional Summary section
            import re
            summary_pattern = r'## Professional Summary\n\n.*?(?=\n---)'
            replacement_summary = f"## Professional Summary\n\n{personalized_summary}"
            content = re.sub(summary_pattern, replacement_summary, content, flags=re.DOTALL)
            
            content = content.replace("{Nombre Completo}", "Antonio Gutierrez Amaranto")  # Personaliza si lo deseas
            dst.write(content)
    else:
        with open(dest_adaptada_cv, "w", encoding="utf-8") as f:
            f.write(f"# Hoja de Vida Adaptada para {data['cargo']} en {data['empresa']}\n")

    # Generate scoring report
    print("Generating scoring report...")
    scoring_engine = AdvancedScoringEngine()
    scoring_result = scoring_engine.calculate_comprehensive_score(
        requirements=data.get('requerimientos', []),
        job_description=data.get('descripcion', ''),
        job_title=data['cargo']
    )
    
    # Generate scoring report markdown
    report_generator = ScoringReportGenerator()
    scoring_report = report_generator.generate_report(
        scoring_result,
        data['cargo'],
        data['empresa'],
        fecha
    )
    
    # Save scoring report
    scoring_report_path = os.path.join(output_dir, "scoring_report.md")
    with open(scoring_report_path, "w", encoding="utf-8") as f:
        f.write(scoring_report)
    
    print(f"Scoring Report Generated:")
    print(f"  - Global Score: {scoring_result['global_score']}%")
    print(f"  - Recommendation: {scoring_result['recommendation_level']}")
    print(f"  - Report saved to: {scoring_report_path}")
    
    # Convertir a PDF usando pandoc con formato profesional
    # Add timestamp to ensure unique filenames and avoid add/add conflicts
    pdf_filename = f"ANTONIO_GUTIERREZ_RESUME_{empresa}_{fecha}_{timestamp}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    # Get the path to the LaTeX header template
    header_path = "aplicaciones_laborales/plantillas/cv_header.tex"
    
    try:
        pandoc_args = [
            "pandoc",
            dest_adaptada_cv,
            "-o", pdf_path,
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=0.75in",
            "-V", "fontsize=11pt",
            "-V", "colorlinks=true",
            "-V", "linkcolor=black",
            "-V", "urlcolor=black",
            "-V", "toccolor=black",
        ]
        
        # Add header include if it exists
        if os.path.exists(header_path):
            pandoc_args.extend(["-H", header_path])
        
        subprocess.run(pandoc_args, check=True)
        print(f"CV PDF generated successfully: {pdf_path}")
    except Exception as e:
        print(f"Error al convertir a PDF con pandoc: {e}")
    
    # Convert scoring report to PDF
    # Add timestamp to ensure unique filenames and avoid add/add conflicts
    scoring_pdf_path = os.path.join(output_dir, f"SCORING_REPORT_{fecha}_{timestamp}.pdf")
    try:
        # Create a cleaned version of the scoring report without emojis for PDF
        with open(scoring_report_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove common emojis used in the report
        emoji_replacements = {
            '🟢': '[EXCELLENT]',
            '🟡': '[GOOD]',
            '🔴': '[NEEDS IMPROVEMENT]',
            '🟠': '[WARNING]',
            '✅': '[+]',
            '⚠️': '[!]',
            '❌': '[-]',
            '🎯': '[TARGET]',
            '📊': '[CHART]',
            '█': '#',
            '░': '-',
        }
        
        for emoji, replacement in emoji_replacements.items():
            content = content.replace(emoji, replacement)
        
        # Save cleaned version temporarily
        cleaned_report_path = os.path.join(output_dir, "scoring_report_cleaned.md")
        with open(cleaned_report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate PDF from cleaned version
        subprocess.run(
            ["pandoc", cleaned_report_path, "-o", scoring_pdf_path,
             "--pdf-engine=xelatex",
             "-V", "geometry:margin=0.75in",
             "-V", "fontsize=11pt"],
            check=True
        )
        
        # Remove the temporary cleaned file
        os.remove(cleaned_report_path)
        
        print(f"Scoring Report PDF: {scoring_pdf_path}")
    except Exception as e:
        print(f"Error al convertir scoring report a PDF: {e}")

    # (Opcional) Mover el YAML procesado
    processed_dir = "to_process_procesados"
    os.makedirs(processed_dir, exist_ok=True)
    shutil.move(yaml_path, os.path.join(processed_dir, os.path.basename(yaml_path)))
    
    # Return folder_name for issue creation
    return folder_name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python procesar_aplicacion.py <archivo_yaml>")
        sys.exit(1)
    folder_name = main(sys.argv[1])
    
    # Create GitHub issue and add to project if GITHUB_TOKEN is available
    if os.environ.get('GITHUB_TOKEN'):
        print("\n" + "="*60)
        print("Creating GitHub issue and adding to project...")
        print("="*60)
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            issue_script = os.path.join(script_dir, "create_issue_and_add_to_project.py")
            subprocess.run([sys.executable, issue_script, folder_name], check=True)
        except Exception as e:
            print(f"⚠️  Warning: Could not create issue: {e}")
            print("   The application was processed successfully, but issue creation failed.")
    else:
        print("\nℹ️  Skipping issue creation (GITHUB_TOKEN not available)")
