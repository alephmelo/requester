from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import FeatureRequest
from .forms import FeatureRequestForm


def index(request):
    results = FeatureRequest.objects.all()
    return render(request, 'index.html', {'results':results})


def new_request(request):
    if request.method == "POST":
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            new_feature_request = form.save(commit=False)
            new_feature_request.save()
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = FeatureRequestForm()

    return render(request, 'new_request.html', {'form': form})