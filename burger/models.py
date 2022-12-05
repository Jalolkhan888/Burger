import datetime

from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Food(models.Model):

    title = models.CharField("Name", max_length=250)
    url = models.SlugField("URL", max_length=250, unique=True)
    description = models.TextField("Description")
    image = models.ImageField("Photo", upload_to="media/foods/")
    main_image = models.ImageField("Main Photo", upload_to='media/foods_main/', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="time_create")
    time_update = models.DateTimeField(auto_now=True, verbose_name="time_update")
    is_published = models.BooleanField(default=True, verbose_name="is_published")
    price = models.PositiveIntegerField(
        "Price", default=0, help_text="show dollar"
    )
    cat = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="category", related_name="foods")

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    # def get_absolute_url(self):
    #     return reverse('menu', kwargs={'cat_slug': self.url})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField("Category Name", max_length=250)
    url = models.SlugField("URL", max_length=250)
    description = models.TextField("Description")
    icon = models.CharField("Icon", max_length=200, null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField("Surname", max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    date = models.DateField()
    time = models.CharField("Time", max_length=200)
    guest = models.PositiveSmallIntegerField()
    is_published = models.BooleanField(default=True, verbose_name="is_published", blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField("Surname", max_length=200)
    position = models.CharField("Position", max_length=100, help_text="position in job")
    image = models.ImageField("Photo", upload_to="media/chefs")
    is_published = models.BooleanField(default=True, verbose_name="is_published")

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField("Fullname", max_length=200)
    profession = models.CharField("Profession", max_length=100)
    content = models.TextField()
    image = models.ImageField("Photo", upload_to="media/clients")
    is_published = models.BooleanField(default=True, verbose_name="is_published")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class BlogFood(models.Model):
    title = models.CharField("Title", max_length=200)
    url = models.SlugField("URL", max_length=200)
    content = models.TextField()
    image = models.ImageField("Photo", upload_to='media/BlogFood')
    time_create = models.DateField("Creat Time", auto_now_add=True)
    cat = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="category")
    is_published = models.BooleanField(default=True, blank=True, verbose_name="Published")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={'id': self.pk})

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Comments(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    text = models.TextField()
    parent = models.ForeignKey(
        "self", verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    food = models.ForeignKey(BlogFood, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.food}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"





