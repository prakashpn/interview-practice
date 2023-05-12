class Vehicle:
    vehicle_pricing = {
        "Honda": 150000,
        "Hero": 200000,
        "Suzuki": 250000,
    }

    def __init__(self, tax):
        self.tax = tax

    def final_price(self, brand):
        if brand in self.vehicle_pricing:
            # print("present")
            vehicle_price = self.vehicle_pricing.get(brand)
            tax_amount = (vehicle_price * self.tax) / 100
            final_price = vehicle_price + tax_amount
            return final_price
        else:
            return "Brand Doesnot Exist"


outcome = Vehicle(18)
honda_finaloutcom = outcome.final_price("Honda")
print(honda_finaloutcom)

hero_finaloutcom = outcome.final_price("Hero")
print(hero_finaloutcom)

suzuki_finaloutcom = outcome.final_price("Suzuki")
print(suzuki_finaloutcom)
