from django import forms
class formSaya(forms.Form):
    nama = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'nama anda',
            }
        )
    )
    email = forms.EmailField()
    ipk = forms.FloatField()
    umur = forms.IntegerField()
    lulus = forms.BooleanField()
    pilihan = (
        ('programming','Programming'),
        ('nilaiDua','Olahraga'),
        ('nilaiTiga','Baca')
    )
    tanggal = range(1994, 2019, 1)
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control col-sm-2'
            },
            years=tanggal
        )
    )
    hobby = forms.ChoiceField(

        choices=pilihan,
        widget=forms.RadioSelect(
            attrs={'class':'form-check-input ',}
        ),
    )
    reason = forms.ChoiceField(
        widget=forms.Textarea
    )
