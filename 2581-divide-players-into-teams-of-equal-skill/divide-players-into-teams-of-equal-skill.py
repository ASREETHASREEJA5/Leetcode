class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tar = skill[0]+skill[-1]
        chem = 0
        for i in range(len(skill)//2):
            if skill[i]+skill[-i-1] != tar:
                return -1
            else:
                chem += skill[i]*skill[-i-1]
        return chem
        