from django.db import models

from common.models import BaseModel
from conference.models import Conference
from user.models import User


class Talk(BaseModel):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name="talks"
    )
    start_date = models.DateTimeField(blank=False, null=False)
    duration = models.DurationField(blank=False, null=False)
    speakers = models.ManyToManyField(User, related_name="speakers")
    participants = models.ManyToManyField(User, related_name="participants")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Talk"
        managed = True
        verbose_name_plural = "Talks"
        db_table = "Talk"
