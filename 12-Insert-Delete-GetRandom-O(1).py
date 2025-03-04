class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False

        self.data_map[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False

        last_element_in_list = self.data[-1]
        index_of_element_to_remove = self.data_map[val]

        self.data_map[last_element_in_list] = index_of_element_to_remove
        self.data[index_of_element_to_remove] = last_element_in_list

        self.data[-1] = val

        self.data.pop()

        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
