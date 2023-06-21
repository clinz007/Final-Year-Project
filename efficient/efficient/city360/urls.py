"""city360 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index),
    path('userreg',views.userreg),
    path('wrkreg',views.wrkreg),
    path('addworker',views.addworker),
    path('adduser',views.adduser),
    path('addcat',views.addcat),
    path('addsubcat',views.addsubcat),
    path('login',views.login),
    path('cat',views.cat),
    path('subcat',views.subcat),
    path('addlogin',views.addlogin),
    path('logout/',views.logout),
    path('prediction',views.prediction),
    path('pred',views.pred),
    path('viewusers',views.viewusers),
    path('viewworker',views.viewworker),
    path('ufeedback',views.ufeedback),
    path('adduserfdbk',views.adduserfdbk),
    path('addwrkrfdbk',views.addwrkrfdbk),
    path('wfeedback',views.wfeedback),
    path('viewfeedbacks',views.viewfeedbacks),
    path('viewwrkrs',views.viewwrkrs),
    path('viewbooking_admin',views.viewbooking_admin),
    path('v_book',views.v_book),
    path('viewwrkreport',views.viewwrkreport),
    path('report',views.report),
    path('viewbooking',views.viewbooking),
    path('uapprove/<int:id>',views.uapprove,name="uapprove"),
    path('wapprove/<int:id>',views.wapprove,name="wapprove"),
    path('gvreport/<int:id>',views.gvreport,name="gvreport"),
    path('gvreport/addreports',views.addreports,name="addreports"),
    path('pay/<int:id>',views.pay,name="pay"),
    path('pay/addpayment',views.addpayment,name="addpayment"),
    path('confirm/<int:id>',views.confirm,name="confirm"),
    path('reject/<int:id>',views.reject,name="reject"),
    path('book',views.book,name="book"),
    path('addbook',views.addbook),
    path('udelete/<int:id>',views.udelete),
    path('wdelete/<int:id>',views.wdelete),
    path('cancel/<int:id>',views.cancel),
    path('viewwrker/<str:wid>',views.viewwrker),
    path('uprofile',views.uprofile),
    path('wprofile',views.wprofile),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
