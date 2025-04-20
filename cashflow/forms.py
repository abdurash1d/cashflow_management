from django import forms
from cashflow.models import CashFlow, Status, Type, Category, Subcategory


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'id_type'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'id_category'}),
            'subcategory': forms.Select(attrs={'class': 'form-control', 'id': 'id_subcategory'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'step': '0.01'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If this is an instance (editing existing record)
        if kwargs.get('instance'):
            instance = kwargs.get('instance')
            self.fields['category'].queryset = Category.objects.filter(type=instance.type)
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=instance.category)
        else:
            # For new records, initially limit choices
            self.fields['category'].queryset = Category.objects.none()
            self.fields['subcategory'].queryset = Subcategory.objects.none()
        
        # If data is submitted
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
                
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        transaction_type = cleaned_data.get('type')
        
        if category and transaction_type and category.type != transaction_type:
            self.add_error('category', 'Category must belong to the selected transaction type.')
        
        if subcategory and category and subcategory.category != category:
            self.add_error('subcategory', 'Subcategory must belong to the selected category.')
            
        return cleaned_data


class CashFlowFilterForm(forms.Form):
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
