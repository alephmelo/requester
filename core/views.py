from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import FeatureRequest
from .forms import FeatureRequestForm


def index(request):
    results = FeatureRequest.objects.all().order_by('priority', 'client_id')
    return render(request, 'index.html', {'results':results})


def new_request(request):
    if request.method == "POST":
        form = FeatureRequestForm(request.POST)

        if form.is_valid():
            new_feature_request = form.save(commit=False)
            queryset = FeatureRequest.objects.filter(
                client_id=new_feature_request.client_id).order_by('priority')

            if queryset.filter(priority=new_feature_request.priority).exists():
                dict_index_priority = {index: item.priority for index, item in enumerate(queryset)}
                
                index = [key for key, value in dict_index_priority.items() \
                        if value == new_feature_request.priority][0]

                for result in queryset[index:]:
                    result.priority += 1
                    result.save()

                new_feature_request.save()

            else:
                new_feature_request.save()

            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = FeatureRequestForm()

    return render(request, 'new_request.html', {'form': form})