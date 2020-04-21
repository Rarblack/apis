def push_notification(receivers, data=None):

    from fcm_django.models import FCMDevice

    devices = FCMDevice.objects.filter(user__in=receivers, active=True)
    if devices:
        for device in devices:
            try:
                device.send_message(data=data)
            except ValueError:
                raise ValueError("Notification couldn't be sent to the device %s" % device.id)
