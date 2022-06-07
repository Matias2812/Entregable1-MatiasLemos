from django import forms

class Autos_formulario(forms.Form):

    marca = forms.CharField(max_length=40)

    ruedas = forms.IntegerField()

    creacion = forms.IntegerField()




class Perros_formulario(forms.Form):

    raza = forms.CharField(max_length=40)

    edad = forms.IntegerField()



class Oficinas_formulario(forms.Form):

    tipo = forms.CharField(max_length=40)

    cantidad = forms.IntegerField()

    

    
