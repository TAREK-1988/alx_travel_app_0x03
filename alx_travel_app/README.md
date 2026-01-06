# alx_travel_app_0x03

Milestone 5: Setting Up Background Jobs for Email Notifications

## Overview
This project implements asynchronous email notifications for booking confirmations using Celery with RabbitMQ.

## Implemented
- Celery configured with RabbitMQ as broker
- Shared task created to send booking confirmation emails
- BookingViewSet triggers the task asynchronously using delay()

## Core Files
- alx_travel_app/settings.py
- listings/tasks.py
- listings/views.py
- README.md
