from django.shortcuts import render, redirect
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def home(request):
    return render(request, 'home.html')

def skin_form(request):
    issue = request.GET.get("issue", "")
    error = None

    if request.method == "POST":
        required_fields = [
            "skin_type", "wash_count", "cleanser_type", "pollution_index",
            "sleep_time", "wake_time", "food_habits"
        ]
        missing = [f for f in required_fields if not request.POST.get(f)]

        if missing:
            error = "⚠️ Please fill all the required information below."
            return render(request, "skin_form.html", {
                "issue": request.POST.get("issue", ""),
                "error": error,
                **request.POST  # Pass all field values back to the form
            })
        else:
            return redirect("/results/")  # or do generate logic directly here

    return render(request, "skin_form.html", {"issue": issue})

def hair_form(request):
    return render(request, 'hair_form.html')

def body_form(request):
    return render(request, 'body_form.html')

def health_form(request):
    return render(request, 'health_form.html')

def generate_suggestions(request):
    if request.method == "POST":
        form_data = dict(request.POST)
        form_data.pop('csrfmiddlewaretoken', None)

        formatted = "\n".join([f"{k.replace('_',' ').title()}: {v[0]}" for k, v in form_data.items()])

        prompt = f"""
        The following is a user profile for a beauty/health issue. Provide friendly, bullet-pointed personalized suggestions (tips, care routines, and products) based on the input:

        {formatted}

        Keep suggestions practical and positive.
        """

        try:
            response = model.generate_content(prompt)
            output = response.text.strip()
            output = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", output)
        except Exception as e:
            output = f"Error: {str(e)}"

        return render(request, 'result.html', {"suggestions": output})
    else:
        return render(request, 'home.html')