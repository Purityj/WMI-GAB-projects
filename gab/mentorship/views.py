from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'mentorship/home.html')

def about(request):
    return render(request, 'mentorship/about.html')


def mentee(request):
    return render(request, 'mentorship/mentee.html')

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


def analytics(request):
    # Demographic Data
    demographics_data = [
        {"country": "Kenya", "mentors": 4, "mentees": 3, "total": 7, "lat": -1.286389, "lng": 36.817223},
        {"country": "Uganda", "mentors": 8, "mentees": 5, "total": 13, "lat": 0.313611, "lng": 32.581111},
        {"country": "Ghana", "mentors": 3, "mentees": 5, "total": 8, "lat": 5.6037, "lng": -0.1869},
        {"country": "Nigeria", "mentors": 3, "mentees": 13, "total": 16, "lat": 9.082, "lng": 8.6753},
        {"country": "Sierra Leone", "mentors": 4, "mentees": 3, "total": 7, "lat": 8.4606, "lng": -11.7799},
        {"country": "Rwanda", "mentors": 3, "mentees": 1, "total": 4, "lat": -1.9403, "lng": 29.8739},
        {"country": "Zambia", "mentors": 3, "mentees": 3, "total": 6, "lat": -15.4167, "lng": 28.2833},
        {"country": "Zimbabwe", "mentors": 1, "mentees": 4, "total": 5, "lat": -17.8252, "lng": 31.0335},
        {"country": "Nepal", "mentors": 0, "mentees": 3, "total": 3, "lat": 28.3949, "lng": 84.1240},
        {"country": "Gambia", "mentors": 1, "mentees": 0, "total": 1, "lat": 13.4432, "lng": -15.3101},
        {"country": "Cameroon", "mentors": 1, "mentees": 1, "total": 2, "lat": 3.8480, "lng": 11.5021},
        {"country": "South Sudan", "mentors": 1, "mentees": 2, "total": 3, "lat": 6.8770, "lng": 31.3070},
        {"country": "Pakistan", "mentors": 0, "mentees": 1, "total": 1, "lat": 30.3753, "lng": 69.3451},
        {"country": "Yemen", "mentors": 0, "mentees": 1, "total": 1, "lat": 15.5527, "lng": 48.5164},
        {"country": "Liberia", "mentors": 1, "mentees": 1, "total": 2, "lat": 6.4281, "lng": -9.4295},
        {"country": "Myanmar", "mentors": 0, "mentees": 1, "total": 1, "lat": 21.9162, "lng": 95.9560},
        {"country": "Bangladesh", "mentors": 0, "mentees": 1, "total": 1, "lat": 23.6850, "lng": 90.3563},
        {"country": "Mozambique", "mentors": 0, "mentees": 1, "total": 1, "lat": -25.9653, "lng": 32.5892},
        {"country": "Jamaica", "mentors": 1, "mentees": 0, "total": 1, "lat": 18.1096, "lng": -77.2975},
        {"country": "Venezuela", "mentors": 0, "mentees": 1, "total": 1, "lat": 6.4238, "lng": -66.5897},
        {"country": "South Africa", "mentors": 1, "mentees": 0, "total": 1, "lat": -30.5595, "lng": 22.9375},
    ]

    return render(request, 'mentorship/analytics.html', {'demographics_data': demographics_data})

def demographics_data_api(request):
    # Return demographics data as JSON
    demographics_data = [
        {"country": "Kenya", "mentors": 4, "mentees": 3, "lat": -1.286389, "lng": 36.817223},
        {"country": "Uganda", "mentors": 8, "mentees": 5, "lat": 0.313611, "lng": 32.581111},
        {"country": "Ghana", "mentors": 4, "mentees": 5, "lat": 5.6037, "lng": -0.1869},
        {"country": "Nigeria", "mentors": 3, "mentees": 13, "lat": 9.082, "lng": 8.6753},
        {"country": "Sierra Leone", "mentors": 4, "mentees": 4, "lat": 8.4606, "lng": -11.7799},
        {"country": "Rwanda", "mentors": 3, "mentees": 1, "lat": -1.9403, "lng": 29.8739},
        {"country": "Zambia", "mentors": 3, "mentees": 2, "lat": -15.4167, "lng": 28.2833},
        {"country": "Zimbabwe", "mentors": 4, "mentees": 1, "lat": -17.8252, "lng": 31.0335},
        {"country": "Nepal", "mentors": 2, "mentees": 0, "lat": 28.3949, "lng": 84.1240},
        {"country": "Gambia", "mentors": 1, "mentees": 0, "lat": 13.4432, "lng": -15.3101},
        {"country": "Cameroon", "mentors": 1, "mentees": 1, "lat": 3.8480, "lng": 11.5021},
        {"country": "South Sudan", "mentors": 1, "mentees": 1, "lat": 6.8770, "lng": 31.3070},
        {"country": "Pakistan", "mentors": 0, "mentees": 1, "lat": 30.3753, "lng": 69.3451},
        {"country": "Yemen", "mentors": 0, "mentees": 1, "lat": 15.5527, "lng": 48.5164},
        {"country": "Liberia", "mentors": 1, "mentees": 1, "lat": 6.4281, "lng": -9.4295},
        {"country": "Myanmar", "mentors": 0, "mentees": 1, "lat": 21.9162, "lng": 95.9560},
        {"country": "Bangladesh", "mentors": 0, "mentees": 1, "lat": 23.6850, "lng": 90.3563},
        {"country": "Mozambique", "mentors": 0, "mentees": 1, "lat": -25.9653, "lng": 32.5892},
        {"country": "Jamaica", "mentors": 1, "mentees": 0, "lat": 18.1096, "lng": -77.2975},
        {"country": "Venezuela", "mentors": 0, "mentees": 1, "lat": 6.4238, "lng": -66.5897},
        {"country": "South Africa", "mentors": 1, "mentees": 0, "lat": -30.5595, "lng": 22.9375},
    ]
    return JsonResponse(demographics_data, safe=False)