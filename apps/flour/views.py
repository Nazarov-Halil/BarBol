from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.flour.models import Flour


class FlourListView(ListView):
    model = Flour
    template_name = 'flour.html'
    context_object_name = 'flour'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        flour_list = Flour.objects.all()

        paginator = Paginator(flour_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            flour_product = paginator.page(page)
        except PageNotAnInteger:
            flour_product = paginator.page(1)
        except EmptyPage:
            flour_product = paginator.page(paginator.num_pages)

        context['flour_product'] = flour_product
        return context


class FlourDetailView(DetailView):
    model = Flour
    template_name = 'flour_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'flour_detail'

    def get_queryset(self):
        return Flour.objects.all()
