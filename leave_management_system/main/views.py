from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .models import Leave
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import EmployeeSignUpForm








def home(request):
    return render(request, 'home.html')
def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_dashboard')  # Redirect to the employee dashboard after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'employee_login.html')
def employee_sign_up(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('employee_login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EmployeeSignUpForm()
    return render(request, 'employee_sign_up.html', {'form': form})
    
    
@login_required
def employee_dashboard(request):
    # Access the logged-in user's information
    username = request.user.username
    return render(request, 'employee_dashboard.html', {'username': username})
def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home') 
# @login_required
# def employee_dashboard(request):
#     return render(request, 'employee_dashboard.html', {'username': request.user.username})

@login_required
def apply_for_leave(request):
    if request.method == "POST":
        # Collect form data
        employee_id = request.user.id  # Use the logged-in user's ID
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        leave_type = request.POST.get("leave_type")
        reason = request.POST.get("reason")

        try:
            # Save leave request
            leave = Leave.objects.create(
                employee=request.user,  # Associate the leave with the logged-in user
                employee_id=employee_id,
                start_date=start_date,
                end_date=end_date,
                leave_type=leave_type,
                reason=reason,
                status="Pending",
            )
            leave.save()
            return render(request, 'leave_success.html', {"message": "Leave application submitted successfully!"})

        except Exception as e:
            return render(request, 'apply_for_leave.html', {"error": str(e)})

    return render(request, 'apply_for_leave.html', {"employee_id": request.user.id})

@login_required
def holidays_taken(request):
    # Fetch all leaves taken by the logged-in employee
    leaves = Leave.objects.filter(employee=request.user)
    leave_count = leaves.count()  # Count the total number of leaves taken
    return render(request, 'holidays_taken.html', {
        'leaves': leaves,
        'leave_count': leave_count,
    })
@login_required
def employee_dashboard(request):
    # Example dynamic data
    leave_count = 5  
    available_leaves = 10 
    pending_requests = 2  
    notifications = [
        "Company holiday announced for Dec 25."
    ]
    upcoming_holidays = [
        {"date": "2024-12-25", "name": "Christmas"},
        {"date": "2025-01-01", "name": "New Year"}
    ]
    department = "IT"  

    context = {
        "username": request.user.username,
        "leave_count": leave_count,
        "available_leaves": available_leaves,
        "pending_requests": pending_requests,
        "notifications": notifications,
        "upcoming_holidays": upcoming_holidays,
        "department": department,
    }

    return render(request, 'employee_dashboard.html', context)

@login_required
def all_leave_requests(request):
    # Fetch all leave requests from the database
    leave_requests = Leave.objects.all().order_by('-applied_on')  # Optionally, order by applied_on (latest first)
    
    # Pass the leave requests to the template
    return render(request, 'holidays_taken.html', {'leave_requests': leave_requests})

@user_passes_test(lambda user: user.is_superuser)
def all_leave_requests(request):
    # Fetch all leave requests from the database
    leave_requests = Leave.objects.all().order_by('-applied_on')  # Optionally, order by applied_on (latest first)
    
    # Pass the leave requests to the template
    return render(request, 'holidays_taken.html', {'leave_requests': leave_requests})
# def custom_admin_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.is_superuser:  # Ensure only superusers can log in
#             login(request, user)
#             return redirect('/admin/')  # Redirect to the Django admin panel
#         else:
#             messages.error(request, "Invalid credentials or you are not an admin.")
#     return render(request, 'admin_login.html')  # Render the custom admin login page





# Custom admin login view
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:  # Check if the user is an admin
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to custom admin dashboard
        else:
            messages.error(request, 'Invalid admin credentials.')

    return render(request, 'admin_login.html')

# Admin dashboard view (restricted to superusers)
# @user_passes_test(lambda user: user.is_superuser)
# def admin_dashboard(request):
#     leave_requests = Leave.objects.all().order_by('-applied_on')  # Fetch leave requests ordered by application date
#     return render(request, 'admin_dashboard.html', {'leave_requests': leave_requests})

# @user_passes_test(lambda user: user.is_superuser)
# def admin_dashboard(request):
#     leave_requests = Leave.objects.all().order_by('-applied_on')
#     return render(request, 'admin_dashboard.html', {'leave_requests': leave_requests})
# from django.shortcuts import render, redirect
# from .models import Leave
# from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    leave_requests = Leave.objects.all().order_by('-applied_on')
    
    # Handle the approve or cancel action from the forms
    if request.method == "POST":
        if "approve_leave" in request.POST:
            leave_id = request.POST.get('leave_id')
            leave = Leave.objects.get(id=leave_id)
            leave.status = "Approved"
            leave.save()
        elif "cancel_leave" in request.POST:
            leave_id = request.POST.get('leave_id')
            leave = Leave.objects.get(id=leave_id)
            leave.status = "Cancelled"
            leave.save()

    context = {'leave_requests': leave_requests}
    return render(request, 'admin_dashboard.html', context)


@user_passes_test(lambda user: user.is_superuser)
def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    
    if leave.status == "Pending":  # Only approve if the status is "Pending"
        leave.status = "Approved"
        leave.save()
    
    return redirect('admin_dashboard')  # Redirect back to admin dashboard after update

# Function to cancel a leave request
@user_passes_test(lambda user: user.is_superuser)
def cancel_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    
    if leave.status == "Pending":  # Only cancel if the status is "Pending"
        leave.status = "Cancelled"
        leave.save()
    
    return redirect('admin_dashboard')

def leave_success(request):
    return render(request, 'leave_success.html', {'message': 'Leave application submitted successfully!'})

def leaves_taken_view(request):
    # Assuming you have a Leave model
    leaves = Leave.objects.filter(employee=request.user)
    approved_leaves = leaves.filter(status='Approved')  # Only count approved leaves
    leave_count = approved_leaves.count()

    return render(request, 'leaves_taken.html', {
        'leaves': leaves,
        'leave_count': leave_count
    })
