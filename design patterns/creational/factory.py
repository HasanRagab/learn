class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type:str) -> Shape:
        shapes = {"circle": Circle, "square": Square}
        return shapes.get(shape_type.lower(), Shape)()

shape = ShapeFactory.get_shape("circle")
print(shape.draw())
