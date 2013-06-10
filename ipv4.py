from collections import defaultdict


class Address():
    def __init__(self, address):
        self.address = address

    def _to_bin(self, x):
        return int(bin(x)[2:])

    def decimal_repr(self):
        return self.address.split('.')

    def binary_repr(self):
        binary = ["{0:08b}".format(int(octet)) for octet in self.decimal_repr()]
        return '.'.join(binary)

    def octets(self):
        return [int(octet) for octet in self.decimal_repr()]

    def __repr__(self):
        return self.address


class Mask():
    def __init__(self, mask):
        self.address = Address(mask)

    def cidr(self):
        d = defaultdict(int)
        for k in self.address.binary_repr():
            d[k] += 1
        return d['1']

    def host_bits(self):
        return 32 - self.cidr()

    def __repr__(self):
        return "/{}".format(self.cidr())


class IPv4():
    def __init__(self, ip, mask):
        self.ip = Address(ip)
        self.mask = Mask(mask)

    @property
    def subnet_mask(self):
        return self.mask.address.address

    @property
    def mask_address(self):
        return self.mask.address

    def hosts(self):
        return 2 ** self.mask.host_bits() - 2

    def network(self):
        network = [str(octet) for octet in self._network()]
        return IPv4('.'.join(network), self.subnet_mask)

    def broadcast(self):
        broadcast = [str(octet) for octet in self._broadcast()]
        return IPv4('.'.join(broadcast), self.subnet_mask)

    def _network(self):
        return \
        [item[0] & item[1] for item in zip(self.ip.octets(), self.mask_address.octets())]

    def _broadcast(self):
        return \
        [item[0] ^ (~item[1] + 256) for item in zip(self._network(), self.mask_address.octets())]

    def __repr__(self):
        return self.ip.__repr__() + self.mask.__repr__()
