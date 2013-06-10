import unittest
from ipv4 import IPv4


class SimpleIPv4Test(unittest.TestCase):
    def setUp(self):
        self.examples = [IPv4('192.168.192.10', '255.255.255.248'),
                         IPv4('10.16.3.65', '255.255.254.0')]

    def test_hosts(self):
        expected = [6, 510]
        for example, answer in zip(self.examples, expected):
            self.assertEqual(answer, example.hosts())

    def test_cidr(self):
        expected = [29, 23]
        for example, answer in zip(self.examples, expected):
            self.assertEqual(answer, example.mask.cidr())


    def test_network(self):
        expected = ['192.168.192.8', '10.16.2.0']
        for example, answer in zip(self.examples, expected):
            self.assertEqual(answer, example.network().ip.address)

    def test_broadcast(self):
        expected = ['192.168.192.15', '10.16.3.255']
        for example, answer in zip(self.examples, expected):
            self.assertEqual(answer, example.broadcast().ip.address)


if __name__ == '__main__':
    unittest.main()