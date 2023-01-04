import Product


class Vendor:
    def __int__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, cpe):
        for product in self.products:
            if product.name == name:
                raise Exception("Product already exist")

        self.products.append(Product(name, cpe))

    def get_cves(self):
        vendor_cves = []
        for product in self.products:
            product_cves = product.get_cves()
            if len(product_cves) > 0:
                vendor_cves.append([])
