# Vector3dm 

Vector3dm is a Python class that provides 3d vector functionality. 

## Dependencies

Vector3dm is dependent on the math, copy, and numpy libraries. 

## Installation

It is not part of pypy (yet? ever?) so put it in the tree and import it. 

## Usage

It's pretty much like every other 3d vector library except for 2 factors: 

First off, it has dual types -- every vector can be either in cartesian coordinates or spherical coordinates with a `type` attribute to differentiate. Methods switch it back and forth (making a copy each time) but all the methods work on both type and return a vector in an arbitrary type. 

Want it in a specific type? Just feed the result into the converter -- it doesn't care which one you give it. 

This is either really clever or a geeky version of "Good Idea, Bad Idea".  We'll see. 

Second, the __array__ method converts it into numpy array (in cartesian coordinates) so I have access to the numpy math internally and you can just dump it into a numpy array if that's more convenient (but make sure you know what coord system it is first).

```python
import foobar

v = vector3dm(x,y,z,"c")
v2 = vector3dm(r,theta,phi,"s") # distance, azimuth, polar (as in mathematics)
v3 = v.add(v2) # sum of v and v2
d = v.distance(v2) # distance from v to v2
v_c = v2.spherical_to_cartesian()
v_s = v.cartesian_to_spherical()

```

## Contributing

To date I seriously doubt there is any point: it has little functionality and fewer tests plus there are lots of these things out there. I only did my own because of the dual coordinate trick (seems like you have to switch back and forth to do anything so why not hide that if you can?). 

## License

[Apache](https://www.apache.org/licenses/LICENSE-2.0)

