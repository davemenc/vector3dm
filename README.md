# Vector3dm 

Vector3dm is a Python class that provides 3d vector functionality. 

## Dependencies

Vector3dm is dependent on the math, copy, and numpy libraries. 

## Installation

It is not part of pypy (yet? ever?) so put it in the tree and import it. The correct syntax would be 
```from vector3dm import Vector3dm```


## Usage

It's pretty much like every other 3d vector library except for 2 factors: 

First off, it has dual types -- every vector can be either in cartesian coordinates or spherical coordinates with a `type` attribute to differentiate. Methods switch it back and forth (making a copy each time) but all the methods work on both type and return a vector in an arbitrary type. 

Want it in a specific type? Just feed the result into the converter -- it doesn't care which one you give it. 

This is either really clever or a geeky version of "Good Idea, Bad Idea".  We'll see. 

Second, the __array__ method converts it into numpy array (in cartesian coordinates) so I have access to the numpy math internally and you can just dump it into a numpy array if that's more convenient (but make sure you know what coord system it is first).

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
#retrival functions: convert to correct type and get it from the right place
x = v.get_x()
y = v.get_y()
z = v.get_z()
r = v.get_r()
theta = v.get_theta()
phi = v.get_phi()
v5 = v.mult(5) 
v6 = v.neg()
v7 = v.cros(v2)
scalar = v.dot(v2)
scalar = v.inner(v2) # same as dot
v8 = v.point_at_that(v2) # vector from v to v2 where v and v2 are both positions
v9 = v.where_from_here (v8) # gets the position of the point by applying the vector v8 to v -- inverse of point_at_that()




```

## Contributing

There are lots of these things out there. I only did my own because of the dual coordinate trick (seems like you have to switch back and forth to do anything so why not hide that if you can?). 
I would say that I need more tests and, as of this writting, there is some broken funcaitonality so if you have a mind to contribute, please ping me. 

## License

[Apache](https://www.apache.org/licenses/LICENSE-2.0)

