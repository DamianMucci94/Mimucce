from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre del titular de la tarjeta")
    card_number = forms.CharField(max_length=16, label="Número de tarjeta")
    expiration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de vencimiento")
    cvv = forms.CharField(max_length=4, label="CVV")  # Máximo 4 dígitos para tarjetas Amex, 3 para otras
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto")

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if card_number is None or not card_number.isdigit() or len(card_number) not in [15, 16]:  # Validar longitud
            raise forms.ValidationError("Ingrese un número de tarjeta válido.")
        return card_number

    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        if cvv is None or cvv.isdigit() or len(cvv) not in [3, 4]:  # Validar CVV
            raise forms.ValidationError("Ingrese un CVV válido.")
        return cvv