from django.db import models


ASSUR_CHOICES = (
    ('SEIS','SEIS'),
    ('EIS', 'EIS'),
    ('NONE','NONE'),
)

STAGE_CHOICES = (
    ('Ideation/Angel','Ideation/Angel'),
    ('Pre-Seed','Pre-Seed'),
    ('Seed','Seed'),
    ('Series-A','Series-A'),
    ('Series-B','Series-B'),
    ('Series-C','Series-C'),
    ('Series-D','Series-D'),
    ('Mezzanine Round','Mezzanine Round'),
    ('IPO','IPO')
)

class PitchDeck(models.Model):
    name = models.CharField(max_length=200, unique=False)
    company_name = models.CharField(max_length=200, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    Sector= models.CharField(max_length=100, unique=False, default=None)
    Location= models.CharField(max_length=100, default=None)
    PMV=models.BigIntegerField(default=None)
    Raising= models.BigIntegerField(default=None)
    Email= models.EmailField(default=None)
    Assurance = models.CharField(max_length=6, choices=ASSUR_CHOICES, default=None)
    Stage= models.CharField(max_length=20, choices=STAGE_CHOICES, default=None)
    upload = models.FileField(upload_to ='uploads/')
