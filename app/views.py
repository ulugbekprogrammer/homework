from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    print(str(request))
    context = {"261": ("Alfred Alen", "aalan@gmail.com", "stocks"),
               "227": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "246": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "212": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "218": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "243": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "232": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "233": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "221": ("Alisson Smart", "asmart@gmail.com", "stocks"),
               "241": ("Alisson Smart", "asmart@gmail.com", "stocks"),}
    
    return render (request=request, template_name="index.html", context= {"context":context})
