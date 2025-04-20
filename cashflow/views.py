from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import CashFlowForm, CashFlowFilterForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm


# Cash Flow Record Views
def cashflow_list(request):
    """View for listing all cash flow records with optional filtering"""
    cashflows = CashFlow.objects.all()
    form = CashFlowFilterForm(request.GET)
    
    if form.is_valid():
        # Apply filters
        if form.cleaned_data.get('date_from'):
            cashflows = cashflows.filter(date__gte=form.cleaned_data['date_from'])
        if form.cleaned_data.get('date_to'):
            cashflows = cashflows.filter(date__lte=form.cleaned_data['date_to'])
        if form.cleaned_data.get('status'):
            cashflows = cashflows.filter(status=form.cleaned_data['status'])
        if form.cleaned_data.get('type'):
            cashflows = cashflows.filter(type=form.cleaned_data['type'])
        if form.cleaned_data.get('category'):
            cashflows = cashflows.filter(category=form.cleaned_data['category'])
        if form.cleaned_data.get('subcategory'):
            cashflows = cashflows.filter(subcategory=form.cleaned_data['subcategory'])
    
    context = {
        'cashflows': cashflows,
        'filter_form': form,
    }
    return render(request, 'cashflow/cashflow_list.html', context)


def cashflow_create(request):
    """View for creating a new cash flow record"""
    if request.method == 'POST':
        form = CashFlowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cash flow record created successfully!')
            return redirect('cashflow:cashflow_list')
    else:
        form = CashFlowForm()
    
    context = {
        'form': form,
        'title': 'Create Cash Flow Record',
    }
    return render(request, 'cashflow/cashflow_form.html', context)


def cashflow_edit(request, pk):
    """View for editing an existing cash flow record"""
    cashflow = get_object_or_404(CashFlow, pk=pk)
    
    if request.method == 'POST':
        form = CashFlowForm(request.POST, instance=cashflow)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cash flow record updated successfully!')
            return redirect('cashflow:cashflow_list')
    else:
        form = CashFlowForm(instance=cashflow)
    
    context = {
        'form': form,
        'title': 'Edit Cash Flow Record',
        'cashflow': cashflow,
    }
    return render(request, 'cashflow/cashflow_form.html', context)


def cashflow_delete(request, pk):
    """View for deleting a cash flow record"""
    cashflow = get_object_or_404(CashFlow, pk=pk)
    
    if request.method == 'POST':
        cashflow.delete()
        messages.success(request, 'Cash flow record deleted successfully!')
        return redirect('cashflow:cashflow_list')
    
    context = {
        'cashflow': cashflow,
    }
    return render(request, 'cashflow/cashflow_delete.html', context)


# Dictionary Management Views
def dictionaries(request):
    """Main view for managing dictionaries"""
    context = {
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
    }
    return render(request, 'cashflow/dictionaries.html', context)


# Status Views
def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'cashflow/status_list.html', {'statuses': statuses})


def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status created successfully!')
            return redirect('cashflow:status_list')
    else:
        form = StatusForm()
    
    context = {
        'form': form,
        'title': 'Create Status',
    }
    return render(request, 'cashflow/status_form.html', context)


def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status updated successfully!')
            return redirect('cashflow:status_list')
    else:
        form = StatusForm(instance=status)
    
    context = {
        'form': form,
        'title': 'Edit Status',
        'status': status,
    }
    return render(request, 'cashflow/status_form.html', context)


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    
    if request.method == 'POST':
        try:
            status.delete()
            messages.success(request, 'Status deleted successfully!')
        except Exception as e:
            messages.error(request, f'Cannot delete status because it is being used. Error: {str(e)}')
        return redirect('cashflow:status_list')
    
    context = {
        'status': status,
    }
    return render(request, 'cashflow/status_delete.html', context)


# Type Views
def type_list(request):
    types = Type.objects.all()
    return render(request, 'cashflow/type_list.html', {'types': types})


def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Type created successfully!')
            return redirect('cashflow:type_list')
    else:
        form = TypeForm()
    
    context = {
        'form': form,
        'title': 'Create Type',
    }
    return render(request, 'cashflow/type_form.html', context)


def type_edit(request, pk):
    transaction_type = get_object_or_404(Type, pk=pk)
    
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=transaction_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Type updated successfully!')
            return redirect('cashflow:type_list')
    else:
        form = TypeForm(instance=transaction_type)
    
    context = {
        'form': form,
        'title': 'Edit Type',
        'type': transaction_type,
    }
    return render(request, 'cashflow/type_form.html', context)


def type_delete(request, pk):
    transaction_type = get_object_or_404(Type, pk=pk)
    
    if request.method == 'POST':
        try:
            transaction_type.delete()
            messages.success(request, 'Type deleted successfully!')
        except Exception as e:
            messages.error(request, f'Cannot delete type because it is being used. Error: {str(e)}')
        return redirect('cashflow:type_list')
    
    context = {
        'type': transaction_type,
    }
    return render(request, 'cashflow/type_delete.html', context)


# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'cashflow/category_list.html', {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('cashflow:category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Create Category',
    }
    return render(request, 'cashflow/category_form.html', context)


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('cashflow:category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Edit Category',
        'category': category,
    }
    return render(request, 'cashflow/category_form.html', context)


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        try:
            category.delete()
            messages.success(request, 'Category deleted successfully!')
        except Exception as e:
            messages.error(request, f'Cannot delete category because it is being used. Error: {str(e)}')
        return redirect('cashflow:category_list')
    
    context = {
        'category': category,
    }
    return render(request, 'cashflow/category_delete.html', context)


# Subcategory Views
def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'cashflow/subcategory_list.html', {'subcategories': subcategories})


def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory created successfully!')
            return redirect('cashflow:subcategory_list')
    else:
        form = SubcategoryForm()
    
    context = {
        'form': form,
        'title': 'Create Subcategory',
    }
    return render(request, 'cashflow/subcategory_form.html', context)


def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory updated successfully!')
            return redirect('cashflow:subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    
    context = {
        'form': form,
        'title': 'Edit Subcategory',
        'subcategory': subcategory,
    }
    return render(request, 'cashflow/subcategory_form.html', context)


def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    
    if request.method == 'POST':
        try:
            subcategory.delete()
            messages.success(request, 'Subcategory deleted successfully!')
        except Exception as e:
            messages.error(request, f'Cannot delete subcategory because it is being used. Error: {str(e)}')
        return redirect('cashflow:subcategory_list')
    
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'cashflow/subcategory_delete.html', context)


# API Views for AJAX
def get_categories(request, type_id):
    """API endpoint to get categories for a specific type"""
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)


def get_subcategories(request, category_id):
    """API endpoint to get subcategories for a specific category"""
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
