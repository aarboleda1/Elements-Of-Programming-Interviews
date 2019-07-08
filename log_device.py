import time
import random
import os
import threading

import logdevice.client as log_device
import logdevice.integration_test_util

TIMEOUT = 30
STOP_MSG = b"STOP"
PRINT_LOCK = threading.Lock()


def publish(publisher_id):
    client = log_device.Client(name="publish")
    for message in [
            "the",
            "fox",
            "jumped",
            "over",
            "the",
            "moon",
            STOP_MSG,
    ]:
        time.sleep(random.randint(0, 1))
        # Publish each event to the message broker
        client.append(publisher_id, message)
    print_locking("Publishing events finished!")


def subscriber(subscriber_id):
    print_locking("Subcribing starting")
    # Subscribers are clients that read from the message broker/queue, LogDevice
    client = log_device.Client()
    reader = client.create_reader(10)
    reader.start_reading(1)
    # Read the events in order
    for log, _ in reader:
        if log:
            print_locking("{} > Got log! {}".format(
                subscriber_id,
                {"payload": log.payload},
            ))

            if log.payload == STOP_MSG:
                break

    print_locking("Sub {} finished".format(sub_num))

# A utility to lock the thread so we can view events happening
def print_locking(*args, **kwargs):
    with PRINT_LOCK:
        print(*args, **kwargs, flush=True)

def main():
    threads = [
        # this is the main publisher that will publish events to the message broker
        threading.Thread(target=publish, publisher_id=0),
        # We can have any number of subscribers that will receive the events
        # published
        threading.Thread(target=subscribe, subscriber_id=0),
        threading.Thread(target=subscribe, subscriber_id=1),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=TIMEOUT)

main()

1 > Got log! {'payload': b'the'}
1 > Got log! {'payload': b'fox'}
1 > Got log! {'payload': b'jumped'}
1 > Got log! {'payload': b'over'}
1 > Got log! {'payload': b'the'}
1 > Got log! {'payload': b'moon'}
Pub finished

# Each subscriber received the messages from the publisher
0 > Got log! {'payload': b'the'}
1 > Got log! {'payload': b'the'}
1 > Got log! {'payload': b'fox'}
0 > Got log! {'payload': b'fox'}
0 > Got log! {'payload': b'fox'}
1 > Got log! {'payload': b'jumped'}
0 > Got log! {'payload': b'over'}
1 > Got log! {'payload': b'jumped'}
1 > Got log! {'payload': b'over'}
1 > Got log! {'payload': b'the'}
0 > Got log! {'payload': b'the'}
1 > Got log! {'payload': b'moon'}
0 > Got log! {'payload': b'moon'}

Messages received!
