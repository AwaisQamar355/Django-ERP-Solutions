# views.py
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from pos.models import StockSaleDetail, StockSaleMain , StockPurchaseDetail, StockPurchaseMain

def generate_bill_pdf(request, bill_no):
    user = request.user
    total_prices = []
    select_main = StockPurchaseMain.objects.get(bill_no=bill_no)
    select_details = StockPurchaseDetail.objects.filter(stock_purchase_main_id=bill_no)
    for i in select_details:
        i.total_price = (i.quantity * i.price)
        total_prices.append(i.total_price)
    total_price_sum = sum(total_prices)
    html_string = render_to_string('pos/purchase/print_bill.html', {
        'select_main': select_main,
        'select_details': select_details,
        'total_price_sum': total_price_sum,
        'store_name':user
    })
    # Convert the rendered HTML to PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    # Create a response object and attach the PDF file
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="purchase_bill.pdf"'
    return response



def generate_invoice_pdf(request, invoice_no):
    print('came here2')
    user = request.user
    total_prices = []
    select_main = StockSaleMain.objects.get(invoice_no=invoice_no)
    select_details = StockSaleDetail.objects.filter(stock_sale_main_id=invoice_no)
    for i in select_details:
        i.total_price = (i.quantity * i.price)
        total_prices.append(i.total_price)
    total_price_sum = sum(total_prices)
    net_amount = total_price_sum - select_main.discount
    html_string = render_to_string('pos/sale/print_invoice.html', {
        'select_main': select_main,
        'select_details': select_details,
        'total_price_sum': total_price_sum,
        'net_amount':net_amount,
        'store_name':user
    })
    # Convert the rendered HTML to PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    # Create a response object and attach the PDF file
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="purchase_bill.pdf"'
    return response