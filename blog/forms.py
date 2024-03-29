from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid Email.Please dont end with edu")
        return email