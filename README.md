# Vector3dm 

Vector3dm is a Python class that provides 3d vector functionality. 

## Dependencies

Vector3dm is dependent on the math, and copy libraries. 

## Installation

It is not part of pypy (yet? ever?) so put it in the tree and import it. The correct syntax would be 
```from vector3dm import Vector3dm```

## Usage

It's pretty much like every other 3d vector library except that it has dual types. 

Every vector can be either in cartesian coordinates or spherical coordinates with a `type` attribute to differentiate. Methods switch it back and forth (making a copy each time) but all the methods work on both type and return a vector in an arbitrary type. 

Want it in a specific type? Just feed the result into the converter -- it doesn't care which one you give it. 

The __array__ method converts it into numpy array (in cartesian coordinates) so I have access to the numpy math internally and you can just dump it into a numpy array if that's more convenient (but make sure you know what coord system it is first).

There is a numpy_to_vector3dm method to get things into Vector3dm from numpy and a vector_to_list method that takes it to a list which you cna then easily convert back to a numpy array. 

I originally was going to use numpy mehods but it added a completely unnecessary dependency and I didn't use it much so I pulled it out. 

```python
from vector3dm import Vector3dm

v = vector3dm(x,y,z,"c")
v2 = vector3dm(r,theta,phi,"s") # distance, azimuth, polar (as in mathematics)
v3 = v.add(v2) # sum of v and v2
v4 = v.sub(v2) # self - v2
d = v.magnitude(v2) # distance from v to v2
v_c = v2.convert_to_cartesian()
v_s = v.convert_to_spherical()
v4 = numpy_to_vector3dm(np_array)

#retrieval functions: convert to correct type and get it from the right place
x = v.get_x()
y = v.get_y()
z = v.get_z()
r = v.get_r()
theta = v.get_theta()
phi = v.get_phi()

#set functions: make sure the right element gets set
v.set_x(10)
v.set_y(10)
v.set_z(10)
v.set_r(10)
v.set_theta(10)
v.set_phi(10)


#various math functions
v5 = v.mult(5) 
v6 = v.neg()
v7 = v.cros(v2)
scalar = v.dot(v2)
scalar = v.inner(v2) # same as dot
v8 = v.point_at_that(v2) # vector from v to v2 where v and v2 are both positions
v9 = v.where_from_here (v8) # gets the position of the point by applying the vector v8 to v -- inverse of point_at_that()
vzero = Vector3dm.zero_vector() # creates a vector of zero length
```

## Contributing

I'm pretty much done but let me know if you think there's something more that would be useful. 
 * More tests are always welcome. 
  
## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
