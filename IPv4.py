class IPv4:
    ip = None
    
    def __init__(self, part1: int, part2: int, part3: int, part4: int):
        if part1 < 0 or part1 > 255:
            raise Exception("Part 1 is out of bound")
        if part2 < 0 or part2 > 255:
            raise Exception("Part 2 is out of bound")
        if part3 < 0 or part3 > 255:
            raise Exception("Part 3 is out of bound")
        if part4 < 0 or part4 > 255:
            raise Exception("Part 4 is out of bound")

        self.ip = (part1, part2, part3, part4)

    def to_string(self) -> str:
        return f"{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}"

ipv4_0 = IPv4(12, 43, 78, 10)
print(ipv4_0.to_string())

ipv4_1_parts = [
    int(input(f"Enter {i}. numeric part: "))
    for i in range(4)
]

ipv4_1 = IPv4(*ipv4_1_parts)
print(ipv4_1.to_string())
