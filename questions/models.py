from django.db import models
    
class Author(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    STATUS_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    title = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=10, choices=STATUS_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    test = models.TextField()
    TAG = [('python', 'Python'), ('django', 'Django'), ('database', 'Database'), ('debugging', 'Debugging')]
    category = models.CharField(max_length=30, choices=TAG, blank=True, null=True)

