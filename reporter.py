from datetime import datetime
import os 
target = input("enter target:")
status = input("enter status:")
server = input("enter server:")
title = input("enter title:")
date = datetime.now().strftime("%Y-%m-%d %H:%M")

def report_template():
	print(f"TARGET: {target}")
	print(f"STATUS: {status}")
	print(f"SERVER: {server}")
	print(f"TITLE: {title}")
	print(f"DATE: {date}")
	os.makedirs("/home/david/Documents/Agent_A/mylearningpython/reports", exist_ok=True)
	with open(f"/home/david/Documents/Agent_A/mylearningpython/reports/report_{target}.txt", "w") as f:
		f.write(f"TARGET:{target}\nSTATUS: {status}\nSERVER: {server}\nTITLE: {title}\nDATE: {date}\n" )
	print(f"[+] Report saved: /home/david/Documents/Agent_A/mylearningpython/reports/report_{target}.txt")
report_template()
