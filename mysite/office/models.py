from django.db import models
from datetime import date

# Create your models here.
from django.urls import reverse
from django.core.validators import MaxValueValidator

class Engineer(models.Model):

    TITLE_LIST=(
        ('SE', 'Support Engineer'),
        ('SEE', 'Support Escalation Engineer'),
        ('EE', 'Escalation Engineer'),
        ('TA', 'Technical Advisor'),
        ('TM', 'Team Manager'),
    )

    REGION_LIST=(

        ('APAC', 'APAC'),
        ('EMEA', 'EMEA'),
        ('US', 'US')
    )
    engr_name = models.CharField('Name', max_length=30,)
    engr_email = models.EmailField('Email', max_length=30,)
    region = models.CharField('Region', max_length=4, choices=REGION_LIST, default='APAC')
    engr_team = models.ForeignKey('Team', on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=TITLE_LIST, default='SE')
    skill = models.ManyToManyField('Product', max_length=20, blank=True)
    vote = models.IntegerField(validators=[MaxValueValidator(10)], null=True, blank=True)
    active = models.BooleanField(default=True)
    #related_case = models.ForeignKey('Case', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'engineer'
        ordering = ['engr_team', 'engr_name']

    def __str__(self):
        return self.engr_name

    def get_absolute_url(self):
        return reverse('engineer-detail', args=[str(self.id)])
    
    def display_skills(self):
        return ' & '.join([skill.prod_name for skill in self.skill.all()[:]])
    display_skills.short_description = 'Skills'

class Product(models.Model):
    prod_name = models.CharField('Name', max_length=30)
    prod_team = models.ForeignKey('Team', on_delete=models.CASCADE)
    queue = models.CharField(max_length=100, blank=True)
    p_description = models.TextField('Description',max_length=500, blank=True)

    class Meta:
        db_table = 'product'
        ordering = ['prod_name']

    def __str__(self):
        return self.prod_name
    
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class Team(models.Model):
    GROUP_LIST = (
        ('OPG', 'OPG'),
        ('WDG', 'WDG'),
        ('C+E', 'C+E')
    )
    team_name = models.CharField('Name',max_length=30)
    ta_name = models.CharField('TA',max_length=30, blank=True)
    group = models.CharField('Group', max_length=8, choices=GROUP_LIST, blank=True)
    #dispatcher = models.ForeignKey('Engineer', on_delete=models.CASCADE, blank=True)
    t_description = models.TextField('Description',max_length=200, blank=True)

    class Meta:
        db_table = 'team'
        ordering = ['team_name']

    def __str__(self):
        return self.team_name
    
    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id)])

class Case(models.Model):
    number = models.CharField(max_length=15)
    title = models.CharField(max_length=50, blank=True)
    link = models.URLField(max_length=200, blank=True)
    c_description = models.TextField(max_length=200, blank=True)

    class Meta:
        db_table = 'case'

    def __str__(self):
        return self.number

class Advice(models.Model):
    name = models.CharField(max_length=200)
    proposer = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'advice'

    def __str__(self):
        return self.name