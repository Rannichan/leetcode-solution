"""
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.
"""


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        uniwage = [x/y for x,y in zip(wage, quality)]
        qw = list(zip(quality, uniwage))
        qw_sort = sorted(qw, key=lambda s: s[1])
        quality = [x[0] for x in qw_sort]
        uniwage = [x[1] for x in qw_sort]
        q = [x for x in quality[0:K]]
        w = uniwage[K-1]
        mincost = w * sum(q)
        if len(uniwage) > K:
            for i in range(K,len(uniwage)):
                w = uniwage[i]
                q.pop(q.index(max(q)))
                q.append(quality[i])
                cost = w * sum(q)
                if cost < mincost:
                    mincost = cost
        return(mincost)