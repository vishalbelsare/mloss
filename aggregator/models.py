from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=200)
    feed_url = models.URLField(unique=True)
    public_url = models.URLField()
    is_defunct = models.BooleanField()

    class Meta:
        db_table = 'aggregator_feeds'

    def __unicode__(self):
        return unicode(self.title)

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=200)
    link = models.URLField()
    summary = models.TextField(blank=True)
    date_modified = models.DateTimeField()
    guid = models.CharField(max_length=200, unique=True, db_index=True)

    class Meta:
        db_table = 'aggregator_feeditems'
        ordering = ("-date_modified",)

    def __unicode__(self):
        return unicode(self.title)

    def get_absolute_url(self):
        return self.link

