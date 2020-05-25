
from django.contrib import admin
from django.urls import path,include


from diseasetables import views2
# from paygate.views import paymentMode
from webapp.views import ActivateAccount
from . import view, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from webapp import views
#from .settings import *
# from django.conf.urls.static import static
from .view import paymentMode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data1/', views.employeeList.as_view()),
    path('ds',views2.getDs,name='getds'),
    path('paymentMode/<int:pk>/', paymentMode, name='paymentMode'),
    #path('home',view.showpage,name='show'),
    #path('data', views1.data, name='data'),
    #path('data/<int:pk>/', views1.details, name='details'),
    #path('login', view.login, name='Login'),
    #path('drlogin', view.login, name='login'),
    # path('scale', view.scale, name='scale'),
    path('reqsend/<int:pk>', view.reqsend, name='reqsend'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # path('addition',views.addition,name='addition'),
    path('about', view.about, name='about'),
    path('index', view.index, name='index'),
    path('appointment', view.appointment, name='appointment'),
    path('contact', view.contact, name='contact'),
    path('scaling/<int:pk>', view.scaling, name='scaling'),
    path('drlogin', view.login, name='drlogin'),
    path('logout', view.logout, name='logout'),
    path('dr_reg', view.dr_reg, name='dr_reg'),
    path('showdr/<int:pk>', view.showdr, name='showdr'),
    path('showpatient', view.showpatient, name='showpatient'), 
    path('profile', view.profile, name='profile'),
   # path('send_date_time', view.send_date_time, name='profile'),
    # path('', include('send.urls')),
    #path('diseases', view.diseases, name='diseases'),
    # path('result',views.result,name="result"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
