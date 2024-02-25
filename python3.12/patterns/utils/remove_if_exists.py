#! /usr/bin/env python3 

import os 

def remove_if_exists(filename: str) -> None:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass 
    
    