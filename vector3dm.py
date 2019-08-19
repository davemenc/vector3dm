import numpy as np
import math
import copy
class Vector3dm:
	def __init__(self,a=None,b=None,c=None,type="s"):
		assert type == "s" or type == "c","Expects spherical (s) or cartesian (c); vector is type {}".format(type)

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
			return "r:{}, phi:{}, theta:{}, type s".format(round(self.vals[0],2),round(self.vals[1],2),round(self.vals[2],2))
		else:
			return "{},{},{}, type: {} (type may be invalid)".format(round(self.vals[0],2),round(self.vals[1],2),round(self.vals[2],2),self.type)
		
	def spherical_to_cartesian(self):
		# converts a spherical vector to a cartesian vector
		# input: vector (self) of type spherical
		# ouput: copy of vector converted to cartesian coordinates
		
		if self.type == "c":
			return copy.copy(self)
		assert self.type=="s","Expects spherical (s) or cartesian (c); vector is type {}".format(self.type)
		r,phi,theta = self.vals
		#print("s2c: r",r,"phi",phi,"theta",theta)
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
		return Vector3dm(r,phi,theta,"s")
		
	def origin_distance(self):
		# Gets distance from origin
		# input Vector (self) of type cartesian, 
		# outputs float scalar
		if self.type =="s":
			return self.vals[0] # for spherical, just return r
		assert self.type=="c" or self.type=="s", "Expects cartesian; vector is type {}".format(self.type)
		x,y,z = self.vals
		return math.sqrt(x**2 + y**2 + z**2)

	def distance(self,v=None):
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
		# output a spherical vector which is the sum of the two 
		return np.add(self.spherical_to_cartesian(), v.spherical_to_cartesian())
		
	
	def sub(self,v): # self - v
		# subtracs v from self
		# input: self and another vector of any type
		# output a spherical vector which is self-v
		if self.type == "s":
			x1,y1,z1 = self.spherical_to_cartesian().vals
		else:
			x1,y1,z1 = self.vals
		if v.type == "s":
			x2,y2,z2 = v.spherical_to_cartesian().vals
		else:
			x2,y2,z2 = v.vals
	
		return cartesian_to_spherical((x1-x2,y1-y2,z1-z2))


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
	print("__________S2C___________")
	print("s_to_c",v1,v1.spherical_to_cartesian())
	print("s_to_c",v2,v2.spherical_to_cartesian())
	print("s_to_c",v3,v3.spherical_to_cartesian())
	print("s_to_c",v9,v9.spherical_to_cartesian())
	print("s_to_c",va,va.spherical_to_cartesian())

	print
	print("__________C2S___________")
	print("c_to_s",v1,v1.cartesian_to_spherical())
	print("c_to_s",v2,v2.cartesian_to_spherical())
	print("c_to_s",v3,v3.cartesian_to_spherical())
	print("c_to_s",v4,v4.cartesian_to_spherical())
	print("c_to_s",v5,v5.cartesian_to_spherical())
	print("c_to_s",v6,v6.cartesian_to_spherical())
	
	print
	print("_________O DIST____________")
	print("origin_distance",v1,v1.origin_distance())
	print("origin_distance",v2,v2.origin_distance())
	print("origin_distance",v3,v3.origin_distance())
	print("origin_distance",v4,v4.origin_distance())
	print("origin_distance",v5,v5.origin_distance())
	print("origin_distance",v6,v6.origin_distance())
	print("origin_distance",v7,v7.origin_distance())

	print
	print("_________DEF DIST____________")
	print("distance",v7,v7.distance())

	print
	print("_________0 DIST____________")
	print("distance",v1,v1,v1.distance(v1))
	print("distance",v2,v2,v2.distance(v2))
	print("distance",v3,v3,v3.distance(v3))
	
	print
	print("___________DIST__________")
	print("distance 1-2 ",v1,v2,v1.distance(v2))
	print("distance 1-3 ",v1,v3,v1.distance(v3))
	print("distance 1-4 ",v1,v4,v1.distance(v4))
	print("distance 2-3",v2,v3,v2.distance(v3))
	print("distance 3-4",v3,v4,v3.distance(v4))
	print("distance 4-5",v4,v5,v4.distance(v5))

	print
	print("________ADD_____________")
	print("add",v3,v4,v3.add(v4))