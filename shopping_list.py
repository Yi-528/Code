class ShoppingList:
    """初始化购物清单，shopping list是字典类型，包含商品名和对应价格
    例子：{"牙刷"：5，“沐浴露”，15，“电池”：7}"""
    def __int__(self, shopping_list):
        self.shopping_list = shopping_list


    def get_item_count(self):
        return len(self.shopping_list)


    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price