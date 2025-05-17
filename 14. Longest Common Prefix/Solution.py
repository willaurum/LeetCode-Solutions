class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs gives a list of strings like ["flower","flow","flight"]
        #I need to find the longest common prefix of them (in this case "fl")


        if len(strs) == 1:
            return(strs[0])
        else:
            firststr = strs[0]
            firstchars = list(firststr)
            matches = []
            
            
            for i in range(1, len(strs)):
                best = 0
                newstr = strs[i]
                newchars = list(newstr)

                if len(firstchars) >= len(newchars): #if the check phrase is longer than the new one
                    for y in range(len(newchars)):
                        if firstchars[y] == newchars[y]:
                            best += 1
                        else:
                            break

                if len(firstchars) < len(newchars): #if the check phrase is longer than the new one
                    for y in range(len(firstchars)):
                        if firstchars[y] == newchars[y]:
                            best += 1
                        else:
                            break

                matches.append(best)

            
            matches.sort()
            if matches:
                prefixcount = matches[0]
                return(firststr[:prefixcount])
            else:
                return ""
        