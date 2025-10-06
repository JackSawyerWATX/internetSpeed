import speedtest as st

def Speed_Test():
  test = st.Speedtest()

  down_speed = test.download() # Download speed in bits per second
  down_speed = round(down_speed / 10**6, 2)  # Convert to Mbps and round to 2 decimal places
  print("Download Speed in Mbps ", down_speed)
  
  up_speed = test.upload() # Upload speed in bits per second
  up_speed = round(up_speed / 10**6, 2)  # Convert to Mbps and round to 2 decimal places
  print("Upload Speed in Mbps ", up_speed)

  ping = test.results.ping
  print("Ping: ", ping)

Speed_Test()