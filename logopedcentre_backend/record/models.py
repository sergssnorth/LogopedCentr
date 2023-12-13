from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.utils.timezone import now

class Direction(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'directions/{self.slug}/'
    
class DirectionPoints(models.Model):
    direction = models.ForeignKey(Direction, related_name='directionpoints', on_delete= models.CASCADE)
    description = models.TextField(blank=True, null =True)
    
    class Meta:
        ordering = ('direction',)

    def __str__(self):
        return self.description
    

class Specialist(models.Model):
    direction = models.ForeignKey(Direction, related_name='specialists', on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    sname = models.CharField(max_length=255)
    tname = models.CharField(max_length=255)
    phone =  models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
           
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.direction.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    

class SpecialistSchedule(models.Model):
    specialist = models.ForeignKey(Specialist, related_name='SpecialistSchedule', on_delete= models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    #10/25/2006
    class Meta:
        ordering = ('date',)

    def __str__(self):
        return  f'{self.specialist.sname} {self.specialist.name} {self.date} {self.time}'

class UserInformation(models.Model):
    user = models.ForeignKey(User, related_name='user_information', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
class UserChildrenInformation(models.Model):
    user = models.ForeignKey(User, related_name='user_children_information', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class RecordStatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Record(models.Model):
    user = models.ForeignKey(User, related_name='record', on_delete=models.CASCADE)
    children = models.ForeignKey(UserChildrenInformation, related_name='record1', on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, related_name='record2', on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, related_name='record3', on_delete=models.CASCADE)
    record_date = models.ForeignKey(SpecialistSchedule, related_name='record4', on_delete=models.CASCADE)
    status = models.ForeignKey(RecordStatus, related_name='record5', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=now, editable=False)

    class Meta:
        ordering = ('user',)
    
    def __str__(self):
        return f'{self.specialist.sname} {self.specialist.name} {self.record_date}'

