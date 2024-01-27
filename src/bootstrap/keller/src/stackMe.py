# three method to deal with new input.
# throw away any of original content, or just bounce off.
class queue:
# i'm gonna die.
	def __init__(self,a):
		self.size=a
		self.core=[]
	def queue(self,a):
		if len(self.core)<self.size:
			self.core.append(a)
		else:
			self.core.pop(0)
			self.core.append(a)
	def dequeue(self):
		if len(self.core)!=0:
			return self.core.pop(0)
		else:
			return
	def dump(self):
		return self.core

class stack:
	def __init__(self,a):
		self.size=a
		self.core=[]
	def push(self,a):
		if len(self.core)<self.size:
			self.core.append(a)
		else:
			self.core.pop(0)
			self.core.append(a)
	def pop(self):
		if len(self.core)!=0:
			return self.core.pop(-1)
		else:
			return
	def dump(self):
		return self.core

class Meta:
# i'm gonna die.
	def __init__(self,a):
		self.size=a
		self.core=[]
	def add(self,a):
		if len(self.core)<self.size:
			self.core.append(a)
		else:
			self.core.pop(0)
			self.core.append(a)
	def minus(self,a):
		if len(self.core)!=0:
			return self.core.pop(-int(a))
		else:
			return
	def dump(self):
		return self.core
	def duplicate(self,a):
		self.add(self.core[-int(a)])
