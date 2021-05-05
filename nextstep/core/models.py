import datetime

from django.db import models

from nextstep.core.validators import cpf_validator


class PersonType(models.Model):
    name = models.CharField(verbose_name='person type', max_length=32, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person_type'


class PersonMediaType(models.Model):
    FOTO = 1
    BIOMETRIA = 2
    MEDIA_TYPE = [
        (FOTO, 'foto'),
        (BIOMETRIA, 'biometria'),
    ]
    name = models.CharField(max_length=32, null=False, choices=MEDIA_TYPE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person_media_type'


class Person(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=32, null=False)
    type = models.ForeignKey('PersonType', on_delete=models.CASCADE)
    # Should CPF be unique too?
    cpf = models.CharField(max_length=14, null=False, validators=[cpf_validator])
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=32, null=False)
    last_update = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name = 'person'
        verbose_name_plural = 'people'


class PersonMedia(models.Model):
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    object_media = models.TextField(null=False)

    class Meta:
        db_table = 'person_media'


class PersonAudit(models.Model):
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    cpf_new = models.CharField(max_length=14, null=False)
    cpf_old = models.CharField(max_length=14, null=False)
    last_update = models.DateTimeField(null=False)

    ADD = 1
    UPDATE = 2
    TYPE = [
        (ADD, 'add'),
        (UPDATE, 'update'),
    ]
    type = models.IntegerField(choices=TYPE, null=False)

    class Meta:
        db_table = 'person_audit'