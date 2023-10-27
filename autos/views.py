from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from autos.forms import MakeForm
from autos.models import Auto, Make

# ? Whats the difference between a view and other types?
# So many abstract classes, so little time

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()

        ctx = {"make_count": mc, "auto_list": al}
        return render(request, "autos/auto_list.html", ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {"make_list": ml}

        return render(request, "autos/make_list.html", ctx)

class MakeCreate(LoginRequiredMixin, View):
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:all")

    def get(self,request):
        form = MakeForm()
        ctx = {"form": form}
        return render(request, self.template, ctx)
    
    def post(self, request):
        form = MakeForm(request.POST)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)    

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy("autos:all")
    template = "autos/make_form.html"
    
    def get(self,request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {"form": form}
        return render(request, self.template, ctx)
    
    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)




class MakeDelete(LoginRequiredMixin, View):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")
    template = "autos/make_confirm_delete.html"

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        ctx = {"make": make}
        return render(request, self.template, ctx)


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy("autos:all")