from django.http.response import HttpResponseNotFound
from django.shortcuts import render

def analises_bianca(request):
    return render(request, 'analises.html', context)

def home(request):
    item = Interesses.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'analises.html', context=mydict)