from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#home page 
class Poll(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Subjects'),
        ('events', 'Events'),
        ('opinion', 'School Opinions'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
    
# academic page
class PollResponse(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Subjects'),
        ('events', 'Events'),
        ('opinion', 'School Opinions'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.question} : {self.answer}"
    
# event page
class EventPolls(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Subjects'),
        ('events', 'Events'),
        ('opinion', 'School Opinions'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.question} : {self.answer}"


# school opinion 
class school_opinion_poll(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Subjects'),
        ('events', 'Events'),
        ('opinion', 'School Opinions'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.question} : {self.answer}"


#poll questions 
class PollQuestion(models.Model):
    question = models.CharField(max_length=255)
    category = models.CharField(max_length=50)

# poll options
class PollOption(models.Model):
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return self.option_text

    