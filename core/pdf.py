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




