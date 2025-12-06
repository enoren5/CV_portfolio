from django.shortcuts import render
from .models import Content
from django.http import Http404

def HomeView(request):
    try:
        content = Content.objects.first()  # get the first (or only) record
    except Content.DoesNotExist:
        raise Http404("No content is available. Add one in the admin panel.")

    return render(request, "beacons/home.html", {"content": content})


'''
class ContentHomeView(HomePageView):
    model = Content
    context_object_name = "content"  # singular, since it’s one object
    template_name = 'index.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        # Require at least one identifier
        if pk is None and slug is None:
            raise Http404("No object identifier provided in URLconf.")

        # Filter by pk or slug
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        elif slug is not None:
            queryset = queryset.filter(**{self.slug_field: slug})

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("Content not found.")

        if not getattr(obj, "is_published", False):
            raise Http404("This content is not published.")

        return obj
''' 
"""
def home(request):
    return render(request, 'beacons/index.html')

# def methoding(request):
#    return render(request, 'beacons/method.html')

# def backing(request):
#    return render(request, 'beacons/backing.html')
"""