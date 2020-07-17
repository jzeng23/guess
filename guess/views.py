from random import randint

from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "guess/index.html")

MAX_NUM = 30 # the
UPPER_OFFSET = 7
LOWER_OFFSET = 3
INITIAL_LIVES = 10

def play(request):

    global MAX_NUM
    global UPPER_OFFSET
    global LOWER_OFFSET
    global INITIAL_LIVES

    if request.method == "POST":
        answer = request.POST.get('answer')
        correct = randint(1, MAX_NUM)
        offset = abs(int(answer)-correct)
        request.session["score"] += MAX_NUM-offset
        request.session["scoreChange"] = MAX_NUM-offset
        if offset > UPPER_OFFSET:
            request.session["lives"] = request.session["lives"] - 1
            request.session["livesChange"] = -1
        elif offset < LOWER_OFFSET:
            request.session["lives"] = request.session["lives"] + 1
            request.session["livesChange"] = 1
        else:
            request.session["livesChange"] = 0
    else:
        # if the request method is not POST, aka. if the player hits the start button on the home page or directly types the url of this page.
        # reset game variables and start a new game
        answer = -1
        correct = -1
        request.session["score"] = 0
        request.session["scoreChange"] = 0
        request.session["lives"] = INITIAL_LIVES
        request.session["livesChange"] = 0

    if request.session["lives"] < 1:
        score = request.session["score"]
        scoreChange = request.session["scoreChange"]
        finalAnswer = answer
        finalCorrect = correct
        return render(request, "guess/end.html", {
            "score":score, "scoreChange":scoreChange, "finalAnswer":finalAnswer, "finalCorrect":finalCorrect
        })
    else:
        return render(request, "guess/play.html", {
            "MAX_NUM":MAX_NUM, "score":request.session["score"], "scoreChange":request.session["scoreChange"], "lives":request.session["lives"], "livesChange":request.session["livesChange"], "answer":answer, "correct":correct
        })