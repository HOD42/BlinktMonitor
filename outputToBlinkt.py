class OutputToBlinkt():
    def __init__(self,
                 p0r,p0g,p0b,
                 p1r,p1g,p1b,
                 p2r,p2g,p2b,
                 p3r,p3g,p3b,
                 p4r,p4g,p4b,
                 p5r,p5g,p5b,
                 p6r,p6g,p6b,
                 p7r,p7g,p7b
                 ):
        self.p0r=p0r
        self.p0g=p0g
        self.p0b=p0b
        self.p1r=p1r
        self.p1g=p1g
        self.p1b=p1b
        self.p2r=p2r
        self.p2g=p2g
        self.p2b=p2b
        self.p3r=p3r
        self.p3g=p3g
        self.p3b=p3b
        self.p4r=p4r
        self.p4g=p4g
        self.p4b=p4b
        self.p5r=p5r
        self.p5g=p5g
        self.p5b=p5b
        self.p6r=p6r
        self.p6g=p6g
        self.p6b=p6b
        self.p7r=p7r
        self.p7g=p7g
        self.p7b=p7b
        
    def set_values(p0r,p0g,p0b,
                   p1r,p1g,p1b,
                   p2r,p2g,p2b,
                   p3r,p3g,p3b,
                   p4r,p4g,p4b,
                   p5r,p5g,p5b,
                   p6r,p6g,p6b,
                   p7r,p7g,p7b):
        #import blinkt
        import time
        print("- - - - - - - - BLINKT! - - - - - - - -")
        #blinkt.set_all(1, 0, 0)
        #blinkt.show()
        #time.sleep(0.05)
        #blinkt.set_all(0, 1, 0)
        #blinkt.show()
        #time.sleep(0.05)
        #blinkt.set_all(0, 0, 1)
        #blinkt.show()
        #time.sleep(0.05)

        #blinkt.set_pixel(0,p0r,p0g,p0b)
        #blinkt.set_pixel(1,p1r,p1g,p1b)
        #blinkt.set_pixel(2,p2r,p2g,p2b)
        #blinkt.set_pixel(3,p3r,p3g,p3b)
        #blinkt.set_pixel(4,p4r,p4g,p4b)
        #blinkt.set_pixel(5,p5r,p5g,p5b)
        #blinkt.set_pixel(6,p6r,p6g,p6b)
        #blinkt.set_pixel(7,p7r,p7g,p7b)

        #blinkt.show()
        
        print(p0r,p0g,p0b)
        print(p1r,p1g,p1b)
        print(p2r,p2g,p2b)
        print(p3r,p3g,p3b)
        print(p4r,p4g,p4b)
        print(p5r,p5g,p5b)
        print(p6r,p6g,p6b)
        print(p7r,p7g,p7b)
        print("- - - - - - - - - - - - - - - - - - - -")
