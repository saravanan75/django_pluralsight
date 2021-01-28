from django.dispatch import Signal, receiver

# Create a custom signal
request_signal = Signal()


class RequestResponseDemo(object):
    # function to send the signal
    def send(self):
        print('Http Request Sent')
        request_signal.send(sender=self.__class__, Request=True)


# Function to receive the signal
@receiver(request_signal)
def receive(**kwargs):
    if kwargs['Request']:
        print('Received Request')


demo = RequestResponseDemo()
demo.send()