

class ITFReader:
    _values = (1, 2, 4, 7, 0)

    def __init__(self, narrow: float, wide: float):
        self.narrow = narrow
        self.wide = wide

    def decode_number(self, b: list[bool]) -> int:
        assert len(b) == 5
        assert sum(b) == 2
        n = self._values[b.index(True)] + self._values[-(b[::-1].index(True)+1)]
        return n if n < 10 else 0

    def decode_block(self, b: list[bool]) -> int:
        assert len(b) == 10
        n1, n2 = b[::2], b[1::2]
        n1, n2 = self.decode_number(n1), self.decode_number(n2)
        return 10 * n1 + n2
    
    def decode_code(self, b: list[bool]) -> int:
        assert not len(b) % 10
        n = sum((self.decode_block(b[i:i+10]) * 100**(i//10) for i in range(0, len(b), 10)))
        return n

    
    def read(self, dists: list[float]) -> int:
        d = [round(n/10)*10 for n in dists]
        assert all((n in (self.narrow, self.wide) for n in d))
        c = [n == self.wide for n in d]
        return self.decode_code(c)

    
if __name__ == '__main__':
    r = ITFReader(10, 20)
    # n = r.decode_number([True, False, True, False, False])
    n = r.decode_code([True, False, True, False, False, True, False, False, False, True,
                       True, False, True, False, False, True, False, True, False, False
                       ])
    n = r.read([19.6, 9.8, 20.3, 10, 10, 20, 10, 10, 10, 20])
    print(n)
