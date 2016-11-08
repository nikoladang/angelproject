from django.db import models
 
# Create your models here.
class Urls(models.Model):
    original_url = models.URLField(max_length=255)
    # short_id = models.SlugField(max_length=6,primary_key=True)
    short_id = models.CharField(max_length=255, primary_key=True)
    tracking_id = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    views_total = models.IntegerField(default=0)
    views_mobile = models.IntegerField(default=0)
    views_tablet = models.IntegerField(default=0)
    views_touch_capable = models.IntegerField(default=0)
    views_pc = models.IntegerField(default=0)
    views_bot = models.IntegerField(default=0)
    distinct_users = 0
    distinct_referrer_sites = 0
    distinct_referer_pages = 0
    private_status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.original_url


class AccessDetails(models.Model):
    short_id = models.ForeignKey(Urls)
    referer = 0 # (click from)
    user_ip = 0 #
    location = 0 # country/city
    access_date = 0 #
    pass
