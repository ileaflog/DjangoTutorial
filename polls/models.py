import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Poll(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
    poll = models.ForeignKey(Poll)
#    yap = models.ForeignKey(Poll, related_name='yaps')
    author = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)