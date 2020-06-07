import speedtest
import click
from send_email2 import send_email
from datetime import datetime

# @click.command()
# @click.option('--smtp-user')
# @click.option('-email-from', '-from')
# @click.option('--email-to', '-to', nagrs=-1)




def speed_test():
    s = speedtest.Speedtest()

    # speedtest results
    server = s.get_best_server()
    download_speed_bytes = s.download()
    upload_speed_bytes = s.upload()

    # retun values
    download_speed_mb = download_speed_bytes // (1024*1024)
    upload_speed_mb = upload_speed_bytes // (1024*1024)
    server_city = server["name"]
    server_country = server["country"]
    ser_loc = [server["name"], server["country"]]
    # print("Server Locaion: ", ser_loc)
    # print("Server Locaion: ", server["name"], "," ,server["country"])
    # print("Upload speed (mbps) :", upload_speed_mb)
    # print("Download speed (mbps):", download_speed_mb)
    now = datetime.now().strftime("%m-%d-%Y  %H:%M:%S")
    
    # formatting result to pass on to the email template
    result = '''
**************** Wifi Status *********************
                                                
   Download speed (mbps) : {d_mb}                 
   Upload speed (mbps)   : {u_mb}                   
                                                
   Server Location       : {City},{Country}              
   Date / Time           : {Now}

**************************************************
'''.format(u_mb=upload_speed_mb, d_mb=download_speed_mb,City=server_city, Country=server_country, Now=now)
    
    # cases 
    if download_speed_mb < 40:
        send_email("WiFi status: SLOW", result) 
    elif download_speed_mb == 0 or upload_speed_mb == 0:
        send_email("WiFi stauts: DOWN", result)
    else:
        send_email("Wifi status: OK", result)

speed_test()