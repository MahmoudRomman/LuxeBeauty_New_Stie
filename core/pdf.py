# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa



# def html2pdf_order_summary(template_source, context_dict={}):
#     template = get_template(template_source)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return result  # Return BytesIO object containing PDF content
#     else:
#         print("Error generating PDF")
#         return None






# def html2pdf_order_summary(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)

#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

#     if not pdf.err:
#         return result.getvalue()
#     return None





from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa




from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

def html2pdf_order_summary(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
    
    # Specify a font that supports Arabic characters
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8', 
                             link_callback=lambda uri, _: uri, path="C:/Windows/Fonts/GE_SS_Unique_Light.otf")
    if not pdf.err:
        return result.getvalue()
    return None








# def html2pdf_order_summary(template_source, context_dict={}):
#     template = get_template(template_source)
#     html = template.render(context_dict)

#     print(html)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
#     if not pdf.err:
#         return result
#     else:
#         return None
    



