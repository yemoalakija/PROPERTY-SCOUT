# pylint: disable=import-error
"""Contacts urls"""
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact


# Create your views here.
class ContactView(APIView):
    """Contact view"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """Post method"""
        data = self.request.data

        try:
            send_mail(
                data['subject'],  # subject
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage: \n'
                + data['message'],  # message
                'adeyemo.myproject@gmail.com',  # from email
                'adeyemo.myproject@gmail.com',  # to email
                fail_silently=False,
            )

            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except:  # pylint: disable=bare-except
            return Response({'error': 'Message failed to send'})
