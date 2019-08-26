import  unittest
import math
from vector3dm import Vector3dm

def compare_close(a,b): # compare a&b to within 1/100000
	#print("compare_close",a,b,b-0.00001,b+0.00001)
	return a >= b-0.00001 and a <= b+0.00001
	#if a >= b-0.00001 and a <= b+0.00001:
	#	return True
	#else:
	#	return False

class TestBasicFunction(unittest.TestCase):
	# tests from https://www.math.utah.edu/lectures/math2210/9PostNotes.pdf
	def test_spherical_to_cartesian(self):
		r = 8
		theta = math.pi/4
		phi = math.pi/6
		
		v = Vector3dm(r,theta,phi,"s")
		#print("s2c start:",v)
	
		# the expected answer
		tx = 2*math.sqrt(2)
		ty = tx
		tz = 4*math.sqrt(3)
		
		v2 =  v.spherical_to_cartesian()
		x,y,z = v2.vals
		#print("s2c result:",x,y,z)
		self.assertTrue(compare_close(x,tx),"s2c bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"s2c bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"s2c bad z: is {} should be {}".format(z,tz))
		
		x,y,z = v2.spherical_to_cartesian().vals # should do nothing
		self.assertTrue(compare_close(x,tx),"s2c #2 bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"s2c #2 bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"s2c #2 bad z: is {} should be {}".format(z,tz))
		


	def test_cartesian_to_spherical(self):
		x = 2*math.sqrt(3)
		y = 6
		z = -4
		
		v = Vector3dm(x,y,z,"c")
		#print("c2s start:",v)
		
		# the expected answer
		tr = 8.0
		ttheta = math.pi/3.0
		tphi = 2*math.pi/3.0
		
		v2 = v.cartesian_to_spherical()
		r,theta,phi = v2.vals
		#print("c2s result:",r,theta,phi)
		self.assertTrue(compare_close(r,tr),"c2s bad r: is {} should be {}".format(r,tr))
		self.assertTrue(compare_close(theta,ttheta),"c2s bad theta: is {} should be {}".format(theta,ttheta))
		self.assertTrue(compare_close(phi,tphi),"c2s bad phi: is {} should be {}".format(phi,tphi))
		
		r,theta,phi = v2.cartesian_to_spherical().vals # should do nothing
		#print("c2s result:",r,theta,phi)
		self.assertTrue(compare_close(r,tr),"c2s #2 bad r: is {} should be {}".format(r,tr))
		self.assertTrue(compare_close(theta,ttheta),"c2s #2 bad theta: is {} should be {}".format(theta,ttheta))
		self.assertTrue(compare_close(phi,tphi),"c2s bad #2 phi: is {} should be {}".format(phi,tphi))

	def test_conversion_inversion_c2s_s2c(self):
		tx = 2*math.sqrt(3)
		ty = 6
		tz = -4

		v = Vector3dm(tx,ty,tz,"c")
		#print("inversion",v)
		#print(v.cartesian_to_spherical())
		#print(v.cartesian_to_spherical().spherical_to_cartesian())
		x,y,z = v.cartesian_to_spherical().spherical_to_cartesian().vals
		#print(x,y,z)
		self.assertTrue(compare_close(x,tx),"inversion1 bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"inversion1 bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"inversion1 bad z: is {} should be {}".format(z,tz))
		
		tr = 8
		ttheta = math.pi/4
		tphi = math.pi/6
		v = Vector3dm(tr,ttheta,tphi,"s")
		r,theta,phi = v.spherical_to_cartesian().cartesian_to_spherical().vals
		self.assertTrue(compare_close(r,tr),"inversion2 #2 bad r: is {} should be {}".format(r,tr))
		self.assertTrue(compare_close(theta,ttheta),"inversion2 #2 bad theta: is {} should be {}".format(theta,ttheta))
		self.assertTrue(compare_close(phi,tphi),"inversion2 bad #2 phi: is {} should be {}".format(phi,tphi))
		
		
		

if __name__ == '__main__':
	unittest.main()
"""
import math


class TestVector3dm(unittest.TestCase):

		
if __name__ == "__main__":
	unittest.main()
"""
