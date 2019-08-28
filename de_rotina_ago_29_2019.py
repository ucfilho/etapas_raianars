# -*- coding: utf-8 -*-
"""DE_rotina_ago_29_2019.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13w9ev9oEh3NRmTlQ1QbGoJQHdnOwynN9
"""

# -*- coding: utf-8 -*-
"""DE_rotina_jul_23_2019.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1USl33DwuBXrmxw7dSut9Dj329wkXGh5o
"""

import numpy as np

def de(MAX,MIN, mut, crossp, popsize, its,fobj,X):
  
  global TOTAL
  global SOMA
  
  
  Num=len(MAX)
  bounds=[(0,0)] * Num
  dimensions = len(bounds)  
  
  for i in range(Num):
    bounds[i]=(MIN[i], MAX[i])

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  

  
  for i in range(its):
    if(SOMA>TOTAL):
      break
    for j in range(popsize):
      if(SOMA>TOTAL):
        break
      SOMA=SOMA+1
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = a + mut * (b - c)

      for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
      cross_points = np.random.rand(dimensions) < crossp
      if not np.any(cross_points):
        cross_points[np.random.randint(0, dimensions)] = True

      trial = np.where(cross_points, mutant, X[j,:])


      f = fobj(trial)
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
        if f < fitness[best_idx]:
          best_idx = j
          best = trial

    fitness = np.asarray([fobj(ind) for ind in X])

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]

  
  y=fitness

  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  
  
  return x,BEST,FOBEST,XY,BEST_XY

'''N=5
M=4
soma=0
for i in range(M):
  if(soma>5):
    break
  for j in range(N):
    soma=soma+1
    print('soma=',soma)
    if(soma>5):
      
      #print("good bye")
      break
      
    #print(soma)'''