from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mentorship/home.html')

def about(request):
    return render(request, 'mentorship/about.html')

# def mentor(request):
#     return render(request, 'mentorship/mentor.html')

def mentee(request):
    return render(request, 'mentorship/mentee.html')

from django.shortcuts import render

def mentor(request):
    academic_sessions = [
        {"number": "Session 1", "title": "Introduction & Mentor-Mentee Relationship", "material_url": "/static/mentorship_materials/academic_track/session1.pdf"},
        {"number": "Session 2", "title": "Setting SMART Goals", "material_url": "/static/mentorship_materials/academic_track/session2.pdf"},
        {"number": "Session 3", "title": "Time Management", "material_url": "/static/mentorship_materials/academic_track/session3.pdf"},
        {"number": "Session 4", "title": "Academic and Extracurricular Activities", "material_url": "/static/mentorship_materials/academic_track/session4.pdf"},
        {"number": "Session 5", "title": "Develop a Career Plan", "material_url": "/static/mentorship_materials/academic_track/session5.pdf"},
        {"number": "Session 6", "title": "Leadership Development and Personal Growth", "material_url": "/static/mentorship_materials/academic_track/session6.pdf"},
    ]

    professional_sessions = [
        {"number": "Session 1", "title": "Introduction & Career Planning", "material_url": "/static/mentorship_materials/professional_track/session1.pdf"},
        {"number": "Session 2", "title": "Job Search Strategies", "material_url": "/static/mentorship_materials/professional_track/session2.pdf"},
        {"number": "Session 3", "title": "Networking", "material_url": "/static/mentorship_materials/professional_track/session3.pdf"},
        {"number": "Session 4", "title": "Interview Part 1", "material_url": "/static/mentorship_materials/professional_track/session4.pdf"},
        {"number": "Session 5", "title": "Interview Part 2", "material_url": "/static/mentorship_materials/professional_track/session5.pdf"},
        {"number": "Session 6", "title": "Enhancing Professional Skills", "material_url": "/static/mentorship_materials/professional_track/session6.pdf"},
    ]

    return render(request, 'mentorship/mentor.html', {
        'academic_sessions': academic_sessions,
        'professional_sessions': professional_sessions,
    })
