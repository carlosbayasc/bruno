from django import forms

class NewEmpresaForm(forms.Form):
    vruc = forms.CharField(max_length=13)
    vnombre = forms.CharField(max_length=250)
    vdireccion = forms.CharField(max_length=250)
    vcontacto= forms.CharField(max_length=50)
    vtelefono = forms.CharField(max_length=50)
    vcorreo = forms.CharField(max_length=50)


   