class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    shape = []
    for row in range(self.height):
      shape.append("*" * self.width + "\n")
    return "".join(shape)

  # Takes another shape object (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
  def get_amount_inside(self, shape):
    times_h = 0
    times_w = 0
    while self.width >= shape.width:
      self.width -= shape.width
      times_w += 1
    while self.height >= shape.height:
      self.height -= shape.height
      times_h += 1
    return times_h * times_w
    
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
  # The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  # The Square class should be able to access the Rectangle class methods but should also contain a set_side method. 
  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)
    
  # If an instance of a Square is represented as a string, 
  # it should look like: Square(side=9)
  def __str__(self):
    return f"Square(side={self.width})"
    
  #Additionally, the set_width and set_height methods on the Square class should set both the width and height.
  def set_width(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_height(self, side):
    super().set_height(side)
    super().set_width(side)