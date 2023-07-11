from django import forms

def validate_for_sname(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('sname cannot start with a')

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError("Name length should be greater than 5")



class StudentForm(forms.Form):
    sname=forms.CharField(max_length=30,validators=[validate_for_sname,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[validate_for_sname])
    remail=forms.EmailField()
    url=forms.URLField()
    botcatcher=forms.CharField(max_length=10,widget=forms.HiddenInput,required=False)
        


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['remail']
        if e!=r:
            raise forms.ValidationError("both mails are not matching")

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError("botcatcher")



