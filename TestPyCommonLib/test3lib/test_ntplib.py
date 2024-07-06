# pip install ntplib
import ntplib
from time import ctime

ntp_cli = ntplib.NTPClient()
resp = ntp_cli.request('ntp.aliyun.com', version=3)

print(ntplib.ref_id_to_text(resp.ref_id))
print(ctime(resp.tx_time))

