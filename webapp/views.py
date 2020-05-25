from __future__ import unicode_literals

# Create your views here.
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View

from diagno.view import login
from webapp.models import data1
from django.contrib.auth.models import User

from webapp.token import account_activation_token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import patient
from .serializers import data1Serializer
from rest_framework import viewsets

# Create your views here.
class employeeList(APIView):
    def get(self,request):
        employee1=patient.objects.all()
        serializer=data1Serializer(employee1,many=True)
        return Response(serializer.patient)

    def post(self):
        pass


# class employeeListPost(APIView):
# def post(self, request):
# serializer = employeeSerializer(data=request.data)
# if serializer.is_valid():
# serializer.save()
# return Response(serializer.data, status=status.HTTP_201_CREATED)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # @api_view(['GET', 'PUT', 'DELETE'])
 # def detail(request, pk):
 #        """
 #        Retrieve, update or delete a code snippet.
 #        """
 #
 #   try:
 #        data1 = employees.objects.get(pk=pk)
 #    except employees.DoesNotExist:
 #        return Response(status=status.HTTP_404_NOT_FOUND)
 #    if request.method == 'GET':
 #        serializer = employeeSerializer(data1)
 #               return Response(serializer.data)
 #    elif request.method == 'PUT':
 #    serializer = employeeSerializer(data1, data=request.data)
 #    if serializer.is_valid():
 #        serializer.save()
 #    return Response(serializer.data)
 #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #    elif request.method == 'DELETE':
 #    data1.delete()
 #    return Response(status=status.HTTP_204_NO_CONTENT)


def Sign_up(request):

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
        if pass1==pass2:
            user = data1(username=un, firstname=fn, lastname=ln, email=em, birthday=bd,password = pass1, gender=gn,qualification=qf,state=st, specialized=sz,experience=ep,license=lc,hospital=hp,fee=fe,res_code=rc,city=ct)
            data  = User.objects.create_user(username = un,password = pass1,email = em)
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
            return redirect('dhome')
        else:
             print('password not match')
    else:
         return render(request, 'Signup.html')


class ActivateAccount(View):
    def get(self,request,uidb64,token, *args, **kwargs):
        try:
            #uid =force_text(urlsafe_base64_decode(uidb64)
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user=None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active =True
            user.save()
            login(request)
            messages.success(request, ('Your Account have been confirmed.'))
            print("Confirmed",user.is_active)
            return render(request,'dhome.html')
        else:
            messages.warning(request, ('The confirmation link was invalid'))
            return redirect('/')


