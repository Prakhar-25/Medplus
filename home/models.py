from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length = 70)
    department = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'doctors/')
    mobile = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
    
class Contacts(models.Model):
    name = models.CharField(max_length = 70,blank = False)
    email = models.EmailField(max_length = 100,blank = False)
    subject = models.TextField(max_length = 250)
    message = models.TextField(blank = False)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length = 70, blank = False)
    email = models.EmailField(blank = False)
    mobile = models.CharField(max_length = 20, blank = False)
    doctor = models.CharField(max_length = 70)
    date = models.DateField(blank = False)
    time = models.TimeField(blank = False)
    problem = models.TextField()

    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    patient_name = models.CharField(max_length = 70, blank = False)
    profession = models.CharField(max_length = 20)
    img = models.ImageField(upload_to = 'testimonial/')
    review = models.TextField()

    