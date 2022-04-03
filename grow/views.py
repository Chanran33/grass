from django.shortcuts import render

# Create your views here.
def main(requests):
    return render(requests, "main.html")

def rank(requests):
    return render(requests, "rank.html")