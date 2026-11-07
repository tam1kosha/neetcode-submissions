class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        

        res = []
        path = []

        def isp(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]: 
                    return False
                l, r = l + 1, r - 1
            return True
        
        def backtrack(base: int) -> None:
            #basecase:
            if base == n:
                res.append(path.copy())
                return

            for index in range(base, n):
                if isp(s, base, index):
                    path.append(s[base:index + 1])
                    backtrack(index + 1)
                    path.pop()

                
        backtrack(0)
        return res




            
            
        


            

