class JsTestTask:

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def __repr__(self):
        return "JsTestTask(%s, %s, %s)" % (self.name, self.image, self.price)