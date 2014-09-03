from django.db import models


class Word(models.Model):
    word = models.CharField(unique=True, max_length=255)
    tag = models.ForeignKey('tags.Tag')
    case_sensitive = models.BooleanField(default=True)

    def __unicode__(self):
        return self.word
