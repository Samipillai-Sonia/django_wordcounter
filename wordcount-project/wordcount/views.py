from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word] = 1

    return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddict':worddictionary})


def about(request):
    return render(request,'about.html')