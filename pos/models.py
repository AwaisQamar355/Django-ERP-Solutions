from django.db import models
from django.contrib.auth.models import User


# Category
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50) 
    description= models.TextField(null=True, max_length=50)
    is_active =  models.BooleanField(default=True)
    created_on  = models.DateField(blank=True, null=True)
    updated_on = models.DateField(blank=True, null=True)
    def __str__(self):
       return str(self.category_id)


#--------------------------------------------------------------------    
# Party    
#--------------------------------------------------------------------
    
# Party Type Model
class RefPartyType(models.Model):
    party_type_code = models.CharField(primary_key=True,max_length = 5)
    description = models.CharField(max_length = 200, null=True)
    is_enabled = models.CharField(max_length = 1, null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_party_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_party_type' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
# Party Profile Model
class RefPartyProfile(models.Model):
    party_code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    address = models.CharField(max_length = 500, null=True)
    ntn_no = models.CharField(max_length = 50, null=True)
    phone_no = models.CharField(max_length = 50, null=True)
    description = models.CharField(max_length = 500, null=True)
    payment_terms = models.CharField(max_length = 500, null=True)
    ref_party_type = models.ForeignKey(
        'RefPartyType', 
        related_name='party_profile',
        null=True,
        on_delete=models.CASCADE,
    )
    # chart_of_account = models.ForeignKey(
    #     'ChartOfAccount', 
    #     related_name='ref_party_profile',
    #     null=True,
    #     on_delete=models.CASCADE,
    # )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_party_profile',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_party_profile' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
#--------------------------------------------------------------------    
#Vouchers    
#--------------------------------------------------------------------
# Voucher Type
class RefVoucherType(models.Model):
    voucher_type_code = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True)
    is_enabled = models.CharField(max_length=1,null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_ref_voucher_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_ref_voucher_type' ,
        null=True,
        on_delete=models.CASCADE,
    )
    
# -------------------------------------------------------------------------------
# Stock Management System
# -------------------------------------------------------------------------------
# Stock Type
class StockType(models.Model):
    stock_type_code = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 200, null=True)
    is_enabled = models.CharField(max_length = 1, null=True)
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_type',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_type' ,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
    
#stock in hand
class StockInHand(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 200, null=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    purchase_price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    stock_in_hand = models.IntegerField(default = 0, null=True)
    order_threshold = models.CharField(max_length = 18, null=True)
    unit = models.ForeignKey(
        'Units',  # Assuming 'Units' is the name of your Units model
        related_name='stock_in_hand',
        null=True,
        blank=True,  # You can choose whether this field can be blank or not based on your requirements
        on_delete=models.CASCADE,  # or SET_DEFAULT, SET(...) depending on how you want to handle Units deletion
    )
    
    stock_type = models.ForeignKey(
        'StockType', 
        related_name='stock_in_hand' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_in_hand',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_in_hand' ,
        null=True,
        on_delete=models.CASCADE,
    )

# --------------------------------------------------------------------------
# Sale
# -------------------------------------------------------------------------
#Stock Sale Main
class StockSaleMain(models.Model):
    invoice_no = models.BigAutoField(primary_key=True)
    invoice_date = models.DateTimeField( null=True)
    ref_party_profile = models.ForeignKey(
        'RefPartyProfile', 
        related_name='stock_sale_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_sale_main',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_sale_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    discount = models.IntegerField(null=True)
    
    
#Stock Sale Details
class StockSaleDetail(models.Model):
    stock_sale_main = models.ForeignKey(
        'StockSaleMain', 
        related_name='sale_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    stock_in_hand = models.ForeignKey(
        'StockInHand', 
        related_name='stock_sale_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=13, decimal_places=3,null=True)

# -------------------------------------------------------------------
# Purchase 
# ------------------------------------------------------------------
# Stock Purchase Main
class StockPurchaseMain(models.Model):
    bill_no = models.CharField(primary_key=True , max_length = 20)
    Bill_date = models.DateTimeField( null=True)
    ref_party_profile = models.ForeignKey(
        'RefPartyProfile', 
        related_name='stock_purchase_main' ,
        null=True,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField( auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='created_stock_purchase_main',
        null=True,
        on_delete=models.CASCADE,
    )
    updated_on = models.DateTimeField( auto_now=True)
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_stock_purchase_main' ,
        null=True,
        on_delete=models.CASCADE,
    ) 
    
# Stock Purchase Details
class StockPurchaseDetail(models.Model):
    stock_purchase_main = models.ForeignKey(
        'StockPurchaseMain', 
        related_name='purchase_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    stock_in_hand = models.ForeignKey(
        'StockInHand', 
        related_name='stock_purchase_detail' ,
        null=True,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    

class Units(models.Model):
    name = models.CharField(max_length = 50)