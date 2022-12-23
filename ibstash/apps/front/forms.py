from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'variant', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        self.fields['product'].widget.attrs.update({
            "class": "form-control selectpicker", "id": "exampleFormControlSelect1", "data-live-search": "true"})
        self.fields['variant'].widget.attrs.update({
            "class": "form-control selectpicker", "id": "exampleFormControlSelect1", "data-live-search": "true"})
        self.fields['quantity'].widget.attrs.update({"class": "form-control", "placeholder": "fill max threshold"})
        self.fields['variant'].queryset = initial.get('product').category.variant.all()

