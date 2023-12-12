from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  age = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  
class Court(models.Model):
    COURT_TYPES = [
        ('GR', 'Grass'),
        ('HD', 'Hard'),
        ('CL', 'Clay'),
        ('CP', 'Carpet'),
    ]
    name = models.CharField(max_length=255)
    court_type = models.CharField(max_length=2, choices=COURT_TYPES)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.get_court_type_display()}) - {self.city}"