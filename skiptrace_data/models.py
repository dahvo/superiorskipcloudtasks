from django.db import models
from django.db.models import JSONField
# Create your models here.


class SkipTraceData(models.Model):
    skip_trace_detail = JSONField(null=True, blank=True)
