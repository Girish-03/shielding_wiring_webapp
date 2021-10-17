#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:55:09 2021

@author: girishsolanki

Met Office Coding Exercise on Shielding and Wiring of Satellite Components
"""

class sat_comps:
    
    def __init__(self,file_path):
        
        self.file_path = file_path


    def get_dim(self):
        
        '''
        Parameters
        ----------
        file_path : STR
            .TXT FILE PATH WITH BOXES DIMENSIONS.
    
        Returns
        -------
        Python List of dimensions for each box with float values.
        '''
        
        # Open file and extract length, width and height values as float from string
        
        with open(self.file_path,'r') as f:
            return [tuple(map(float,l.lower().split('x'))) for l in f.readlines()]
    

    def cal_shielding(self, dim):
        
        '''
        Parameters
        ----------
        dim : TUPLE
            A TUPLE CONTAINING LENGTH, WIDTH, HEIGHT OF THE BOX.
    
        Returns
        -------
        FLOAT value containing surface area or shielding required
        '''
        
        # Calculate Shielding surface area
        
        l,w,h = dim
        sa= (2 * l * w) + (2 * w * h) + (2 * l * h)
        
        return sa+min((l*w),(w*h),(l*h))


    def cal_wiring(self, dim):
        
        '''
        Parameters
        ----------
        dim : TUPLE
            A TUPLE CONTAINING LENGTH, WIDTH, HEIGHT OF THE BOX.
    
        Returns
        -------
        FLOAT value containing required length of wire.
    
        '''
        
        # Calculate Wiring length
        
        l,w,h = dim
        vol = l*w*h
        
        se1,se2 = sorted(dim)[:2] # First two smallest edges
        
        slack = (2*se1) + (2*se2)
        
        return vol+slack


if __name__ == "__main__":

    file = 'example3.txt'
    print(f"File - {file}")
    print("*******************") 
    
    # create object
    components = sat_comps(file)
    
    # get dimensions
    box_dims = components.get_dim()
    
    # get shielding and wiring calculations
    shielding = sum(list(map(components.cal_shielding,box_dims)))
    wiring = sum(list(map(components.cal_wiring,box_dims)))
    
    print(f"Shielding required for this group of boxes: {shielding} mm^2")
    print(f"Wiring required for this group of boxes: {wiring} mm")