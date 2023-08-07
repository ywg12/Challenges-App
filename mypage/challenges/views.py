from django.shortcuts import render
from django.http  import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"Eat no meat for an entire month!",
    "febraury":"Walk for at least 30 minutes a day!",
    "march":"Learn Djnago for atleast 20 minutes everyday!",
    "april":"Eat no meat for an entire month!",
    "may":"Walk for at least 30 minutes a day!",
    "june":"Learn Djnago for atleast 20 minutes everyday!",
    "july":"Eat no meat for an entire month!",
    "august":"Walk for at least 30 minutes a day!",
    "september":"Learn Djnago for atleast 20 minutes everyday!",
    "october":"Eat no meat for an entire month!",
    "november":"Walk for at least 30 minutes a day!",
    "december":None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_url = reverse("month-challenge",args=[redirect_month]) #challenge/followed by month_name
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        return render(request, "challenges/challenge.html",{
            "text":challenge_text,
            "month":month.capitalize()
        })

    except:
        raise Http404()   
    
    
