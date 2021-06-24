import time

def countdown (time_secs):
  """
  function to create a countdowm timer to be displayed on the screen.
  :param: time_secs is the duration of the countdowm im seconds.
  """
  
  while time_secs >= 0:
    mins, secs = divmod(time_secs, 60)
    print("{:02d}:{:02d}".format (mins, secs), end="\r")
    time.sleep(1)
    time_secs -=1

countdown(10)

