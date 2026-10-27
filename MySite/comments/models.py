from django.db import models

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    rating = models.IntegerField() # Поле из твоего варианта

    def __str__(self):
        return f"{self.user_name} - {self.text[:20]}"