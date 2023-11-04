image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

def floodfill(image, sr, sc, color):
    origColor = image[sr][sc]
    newColor = color

    if origColor == newColor:
        return image
    
    def fill(image, sr, sc, newColor, origColor):
        #Checking boundaries and if the current's box's color is same as orignal color or not
        if (sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc] != origColor):
            return 
        
        #update the blocks color to the new color
        image[sr][sc] = newColor
        
        fill(image, sr+1, sc, newColor, origColor)
        fill(image, sr-1, sc, newColor, origColor)
        fill(image, sr, sc+1, newColor, origColor)
        fill(image, sr, sc-1, newColor, origColor)

    fill(image, sr, sc, newColor, origColor)
    return image

im = floodfill(image, sr, sc, color)
print(im)