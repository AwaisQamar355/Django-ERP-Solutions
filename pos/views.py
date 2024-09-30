# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from pos.models import (
    Category,
    RefPartyType, 
    RefPartyProfile,
    StockType,
    StockInHand,
    StockPurchaseMain,
    StockPurchaseDetail,
    StockSaleMain,
    StockSaleDetail,
    Units,
)
from datetime import datetime
from django.db.models import Count,F, Sum ,Q
from django.contrib.auth.decorators import login_required 
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets , generics
from rest_framework.views import APIView
from rest_framework.response import Response 
from pos.serializers import StockTypeSerializer, StockInHandSerializer, UnitSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.db import transaction
from rest_framework.permissions import AllowAny

from pos.print_views import generate_invoice_pdf
from datetime import timedelta




x = datetime.now() 
date = x.strftime('%Y-%m-%d')

x = datetime.now()
y = x.strftime('%Y-%m-%d')
# -----------------------------------------------------------------------------------------------------
# Home
# -----------------------------------------------------------------------------------------------------
def home(request):
    return render(request,'before_login/home.html')
# -----------------------------------------------------------------------------------------------------
# Dashboard , pos
# -----------------------------------------------------------------------------------------------------
@login_required(login_url='/home')
def dashboard(request):
    user = request.user
    low_stock = StockInHand.objects.filter(stock_in_hand__lt= 10)
    today_purchase = StockPurchaseMain.objects.filter(Bill_date__date=date).count()
    today_sale = StockSaleMain.objects.filter(invoice_date__date=date).count()
    ten_days_ago = timezone.now() - timedelta(days=10)

    last_ten_days_sale = StockSaleMain.objects.filter(
    created_on__gte=ten_days_ago
        ).values(
        'invoice_no',
        'created_on__date',
        ).annotate(
            total_amount=(Sum(F('sale_detail__quantity') * F('sale_detail__price'))-F('discount'))
        )
    print(last_ten_days_sale)

   
    return render(request,'dashboard.html',{'user':user, 'low_stock':low_stock, 'today_purchase':today_purchase, 'today_sale':today_sale})

@login_required(login_url="/home")
def pos(request):
    customer_list = RefPartyProfile.objects.filter(ref_party_type_id=123)
    return render(request, "pos/pos.html",{"customer_list":customer_list, "date":date})
