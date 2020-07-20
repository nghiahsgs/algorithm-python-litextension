def min(x,y):
    if x<y:
        return x
    else:
        return y

visit=set()
def minSteps(x,y):
    if x == 0:
        return 1000
    if x == y:
        return 0
    if x*2==y:
        return 1
    if x>y:
        return minSteps(x-1,y)
    
    visit.add(x)

    sol_a=1000
    sol_b=1000
    if x*2 not in visit:
        sol_a = 1 + minSteps(x*2,y)
    if x-1 not in visit:
        sol_b = 1 + minSteps(x-1,y)
      
    return min(sol_a, sol_b)

print(minSteps(1,5))
