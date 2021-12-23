class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops > 0 and scoops < 4:
            print('Order created!')
        elif(flavor not in self.flavors):
            print("We don't have that flavor")
        elif(scoops <= 0 or scoops > 4):
            print("Choose between 1-3 scoops")

        order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print(f'All Pending Ice Cream Orders:')
        while True:
            for order in self.orders.items:
                if order.get("Flavor") in self.flavors and order.get("Scoops") > 0 and order.get("Scoops") < 4:
                    pop_order = self.orders.items.pop(
                        self.orders.items.index(order))
                    print(
                        f'Customer: {pop_order.get("Customer")} -- Flavor: {pop_order.get("Flavor")} -- Scoops: {pop_order.get("Scoops")}')
                    continue

    def next_order(self):
        print("Next Order Up!")
        dequeue_order = self.orders.items.pop(self.orders.dequeue())
        return print(
            f'Customer: {dequeue_order.get("Customer")} -- Flavor: {dequeue_order.orders.get("Flavor")} -- Scoops: {dequeue_order.orders.get("Scoops")}')


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
