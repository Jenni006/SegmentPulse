from ping3 import ping
from influxdb_client import InfluxDBClient, Point, WritePrecision
import time

INFLUX_URL = "http://influxdb:8086"
TOKEN = "my-token"
ORG = "segmentpulse"
BUCKET = "network"

client = InfluxDBClient(url=INFLUX_URL, token=TOKEN, org=ORG)
write_api = client.write_api()

target = "8.8.8.8"

while True:

    latency = ping(target)

    if latency:

        point = Point("latency") \
            .tag("host", target) \
            .field("value", latency)

        write_api.write(bucket=BUCKET, record=point)

        print("Latency:", latency)

    time.sleep(5)