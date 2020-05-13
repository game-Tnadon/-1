'''

print("student ID 62055008")

value[] = {60, 100, 120};
weight[] = {10, 20, 30};
w = 50;

solution: 220
---------------------------------
value[] = {2, 5, 10, 5};
weight[] = {20, 30, 10, 50};
w = 50;
'''
def knapSack(W , wt , val , n):
    # Base Case
    if n == 0 or W == 0 :
        return 0
        # If weight of the nth item is more than Knapsack of capacity
        # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
            # return the maximum of two cases:
            # (1) nth item included
            # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
        knapSack(W , wt , val , n-1))
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print (knapSack(W , wt , val , n))
