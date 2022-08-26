import telnetlib

tel = telnetlib.Telnet(host="10.10.87.91", port="9092", timeout=3)
tel.close()

