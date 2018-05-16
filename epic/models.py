from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
