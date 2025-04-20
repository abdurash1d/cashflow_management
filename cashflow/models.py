import datetime

from django.db import models
from django.core.validators import MinValueValidator


class Status(models.Model):
    """
    Model representing the status of a cash flow transaction.
    Example: Business, Personal, Tax
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Statuses"


class Type(models.Model):
    """
    Model representing the type of cash flow transaction.
    Example: Income, Expense
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Model representing a category for cash flow transactions.
    Categories are linked to specific transaction types.
    Example: Infrastructure, Marketing
    """
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    
    def __str__(self):
        return f"{self.name} ({self.type.name})"
    
    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ['name', 'type']


class Subcategory(models.Model):
    """
    Model representing a subcategory for cash flow transactions.
    Subcategories are linked to specific categories.
    Example: VPS, Proxy (for Infrastructure)
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"
    
    class Meta:
        verbose_name_plural = "Subcategories"
        unique_together = ['name', 'category']


class CashFlow(models.Model):
    """
    Model representing a cash flow transaction with all required fields.
    """
    date = models.DateField()  # Remove auto_now_add=True to make it editable
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # This tracks when record was created
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.date} - {self.type.name} - {self.amount} ₽"
    
    class Meta:
        verbose_name_plural = "Cash Flow Records"
        ordering = ['-date']


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Set default date to today for new records
    if not kwargs.get('instance'):
        self.fields['date'].initial = datetime.date.today()
