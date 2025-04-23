from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Report(models.Model):
    REPORT_CHOICES = (
        ('user', '사용자'),
        ('product', '상품'),
    )

    report_type = models.CharField(max_length=10, choices=REPORT_CHOICES)
    reason = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reported_user')
    reported_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter.username} → {self.report_type}"