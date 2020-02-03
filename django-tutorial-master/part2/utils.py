from django.contrib.auth.models import User, Group


def count_users():
    return User.objects.count()


def count_groups():
    return Group.objects.count()


def has_perms_to_users(request):
    return request.user.is_authenticated and request.user.is_superuser
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None