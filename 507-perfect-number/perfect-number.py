class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum1 = 0
        num1 = num
        for i in range(1,int(math.sqrt(num))+1):
            if num % i == 0:
                sum1+=i
                if i!=num//i:
                    sum1+=num//i
        if (sum1-num1) == num1:
            return True
        return False

        