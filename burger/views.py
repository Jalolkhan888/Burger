from unicodedata import category

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.views import View
from .forms import *
from django.views.generic import ListView, DetailView


class HomeView(View):
    def get(self, request):
        chef = Chef.objects.all()
        client = Client.objects.all()
        category = Category.objects.all()
        context = {
            "chefs": chef,
            "clients": client,
            "title": "home",
            'nbar': 'home',
            'categories': category,

        }
        return render(request, "burgers/index.html", context)


class AboutView(View):
    def get(self, request):
        chef = Chef.objects.all()
        client = Client.objects.all()
        category = Category.objects.all()
        context = {
            "chefs": chef,
            "clients": client,
            "title": "about",
            "page_name": 'About Us',
            'page_title': 'About Us',
            'nbar': 'about',
            'categories': category,
        }
        return render(request, "burgers/about.html", context)


class FeatureView(View):
    def get(self, request):
        context = {
            'title': "feature",
            'page_name': 'Why Choose Us',
            'page_title': "feature",
            'nbar': 'feature',
        }
        return render(request, "burgers/feature.html", context)


class TeamView(View):
    def get(self, request):
        chef = Chef.objects.all()
        context = {
            "chefs": chef,
            'title': "team",
            'page_name': 'Master Chef',
            'page_title': 'Chef',
            'nbar': 'team'
        }
        return render(request, "burgers/team.html", context)


class MenuView(View):
    def get(self, request):
        food = Food.objects.all()
        category = Category.objects.all()
        context = {
            "title": "Menu",
            "page_name": "Food Menu",
            "page_title": "Menu",
            'nbar': 'menu',
            'categories': category,
            'foods': food,
        }
        return render(request, "burgers/menu.html", context)


class CategoryView(View):
    def get(self, request, cat_id):
        food = Food.objects.filter(cat_id=cat_id)
        category = Category.objects.all()
        context = {
            "title": "Menu",
            "page_name": "Food Menu",
            "page_title": "Menu",
            'nbar': 'menu',
            'categories': category,
            'foods': food,
            'cat_id': cat_id,
        }
        return render(request, "burgers/menu.html", context)


class BookingView(View):
    def get(self, request):
        context = {
            "title": "Booking",
            "page_name": "Book A Table",
            "page_title": "Booking",
            'nbar': 'booking',

        }
        return render(request, "burgers/booking.html", context)


class OrderView(View):
    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        return redirect('/')


class BlogView(ListView):
    paginate_by = 2
    model = BlogFood
    template_name = 'burgers/blog.html'
    context_object_name = 'blog_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['page_name'] = 'Food Blog'
        context['page_title'] = 'Blog'
        context['nbar'] = 'blog'
        return context

    # def get(self, request):
    #     blog = BlogFood.objects.all()
    #     context = {
    #         "title": "Blog",
    #         "page_name": "Food Blog",
    #         "page_title": "Blog",
    #         'nbar': 'blog',
    #         "blog_list": blog
    #     }
    #     return render(request, "burgers/blog.html", context)


class DetailBlog(View):

    def get(self, request, id):
        search_query = request.GET.get("search", "")
        print("----->" + search_query)
        if search_query:
            detail = BlogFood.objects.get(title=search_query.title())
        else:
            detail = BlogFood.objects.get(pk=id)
        # detail = BlogFood.objects.get(pk=id)
        detail_cat = detail.cat
        print(detail_cat)
        # print(detail.title__icontains)
        related_post = BlogFood.objects.filter(cat=detail_cat)
        print(related_post)
        recent_post = BlogFood.objects.all().order_by('-time_create')[0:4]
        print("-" * 100)
        print(recent_post)
        context = {
            "title": "Detail",
            "page_name": "Blog Detail",
            "page_title": "Detail",
            'nbar': 'detail',
            'blog': detail,
            'related_post': related_post,
            "recent_post": recent_post,

        }
        return render(request, "burgers/single.html", context)


class CommentView(View):
    def post(self, request, id):
        form = CommentForm(request.POST)
        food = BlogFood.objects.get(pk=id)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                print("-" * 10 + request.POST.get('parent'))
                form.parent_id = int(request.POST.get("parent"))
            form.food = food
            form.save()
        return redirect(food.get_absolute_url())


class ContactView(View):
    def get(self, request):
        context = {
            "title": "Contact",
            "page_name": "Contact Us",
            "page_title": "Contact",
            'nbar': 'contact',
        }
        return render(request, "burgers/contact.html", context)


def register_1(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        "title": "Register",
        "page_name": "Sign In",
        "page_title": "Register",
        'nbar': 'register',
        'form': form,
    }
    return render(request, "burgers/register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")

    context = {
        "title": "Login",
        "page_name": "Sign Up",
        "page_title": "Log in",
        'nbar': 'login',
    }
    return render(request, "burgers/login.html", context)


def log_out(request):
    logout(request)
    return redirect('login')
