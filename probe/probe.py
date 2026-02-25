from ping3 import ping
import time

segments = {
    "Customer": "8.8.8.8",
    "ONT": "1.1.1.1",
    "Gateway": "8.8.4.4"
}

while True:

    print("Probing...\n")

    for name, ip in segments.items():

        rtt = ping(ip, timeout=2)

        if rtt is None:

            print(name, "DOWN")

        else:

            print(name, round(rtt*1000,2), "ms")

    print("\n-------------------\n")

    time.sleep(5)