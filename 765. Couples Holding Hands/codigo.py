class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0

        def encontra_parceiro(x: int) -> int:
            """Retorna o número parceiro de x"""
            return x + 1 if x % 2 == 0 else x - 1

        n = len(row)
        # mapa: valor -> índice atual em row
        pos = {val: idx for idx, val in enumerate(row)}

        for i in range(0, n, 2):
            x = row[i]
            y = row[i + 1]
            p = encontra_parceiro(x)

            if y != p:
                count += 1
                j = pos[p]                # índice onde está p
                # troca row[i+1] com row[j]
                row[i + 1], row[j] = row[j], row[i + 1]
                # atualiza posições no mapa
                pos[row[j]] = j          # row[j] agora é o que foi trocado para j
                pos[row[i + 1]] = i + 1  # row[i+1] agora é p

        return count