from random import randint

from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "guess/index.html")

def play(request):
    answer = -1
    correct = -1
    if "score" not in request.session:
        request.session["score"] = 0
        request.session["scoreChange"] = 0
        request.session["lives"] = 10
        request.session["livesChange"] = 0
    if request.method == "POST":
        answer = request.POST.get('answer')
        correct = randint(1, 30)
        offset = abs(int(answer)-correct)
        request.session["score"] += 30-offset
        request.session["scoreChange"] = 30-offset
        if offset > 7:
            request.session["lives"] = request.session["lives"] - 1
            request.session["livesChange"] = -1
        elif offset < 3:
            request.session["lives"] = request.session["lives"] + 1
            request.session["livesChange"] = 1
        else:
            request.session["livesChange"] = 0
    if request.session["lives"] < 1:
        score = request.session["score"]
        scoreChange = request.session["scoreChange"]
        finalAnswer = answer
        finalCorrect = correct
        request.session["score"] = 0
        request.session["lives"] = 10
        request.session["scoreChange"] = 0
        request.session["livesChange"] = 0
        answer = -1
        correct = -1
        return render(request, "guess/end.html", {
            "score":score, "scoreChange":scoreChange, "finalAnswer":finalAnswer, "finalCorrect":finalCorrect
        })
    else:
        return render(request, "guess/play.html", {
            "score":request.session["score"], "scoreChange":request.session["scoreChange"], "lives":request.session["lives"], "livesChange":request.session["livesChange"], "answer":answer, "correct":correct
        })