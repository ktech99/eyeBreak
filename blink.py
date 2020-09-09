import win10toast
import time

toaster = win10toast.ToastNotifier()

while True:
    toaster.show_toast('Eye  break', "Take a break from the screen", duration=5)
    time.sleep(1200)