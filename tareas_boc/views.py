from django.http import HttpResponse
from django.template import loader
import json
from django.shortcuts import render

#def tareas_boc(request):
 # template = loader.get_template('index.html')
#return HttpResponse(template.render())


def json_to_grid(request):
    if request.method == "POST":
        json_input = request.POST.get("json_input")
        
        try:
            json_data = json.loads(json_input)
        except json.JSONDecodeError:
            return HttpResponse("JSON no válido.", status=400)
        
        context = {
            "json_data": json_data,
            "is_dict": isinstance(json_data, dict),
            "is_list": isinstance(json_data, list)
        }
        
        return render(request, "json_to_grid.html", context)
    
    return render(request, "json_to_grid.html")