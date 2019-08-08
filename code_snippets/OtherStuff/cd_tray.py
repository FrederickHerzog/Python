#Frederick Herzog
#Opens and closes the cd tray

import ctypes
import time


def cdDriveChaos(n,p,p2):
	for i in range (n):
		ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
		time.sleep(p)
		ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
		time.sleep(p2)

cdDriveChaos(3,1,3)
