from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello')# 回傳字串
    return render(request, 'home.html', {'mes': 'Type some words in the box below'})  # 回傳html檔案


def eggs(request):
    # 回傳html碼
    return HttpResponse('<h1>Eggs are great</h1>')


def count(request):
    fulltext = request.GET['fulltext']  # 存取url的變數
    wordlist = fulltext.split()
    words = len(wordlist)
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'words': words, 'word_dict': word_dict.items()})


def about(request):
    return render(request, 'about.html')
