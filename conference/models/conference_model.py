from django.db import models

from common.models import BaseModel


class Conference(BaseModel):
    # Title is made unique as in future users might wanna search for Conferences by Title
    title = models.CharField(
        max_length=32, blank=True, null=True, db_index=True, unique=True
    )
    description = models.CharField(max_length=512, blank=True, null=True)

    banner_url = models.URLField(max_length=128, blank=True, null=True)
    talks_count = models.PositiveIntegerField(default=0)

    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Conference"
        managed = True
        verbose_name_plural = "Conferences"
        db_table = "Conference"
