from django.db import models


class data1(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    specialized = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    license = models.CharField(max_length=30)
    hospital = models.CharField(max_length=30)
    fee = models.CharField(max_length=5)
    res_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profilePicture = models.ImageField(upload_to='', default='hlo')




class patient(models.Model):
    dr_name= models.ForeignKey(data1,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length = 8)
    age = models.IntegerField()
    email = models.CharField(max_length = 50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    ph_no = models.CharField(max_length=14)
    disease = models.CharField(max_length=100)

class merge(models.Model):
    patient_id=models.IntegerField(default=None)
    doctor_id=models.IntegerField(default=None)
    p_email = models.CharField(max_length=50)
    p_name = models.CharField(max_length=50,null=True)
    p_gender = models.CharField(max_length=8)
    p_age = models.IntegerField()
    p_ph_no = models.IntegerField()
    dr_name= models.CharField(max_length=30)
    dr_username = models.CharField(max_length=30,default=None)
    p_disease = models.CharField(max_length=100)
    a_date = models.DateField()
    a_time = models.TimeField()
    hospital_name = models.CharField(max_length=30)

