from random import randint

from django import forms
from django.shortcuts import render
from django.http import HttpResponse

score = 0
lives = 10

def index(request):
    return render(request, "guess/index.html")

def play(request):
    global score
    global lives
    scoreChange = 0
    livesChange = 0
    if request.method == "POST":
        answer = request.POST.get('answer')
        correct = randint(1, 31)
        offset = abs(int(answer)-correct)
        score += 30-offset
        scoreChange = 30-offset
        if offset > 7:
            --lives
            livesChange = -1
        elif offset < 3:
            ++lives
            livesChange = 1
        else:
            livesChange = 0
    return render(request, "guess/play.html", {
        "score":score, "scoreChange":scoreChange, "lives":lives, "livesChange":livesChange
    })
