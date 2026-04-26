from django import forms
from .models import Comment, Subscription

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']