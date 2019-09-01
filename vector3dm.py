import numpy as np
import math
import copy

def numpy_to_vector3dm(np_array):
	# converts a numpy array of 3 elements in cartesion coordinates to a vector3dm
	# input: numpy array (3 el, cartesian values)
	# output: a vector3dm of catesian type
	return Vector3dm(np_array[0],np_array[1],np_array[2],"c")
	
class Vector3dm:
	def __init__(self,a,b,c,type):
		assert type == "s" or type == "c","Expects spherical (s) or cartesian (c); vector is type {}".format(type)

		# in spherical the order is r,theta,phi
		# in cartesian it's x,yz
		self.vals = [float(a),float(b),float(c)]
		self.type = type # s==spherical, c==cartesian

	def __array__(self):
		v = self.spherical_to_cartesian() # makes a copy and converts to cartesian coords (even if already c type)
		return np.array([v.vals[0], v.vals[1], v.vals[2]])

	def __repr__(self):
		return "{},{},{}, type: {}".format(self.vals[0],self.vals[1],self.vals[2],self.type)
	
	def __str__(self):
		if self.type == "c":
			return "x:{}, y:{}, z:{}, type c".format(round(self.vals[0],2),round(self.vals[1],2),round(self.vals[2],2))
		elif self.type == "s":
			return "r:{}, theta:{}, phi:{},  type s".format(round(self.vals[0],2),round(self.vals[1],2),round(self.vals[2],2))
		else:
			return "{},{},{}, type: {} (type may be invalid)".format(round(self.vals[0],2),round(self.vals[1],2),round(self.vals[2],2),self.type)
	
	def spherical_to_cartesian(self):
		# converts a spherical vector to a cartesian vector
		# input: vector (self) of type spherical
		# ouput: copy of vector converted to cartesian coordinates
		
		if self.type == "c":
			return copy.copy(self)
		assert self.type=="s","Expects spherical (s) or cartesian (c); vector is type {}".format(self.type)
		r,theta,phi = self.vals
		#print("s2c: r",r,"theta",theta,"phi",phi)
		x = r * math.sin(phi) * math.cos (theta)
		y = r * math.sin(phi) * math.sin (theta)
		z = r * math.cos(phi)
		return Vector3dm(x,y,z,"c")
		
	def cartesian_to_spherical(self):
		# converts a cartesian vector to a spherical vector
		# input: vector (self) of type catesian
		# output: copy ot vector converted to spherical coordinates
		if self.type == "s":
			return copy.copy(self)
		assert self.type=="c","Expects spherical (s) or cartesian (c); vector is type {}".format(self.type)
		x,y,z = self.vals
		#print(" in c2s: x",x,"y",y,"z",z)
		r = self.origin_distance()
		if r==0.0:
			r=0.000000001
		phi = math.acos(float(z)/r)
		theta = math.atan2(float(y),float(x))
		return Vector3dm(r,theta,phi,"s")
		
	def origin_distance(self):
		# Gets distance from origin
		# input Vector (self) of type cartesian, 
		# outputs float scalar
		if self.type =="s":
			return self.vals[0] # for spherical, just return r
		assert self.type=="c" or self.type=="s", "Expects cartesian; vector is type {}".format(self.type)
		x,y,z = self.vals
		return math.sqrt(x**2 + y**2 + z**2)

	def magnitude(self,v=None):
		# Gets distance from self to v or from self to origin
		# input: any 1 or 2 vectors
		# output: float scalar

		if v is None:
			return self.origin_distance()
		if self.type=="s":
			v1 = self.spherical_to_cartesian()
		else:
			v1 = self
		if v.type=="s":
			v2 = v.spherical_to_cartesian()
		else:
			v2 = v
		x1,y1,z1 = v1.vals
		x2,y2,z2 = v2.vals
		return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
		
	
	def add(self,v):
		# adds two vectors
		# input: self and another vector of any type
		# output a vector which is the sum of the two 
		np_vect = np.add(self.spherical_to_cartesian(), v.spherical_to_cartesian())
		return numpy_to_vector3dm(np_vect)
	
	def sub(self,v): # self - v
		# subtracs v from self
		# input: self and another vector of any type
		# output a cartesion vector which is self-v
		x1,y1,z1 = self.spherical_to_cartesian().vals
		x2,y2,z2 = v.spherical_to_cartesian().vals
	
		return Vector3dm(x1-x2,y1-y2,z1-z2,"c")

	def mult(self,number):
		# multiplies the vector self by number (a scalor)
		# input: self and a number
		# output: a cartesion vector with each element multiplied by number
		x,y,z = self.spherical_to_cartesian().vals
		return Vector3dm(x*number,y*number,z*number,"c")
	
	def neg(self):
		# takes the negative of the vector self
		# input: self (vector of any type)
		# output: cartesion vector with each element negated
		x,y,z = self.spherical_to_cartesian().vals
		return Vector3dm(-x,-y,-z,"c")

	def cross(self,v):
		v1 = self.spherical_to_cartesian()
		v2 = v.spherical_to_cartesian()
		v3 = np.cross(v1,v2)
		print("cross",type(v3),v3)
		return Vector3dm(np.cross(v1, v2),"c")

	def inner(self,v):
		v1 = self.spherical_to_cartesian()
		v2 = v.spherical_to_cartesian()
		v3 = np.cross(v1,v2)
		print("inner",type(v3),v3)
		return Vector3dm(np.inner(v1, v2),"c")



if __name__ == "__main__":
	print()
	print("______________________________________________________________________________________________________________")
	print("______________________________________________________________________________________________________________")
	v1 = Vector3dm(0,0,0)
	v2 = Vector3dm(0,0,0,"c")
	v3 = Vector3dm(0,100,0,"c")
	v4 = Vector3dm(100,0,0,"c")
	v5 = Vector3dm(0,0,100,"c")
	v6 = Vector3dm(100,0,100,"c")
	v7 = Vector3dm(100,100,0,"c")
	v8 = Vector3dm(100,100,100,"c")
	#v9 = Vector3dm(100,100,100,"wrong")
	v9 = Vector3dm(-100,math.pi,math.pi,"s")
	va = Vector3dm(100,math.pi,math.pi,"s")
	
#	print(v7.cross(v8))
	#tests
	print(1,v1)
	print(2,v2)
	print(3,v3)
	print(4,v4)
	print(5,v5)
	print(6,v6)
	print(7,v7)
	print(8,v8)
	print(9,v9)
	print("a",va)
	print("np",np.array(v1))


	print
	print("________ADD_____________")
	print("add",v3,v4,v3.add(v4))