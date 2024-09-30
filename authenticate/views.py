from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/pos_admin/admin_dashboard/')
        else:
            return redirect('/pos/dashboard/')
    
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return redirect('/pos_admin/admin_dashboard/')
                else:
                    return redirect('/pos/dashboard/')
            else:
                message = 'Account temporarily blocked.'
        else:
            message = 'Invalid username or password.'
    
    return render(request, 'login.html', {'message': message})
 
def user_logout(request):
    logout(request)
    return redirect('login/')

# --------------------------------------------------------------------------------------
# User
# ---------------------------------------------------------------------------------
# @login_required(login_url='/login')
# def user_page(request):
#     username = request.user.username
#     return render(request, 'Admin_Penal/User/users.html', {'username': username})


# Insert User
# def insert_user(request):
#     if request.method == "POST":
#         Name = request.POST['Name']
#         Email = request.POST['Email']
#         Login_Name = request.POST['Login_Name']
#         Password = request.POST['Password']
#         super_admin = 1
#         ins = User.objects.create_user(first_name=Name, email=Email, username=Login_Name, password=Password,
#                                        is_superuser=super_admin)
#         ins.save()
#         # send_mail(
#         #     'Test Mail',
#         #     'It is testing email',
#         #     'junaidanwar080@gmail.com',
#         #     [Email],
#         # )
#         return JsonResponse('User Created', safe=False)


# Select User
# def select_all_users(request):
#     allusers = User.objects.all()
#     return render(request, 'Admin_Penal/User/select_all_users.html', {'User_table': allusers})


# def user_profile_load_for_update(request, user_id):
#     # print('came here')
#     user_data = User.objects.get(id=user_id)
#     return JsonResponse(model_to_dict(user_data))


# def update_user_profile(request):
#     if request.method == "POST":
#         edit_user_id = request.POST['edit_user_id']
#         edit_first_name = request.POST['edit_first_name']
#         edit_last_name = request.POST['edit_last_name']
#         edit_user_name = request.POST['edit_username']
#         user_id = User.objects.get(id=edit_user_id)
#         user_id.username = edit_user_name
#         user_id.first_name = edit_first_name
#         user_id.last_name = edit_last_name
#         user_id.save()
#         return JsonResponse("User Data Updated", safe=False)

