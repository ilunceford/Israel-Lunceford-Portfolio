from django import forms


class ProjectRecommendationForm(forms.Form):
    visitor_name = forms.CharField(
        label="Your name",
        min_length=2,
        max_length=60,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )
    interest = forms.ChoiceField(
        label="What do you want to see?",
        choices=[
            ("", "Choose a project type"),
            ("logic", "Logic and strategy"),
            ("creative", "Creative tools"),
            ("utility", "Everyday utility"),
            ("mobile", "Mobile learning"),
        ],
    )


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", min_length=2, max_length=60)
    email = forms.EmailField(label="Email")
    reason = forms.ChoiceField(
        label="Reason",
        choices=[
            ("", "Choose one"),
            ("Project Opportunity", "Project Opportunity"),
            ("Portfolio Feedback", "Portfolio Feedback"),
            ("Collaboration", "Collaboration"),
            ("General Question", "General Question"),
        ],
    )
    message = forms.CharField(
        label="Message",
        min_length=20,
        widget=forms.Textarea(attrs={"rows": 7}),
    )
