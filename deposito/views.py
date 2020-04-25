from django.shortcuts import render,  redirect
from .forms import mercadoForm
from .models import itens
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def Index(request):
    object_list = itens.objects.all()  
    paginator = Paginator(object_list, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html", {'page_obj': page_obj})


def Cadastro(request):
    if request.method == 'POST':
        form = mercadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = mercadoForm()
        return render(request, 'cadastro.html', {'form': form})


# Create your views here.
