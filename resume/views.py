from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile


def create_resume(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        linkedin = request.POST.get('linkedin')
        phone_number = request.POST.get('phone')
        profile = request.POST.get('profile')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        objective = request.POST.get('objective')

        resume = Resume.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            education=education,
            profile=profile,
            skills=skills,
            linkedin=linkedin,
            objective=objective
        )

        return redirect('resume_detail', id=resume.id)

    return render(request, 'resume_add.html')


def resume_detail(request, id):
    resume = get_object_or_404(Resume, id=id)
    return render(request, 'resume_detail.html', {'resume': resume})

def download_pdf(request, id):
    resume = get_object_or_404(Resume, id=id)
    html_string = render_to_string('resume_pdf.html', {'resume': resume})
    html = HTML(string=html_string)
    result = html.write_pdf()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=resume_{resume.id}.pdf'

    response.write(result)
    return response