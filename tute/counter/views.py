from django.shortcuts import render

from .models import Counter

# Create your views here.
def index(request):
    # This is a terrible example, as a GET request changes the database!
    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()

    counter.count += 1
    counter.save()

    context = {
        "count": counter.count
    }
    return render(request, 'counter/index.html', context)