import requests
def get_url():
    domain = input("enter domain: ")
    url = "https://"+ domain
    return(url)

def get_header():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"}
    return headers
def find_working_url(url):
    L = [".com",".net",".org",".co",".io",".edu",".gov",".info",".biz",".name",".me",".ai",".tech"]
    for ext in L:
        try:
            print("[*] Checking: " + url + ext)
            respond = requests.get(url + ext, headers=get_header())
            if respond.status_code == 200:
                print("[+] Found: " + url + ext)
                return url + ext
        except:
            continue
    print("[-] No working URL found")
    return None


  
mode = input("pick a mode\n[1] Basic Recon\n[2] POST Probe\n[3] Session Test\n[4] Response Diff\nenter mode(1-4): ")
if mode == "1":
    print("You are in Basic Recon mode")
    url = get_url()
    print("You are in Basic Recon mode")
    try:
        working_url = find_working_url(url)
        respond = requests.get(working_url, get_header())
        print("[+] Server: " + respond.headers.get("Server", "unknown"))
        print("[+] Content-Type: " + respond.headers.get("Content-Type", "unknown"))
        html_title = respond.text
        title_tag = html_title.find("<title>")
        end_tag = html_title.find("</title>")
        print("[+] Title: " + html_title[title_tag + 7 : end_tag])
        print("[*] Scan complete.")
    except Exception as e:
        print("[-] Failed to connect: " + str(e))
elif mode == "2":
    print("You are in POST Probe mode")
    url = get_url()
    headers = get_header()
    try:
        working_url = find_working_url(url)
        field1 = input("enter your field: ")
        value1 = input("enter your value: ")
        data = {field1: value1}
        respond = requests.post(working_url, data=data, headers=headers)
        print("[+] Status: " + str(respond.status_code))
        print("[+] Content: " + respond.text[:200])
    except Exception as e:
        print("[-] Failed to connect: " + str(e))
elif mode == "3":
    print("You are in Session Test mode")
    url = get_url()
    headers = get_header()
    try:
        working_url = find_working_url(url)
        cookie_name = input("enter cookie name: ")
        cookie_value = input("enter cookie value: ")
        session = requests.Session()
        session.cookies.set(cookie_name, cookie_value)
        respond = session.get(working_url, headers = headers)
        print("[+] Status: " + str(respond.status_code))
        print("[+] Content: " + respond.text[:200])
    except Exception as e:
        print("[-] Failed to connect: " + str(e))
elif mode == "4":
    print("You are in Response Diff mode")
    url = get_url()
    headers = get_header()
    try:
        working_url = find_working_url(url)
        cookie_name1 = input("enter cookie name: ")
        cookie_value1 = input("enter cookie value: ")
        attacker_cookie = {cookie_name1: cookie_value1}
        cookie_name2 = input("enter cookie name: ")
        cookie_value2 = input("enter cookie value: ")
        victim_cookie = {cookie_name2: cookie_value2}
        respond_1 = requests.get(working_url, headers = headers, cookies = attacker_cookie)
        respond_2 = requests.get(working_url, headers = headers, cookies = victim_cookie)
        if respond_1.text == respond_2.text:
            print("[+] Response is the same")
        else:
            print("[+] Responses differ - potential auth issue")
            print("Response A length: " + str(len(respond_1.text)))
            print("Response B length: " + str(len(respond_2.text)))
            print("Response A: " + respond_1.text[:200])
            print("Response B: " + respond_2.text[:200])
    except Exception as e:
        print("[-] Failed to connect: " + str(e))
    
    
    
    
    

   



    



