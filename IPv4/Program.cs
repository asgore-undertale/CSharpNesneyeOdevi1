public class IPv4
{
    public int Part1 { get; private set; }
    public int Part2 { get; private set; }
    public int Part3 { get; private set; }
    public int Part4 { get; private set; }

    public IPv4(int part1, int part2, int part3, int part4)
    {
        if (part1 < 0 || part1 > 255) {
        	throw new ArgumentException("Part 1 is out of bound.");
        }
        if (part2 < 0 || part2 > 255) {
        	throw new ArgumentException("Part 2 is out of bound.");
        }
        if (part3 < 0 || part3 > 255) {
        	throw new ArgumentException("Part 3 is out of bound.");
        }
        if (part4 < 0 || part4 > 255) {
        	throw new ArgumentException("Part 4 is out of bound.");
        }

        Part1 = part1;
        Part2 = part2;
        Part3 = part3;
        Part4 = part4;
    }

    public string Tostring()
    {
        return $"{Part1}.{Part2}.{Part3}.{Part4}";
    }
}

class Program
{
    static void Main(string[] args)
    {
        IPv4 ipv4_0 = new IPv4(12, 43, 78, 10);
        Console.WriteLine(ipv4_0.Tostring());

        int[] ipv4_1_parts = new int[4];
        for (int i = 0; i < 4; i++)
        {
            Console.Write($"Enter {i + 1}. numeric part: ");
            ipv4_1_parts[i] = Convert.ToInt32(Console.ReadLine());
        }

        IPv4 ipv4_1 = new IPv4(ipv4_1_parts[0], ipv4_1_parts[1], ipv4_1_parts[2], ipv4_1_parts[3]);
        Console.WriteLine(ipv4_1.Tostring());
    }
}
