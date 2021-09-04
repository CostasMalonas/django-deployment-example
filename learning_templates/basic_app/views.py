from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello assholes', 'number':666}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

"""
Now we need to set up the urls to actually point to these views.
We should make sure that we set up the urls correctly so that they
actually use the template tagging correctly.
"""
