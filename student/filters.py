import django_filters
from .models import Enrollment

class EnrolledFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields =['course','student']