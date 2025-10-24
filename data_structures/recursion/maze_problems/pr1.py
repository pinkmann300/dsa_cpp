def wtr(x, y, finx, finy, stringy): 
    if (x > finx or y > finy):
        return []
    
    if (x == finx and y == finy): 
        return [stringy]
    
    right = wtr(x + 1, y, finx, finy, stringy + "R" ) 
    down = wtr(x, y + 1, finx, finy, stringy + "D") 
    diagonal = wtr(x + 1, y + 1, finx, finy, stringy + "d")
    return right + down + diagonal


print(len(wtr(0,0, 2,2, "")))