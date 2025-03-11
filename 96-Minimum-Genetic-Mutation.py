class Solution:
    def get_dif(self, s1: str, s2: str) -> int:
        dif_len = 0
        for i, j in zip(s1, s2):
            if i != j:
                dif_len += 1
        return dif_len

    def minMutation(
        self, startGene: str, endGene: str, bank: list[str] | set[str]
    ) -> int:
        if startGene == endGene:
            return 0

        if not isinstance(bank, set):
            bank = set(bank)

        min_mutations = -1
        for i in bank:
            if self.get_dif(i, startGene) != 1:
                continue

            res = self.minMutation(i, endGene, bank - {i})
            if res == 0:
                return 1
            if res != -1 and (res < min_mutations or min_mutations == -1):
                min_mutations = res + 1

        return min_mutations