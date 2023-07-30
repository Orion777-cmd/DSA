class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_addresses = []

        def backtrack(s, address, ip_addresses):
            if len(address) == 4 and len(s) == 0:
                ip_addresses.append(".".join(address))
            elif len(address) < 4 and len(s) > 0:
                for i in range(1, min(4, len(s) + 1)):
                    addres = s[:i]
                    if is_valid_segment(addres):
                        backtrack(s[i:], address + [addres], ip_addresses)

        def is_valid_segment(address):
            if len(address) > 1 and address[0] == '0':
                return False
            num = int(address)
            return 0 <= num <= 255
        
        backtrack(s, [], ip_addresses)
        return ip_addresses
