from django.shortcuts import render,redirect    
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import EnrolledFilter
from .models import Student,Enrollment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .serializers import Student_Serializer,enroll_Serializer,Registration_Serializer,UserLogin
# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

class EnrollView(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = enroll_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EnrolledFilter

class UserRegistration(APIView):
    serializer_class = Registration_Serializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            # token = default_token_generator.make_token(user)
            # uid = urlsafe_base64_encode(force_bytes(user.pk))
            # confirm_link = f"http://127.0.0.1:8000/student/active/{uid}/{token}"
            # email_subject = "Confirm Your Email"
            # email_body = render_to_string('confirm_mail.html',{'confirm_link': confirm_link})
            # email = EmailMultiAlternatives(email_subject, "",to=[user.email])
            # email.attach_alternative(email_body,"text/html")
            # email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)
    
class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLogin(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)
            if user :
                token,created = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token': token.key,'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credential'})
        return Response(serializer.errors)
    
class User_logout_view(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')