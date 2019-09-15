import  unittest
import math
from vector3dm import Vector3dm

def compare_close(a,b): # compare a&b to within delta
	delta = .000001
	#print("compare_close"delta,,a,b,b-delta,b+delta)
	return a >= b-delta and a <= b+delta
	#if a >= b-delta and a <= b+delta1:
	#	return True
	#else:
	#	return False

class TestVector3dm(unittest.TestCase):
	# tests from https://www.math.utah.edu/lectures/math2210/9PostNotes.pdf
	def test_convert_to_cartesian(self):
		r = 8
		theta = math.pi/4
		phi = math.pi/6
		
		v = Vector3dm(r,theta,phi,"s")
		#print("s2c start:",v)
	
		# the expected answer
		tx = 2*math.sqrt(2)
		ty = tx
		tz = 4*math.sqrt(3)
		
		v2 =  v.convert_to_cartesian()
		x,y,z = v2.vals
		#print("s2c result:",x,y,z)
		self.assertTrue(compare_close(x,tx),"s2c bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"s2c bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"s2c bad z: is {} should be {}".format(z,tz))
		
		x,y,z = v2.convert_to_cartesian().vals # should do nothing
		self.assertTrue(compare_close(x,tx),"s2c #2 bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"s2c #2 bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"s2c #2 bad z: is {} should be {}".format(z,tz))
		


	def test_convert_to_spherical(self):
		x = 2*math.sqrt(3)
		y = 6
		z = -4
		
		v = Vector3dm(x,y,z,"c")
		#print("c2s start:",v)
		
		# the expected answer
		tr = 8.0
		ttheta = math.pi/3.0
		tphi = 2*math.pi/3.0
		
		v2 = v.convert_to_spherical()
		r,theta,phi = v2.vals
		#print("c2s result:",r,theta,phi)
		self.assertTrue(compare_close(r,tr),"c2s bad r: is {} should be {}".format(r,tr))
		self.assertTrue(compare_close(theta,ttheta),"c2s bad theta: is {} should be {}".format(theta,ttheta))
		self.assertTrue(compare_close(phi,tphi),"c2s bad phi: is {} should be {}".format(phi,tphi))
		
		r,theta,phi = v2.convert_to_spherical().vals # should do nothing
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
		#print(v.convert_to_spherical())
		#print(v.convert_to_spherical().convert_to_cartesian())
		x,y,z = v.convert_to_spherical().convert_to_cartesian().vals
		#print(x,y,z)
		self.assertTrue(compare_close(x,tx),"inversion1 bad x: is {} should be {}".format(x,tx))
		self.assertTrue(compare_close(y,ty),"inversion1 bad y: is {} should be {}".format(y,ty))
		self.assertTrue(compare_close(z,tz),"inversion1 bad z: is {} should be {}".format(z,tz))
		
		tr = 8
		ttheta = math.pi/4
		tphi = math.pi/6
		v = Vector3dm(tr,ttheta,tphi,"s")
		r,theta,phi = v.convert_to_cartesian().convert_to_spherical().vals
		self.assertTrue(compare_close(r,tr),"inversion2 #2 bad r: is {} should be {}".format(r,tr))
		self.assertTrue(compare_close(theta,ttheta),"inversion2 #2 bad theta: is {} should be {}".format(theta,ttheta))
		self.assertTrue(compare_close(phi,tphi),"inversion2 bad #2 phi: is {} should be {}".format(phi,tphi))
		
	def test_magnitude(self):
		expected_mag = 18.78829423
		v1 = Vector3dm(7,4,1,"c")
		v2 = Vector3dm(13,18,-10,"c")
		mag = v1.magnitude(v2)
		self.assertTrue(compare_close(mag,expected_mag),"magnitude1 bad mag: is {} should be {}".format(mag,expected_mag))

		expected_mag = 29.06888371
		v1 = Vector3dm(-3,18,6,"c")
		v2 = Vector3dm(8,-2,-12,"c")
		mag = v1.magnitude(v2)
		self.assertTrue(compare_close(mag,expected_mag),"magnitude2 bad mag: is {} should be {}".format(mag,expected_mag))

		expected_mag = 23.53720459
		v1 = Vector3dm(12,-19,7,"c")
		
		mag = v1.magnitude()
		self.assertTrue(compare_close(mag,expected_mag),"magnitude3 bad mag: is {} should be {}".format(mag,expected_mag))

	def test_origin_distance(self):
		expected_dist = 1.7320508075688772935274463415059
		v1 = Vector3dm(-1,1,1,"c")	
		#print("test_origin_distance",expected_dist,v1)
		dist = v1.origin_distance()
		#print("dist",dist,"expected",expected_dist)
		self.assertTrue(compare_close(dist,expected_dist),"origindist bad distance: is {} should be {}".format(dist,expected_dist))
	
	def test_add(self):
		expected_sum_x = -6
		expected_sum_y = 13
		expected_sum_z = -25
		v1 = Vector3dm(13,-5,-20,"c")
		v2 = Vector3dm(-19,18,-5,"c")
		v3 = v1.add(v2)
		x,y,z = v3.vals
		self.assertTrue(compare_close(x,expected_sum_x),"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertTrue(compare_close(y,expected_sum_y),"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertTrue(compare_close(z,expected_sum_z),"origindist bad distance: is {} should be {}".format(z,expected_sum_z))

	def test_sub(self):
		expected_sum_x = 10
		expected_sum_y = -21
		expected_sum_z = 9
		v1 = Vector3dm(-9,-4,10,"c")
		v2 = Vector3dm(-19,17,1,"c")
		v3 = v1.sub(v2)
		x,y,z = v3.vals
		self.assertTrue(compare_close(x,expected_sum_x),"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertTrue(compare_close(y,expected_sum_y),"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertTrue(compare_close(z,expected_sum_z),"origindist bad distance: is {} should be {}".format(z,expected_sum_z))

	def test_neg(self):
		expected_sum_x = 5
		expected_sum_y = 13
		expected_sum_z = -4
		v1 = Vector3dm(-5,-13,4,"c")
		v3 = v1.neg()
		x,y,z = v3.vals
		self.assertTrue(compare_close(x,expected_sum_x),"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertTrue(compare_close(y,expected_sum_y),"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertTrue(compare_close(z,expected_sum_z),"origindist bad distance: is {} should be {}".format(z,expected_sum_z))

	def test_where_from_here(self):
		#example from http://mathonline.wikidot.com/determining-a-vector-given-two-points; rearranged
		x1 = 2
		y1 = 2
		z1 = 1
		x2 = 4
		y2 = 1
		z2 = 1
		exp_x = 6
		exp_y = 3
		exp_z = 2
		v1 = Vector3dm(x1,y1,z1,"c")
		v2 = Vector3dm(x2,y2,z2,"c")
		res_v = v1.where_from_here(v2).convert_to_cartesian()
		rx = res_v.vals[0]
		ry = res_v.vals[1]
		rz = res_v.vals[2]
		self.assertTrue(compare_close(rx,exp_x),"where_from_here x bad result: is {} should be {}".format(rx,exp_x))
		self.assertTrue(compare_close(ry,exp_y),"where_from_here y bad result: is {} should be {}".format(ry,exp_y))
		self.assertTrue(compare_close(rz,exp_z),"where_from_here z bad result: is {} should be {}".format(rz,exp_z))

	def test_dot(self):
		# got example from https://chortle.ccsu.edu/VectorLessons/vch07/vch07_14.html
		expected_dot = -14.0
		x1 = -1
		y1 = 2
		z1 = -3
		x2 = 1
		y2 = -2
		z2 = 3
		v1 = Vector3dm(x1,y1,z1,"c")
		v2 = Vector3dm(x2,y2,z2,"c")
		dot = v1.dot(v2)
		self.assertTrue(compare_close(dot,expected_dot),"Dot bad result: is {} should be {}".format(dot,expected_dot))
		
	def test_point_at_that(self):
		#example from http://mathonline.wikidot.com/determining-a-vector-given-two-points
		x1 = 2
		y1 = 2
		z1 = 1
		x2 = 6
		y2 = 3
		z2 = 2
		exp_x = 4
		exp_y = 1
		exp_z = 1
		v1 = Vector3dm(x1,y1,z1,"c")
		v2 = Vector3dm(x2,y2,z2,"c")
		res_v = v1.point_at_that(v2).convert_to_cartesian()
		rx = res_v.vals[0]
		ry = res_v.vals[1]
		rz = res_v.vals[2]
		self.assertTrue(compare_close(rx,exp_x),"point_at_that x bad result: is {} should be {}".format(rx,exp_x))
		self.assertTrue(compare_close(ry,exp_y),"point_at_that y bad result: is {} should be {}".format(ry,exp_y))
		self.assertTrue(compare_close(rz,exp_z),"point_at_that z bad result: is {} should be {}".format(rz,exp_z))
		
	
	def test_inner(self):
		expected_dot = -14.0
		x1 = -1
		y1 = 2
		z1 = -3
		x2 = 1
		y2 = -2
		z2 = 3
		v1 = Vector3dm(x1,y1,z1,"c")
		v2 = Vector3dm(x2,y2,z2,"c")
		dot = v1.dot(v2)
		self.assertTrue(compare_close(dot,expected_dot),"Dot bad result: is {} should be {}".format(dot,expected_dot))
		
	def test_get_x(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(x,y,z,"c")
		res_x = v1.get_x()
		self.assertTrue(compare_close(res_x,x),"get_x bad result: is {} should be {}".format(res_x,x))
	def test_get_y(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(x,y,z,"c")
		res_y = v1.get_y()
		self.assertTrue(compare_close(res_y,y),"get_y bad result: is {} should be {}".format(res_y,y))
	def test_get_z(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(z,y,z,"c")
		res_z = v1.get_z()
		self.assertTrue(compare_close(res_z,z),"get_z bad result: is {} should be {}".format(res_z,z))
	def test_get_r(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_r = v1.get_r()
		self.assertTrue(compare_close(res_r,r),"get_r bad result: is {} should be {}".format(res_r,r))
	def test_get_theta(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_theta = v1.get_theta()
		self.assertTrue(compare_close(res_theta,theta),"get_r bad result: is {} should be {}".format(res_theta,theta))
	def test_get_phi(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_phi = v1.get_phi()
		self.assertTrue(compare_close(res_phi,phi),"get_phi bad result: is {} should be {}".format(res_phi,phi))
		
if __name__ == '__main__':
	unittest.main()
