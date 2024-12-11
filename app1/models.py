from django.db import models

# Create your models here.
class AddTable(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(max_length=10, null=False, blank=False)
    time = models.TimeField(max_length=10, null=False, blank=False)
    BRANCH = (
        ('select branch','select branch'),
        ('hyderabad', 'Hyderabad'),
        ('vijayawada', 'Vijayawada'),
        ('vishakhapatnam', 'Vishakhapatnam'),
    )
    branch = models.CharField(max_length=20, choices=BRANCH, default='select branch')
    PEOPLE = (
        (0,'select persons'),
        (1, '1 person'),
        (2, '2 persons'),
        (3, '3 persons'),
        (4, '4 persons'),
        (5, '5 persons'),
        (6, '6 persons'),
    )
    people = models.IntegerField(choices=PEOPLE, default='select persons')

    def __str__(self):
        return self.name