'''
Frederick Herzog
Hello world kivy app
'''

import kivy 
from kivy.app import App
from kivy.uix.label import Label 

class myApp(App):
	def build(self):
		return Label(text='Hello World')

if __name__ == "__main__":
	myApp().run()
