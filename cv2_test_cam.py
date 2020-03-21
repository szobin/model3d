import cv2_tools
from cv2_tools.Management import ManagerCV2
import cv2

print('Name: {}\nVersion:{}\nHelp:{}'.format(cv2_tools.name,cv2_tools.__version__,cv2_tools.help))

# keystroke=27 is the button `esc`
manager_cv2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True, fps_limit=60)

# This for will manage file descriptor for you
for frame in manager_cv2:
    # Each time you press a button, you will get its id in your terminal
    last_keystroke = manager_cv2.get_last_keystroke()
    if last_keystroke != -1:
        print(last_keystroke)
    cv2.imshow('Easy button checker', frame)
cv2.destroyAllWindows()
