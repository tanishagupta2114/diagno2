import email
import string
from random import random
from datetime import date,datetime
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import auth
# noinspection PyUnresolvedReferences
#from django.contrib.auth.models import Sign_up
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from diseasetables.models import disease
from webapp.models import patient, data1, merge
from webapp.token import account_activation_token

from django.views.decorators.csrf import csrf_exempt
from . import checksum

MERCHANT_KEY = "xZXkVgPSklrs_nN3"
current_user=0
# fees=10
em=email

# def login(request):
#     if request.method == 'POST':
#         un = request.POST['username']
#         pass1 = request.POST['password']
#
#         user = auth.authenticate(username=un,password=pass1)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('dhome')
#         else:
#             print('invalid' + un + pass1)
#     else:
#         return render(request, 'login.html')



#def Sign_up(request):
 #   user=Sign_up.objects.all()
  #  if request.method=='POST':
   #     fn =request.POST['firstname']
    #    ln = request.POST['lastname']
     #   un = request.POST['username']
        #bd=request.POST['birthday']
        #gn=request.POST['gender']
        #qf = request.POST['qualification']
      #  em = request.POST['email']
        #st = request.POST['state']
        #sz = request.POST['specialized']
        #ep = request.POST['experience']
        #lc = request.POST['license']
        #hp = request.POST['hospital']
        #fe = request.POST['fee']
        #rc = request.POST['res_code']
        #ct = request.POST['city']
       # pass1 = request.POST['password']
        #pass2 = request.POST['password1']
    #     if pass1==pass2:
    #
    #             user = Sign_u(username=un, firstname=fn, lastname=ln, email=em, password=pass1)p
    #             user.save()
    #             return redirect('dhome')
    #     else:
    #         print('password not match')
    # else:
    #     return render(request, 'Signup.html',{'user':user})



def scale(request):
    return render(request, 'scale.html')


def reqsend(request,pk):

    return render(request, 'reqsend.html')

def index(request):
    return render(request, 'index.html')
def appointment(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        ph_no = request.POST["phn"]
        age = request.POST["age"]
        city = request.POST["city"]
        state = request.POST["state"]
        gender = request.POST["gender"]
        ds = request.POST["disease"]
        x = patient(name = name, email = email, ph_no = ph_no, age = age, city = city, state = state, gender = gender, disease = ds)
        x.save()
        pid=patient.objects.last()
        print(ds)
        print(pid)
        ds1 = disease.objects.filter(d=ds)
        return render(request, 'diseases.html', {'ds': ds1,'pid':pid})
    else:
        return render(request, 'appointment.html')

def contact(request):
    return render(request, 'contact.html')


def scaling(request,pk):
    pd=patient.objects.get(pk=pk)
    return render(request, 'scaling.html',{'p_data':pd})

def login(request):

    if request.method == 'POST':
        un = request.POST['username']
        pass1 = request.POST['password']

        user = auth.authenticate(username=un,password=pass1)

        if user is not None:
            print(user.username)

            k = merge.objects.filter(dr_username=user.username)

            return render(request, 'showpatient.html',{'doc':k})
        else:
            print('invalid' + un + pass1)
    else:
       return render(request, 'drlogin.html')

def logout(request):
    auth.logout(request)
    return redirect('drlogin')

def dr_reg(request):
    if request.method=='POST':
        fn =request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        bd=request.POST['birthday']
        gn=request.POST['gender']
        qf = request.POST['qualification']
        em = request.POST['email']
        st = request.POST['state']
        sz = request.POST['specialized']
        ep = request.POST['experience']
        lc = request.POST['license']
        hp = request.POST['hospital']
        fe = request.POST['fee']
        rc = request.POST['res_code']
        ct = request.POST['city']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        fp = request.POST['file_photo']
        fees=fe

        if pass1==pass2:
            user = data1(username=un, firstname=fn, lastname=ln, email=em, birthday=bd,profilePicture=fp,password = pass1, gender=gn,qualification=qf,state=st, specialized=sz,experience=ep,license=lc,hospital=hp,fee=fe,res_code=rc,city=ct)
            data  = User.objects.create_user(first_name=fn,last_name=ln,username = un,password = pass1,email = em)
            data.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request)

            subject = 'Activate your Account'

            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })


            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [em],
                fail_silently=False,
            )
            # amnt= data1.fee
            return redirect('index')
        else:
             print('password not match')
    else:
         return render(request, 'dr_reg.html')


def showdr(request,pk):
    pd = patient.objects.get(pk=pk)

    dd = data1.objects.filter(specialized=pd.disease)
    return render(request, 'showdr.html',{'x':dd})

def showpatient(request,pk):
    if request.method=='POST':
        x = merge.objects.get(pk=pk)
        z = x.p_email

        subject = 'hi'
        message = render_to_string('send_date_time.html', {
            'x': x,
        })
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            [z],
            fail_silently=False,
        )

    doc = merge.objects.all()
    return render(request, 'showpatient.html',{'doc':doc})

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')


def paymentMode(request, pk):
    ddata = data1.objects.get(pk=pk)
    current_user=patient.objects.last()
    print(current_user.name)
    m=merge(patient_id=current_user.id,doctor_id=ddata.pk,p_email=current_user.email,p_name=current_user.name,p_gender=current_user.gender,p_age=current_user.age,p_ph_no=current_user.ph_no,dr_name=ddata.firstname,dr_username=ddata.username,p_disease=current_user.disease,a_date=date.today(),a_time=datetime.now().time(),hospital_name=ddata.hospital)
    m.save()

    print("Data Saved !")
    param_dict = {
        "MID": "vkNHCP48516702847947",
        "ORDER_ID": (ddata.email),
        "CUST_ID": "101",
        "TXN_AMOUNT": str(ddata.fee),
        "CHANNEL_ID": "WEB",
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        #"CALLBACK_URL": "http/127.0.0.1:8000/handleRequest/",
        "CALLBACK_URL":"https://merchant.com/callback/"

    }
    param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,MERCHANT_KEY)

    return render(request,'paytm.html',{'params':param_dict})

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
    return redirect('/Thanks')

def UpdateProfile(view):
    pass
