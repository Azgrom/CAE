#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:12:39 2020

@author: Rafael Lúcio
"""

# Exercício 1


k1 = 20e4 # N / m
k2 = 30e4 # N / m
k3 = 10e4 # N / m

f2 = 1000 # N
f3 = 0 # N

u1 = u4 = 0 # Unidade de deslocamento


# Compondo o sistema na notaçao matricial [K(g)]{U(g)} = {F(g)}, temos:
K_g = [[k1, -k1,     0,      0],
       [-k1, k1+k2, -k2,     0],
       [0,  -k2,     k2+k3, -k3],
       [0,   0,     -k3,     k3]]

U_g = [u1, u2, u3, u4]

F_g = [R1, 1000, 0, R4]
