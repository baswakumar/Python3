'''
Define a class Painting and a constructor to initialize variables followed by a method to display the
values held by variables. Use list to declare the values.
'''

class Paint():
    def __init__(self,pname,prate,ppainter):
        self.pname = pname
        self.prate = prate
        self.ppainter = ppainter

    def p_info(self):
        print("Paint Name is:", self.pname)
        print("\nPaint Rate is:", self.prate)
        print("\nPainter Name is:", self.ppainter)

#px = Paint('ABC',12345,'Don')
#px.p_info()
p1=[Paint('Acrylic Painting',10000,'Ram'),
    Paint('Canvas Painting',20000,'Sham'),
    Paint('Water Painting',30000,'Ravi'),
    Paint('Oil Painting',40000,'Ramesh')]

for x in p1:
    x.p_info()

