from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pos_admin.models import * 
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .models import EmailLog
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import socket
x = datetime.now() 
date = x.strftime('%Y-%m-%d')
x = datetime.now()
y = x.strftime('%Y-%m-%d')
@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard_pos.html')
#=========================USER===================
User = get_user_model()
@login_required
def user_list(request):
    users = AdminUser.objects.all()
    query = request.GET.get('q')
    if query:
        users = users.filter(username__icontains=query) 
    return render(request, 'admin/user/user_list.html', {'users': users})
@login_required
def add_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        status = request.POST.get('status_val')  
        # Split the full_name into first_name and last_name
        names = full_name.split(' ', 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ''
        
        is_super_admin = True
    if AdminUser.objects.filter(user_id=user_id).exists() or AdminUser.objects.filter(username=username).exists():
            messages.error(request, 'Username or User ID already exists!')
    else:
        user = AdminUser.objects.create(
            user_id=user_id,
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            status=status, 
        )
        user.is_super_admin = is_super_admin
        user.save()
        return redirect('user_list')
    return render(request, 'admin/user/user_list.html')
# views.py
@login_required
@require_POST
def activate_user(request):
    user_id = request.POST.get('user_id')
    try:
        user = AdminUser.objects.get(id=user_id)
        user.status = True  # Set status to active
        user.save()
        return HttpResponse('User activated successfully')
    except AdminUser.DoesNotExist:
        return HttpResponse('User not found', status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)

@login_required
@require_POST
def deactivate_user(request):
    user_id = request.POST.get('user_id')
    try:
        user = AdminUser.objects.get(id=user_id)
        user.status = False  # Set status to inactive
        user.save()
        return HttpResponse('User deactivated successfully')
    except AdminUser.DoesNotExist:
        return HttpResponse('User not found', status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)

@login_required

def user_update(request, user_id):
    user = get_object_or_404(AdminUser, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        user.first_name, user.last_name = full_name.split(' ', 1)
        user.phone_number = request.POST.get('phone_number')
        # user.role = request.POST.get('role')   
        user.status = request.POST.get('status') == 'True'
        
        password = request.POST.get('password')
        
        user.save()
        return redirect('user_list')
    return render(request, 'admin/user/update_user.html', {'user': user})

@login_required
def toggle_user_status(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(AdminUser, pk=user_id)
        user.is_active = not user.is_active
        user.save()
        status = 'activated' if user.is_active else 'deactivated'
        # messages.success(request, f'User has been {status} successfully.')
    return redirect('user_list')

#======================COMPANY=========================
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'admin/company/company_list.html', {'companies': companies})
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'admin/company/company_detail.html', {'company': company})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from django.contrib.auth.decorators import login_required

@login_required
def company_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        company_id = request.POST['company_id']
        contact_person_name = request.POST['contact_person_name']
        contact_email = request.POST['contact_email']
        contact_phone_number = request.POST['contact_phone_number']
        address = request.POST['address']
        company_type = request.POST['company_type']
        registration_number = request.POST['registration_number']
        tax_identification_number = request.POST['tax_identification_number']
        industry_type = request.POST['industry_type']
        date_of_establishment = request.POST['date_of_establishment']
        number_of_employees = request.POST['number_of_employees']
        business_hours = request.POST['business_hours']
        website_url = request.POST['website_url']
        social_media_links = request.POST['social_media_links']
        additional_notes = request.POST['additional_notes']
        is_active = 'is_active' in request.POST
        logo = request.FILES.get('logo')
        
        if Company.objects.filter(company_id=company_id).exists():
            messages.error(request, 'Company ID already exists!')        
            return render(request, 'admin/company/add_company.html')

        else:
            company = Company.objects.create(
                name=name,
                company_id=company_id,
                contact_person_name=contact_person_name,
                contact_email=contact_email,
                contact_phone_number=contact_phone_number,
                address=address,
                company_type=company_type,
                registration_number=registration_number,
                tax_identification_number=tax_identification_number,
                industry_type=industry_type,
                date_of_establishment=date_of_establishment,
                number_of_employees=number_of_employees,
                business_hours=business_hours,
                website_url=website_url,
                social_media_links=social_media_links,
                additional_notes=additional_notes,
                is_active=is_active,
                logo=logo,
            )
            messages.success(request, 'Company added successfully!')
            return redirect('company_list') 

    return render(request, 'admin/company/add_company.html')

def update_company(request, company_id):
    company = get_object_or_404(Company, company_id=company_id)

    if request.method == 'POST':
        company.name = request.POST['name']
        company.contact_person_name = request.POST['contact_person_name']
        company.contact_email = request.POST['contact_email']
        company.contact_phone_number = request.POST['contact_phone_number']
        company.address = request.POST['address']
        company.company_type = request.POST['company_type']
        company.registration_number = request.POST['registration_number']
        company.tax_identification_number = request.POST['tax_identification_number']
        company.industry_type = request.POST['industry_type']
        company.date_of_establishment = request.POST['date_of_establishment']
        company.number_of_employees = request.POST['number_of_employees']
        company.business_hours = request.POST['business_hours']
        company.website_url = request.POST['website_url']
        company.social_media_links = request.POST['social_media_links']
        company.additional_notes = request.POST['additional_notes']
        company.is_active = 'is_active' in request.POST
  
        if 'logo' in request.FILES:
            company.logo = request.FILES['logo']

        company.save()
        # messages.success(request, 'Company updated successfully!')
        return redirect('company_list')  
    context = {
        'company': company
    }
    return render(request, 'admin/company/update_company.html', context)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Company

@login_required
@require_POST
def activate_company(request):
    company_id = request.POST.get('company_id')
    try:
        company = Company.objects.get(id=company_id)
        company.is_active = True  # Correct field name
        company.save()
        return HttpResponse('company activated successfully')
    except Company.DoesNotExist:
        return HttpResponse('company not found', status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)

@login_required
@require_POST
def deactivate_company(request):
    company_id = request.POST.get('company_id')
    try:
        company = Company.objects.get(id=company_id)
        company.is_active = False  # Correct field name
        company.save()
        return HttpResponse('company deactivated successfully')
    except Company.DoesNotExist:
        return HttpResponse('company not found', status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)

#=======================PAYMENT=========================

def add_payment(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        # company_name = request.POST.get('company_name')
        owner_name = request.POST.get('owner_name')
        payment_date = request.POST.get('payment_date')
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id')
        payment_status = request.POST.get('payment_status')
        notes = request.POST.get('notes')
        
        Payment.objects.create(
            company_id=company_id,
            
            owner_name=owner_name,
            payment_date=payment_date,
            amount=amount,
            payment_method=payment_method,
            transaction_id=transaction_id,
            payment_status=payment_status,
            notes=notes
        )
        
        return redirect('payment_list')
    
    companies = Company.objects.all()
    return render(request, 'admin/payments/add_payment.html', {'companies': companies})

def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    companies = Company.objects.all()
    
    if request.method == 'POST':
        payment.company_id = request.POST.get('company_id')
        # payment.company_name = request.POST.get('company_name')
        payment.owner_name = request.POST.get('owner_name')
        payment.payment_date = request.POST.get('payment_date')
        payment.amount = request.POST.get('amount')
        payment.payment_method = request.POST.get('payment_method')
        payment.transaction_id = request.POST.get('transaction_id')
        payment.payment_status = request.POST.get('payment_status')
        payment.notes = request.POST.get('notes')
        
        payment.save()
        return redirect('payment_list')
    
    return render(request, 'admin/payments/updata_payment.html', {'payment': payment, 'companies': companies})

def generate_invoice(request, payment_id):
    payment = get_object_or_404(Payment, payment_id=payment_id)
    html_string = render_to_string('admin/payments/invoice.html', {'payment': payment})
    html = HTML(string=html_string)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=invoice_{payment.payment_id}.pdf'
    html.write_pdf(response)
    return response 
def financial_report(request):
    payments = Payment.objects.all()
    total_amount = payments.aggregate(total=models.Sum('amount'))['total']
    context = {
        'payments': payments,
        'total_amount': total_amount,
    }
    return render(request, 'admin/payments/financial_report.html', context)

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'admin/payments/payment_list.html', {'payments': payments})

#====================EMAIL======================

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import AdminUser, EmailLog, Attachment
import socket

def send_email(request, user_id):
    # Retrieve the user based on user_id
    user = get_object_or_404(AdminUser, id=user_id)

    if request.method == 'POST':
        # Extract form data from POST request
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message_body')
        attachments = request.FILES.getlist('attachments')
        email_template = request.POST.get('email_template')
        priority_level = request.POST.get('priority_level')
        cc = request.POST.get('cc')
        bcc = request.POST.get('bcc')
        personalization_tags = request.POST.get('personalization_tags')

        errors = []

        # Validate required fields
        if not recipient:
            errors.append('Recipient email address is required.')
        if not subject:
            errors.append('Subject is required.')
        if not message_body:
            errors.append('Message body is required.')

        if errors:
            # If there are validation errors, display error messages
            for error in errors:
                messages.error(request, error)
        else:
            try:
                # Create EmailMessage instance
                email = EmailMessage(
                    subject,
                    message_body,
                    'your_email@example.com',  # Replace with your actual email
                    [recipient],
                    cc=[cc] if cc else [],
                    bcc=[bcc] if bcc else []
                )

                # Attach files to the email if any
                for attachment in attachments:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)

                # Send the email
                email.send()

                # Create EmailLog instance to log the sent email
                email_log = EmailLog.objects.create(
                    user=user,
                    recipient=recipient,
                    subject=subject,
                    message_body=message_body,
                    email_template=email_template,
                    priority_level=priority_level,
                    cc=cc,
                    bcc=bcc,
                    personalization_tags=personalization_tags
                )

                # Create Attachment instances for each attached file
                for attachment in attachments:
                    Attachment.objects.create(email_log=email_log, file=attachment)

                # Optionally, add a success message (uncomment the line below)
                # messages.success(request, 'Email sent successfully!')

                # Redirect to a success page or another view after sending the email
                return redirect('email_success')  # Adjust this as per your URL configuration

            except socket.gaierror as e:
                # Handle DNS errors
                messages.error(request, 'A DNS error occurred while sending the email: {}. Please check the recipient\'s email address and try again.'.format(str(e)))
            except ValueError as e:
                # Handle specific value errors
                messages.error(request, str(e))
            except Exception as e:
                # Handle any other exceptions
                messages.error(request, 'An error occurred: {}'.format(str(e)))

    # Render the send_email form template with the user object
    return render(request, 'admin/communication/send_email.html', {'user': user})

def email_success(request):
    return render(request, 'admin/communication/email_success.html')

def email_log_list(request):
    logs = EmailLog.objects.all()
    print(logs)
    return render(request, 'admin/communication/email_logs.html', {'logs': logs})
# views.py

def email_log_detail(request, user_id):
    # Retrieve the AdminUser instance based on user_id
    user = get_object_or_404(AdminUser, user_id=user_id)
    
    # Retrieve email logs related to the user's user_id
    logs = EmailLog.objects.filter(user=user)
    
    context = {
        'user': user,
        'logs': logs,
    }
     
    return render(request, 'admin/user/user_detail.html', context)