def send_notification(**kwargs):
    from fcm_django.models import FCMDevice
    device_id = kwargs.get('device_id')

    def to_single_device():
        device = FCMDevice.objects.get(device_id=device_id, active=True)
        if device:
            try:
                device.send_message(data=kwargs.get('data'))
            except ValueError:
                raise ValueError("Notification couldn't be sent to the device")

    def to_all_devices():
        devices = FCMDevice.objects.all()
        if devices:
            for device in devices:
                device.send_message(data=kwargs.get('data'))

    if device_id:
        to_single_device()
    else:
        to_all_devices()


def record_notification(**kwargs):
    from notification.models import Notification
    from django.utils import timezone
    Notification.objects.create(data=kwargs.get('data'),
                                created_by=kwargs.get('created_by'),
                                created_datetime=timezone.now())
