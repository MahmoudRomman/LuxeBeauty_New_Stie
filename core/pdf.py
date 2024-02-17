from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa



def html2pdf_order_summary(template_source, context_dict={}):
    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result 
    else:
        print("Error generating PDF")
        return None







from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.utils import timezone
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf_and_save_to_model(template_name, context, model_instance):
    # Render HTML template to PDF
    template = get_template(template_name)
    html_content = template.render(context)
    pdf_content = BytesIO()
    pisa.pisaDocument(BytesIO(html_content.encode("UTF-8")), pdf_content)

    # Check if the model instance already has a file
    if model_instance.pdf_file:
        # If a file exists, update its content
        file_path = model_instance.pdf_file.path
        with default_storage.open(file_path, 'wb') as f:
            f.write(pdf_content.getvalue())
    else:
        # If no file exists, create a new instance and save the PDF content
        filename = f'{timezone.now().strftime("%Y-%m-%d_%H-%M-%S")}_Repo.pdf'
        file_content = ContentFile(pdf_content.getvalue())
        model_instance.pdf_file.save(filename, file_content)

    # Optionally, you can save other fields of the model instance if needed
    model_instance.save()
