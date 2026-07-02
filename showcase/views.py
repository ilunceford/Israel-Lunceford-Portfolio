from django.shortcuts import render

from .forms import ContactForm, ProjectRecommendationForm


PROJECTS = [
    {
        "number": "01",
        "title": "Chess Game",
        "type": "Game",
        "summary": "A chess project focused on board interaction, turn-based logic, and presenting a classic strategy game through a playable software interface.",
        "features": ["Game board structure", "Piece movement logic", "Interactive play experience"],
        "github": "https://github.com/ilunceford/Chess-Game-CSE310",
        "demo": "https://youtu.be/hnBraJea2mY",
        "match": "logic",
    },
    {
        "number": "02",
        "title": "Paint Program",
        "type": "Creative Tool",
        "summary": "A drawing application sprint that emphasizes direct manipulation, visual creation tools, and a responsive workspace for sketching ideas on screen.",
        "features": ["Canvas-style interaction", "Creative user controls", "Visual feedback while drawing"],
        "github": "https://github.com/ilunceford/cse-310-sprint2-paint-program",
        "demo": "https://youtu.be/qaKhNTbw5m4",
        "match": "creative",
    },
    {
        "number": "03",
        "title": "Calculator",
        "type": "Utility App",
        "summary": "A calculator project built around clear controls, dependable input handling, and immediate results for everyday arithmetic workflows.",
        "features": ["Button-based input", "Calculation flow", "Clean utility interface"],
        "github": "https://github.com/ilunceford/cse310-sprint3-calculator",
        "demo": "https://youtu.be/XpUiToTScbg",
        "match": "utility",
    },
    {
        "number": "04",
        "title": "Flash Card Mobile App",
        "type": "Mobile App",
        "summary": "A mobile learning app concept designed around study cards, quick review sessions, and a simple interface for practicing information on the go.",
        "features": ["Study-focused experience", "Mobile app structure", "Flash card review flow"],
        "github": "https://github.com/ilunceford/cse310-sprint4-flash-card-mobile-app",
        "demo": "https://youtu.be/UPJGGu4-4F0",
        "match": "mobile",
    },
]


def home(request):
    recommendation = None

    if request.method == "POST":
        form = ProjectRecommendationForm(request.POST)
        if form.is_valid():
            interest = form.cleaned_data["interest"]
            recommendation = next(project for project in PROJECTS if project["match"] == interest)
    else:
        form = ProjectRecommendationForm()

    return render(
        request,
        "showcase/home.html",
        {"projects": PROJECTS, "form": form, "recommendation": recommendation},
    )


def contact(request):
    submitted_message = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            submitted_message = form.cleaned_data
            form = ContactForm()
    else:
        form = ContactForm()

    return render(
        request,
        "showcase/contact.html",
        {"form": form, "submitted_message": submitted_message},
    )


def report(request):
    completed_requirements = [
        "Generated multiple HTML pages from Django templates: Home, Contact, and Report.",
        "Served CSS and JavaScript files from the app code using Django static files.",
        "Accepted user input through the project recommendation form and contact form.",
        "Performed error checking with Django forms, including required fields, email validation, and minimum message length.",
        "Changed generated HTML based on user input by displaying a matching project recommendation and a contact message preview.",
        "Completed the stretch challenge by adding a third dynamically generated page: the Report page.",
    ]
    incomplete_requirements = [
        "Database integration was not selected because the third dynamic page stretch challenge was completed instead.",
    ]

    return render(
        request,
        "showcase/report.html",
        {
            "completed_requirements": completed_requirements,
            "incomplete_requirements": incomplete_requirements,
        },
    )
