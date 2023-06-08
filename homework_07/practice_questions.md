
----

1. Write the CommandPrompt class that outputs a command line with a prompt text as follows:

* The '**__init __**' method of the class will have the following parametric structure:

      def __init__(self, prompt)

    This method will take the prompt text and assign it to the instance attribute called prompt.


* The class's '**run**' method will output the command line. This method will take input text from the keyboard in an 
infinite loop, and it will print the text in reverse. When the "**quit**" command is given, it will end the process. 
The run method's parametric structure is as follows:

      def run(self)

    You can test the class with the following code:

      cp = CommandPrompt('CSD')
      cp.run()

----

2. Write a class called Rectangle as follows:

* The init method of the class will take the coordinates of the upper left and lower right corner points of the 
rectangle and store them in int-type instance attributes called x1, y1, x2, and y2. The parametric structure of 
the init method is as follows:

      def init(self, x1, y1, x2, y2)

    Here, the coordinates of the upper left and lower right corner of the rectangle are specified in terms of the screen 
coordinate system, not the Cartesian coordinate system.


* The isinside method of the class will take the coordinates of a point and return a bool value indicating whether 
the point is inside the rectangle. The parametric structure of the isinside method is as follows:

      def isinside(self, x, y)

    The x and y parameters of the method specify the coordinates of the point.


* The disp method of the class will print the rectangle in the following format:

      x1 = <value>, y1 = <value>, x2 = <value>, y2 = <value>

    Here, the x and y coordinates of the point also specify the position in terms of the screen coordinate system.


* The intersect method of the class will take another Rectangle object as a parameter and return the rectangle of 
intersection between the rectangle and the parameter-specified rectangle. If there is no intersection set between the 
* two rectangles, the intersect method will return None. The parametric structure of the method is as follows:

      def intersect(self, rect)

    You can test the class with the following code:

      r1 = Rectangle(10, 10, 20, 20)
      r1.disp()

      print('Inside' if r1.isinside(12, 14) else 'Not Inside')

      r2 = Rectangle(15, 15, 30, 30)
      r3 = r1.intersect(r2)
      if r3:
        r3.disp()
      else:
        print('There is no intersection')

Note: the test code is provided as an example and the outcome may vary depending on the input values provided.

----

3. Write a class called Circle. The class's init method should store the center coordinates and radius of the circle 
given in the Cartesian coordinate system in the class's instance attributes, centerx, centery, and radius. The other 
methods should use these instance attributes to perform the operations listed below. The class declaration should 
be as follows:

       class Circle:
            def init(self, *, x, y, r):
                pass

            def disp(self):
                pass

            def move(self, xoff, yoff):
                pass

            def isinside(self, x, y):
                pass

* The disp method will print the circle information to the screen as:

      center = (<value>, <value), radius = <value>

* The move method should move the center of the circle by xoff and yoff.

* The isinside method should determine whether the given point is inside the circle. The method's return value should 
* be of type bool. You can test the class with the following code:

      c = Circle(10, 12, 5)
      c.disp()

      c.move(-2, 4)
      c.disp()

      print('Inside' if c.isinside(5, 7) else 'Not Inside')

----