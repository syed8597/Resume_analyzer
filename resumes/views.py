from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume
from django.contrib.auth.decorators import login_required
from .resume_parser import extract_text_from_pdf, extract_skills, extract_experience
import os
from django.conf import settings
# from .ml_model import match_job
from .ml_model import match_top_jobs
# from .langchain_bot import ask_career_bot

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            # ✅ Step 1: Get file path
            file_path = os.path.join(settings.MEDIA_ROOT, resume.file.name)

            # ✅ Step 2: Extract text from resume
            text = extract_text_from_pdf(file_path)

            # ✅ 🔥 Store text in session for chatbot
            request.session['resume_text'] = text

            # ✅ Step 3: Extract skills & experience
            skills = extract_skills(text)
            experience = extract_experience(text)

            # ✅ Step 4: Match jobs using ML
            top_matches = match_top_jobs(text)

            return render(request, 'upload_success.html', {
                'skills': skills,
                'experience': experience,
                'top_matches': top_matches,
            })
    else:
        form = ResumeUploadForm()

    return render(request, 'upload_resume.html', {'form': form})

@login_required
def resume_success(request):
    return render(request, 'upload_success.html')
# @login_required
# def career_chatbot(request):
#     resume_text = request.session.get("resume_text", "")
#     bot_reply = None
#     if request.method == "POST":
#         user_message = request.POST.get("message")
#         bot_reply = ask_career_bot(user_message, resume_text)

#     return render(request, "career_chatbot.html", {
#         "bot_reply": bot_reply
#     })
