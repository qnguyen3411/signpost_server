from django.db import models

# Create your models here.
class ClueNode(models.Model):
    title = models.CharField(max_length=140)
    unique_id = models.CharField(max_length=7, unique=True)
    text = models.CharField(max_length=140)
    latitude = models.FloatField()
    longitude = models.FloatField()
    prev_node =  models.OneToOneField("self", related_name="next_node", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class TreasureHunt(models.Model):  
    first_node = models.OneToOneField(ClueNode, related_name="treasure_hunt")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

