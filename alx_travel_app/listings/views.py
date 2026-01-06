from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by("-id")
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        booking = serializer.save()

        email = ""
        if getattr(booking, "user", None) and getattr(booking.user, "email", ""):
            email = booking.user.email
        elif getattr(booking, "email", ""):
            email = booking.email

        if email:
            send_booking_confirmation_email.delay(email, booking.id)
