import sys
ADDRESS_SEPARATER = "."


def __main():
    for arg in sys.argv[1:]:
        print(get_broadcast(arg))


def decIP_to_binIP(address):
    separated = [int(dec) for dec in address.split(ADDRESS_SEPARATER)]
    array = [str(dec_to_bin(dec)).rjust(8, "0") for dec in separated]
    return array


def dec_to_bin(dec):
    binChar = bin(dec)[2:]
    return int(binChar)


def increment_address(baseArray, count):
    result = []
    for addr in baseArray:
        binArray = list(addr)
        for index in range(8):
            if count <= 0:
                binArray[index] = "1"
            count -= 1
        result.append("".join([str(bin) for bin in binArray]))
    return result


def get_broadcast(address):
    base, digit = address.split("/")
    binBase = decIP_to_binIP(base)
    binAddr = increment_address(binBase, int(digit))
    decAddr = [int(i, 2) for i in binAddr]
    return ADDRESS_SEPARATER.join([str(i) for i in decAddr])


if __name__ == "__main__":
    __main()
