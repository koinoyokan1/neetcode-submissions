class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('|')
        encoded.append('%')
        for s in strs:
            encoded.append(s)
        print(''.join(encoded))
        return ''.join(encoded)
            

    def decode(self, s: str) -> List[str]:
        meta = s.split('%')[0]
        lns = meta.split('|')
        lns = [int(l) for l in lns[:-1]]
        decoded = []

        st = s.split('%')
        st = st[1:]
        st = '%'.join(st)
        start = 0
        for l in lns:
            decoded.append(st[start:start+l])
            start += l
        
        return decoded
