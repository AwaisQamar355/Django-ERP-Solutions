from django.contrib import admin
from pos.models import *



@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(StockType)
class StockTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(RefPartyType)
class RefPartyTypeAdmin(admin.ModelAdmin):
    list_display = ["description"]

@admin.register(StockInHand)
class StockInHandAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(StockPurchaseMain)
class StockPurchaseMainAdmin(admin.ModelAdmin):
    list_display = ["bill_no"]

@admin.register(StockPurchaseDetail)
class StockPurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ["stock_purchase_main"]


@admin.register(StockSaleMain)
class StockSaleMainAdmin(admin.ModelAdmin):
    list_display = ["invoice_no"]


@admin.register(StockSaleDetail)
class StockSaleDetailAdmin(admin.ModelAdmin):
    list_display = ["stock_sale_main"]

