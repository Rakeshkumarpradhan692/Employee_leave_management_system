from django.db import models
from django.contrib.auth.models import User

class Leave(models.Model):
    LEAVE_TYPES = [
        ('Sick', 'Sick Leave'),
        ('Casual', 'Casual Leave'),
        ('Earned', 'Earned Leave'),
        ('Maternity', 'Maternity Leave'),
        ('Paternity', 'Paternity Leave'),
        ('Vacation', 'Vacation Leave'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)  # Relation with User
    employee_unique_id = models.CharField(max_length=20)  # Renamed employee ID field
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)  # Added choices for leave types
    reason = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    applied_on = models.DateTimeField(auto_now_add=True)  # Timestamp when the leave is applied

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type}"
    
   
