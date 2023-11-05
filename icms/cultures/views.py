from django.shortcuts import render, redirect
from .models import Culture

def culture_list(request, culture_id=None):
    if culture_id is None:
        cultures = Culture.objects.filter(parent_category__isnull=True)
        return render(request, 'cultures/culture_list.html', {'cultures': cultures})
    else:
        culture = Culture.objects.get(pk=culture_id)
        if culture.external_url:
            return redirect(culture.external_url)
        else:
            subcategories = culture.subcategories.all()
            return render(request, 'cultures/culture_list.html', {'cultures': subcategories})
