import sys

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y 
  def __str__(self):
      return f"({self.x}, {self.y})"


class Line():
    def __init__(self, start:"Point", end:"Point"):
        self.start = start
        self.end = end
        self.__lenght = ((end.x + start.x)**2 + (end.y + start.y)**2)**0.5
        self.__slope = (end.y - start.y)/(end.x - start.x) if (end.x - start.x) != 0 else "indefinida"
    def compute_length(self):
        return self.__lenght
    def compute_slope(self):
        return self.__slope
    def compute_horizontal_cross(self):
        return self.start.y <= 0 <= self.end.y or self.start.y >= 0 >= self.end.y
    def compute_vertical_cross(self):
        return self.start.x <= 0 <= self.end.x or self.start.x >= 0 >= self.end.x

line = Line(Point(0, 0), Point(0, 5))
print(line.start, line.end, 
      line.compute_length, line.compute_slope, 
      line.compute_horizontal_cross,
      line.compute_vertical_cross)


class Rectangle: 
    def __confirm_data(self, values:list):
        isValid = True
        for value in values:
            isValid = value != None and isValid
        if not isValid: 
            print("Datos inválidos. Terminando el programa...")
            sys.exit(1)
    def __calc_height_n_width(self, a:"Point", c:"Point"):
        return abs(c.x - a.x), abs(c.y - a.y)
        
    def Method1(self, point:"Point", width:float, height:float):
        self.__confirm_data([point, width, height])
        self.a = point
        self.b = Point(point.x + width, point.y)
        self.c = Point(point.x + width, point.y + height)
        self.d = Point(point.x, point.y + height)

    def Method2(self, center:"Point", width:float, height:float):
        self.__confirm_data([center, width, height])
        self.a = Point(center.x - (width / 2), center.y - (height / 2))
        self.b = Point(center.x + (width / 2), center.y - (height / 2))
        self.c = Point(center.x + (width / 2), center.y + (height / 2))
        self.d = Point(center.x - (width / 2), center.y + (height / 2))

    def Method3(self, point:"Point", point2:"Point"):
        self.__confirm_data([point, point2])
        self.a = point
        self.b = Point(point2.x, point.y)
        self.c = point2
        self.d = Point(point.x, point2.y)
    def Method4(self, lines:list["Line"]):
        self.__confirm_data(lines)
        self.a = lines[0].start
        self.b = lines[1].start
        self.c = lines[2].start
        self.d = lines[3].start
   
    def __init__(self, method:int, values:list):
        match(method):
            case 1: self.Method1(values[0], values[1], values[2])
            case 2: self.Method2(values[0], values[1], values[2])
            case 3: self.Method3(values[0], values[1])
            case 4: self.Method4(values[0])
        (self.width, self.height) = self.__calc_height_n_width(self.a, self.c)
        
    def __str__(self):
        return (
            f"{self.__class__.__name__} con valores:\n"
            f"Punto a: {self.a}\n"
            f"Punto b: {self.b}\n"
            f"Punto c: {self.c}\n"
            f"Punto d: {self.d}\n"
            f"Ancho: {self.width}\n"
            f"Alto: {self.height}"
        )
