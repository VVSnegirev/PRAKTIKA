from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
def news_home(requests):
    news = Articles.objects.order_by('-date')
    return render(requests, 'news/news_home.html',{'news':news})

class NewsDetailView(DetailView):
    model=Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/news-update.html"

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = "news/news-delete.html"

def create(requests):
    error = ''
    if requests.method == 'POST':
        form = ArticlesForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error='Форма была неверной'
    form = ArticlesForm()
    data = {
        'form':form,
        'error':error
    }
    return render(requests, 'news/create.html', data)