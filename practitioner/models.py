from django.db import models


class Practitioner(models.Model):
    """
    Represents a healthcare practitioner.
    """

    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    telecom = models.ManyToManyField('Telecom')
    address = models.ManyToManyField('Address')
    gender = models.CharField(max_length=10)
    birthDate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='practitioners', blank=True, null=True)
    roles = models.ManyToManyField('PractitionerRole')
    specialty = models.ManyToManyField('Specialty')

    class Meta:
        verbose_name = 'Practitioner'
        verbose_name_plural = 'Practitioners'