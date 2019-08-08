## Frederick Herzog
## A simple class for timing algorithms.

import time

class Timer:

	def __init__(self):
		self.start_time = time.time()
		self.stop_time = time.time()

	def start(self):
		self.start_time = time.time()

	def stop(self):
		self.stop_time = time.time()

	def elapsed(self):
		return self.stop_time - self.start_time

	def clear(self):
		self.start_time = time.time()
		self.stop_time = time.time()
