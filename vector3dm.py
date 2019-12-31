import math
import copy

def numpy_to_vector3dm(np_array):
	# converts a numpy array of 3 elements in cartesion coordinates to a vector3dm
	# input: numpy array (3 el, cartesian values)
	# output: a vector3dm of catesian type
	return Vector3dm(np_array[0],np_array[1],np_array[2],"c")

def vector_to_list(v):
	# converts vector3dm to a simple list which can then be converted to numpy arry
	# input: vector3dm vector
	# output: a list with 3 elements, x,y, z
	return v.convert_to_cartesian().vals
	
class Vector3dm:
	def __init__(self,r,theta,phi,type):
		# in spherical the order is r,theta,phi
		# in cartesian it's x,y,z
		# params are named for spherical because that way you can name them in the call
		# for type, "s"==spherical, "c"==cartesian
		assert type == "s" or type == "c","Expects spherical (s) or cartesian (c); vector is type {}".format(type)
		self.vals = [float(r),float(theta),float(phi)]
		self.type = type # s==spherical, c==cartesian

	def __array__(self):
		v = self.convert_to_cartesian() # makes a copy and converts to cartesian coords (even if already c type)
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

	# init methods
	def zero_vector():
		return Vector3dm(0,0,0,"c")
		
	# retrieval methods
	def get_x(self):
		return self.convert_to_cartesian().vals[0]
	def get_y(self):
		return self.convert_to_cartesian().vals[1]
	def get_z(self):
		return self.convert_to_cartesian().vals[2]
	def get_r(self):
		return self.convert_to_spherical().vals[0]
	def get_theta(self):
		return self.convert_to_spherical().vals[1]
	def get_phi(self):
		return self.convert_to_spherical().vals[2]
	
	# set methods
	def set_r(self,r):
		v = self.convert_to_spherical()
		v.vals[0] = float(r)
		self.vals = v.vals
		self.type = v.type

	def set_theta(self,theta):
		v = self.convert_to_spherical()
		v.vals[1] = float(theta)
		self.vals = v.vals
		self.type = v.type
		
	def set_phi(self,phi):
		v = self.convert_to_spherical()
		v.vals[2] = float(phi)
		self.vals = v.vals
		self.type = v.type

	def set_x(self,x):
		v = self.convert_to_cartesian()
		v.vals[0] = float(x)
		self.vals = v.vals
		self.type = v.type

	def set_y(self,y):
		v = self.convert_to_cartesian()
		v.vals[1] = float(y)
		self.vals = v.vals
		self.type = v.type

	def set_z(self,z):
		v = self.convert_to_cartesian()
		v.vals[2] = float(z)
		self.vals = v.vals
		self.type = v.type
	
	# conversion methods
	def convert_to_cartesian(self):
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
		
	def convert_to_spherical(self):
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
			v1 = self.convert_to_cartesian()
		else:
			v1 = self
		if v.type=="s":
			v2 = v.convert_to_cartesian()
		else:
			v2 = v
		x1,y1,z1 = v1.vals
		x2,y2,z2 = v2.vals
		return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
		
	def add(self,v):
		# adds two vectors
		# input: self and another vector of any type
		# output a vector which is the sum of the two 
		#np_vect = np.add(self.convert_to_cartesian(), v.convert_to_cartesian())
		#return numpy_to_vector3dm(np_vect)
		result = Vector3dm.zero_vector()
		result.vals = v.vals[0]+self.vals[0],v.vals[1]+self.vals[1],v.vals[2]+self.vals[2]
		return result
		
	def sub(self,v): # self - v
		# subtracs v from self
		# input: self and another vector of any type
		# output: a cartesion vector which is self-v
		x1,y1,z1 = self.convert_to_cartesian().vals
		x2,y2,z2 = v.convert_to_cartesian().vals	
		return Vector3dm(x1-x2,y1-y2,z1-z2,"c")

	def mult(self,number):
		# multiplies the vector self by number (a scalor)
		# input: self and a number
		# output: a cartesion vector with each element multiplied by number
		x,y,z = self.convert_to_cartesian().vals
		return Vector3dm(x*number,y*number,z*number,"c")
	
	def neg(self):
		# takes the negative of the vector self
		# input: self (vector of any type)
		# output: cartesion vector with each element negated
		x,y,z = self.convert_to_cartesian().vals
		return Vector3dm(-x,-y,-z,"c")

	def cross(self,v):
		#calculates the cross product of two vectors
		# input: self vector & another vector v
		# output: vector of right angle vector of 2 vectors: cross product
		ax,ay,az = self.convert_to_cartesian().vals
		bx,by,bz = v.convert_to_cartesian().vals
		cx = ay*bz - az*by
		cy = az*bx - ax*bz
		cz = ax*by - ay*bx
		vc = Vector3dm(cx,cy,cz,"c")
		return vc  		
			
	def dot(self,v):
		# calculates the dot product of two vectors
		# input: self vector & another vector v
		# output: scalar dot product of the two vectors
		v1 = self.convert_to_cartesian()
		v2 = v.convert_to_cartesian()
		return v1.vals[0]*v2.vals[0]+v1.vals[1]*v2.vals[1]+v1.vals[2]*v2.vals[2]
		
	def inner(self,v):
		return self.dot(v)
	
	def point_at_that(self,v):
		# creates  vector from here to there
		# input: self (my location)  and a vector (location of destination or "that")
		# output: a vector that points from self to the vector
		v1 = v.sub(self)
		return v1.convert_to_spherical()
	
	def where_from_here(self,v):
		# given a vector from here to a point, finds the location of the point
		# input: self (my location) and a vector (direction and distance to a point)
		# output: a vector that represents the location of hte destination
		v1 = self.add(v)
		return v1.convert_to_spherical()

	def unit(self):
		# given a vector, find the unit vector (that is, the vector with magnitude 1)
		# input self
		# output: self but with magnitude 1
		v = self.convert_to_spherical()
		v.set_r(1.0)
		return v
if __name__ == "__main__":
	print(Vector3dm.zero_vector())
