from django.db import models


class AVRIndex(models.Model):
    """AVR Index"""
    avr_scheme = models.CharField(max_length=5)
    article = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    power_devices_brand = models.CharField(max_length=100)
    power_devices_type = models.CharField(max_length=100)
    spring_time = models.CharField(max_length=50, default=None, blank=True, null=True)
    plc = models.CharField(max_length=10)
    extension_module = models.CharField(max_length=10, default=None, blank=True, null=True)
    specification = models.CharField(max_length=30)
    documentation = models.TextField(default=None, blank=True, null=True)
    specification_link = models.TextField()
    xlsx_export_link = models.TextField()
    pdf_avr_link = models.TextField()
    pdf_scheme_link = models.TextField()
    zip_link = models.TextField()
    xlsx_link = models.TextField()
    status = models.TextField(default=None, blank=True, null=True)


class AVRSpec(models.Model):
    """AVR Spec"""
    specification = models.TextField()
    name = models.TextField()
    note = models.TextField()


class AVRSpecData(models.Model):
    """AVR Spec Data"""
    avr_spec = models.ForeignKey(AVRSpec, on_delete=models.CASCADE)
    number = models.IntegerField()
    item = models.TextField()
    value = models.TextField()


class AVRLog1(models.Model):
    """AVR Log 1"""
    date = models.DateTimeField(auto_now_add=True)
    avr_scheme = models.CharField(max_length=5)
    power_part = models.CharField(max_length=30)
    plc_voltage = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class AVRLog2(models.Model):
    """AVR Log 2"""
    date = models.DateTimeField(auto_now_add=True)
    ua = models.TextField()


class AVRLog3(models.Model):
    """AVR Log 3"""
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=5)
    info = models.TextField()
