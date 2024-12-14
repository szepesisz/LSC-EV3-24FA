
class ITFReader:
    _values = [1, 2, 4, 7, 0]

    def __init__(self, narrow: float, wide: float):
        self.narrow = narrow
        self.wide = wide

    def get_length(self, n_digits: int) -> float:
        assert not n_digits % 2
        code_length = n_digits * (2*self.wide + 3*self.narrow)
        return code_length


    def decode_number(self, b: list[bool]) -> int:
        assert len(b) == 5
        assert sum(b) == 2
        n = sum([v*b for v, b in zip(self._values, b)])
        n = self._values[b.index(True)] + self._values[4-b[::-1].index(True)]
        return n if n < 10 else 0

    def decode_block(self, b: list[bool]) -> int:
        assert len(b) == 10
        n1, n2 = b[::2], b[1::2]
        n1, n2 = self.decode_number(n1), self.decode_number(n2)

        return 10 * n1 + n2

    def decode_code(self, b: list[bool]) -> int:
        assert not len(b) % 10
        n = 0 / 100
        for i in range(0, len(b), 10):
            block = b[i:i+10]
            n *= 100
            n += self.decode_block(block)
        return int(n)

    def read(self, dists: list[float]) -> int:
        d = [round(n/10)*10 for n in dists]
        print(d)
        assert all((n == self.narrow or n == self.wide for n in d))

        d = [n == self.wide for n in d]
        return self.decode_code(d)


if __name__ == '__main__':
    distances = [10, 11, 10, 19, 21, 10, 11, 10, 19, 19, 10, 11, 10, 19, 21, 10, 11, 10, 19, 19]
    r = ITFReader(10, 20)
    print(r.read(distances))