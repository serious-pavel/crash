from django.shortcuts import render
from .models import Frame

# Create your views here.


def main_page(request):
    f = Frame.objects.latest('update_date')

    return render(request, "main_page.html", context={"f": f})
