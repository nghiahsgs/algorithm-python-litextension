import queue 
  
class node: 
    def __init__(self, val, level): 
        self.val = val  
        self.level = level 
    def __str__(self):
        return 'level: %s and val: %s'%(self.level,self.val)
  
 
def minOperations(x, y): 
      
    visit = set()  
    
    q = queue.Queue() 
    n = node(x, 0)  
    q.put(n)  
  
    
    while (not q.empty()): 
        t = q.get()
        print(t)
        
        if (t.val == y): 
            return t.level  
  
        visit.add(t.val) 
  
        if (t.val * 2 == y or t.val - 1 == y):  
            return t.level+1

        print('visit',visit)
        if (t.val * 2 not in visit): 
            # input('z1')
            n.val = t.val * 2
            n.level = t.level + 1
            q.put(n) 
        if (t.val - 1 >= 0 and t.val - 1 not in visit): 
            # input('z2')
            n.val = t.val - 1
            n.level = t.level + 1
            q.put(n) 

if __name__ == '__main__': 
    x = 1
    y = 5
    print(minOperations(x, y)) 
