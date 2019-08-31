import  unittest
import math
from vector3dm import Vector3dm

def compare_close(a,b): # compare a&b to within 1/1000
	print("compare_close",a,b,b-0.001,b+0.001)
	if a >= b-0.001 and a <= b+0.001:
		print("TRUE")
		return True
	else:
		print("FALSE")
		return False

class TestBasicFunction(unittest.TestCase):
	def setUp(self):
		v2 = Vector3dm(8,math.pi/5.0,math.pi/6.0,"s")
	def test(self):
		self.assertTrue(True)
	def test_1(self):
		self.assertTrue(True)

	def test_2(self):
		self.assertTrue(True)
	def test_spherical_to_cartesian(self):
		v = Vector3dm(8,math.pi/5.0,math.pi/6.0,"s")
		print("s2c start:",v)
	
		# the expected answer
		tx = math.sqrt(2)
		ty = tx
		tz = 4*math.sqrt(3)
		
		x,y,z = v.spherical_to_cartesian().vals
		print("s2c result:",x,y,z)
		self.assertTrue(compare_close(x,tx),"bad x in s2c")
		self.assertTrue(compare_close(y,ty),"bad y in s2c")
		self.assertTrue(compare_close(z,tz),"bad z in s2c")
if __name__ == '__main__':
	unittest.main()
"""
import math


class TestVector3dm(unittest.TestCase):

	def test_spherical_to_cartesian(self):
		v = Vector3dm(8,math.pi/5.0,math.pi/6.0,"s")
		print("s2c start:",v)
	
		# the expected answer
		tx = math.sqrt(2)
		ty = tx
		tz = 4*math.sqrt(3)
		
		x,y,z = v.spherical_to_cartesian().vals
		print("s2c result:",x,y,z)
		self.assertTrue(compare_close(x,tx),"bad x in s2c")
		self.assertTrue(compare_close(y,ty),"bad y in s2c")
		self.assertTrue(compare_close(z,tz),"bad z in s2c")
		
	def test_cartesian_to_spherical(self):
		v = Vector3dm(2*sqrt(3),6,-4,"c")
		print("c2s start:",v)
		
		# the expected answer
		tr = 8.0
		tphi = math.pi/3.0
		ttheta = 2*math.pi/3.0
		
		r,phi,theta = v.cartesian_to_spherical().vals
		print("c2s result:",r,phi,theta)
		self.assertTrue(compare_close(r,tr))
		self.assertTrue(compare_close(phi,tphi))
		self.assertTrue(compare_close(theta,ttheta))
		
if __name__ == "__main__":
	unittest.main()
"""
