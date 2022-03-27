#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cobra import Model,Reaction,Metabolite
model=Model('example')

x1=Reaction('x1')
x1.name='x1'
x1.lower_bound=0
x1.upper_bound=1000

x2=Reaction('x2')
x2.name='x2'
x2.lower_bound=0
x2.upper_bound=1000

x0=Reaction('x0')
x0.name='x0'
x0.lower_bound=1
x0.upper_bound=1

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000

ATP_R=Reaction('ATP_R')
ATP_R.name='ATP_R'
ATP_R.lower_bound=0
ATP_R.upper_bound=1000

x3=Reaction('x3')
ATP_R.name='x3'
ATP_R.lower_bound=.9
ATP_R.upper_bound=.9
A= Metabolite(
    'A',compartment='c')
B=Metabolite(
    'B',compartment='c')
C= Metabolite(
    'C',compartment='c')
ATP= Metabolite(
    'ATP',compartment='c')

x1.add_metabolites({A:-1,B:1})

x2.add_metabolites({B:-1,C:1})

x0.add_metabolites({A:1})

M.add_metabolites({C:-1})

ATP_R.add_metabolites({A:-1,ATP:1})

x3.add_metabolites({ATP:-1})

model.add_reactions([x0,x1,ATP_R,x2,x3,M])

model.objective = 'M'
model.optimize()


# In[2]:


model.summary()


# In[ ]:




