def bomberMan(n, grid):
    if n ==1:
        return grid
    if n%2==0:
        return['O'*6 for i in range(7)]

    def replace_str_index(text, index=0, replacement=''):
    	return '%s%s%s' % (text[:index], replacement, text[index + 1:])

    n//=2
    for q in range((n+1)%2+1):
        newgrid = [['O']*6 for i in range(7)]
        def set(x,y):
            if 0<=x<7 and 0<=y<c:
                replace_str_index(newgrid[x],y,'.')

        for x in range(7):
            for y in range(6):
                if grid[x][y]=='O':
                    replace_str_index(newgrid[x+i],y+j,'.')

        grid = newgrid
    return["".join(x) for x in grid]