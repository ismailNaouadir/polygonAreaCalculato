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
    return (self.width ** 2 + self.height ** 2) ** .5


  def __str__(self):
    st = "Rectangle(width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
    return st


  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      st = ""
      for l in range(self.height):
        for c in range(self.width):
          st += "*"
        st += "\n"
      return st
    



class Square(Rectangle):
  
  def __init__(self, side):
    Rectangle.__init__(self, side, side)


  def set_side(self, side):
    Rectangle.set_width(self, side)
    Rectangle.set_height(self, side)


  def set_width(self, side):
    Rectangle.set_width(self, side)
    Rectangle.set_height(self, side)

  def set_height(self, side):
    Rectangle.set_width(self, side)
    Rectangle.set_height(self, side)


  def __str__(self):
    st = "Square(side=" + str(self.width) + ")"
    return st


