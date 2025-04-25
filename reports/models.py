from django.db import models
from django.conf import settings
from products.models import Product

class Report(models.Model):
    REPORT_CHOICES = (
        ('user', '사용자'),
        ('product', '상품'),
    )

    report_type = models.CharField(max_length=10, choices=REPORT_CHOICES)
    reason = models.TextField()
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reports_against_user'  # ✅ 명확하게 이름 변경
    )
    reported_product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.report_type == 'user' and self.reported_user:
            target = self.reported_user.username
        elif self.report_type == 'product' and self.reported_product:
            target = self.reported_product.name
        else:
            target = 'Unknown'
        return f"{self.reporter.username} → {self.report_type.upper()} ({target})"