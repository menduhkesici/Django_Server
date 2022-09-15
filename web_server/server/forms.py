from django import forms


class Form_1(forms.Form):
    name = forms.CharField(label='Write message:')
    category = forms.ChoiceField(choices=tuple([(i, i) for i in range(10)]), label='Choose a number:')


class Form_2(forms.Form):
    name = forms.ChoiceField(choices=tuple([(chr(i), chr(i)) for i in range(ord('a'), ord('z') + 1)]),
                             label='Choose a character')
    category = forms.ChoiceField(choices=[(i, i) for i in range(10)], label='Choose a number:')
