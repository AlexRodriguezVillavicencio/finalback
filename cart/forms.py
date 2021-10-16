from django import forms
from .models import OrderItem, BebidaVariation, Product, PostreVariation, Address
from django.contrib.auth import get_user_model

User = get_user_model()

class AddToCartForm(forms.ModelForm):
    bebida = forms.ModelChoiceField(queryset=BebidaVariation.objects.none())
    postre = forms.ModelChoiceField(queryset=PostreVariation.objects.none())
    cantidad = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['cantidad', 'bebida', 'postre']

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        self.fields['bebida'].queryset = product.bebidas.all()
        self.fields['postre'].queryset = product.postres.all()

    def clean(self):
        product_id = self.product_id
        product = Product.objects.get(id=self.product_id)
        cantidad = self.cleaned_data['cantidad']

        if product.stock < cantidad:
            raise forms.ValidationError(f"The maximum stock is {product.stock}")



class AddressForm(forms.Form):
    
    shipping_address_line_1 = forms.CharField(required=False)

    shipping_zip_code = forms.CharField(required=False)
    shipping_city = forms.CharField(required=False)


    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )


    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id=user_id)

        shipping_address_qs = Address.objects.filter(
            user=user,
            address_type='S'
        )



        self.fields['selected_shipping_address'].queryset = shipping_address_qs
     


    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1', None):
                self.add_error("shipping_address_line_1", "lelne este campo")
            if not data.get('shipping_zip_code', None):
                self.add_error("shipping_zip_code", "lelne este campo")
            if not data.get('shipping_city', None):
                self.add_error("shipping_city", "lelne este campo")


