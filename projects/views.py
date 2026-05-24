from django.shortcuts import render


projectsList = [
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "A personal portfolio website to showcase projects, skills, and contact information."
    },
    {
        "id": 2,
        "title": "E-Commerce Store",
        "description": "An online shopping platform with product listings, cart functionality, and payment integration."
    },
    {
        "id": 3,
        "title": "Task Manager App",
        "description": "A productivity application for creating, organizing, and tracking daily tasks."
    },
    {
        "id": 4,
        "title": "Weather Dashboard",
        "description": "A web application that displays current weather conditions and forecasts for different cities."
    },
    {
        "id": 5,
        "title": "Blog Platform",
        "description": "A content management system where users can create, edit, and publish blog posts."
    }
]


def projects(request):
    context = {
        'projects': projectsList
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = None

    for i in projectsList:
        if i['id'] == int(pk):
            projectobj = i

    return render(request, 'projects/single-projects.html', {
        'project': projectobj
    })