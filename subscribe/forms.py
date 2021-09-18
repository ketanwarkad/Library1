from django import forms

class Subscribe(forms.Form):
    Email = forms.CharField()
    # name=forms.CharField(max_length=100)
    # age=forms.IntegerField()


    # def __str__(self):
    #     return self.Email

#<tr><th><label for="id_Email">Email:</label></th><td><input type="email" name="Email" required id="id_Email"></td></tr>