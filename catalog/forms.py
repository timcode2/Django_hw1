from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')

        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for word in prohibited_words:
            if word in cleaned_name.lower():
                raise forms.ValidationError('Запретное слово в названии товара')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')

        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for word in prohibited_words:
            if word in cleaned_description.lower():
                raise forms.ValidationError('Запретное слово в описании товара')

        return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
