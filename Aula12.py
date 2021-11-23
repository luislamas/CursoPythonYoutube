# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 21:04:45 2021

@author: luisf
"""

import numpy as np
from scipy.optimize import minimize



def Vazoes(x):
    Q1, Q2, Q3 = x
    Qw1 = Q1*0.75
    Qw2 = Q2*0.90
    Qw3 = Q3*0.60
    
    Qo1 = Q1-Qw1
    Qo2 = Q2-Qw2
    Qo3 = Q3-Qw3
    
    Qg1 = Qo1*100
    Qg2 = Qo2*150
    Qg3 = Qo3*200   
    
    return (Q1,Q2,Q3,Qw1,Qw2,Qw3,Qo1,Qo2,Qo3,Qg1,Qg2,Qg3)

def Lucro(x):
    (Q1,Q2,Q3,Qw1,Qw2,Qw3,Qo1,Qo2,Qo3,Qg1,Qg2,Qg3) = Vazoes(x)
    
    Receita_oleo = 70 * (Qo1 + Qo2 + Qo3) 
    Receita_gas = 29 * (Qg1 + Qg2 + Qg3)   # 5,00 USD/MMBtu
    Receitas = Receita_oleo + Receita_gas
    
    Custo_oleo = 1 * (Qo1 + Qo2 + Qo3) 
    Custo_agua = 1 * (Qw1 + Qw2 + Qw3)
    Custos = Custo_oleo + Custo_agua
    
    Lucro = Receitas - Custos
    
    return Lucro



def Minimo_gas(x):
    (Q1,Q2,Q3,Qw1,Qw2,Qw3,Qo1,Qo2,Qo3,Qg1,Qg2,Qg3) = Vazoes(x)
    
    return (Qg1 + Qg2 + Qg3) - 150000

def Maximo_agua(x):
    (Q1,Q2,Q3,Qw1,Qw2,Qw3,Qo1,Qo2,Qo3,Qg1,Qg2,Qg3) = Vazoes(x)
    return 5000 - (Qw1 + Qw2 + Qw3)

rest = [{'type':'ineq', 'fun':Minimo_gas},
        {'type':'ineq', 'fun':Maximo_agua}]


bnds = ((0, 2000), (0, 3000), (0, 4000))

def funcao_objetivo(x):
    return -Lucro(x)


x0 = [1000, 1000, 1000]

res = minimize(funcao_objetivo, x0, bounds=bnds, constraints = rest)

(Q1,Q2,Q3,Qw1,Qw2,Qw3,Qo1,Qo2,Qo3,Qg1,Qg2,Qg3) = Vazoes(res.x)

print(Qg1+Qg2+Qg3)
print(Qw1+Qw2+Qw3)
print(Qo1+Qo2+Qo3)




