from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class AccessInfo(models.Model):
    access_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-access_time',)

    def __str__(self):
        return self.access_time
    
class PlayList(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class PlayList1(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class PlayList2(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class PlayList3(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    wiki = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

class PlayListcar(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name
class Video(models.Model):
    title = models.CharField(max_length=200)
    vid = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Branch(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class StoreIncome(models.Model):
    income_year = models.CharField(max_length=4)
    income_month = models.CharField(max_length=2)
    income = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.income)