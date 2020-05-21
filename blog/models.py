from django.db import models
from django.utils import timezone
from django.core.urlsolvers import reverse
# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    published = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_details",kwargs={'pk':self.pk})    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments=True
        self.save()

    def __str__(self):
        return self.text
