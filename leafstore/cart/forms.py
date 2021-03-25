from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
  quantity = forms.TypedChoiceField(
      choices=PRODUCT_QUANTITY_CHOICES,
      coerce=int)
  override = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

  def __init__(self, *args, **kwargs):
    self.site_id = kwargs.pop('site_id')
    super(StylesForm, self).__init__(*args, **kwargs)
    # self.fields['height'].widget = forms.
