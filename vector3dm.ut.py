import  unittest
import math
from vector3dm import Vector3dm


class TestVector3dm(unittest.TestCase):
	# tests from https://www.math.utah.edu/lectures/math2210/9PostNotes.pdf
	def test_convert_to_cartesian(self):
		r = 8
		theta = math.pi/4
		phi = math.pi/6
		
		v = Vector3dm(r,theta,phi,"s")
	
		# the expected answer
		tx = 2*math.sqrt(2)
		ty = tx
		tz = 4*math.sqrt(3)
		
		v2 =  v.convert_to_cartesian()
		x,y,z = v2.vals
		self.assertAlmostEqual(x,tx,6,"s2c bad x: is {} should be {}".format(x,tx))
		self.assertAlmostEqual(y,ty,6,"s2c bad y: is {} should be {}".format(y,ty))
		self.assertAlmostEqual(z,tz,6,"s2c bad z: is {} should be {}".format(z,tz))
		
		x,y,z = v2.convert_to_cartesian().vals # should do nothing
		self.assertAlmostEqual(x,tx,6,"s2c #2 bad x: is {} should be {}".format(x,tx))
		self.assertAlmostEqual(y,ty,6,"s2c #2 bad y: is {} should be {}".format(y,ty))
		self.assertAlmostEqual(z,tz,6,"s2c #2 bad z: is {} should be {}".format(z,tz))
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		self.assertEqual(type(v.vals),type([]),"test changed vals type")


	def test_convert_to_spherical(self):
		x = 2*math.sqrt(3)
		y = 6
		z = -4
		
		v = Vector3dm(x,y,z,"c")

		
		# the expected answer
		tr = 8.0
		ttheta = math.pi/3.0
		tphi = 2*math.pi/3.0
		
		v2 = v.convert_to_spherical()
		r,theta,phi = v2.vals

		self.assertAlmostEqual(r,tr,6,"c2s bad r: is {} should be {}".format(r,tr))
		self.assertAlmostEqual(theta,ttheta,6,"c2s bad theta: is {} should be {}".format(theta,ttheta))
		self.assertAlmostEqual(phi,tphi,6,"c2s bad phi: is {} should be {}".format(phi,tphi))
		
		r,theta,phi = v2.convert_to_spherical().vals # should do nothing

		self.assertAlmostEqual(r,tr,6,"c2s #2 bad r: is {} should be {}".format(r,tr))
		self.assertAlmostEqual(theta,ttheta,6,"c2s #2 bad theta: is {} should be {}".format(theta,ttheta))
		self.assertAlmostEqual(phi,tphi,6,"c2s bad #2 phi: is {} should be {}".format(phi,tphi))
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")

	def test_conversion_inversion_c2s_s2c(self):
		tx = 2*math.sqrt(3)
		ty = 6
		tz = -4

		v = Vector3dm(tx,ty,tz,"c")
		x,y,z = v.convert_to_spherical().convert_to_cartesian().vals
		self.assertAlmostEqual(x,tx,6,"inversion1 bad x: is {} should be {}".format(x,tx))
		self.assertAlmostEqual(y,ty,6,"inversion1 bad y: is {} should be {}".format(y,ty))
		self.assertAlmostEqual(z,tz,6,"inversion1 bad z: is {} should be {}".format(z,tz))
		
		tr = 8
		ttheta = math.pi/4
		tphi = math.pi/6
		v = Vector3dm(tr,ttheta,tphi,"s")
		r,theta,phi = v.convert_to_cartesian().convert_to_spherical().vals
		self.assertAlmostEqual(r,tr,6,"inversion2 #2 bad r: is {} should be {}".format(r,tr))
		self.assertAlmostEqual(theta,ttheta,6,"inversion2 #2 bad theta: is {} should be {}".format(theta,ttheta))
		self.assertAlmostEqual(phi,tphi,6,"inversion2 bad #2 phi: is {} should be {}".format(phi,tphi))
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
		
	def test_magnitude(self):
		expected_mag = 18.78829423
		v1 = Vector3dm(7,4,1,"c")
		v2 = Vector3dm(13,18,-10,"c")
		mag = v1.magnitude(v2)
		self.assertAlmostEqual(mag,expected_mag,6,"magnitude1 bad mag: is {} should be {}".format(mag,expected_mag))

		expected_mag = 29.06888371
		v1 = Vector3dm(-3,18,6,"c")
		v2 = Vector3dm(8,-2,-12,"c")
		mag = v1.magnitude(v2)
		self.assertAlmostEqual(mag,expected_mag,6,"magnitude2 bad mag: is {} should be {}".format(mag,expected_mag))

		expected_mag = 23.53720459
		v1 = Vector3dm(12,-19,7,"c")
		
		mag = v1.magnitude()
		self.assertAlmostEqual(mag,expected_mag,6,"magnitude3 bad mag: is {} should be {}".format(mag,expected_mag))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")

	def test_origin_distance(self):
		expected_dist = 1.7320508075688772935274463415059
		v1 = Vector3dm(-1,1,1,"c")	

		dist = v1.origin_distance()
		self.assertAlmostEqual(dist,expected_dist,6,"origindist bad distance: is {} should be {}".format(dist,expected_dist))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_add(self):
		expected_sum_x = -6
		expected_sum_y = 13
		expected_sum_z = -25
		v1 = Vector3dm(13,-5,-20,"c")
		v2 = Vector3dm(-19,18,-5,"c")
		v3 = v1.add(v2)
		x,y,z = v3.vals
		self.assertAlmostEqual(x,expected_sum_x,6,"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertAlmostEqual(y,expected_sum_y,6,"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertAlmostEqual(z,expected_sum_z,6,"origindist bad distance: is {} should be {}".format(z,expected_sum_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		self.assertEqual(type(v3.vals),type([]),"test changed vals type")

	def test_sub(self):
		expected_sum_x = 10
		expected_sum_y = -21
		expected_sum_z = 9
		v1 = Vector3dm(-9,-4,10,"c")
		v2 = Vector3dm(-19,17,1,"c")
		v3 = v1.sub(v2)
		x,y,z = v3.vals
		self.assertAlmostEqual(x,expected_sum_x,6,"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertAlmostEqual(y,expected_sum_y,6,"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertAlmostEqual(z,expected_sum_z,6,"origindist bad distance: is {} should be {}".format(z,expected_sum_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		self.assertEqual(type(v3.vals),type([]),"test changed vals type")

	def test_neg(self):
		expected_sum_x = 5
		expected_sum_y = 13
		expected_sum_z = -4
		v1 = Vector3dm(-5,-13,4,"c")
		v3 = v1.neg()
		x,y,z = v3.vals
		self.assertAlmostEqual(x,expected_sum_x,6,"origindist bad distance: is {} should be {}".format(x,expected_sum_x))
		self.assertAlmostEqual(y,expected_sum_y,6,"origindist bad distance: is {} should be {}".format(y,expected_sum_y))
		self.assertAlmostEqual(z,expected_sum_z,6,"origindist bad distance: is {} should be {}".format(z,expected_sum_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v3.vals),type([]),"test changed vals type")

	def test_mult(self):
		v = Vector3dm(1,1,1,"c")
		v_mult = v.mult(6.0)
		x,y,z = v_mult.vals
		self.assertAlmostEqual(x,6.0,6,"mult x: is {} should be {}".format(x,6.0))
		self.assertAlmostEqual(y,6.0,6,"mult y: is {} should be {}".format(y,6.0))
		self.assertAlmostEqual(z,6.0,6,"mult z: is {} should be {}".format(z,6.0))
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
		
		r = v_mult.get_r()
		self.assertAlmostEqual(r, 10.392304845413264,6,"mult r: is {} should be {}".format(r,6.0))
		
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
		self.assertAlmostEqual(rx,exp_x,6,"where_from_here x bad result: is {} should be {}".format(rx,exp_x))
		self.assertAlmostEqual(ry,exp_y,6,"where_from_here y bad result: is {} should be {}".format(ry,exp_y))
		self.assertAlmostEqual(rz,exp_z,6,"where_from_here z bad result: is {} should be {}".format(rz,exp_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		self.assertEqual(type(res_v.vals),type([]),"test changed vals type")

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
		self.assertAlmostEqual(dot,expected_dot,6,"Dot bad result: is {} should be {}".format(dot,expected_dot))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		
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
		self.assertAlmostEqual(rx,exp_x,6,"point_at_that x bad result: is {} should be {}".format(rx,exp_x))
		self.assertAlmostEqual(ry,exp_y,6,"point_at_that y bad result: is {} should be {}".format(ry,exp_y))
		self.assertAlmostEqual(rz,exp_z,6,"point_at_that z bad result: is {} should be {}".format(rz,exp_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		
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
		self.assertAlmostEqual(dot,expected_dot,6,"Dot bad result: is {} should be {}".format(dot,expected_dot))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
		
	def test_get_x(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(x,y,z,"c")
		res_x = v1.get_x()
		self.assertAlmostEqual(res_x,x,6,"get_x bad result: is {} should be {}".format(res_x,x))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_get_y(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(x,y,z,"c")
		res_y = v1.get_y()
		self.assertAlmostEqual(res_y,y,6,"get_y bad result: is {} should be {}".format(res_y,y))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_get_z(self):
		x = 1
		y = 2
		z = 3
		v1 = Vector3dm(z,y,z,"c")
		res_z = v1.get_z()
		self.assertAlmostEqual(res_z,z,6,"get_z bad result: is {} should be {}".format(res_z,z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_get_r(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_r = v1.get_r()
		self.assertAlmostEqual(res_r,r,6,"get_r bad result: is {} should be {}".format(res_r,r))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_get_theta(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_theta = v1.get_theta()
		self.assertAlmostEqual(res_theta,theta,6,"get_r bad result: is {} should be {}".format(res_theta,theta))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
	
	def test_get_phi(self):
		r = 1
		theta = 2
		phi = 3
		v1 = Vector3dm(r,theta,phi,"s")
		res_phi = v1.get_phi()
		self.assertAlmostEqual(res_phi,phi,6,"get_phi bad result: is {} should be {}".format(res_phi,phi))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")

	def test_set_phi(self):
		r = 1
		theta = 2
		phi = 3
		v = Vector3dm(r,theta,phi,"s")
		v.set_phi(10)
		phi = v.get_phi()
		self.assertAlmostEqual(10,phi,6,"set_phi bad result: is {} should be {}".format(phi,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")

	def test_set_theta(self):
		r = 1
		theta = 2
		phi = 3
		v = Vector3dm(r,theta,phi,"s")
		v.set_theta(10)
		theta = v.get_theta()
		self.assertAlmostEqual(10,theta,6,"set_phi bad result: is {} should be {}".format(theta,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
	
	def test_set_r(self):
		r = 1
		theta = 2
		phi = 3
		v = Vector3dm(r,theta,phi,"s")
		v.set_r(10)
		r = v.get_r()
		self.assertAlmostEqual(10,r,6,"set_phi bad result: is {} should be {}".format(r,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")

	def test_set_x(self):
		x = 1
		y = 2
		z = 3
		v = Vector3dm(x,y,z,"c")
		v.set_x(10)
		x = v.get_x()
		self.assertAlmostEqual(10,x,6,"set_x bad result: is {} should be {}".format(x,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")

	def test_set_y(self):
		x = 1
		y = 2
		z = 3
		v = Vector3dm(x,y,z,"c")
		v.set_y(10)
		y = v.get_y()
		self.assertAlmostEqual(10,y,6,"set_y bad result: is {} should be {}".format(y,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")

	def test_set_z(self):
		x = 1
		y = 2
		z = 3
		v = Vector3dm(x,y,z,"c")
		v.set_z(10)
		z = v.get_z()
		self.assertAlmostEqual(10,z,6,"set_z bad result: is {} should be {}".format(z,10))		
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
	
	def test_zero_vector(self):
		zero_vector = Vector3dm.zero_vector()
		vx = zero_vector.get_x()
		vy = zero_vector.get_y()
		vz = zero_vector.get_z()
		vr = zero_vector.get_r()
		self.assertAlmostEqual(vx,0.0,6,"test_zero_vector bad result: is {} should be {}".format(vx,0.0))
		self.assertAlmostEqual(vy,0.0,6,"test_zero_vector bad result: is {} should be {}".format(vy,0.0))
		self.assertAlmostEqual(vz,0.0,6,"test_zero_vector bad result: is {} should be {}".format(vz,0.0))
		self.assertAlmostEqual(vr,0.0,6,"test_zero_vector bad result: is {} should be {}".format(vr,0.0))
		self.assertEqual(type(zero_vector.vals),type([]),"test changed vals type")

	def test_cross_product(self):
		v1 = Vector3dm(2,3,4,"c")
		v2 = Vector3dm(5,6,7,"c")
		r_x = -3.0
		r_y = 6.0
		r_z = -3.0
		v1_x_v2 = v1.cross(v2)
		x = v1_x_v2.get_x()
		y = v1_x_v2.get_y()
		z = v1_x_v2.get_z()
		self.assertAlmostEqual(x,r_x,6,"test_cross bad result: is {} should be {}".format(x,r_x))
		self.assertAlmostEqual(y,r_y,6,"test_cross bad result: is {} should be {}".format(y,r_y))
		self.assertAlmostEqual(z,r_z,6,"test_cross bad result: is {} should be {}".format(z,r_z))
		self.assertEqual(type(v1.vals),type([]),"test changed vals type")
		self.assertEqual(type(v2.vals),type([]),"test changed vals type")
	
	def test_unit_vector(self):
		v = Vector3dm(12,-3,-4,"c").unit()
		r_x = 12/13
		r_y = -3/13
		r_z = -4/13
		x,y,z = v.get_x(),v.get_y(),v.get_z()
		self.assertAlmostEqual(x,r_x,6,"test_unit bad result: is {} should be {}".format(x,r_x))
		self.assertAlmostEqual(y,r_y,6,"test_unit bad result: is {} should be {}".format(y,r_y))
		self.assertAlmostEqual(z,r_z,6,"test_unit bad result: is {} should be {}".format(z,r_z))
		self.assertEqual(type(v.vals),type([]),"test changed vals type")
		
	
if __name__ == '__main__':
	unittest.main()
