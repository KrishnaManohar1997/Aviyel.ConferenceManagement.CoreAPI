from django.db import models

from common.models import BaseModel
from conference.models import Conference
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Talk(BaseModel):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name="talks"
    )
    start_date = models.DateTimeField(blank=False, null=False)
    # Duration in days
    duration = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=2,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    speakers = models.ManyToManyField(User, related_name="speakers")
    participants = models.ManyToManyField(User, related_name="participants")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Talk"
        managed = True
        verbose_name_plural = "Talks"
        db_table = "Talk"
