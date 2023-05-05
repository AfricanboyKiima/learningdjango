from django.shortcuts import render

# Create your views here.
def helloworld(request):
    message = "Hellow world this is kiima from the democratic republic of Congo"
    context = {"detail":message}
    return render(request,"idea/helloworld.html",context)