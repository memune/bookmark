from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect


from .models import Bookmark, Category

class BookmarkListView(ListView):
    model = Bookmark
    # 페이지네이션 설정
    # paginate_by = 6

    # 'votes' 필드를 기준으로 내림차순 정렬
    # def get_queryset(self):
    #     return Bookmark.objects.order_by('-votes')

    def get_queryset(self):
        return Bookmark.objects.order_by('-votes')

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'description', 'url', 'category']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'description', 'url', 'category']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')


def vote(request, pk):
    bookmark_list = get_object_or_404(Bookmark, pk=pk)
    bookmark_list.votes += 1
    bookmark_list.save()

    return HttpResponseRedirect(reverse('bookmark:list'))
    
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
        # 
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

