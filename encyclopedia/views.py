from django.shortcuts import render
from django import forms
from . import util
import random
from django.http import HttpResponse
from markdown2 import markdown

random.seed(42)

class newEntry(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': "e.g. JavaScript"}))
    content = forms.CharField(label = '', widget=forms.Textarea(attrs={"placeholder" : "write the content here...."}))

class EditForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea())

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_entry_page(request, TITLE): 
    entry_list = util.list_entries()
    temp = list(map(util.to_lower, entry_list))
    entry = util.get_entry(entry_list[temp.index(TITLE.lower())]) if TITLE.lower() in temp else None

    return render(request, "encyclopedia/entry_page.html", {
        "title": TITLE, 
        "entry": None if entry == None else markdown(entry)
    })


def search(request):
    query = request.GET.get('q', '').strip().lower()
    entries = util.list_entries()
    search_list = list(map(util.to_lower, entries))
    similar_entries = []
    
    if query in search_list:
        temp = entries[search_list.index(query)]
        return render(request, "encyclopedia/entry_page.html", {
        "title": temp, 
        "entry": markdown(util.get_entry(temp))
    })
    
    else: 
        for entry in search_list: 
            if query in entry or entry in query:
                similar_entries.append(entries[search_list.index(entry)]); 
        if similar_entries: 
            return render(request, "encyclopedia/search_result.html", {
                "search" : query, 
                "entries": similar_entries
            })
        else:
            return render(request, "encyclopedia/search_result.html", {"search": "Not Found", "entries":similar_entries})


def new_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_page.html", {
            'form': newEntry()
        })
    
    if request.method == 'POST':
        form = newEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            current_entries = list(map(util.to_lower, util.list_entries()))
            if title.lower() not in current_entries:
                util.save_entry(title, content)
                return render(request, "encyclopedia/entry_page.html", {
                    "title": title, 
                    "entry": markdown(util.get_entry(title))
                })
            else:
                form = newEntry(initial={'content':content})
                return render(request, "encyclopedia/new_page.html", {
                    "form":form,
                    'error': "this title is taken, enter another title"
                })
        

def random_page(request):
    entries = util.list_entries()
    index = random.randint(0, len(entries)-1)
    return render(request, "encyclopedia/entry_page.html", {
        'title': entries[index], 
        'entry': markdown(util.get_entry(entries[index]))
    })

def edit(request, title):
    if request.method == 'GET':
        form = EditForm(initial={'content':util.get_entry(title)})
        return render(request, "encyclopedia/edit_page.html", {
            'title':title, 
            'form':form           
        })
    
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry_page.html", {
                "title": title, 
                "entry": markdown(util.get_entry(title))
            })