from django.db import models


class AVRIndex(models.Model):
    avr_scheme = models.TextField()
    article = models.TextField()
    name = models.TextField()
    power_devices_brand = models.TextField()
    power_devices_type = models.TextField()
    spring_time = models.TextField()
    plc = models.TextField()
    extension_module = models.TextField()
    specification = models.TextField()
    documentation = models.TextField()
    specification_link = models.TextField()
    xlsx_export_link = models.TextField()
    pdf_avr_link = models.TextField()
    pdf_scheme_link = models.TextField()
    zip_link = models.TextField()
    xlsx_link = models.TextField()
    status = models.TextField()


class AVRLog(models.Model):
    date = models.DateTimeField()
    avr_scheme = models.TextField()
    power_part = models.TextField()
    plc_voltage = models.TextField()
    brand = models.TextField()
    type = models.TextField()


class AVRSpec(models.Model):
    specification = models.TextField()
    name = models.TextField()
    note = models.TextField()


class AVRSpecData(models.Model):
    avr_spec = models.ForeignKey(AVRSpec, on_delete=models.CASCADE)
    number = models.IntegerField()
    item = models.TextField()
    value = models.TextField()
