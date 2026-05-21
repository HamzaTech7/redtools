import socket 
target_host = socket.gethostbyname(input("enter target domain: "))
print(f"scaning {target_host}")
try:
	for port in range(20, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.settimeout(0.5)
		result = s.connect_ex((target_host , port))
		if result == 0:
			 print(f"[*] port {port} is open")
		s.close()
except Exception as e:
	print("failed to scan" + str(e))

