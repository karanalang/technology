from typing import List

# https://leetcode.com/discuss/interview-question/336746/google-onsite-product-of-k-consecutive-numbers

class GoogleInterviewQuestion:

    def prodOfKConsecutiveNos_bruteForce(self, l:List[int], k:int):

        res = []

        for i in range(len(l)-2):
            prod = 1
            l1 = l[i:i+3]
            for j in range(len(l1)):
                prod = l1[j] * prod
            res += [prod]

        return res
        # O(n-3) * O(3) = O(n)



    def prodOfKConsecutiveNos_dp(self, l, k):


        N = len(l)
        print(N)
        prod = 1

        if(N <= k):
            for i in range(N):
                prod = prod * l[i]
                res = [prod]
            return res

        res = [0] * (N-2)
        # print(res)
        res[0] = 1

        for i in range(0,N-2):
            if(i == 0):
                for i in range(k):
                    res[0] = res[0] * l[i]
            else:
                # print(" i -> ", i, " (i + k) -> ", (i+k-1), "l[i+k] -> ", l[i+k-1])
                res[i] = (res[i-1] * l[i+k-1])//l[i-1]
                # print(" 1. res -> ", res[i], " res[i-1] -> ", res[i-1], " res -> ", res)

        return res



    def prodOfKConsecutiveNos_dp_1(self, nums, k):

        width = len(nums)

        dp = [num for num in nums]
        # dp = [0] * width
        # [1, 3, 9, 54, 90, 210, 0, 0]
        # print(" dp -> ", dp)
        # print(" <- width -> ", width, " <- k -> ", 3)

        k = width if k > width else k
        # print(" k = width or k -> ", k)
        for i in range(1, k):
            for j in range(i + 1, width):
                dp[j] *= nums[j - i]
        return dp

    def consecutive_products(self, nums, k):
        product = 1
        output = []
        for index in range(len(nums)):
            product *= nums[index]
            product /= 1 if index < k else nums[index - k]
            output.append(product)
        return output

    def soln(self, l, k):
        k = min(len(l), k)
        ret = l.copy()
        for i in range(1, k):
            for j in range(i, len(l)):
                ret[j] *= l[j - i]
        return ret


    # print(consecutive_products([1, 3, 3, 6, 5, 7, 0, -3], 3))



google = GoogleInterviewQuestion()
l = [1, 3, 3, 6, 5, 7, 0, -3]
l1 = [1, 3, 6]
l2 = [1, 2, 3, 4]
k = 3
# res_bf = google.prodOfKConsecutiveNos_bruteForce(l1, k)
# print(res_bf)

res_bf_1 = google.prodOfKConsecutiveNos_bruteForce(l2, k)
print(" 1.res_bf_1 -> ", res_bf_1)
#
res_dp_1 = google.prodOfKConsecutiveNos_dp(l2,k)
print(" 2.res_dp_1 -> ", res_dp_1)


res_dp_2 = google.prodOfKConsecutiveNos_dp_1(l2, k)
print("res_dp_2 -> ", res_dp_2)

# res_dp_3 = google.consecutive_products(l, k)
# print("res_dp_3 -> ", res_dp_3)
#
# res_dp_4 = google.soln(l, k)
# print("res_dp_4  -> ", res_dp_4)