"""
969. Pancake Sorting

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length,
then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips
(doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.
"""


class Solution(object):

    def findMaxValAndPos(self, A):
        maxVal = A[0]
        maxIdx = 0
        for idx in range(1, len(A)):
            if maxVal < A[idx]:
                maxVal = A[idx]
                maxIdx = idx
        return maxVal, maxIdx

    def moveToBeginning(self, A, index):
        return self.flip(A, index)

    def moveToLast(self, A, index):
        return self.flip(A, index)

    def flip(self, A, K):
        newList = []
        for idx in range(K, -1, -1):
            newList.append(A[idx])
        newList.extend(A[K + 1:])
        return newList

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        count = 0
        result = []
        while count < len(A):
            tmpArr = A[:len(A) - count]
            maxVal, maxIdx = self.findMaxValAndPos(tmpArr)
            if maxIdx == len(tmpArr) - 1:
                count += 1
                continue
            result.append(maxIdx + 1)
            result.append(len(tmpArr))
            A = self.moveToBeginning(A, maxIdx)
            A = self.moveToLast(A, len(tmpArr) - 1)
            count += 1
        return result


sol = Solution()
inputList = [1, 2, 3]
print(sol.pancakeSort(inputList))
