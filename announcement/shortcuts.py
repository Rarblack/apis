def push_notification(receivers=None, data=None):

    if receivers is None:
        receivers = []

    from fcm_django.models import FCMDevice

    devices = FCMDevice.objects.filter(user_id__in=receivers, active=True)

    if devices:
        for device in devices:
            try:
                device.send_message(data=data)
            except ValueError:
                raise ValueError("Notification couldn't be sent to the device %s" % device.id)
