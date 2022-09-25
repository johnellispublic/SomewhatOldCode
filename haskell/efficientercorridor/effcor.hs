import Graphics.Image as I
import Data.List as L

sign :: [Numeric] -> [Numeric]
sign x = if x < 0 then -1 else if x > 0 then 1 else 0

x1 = 1.416
y1 = -0.105
A1 = 5.53
F = -0.5
C = 0.3
R = 1.5
L = 0.5
b0 = 3.5

n = 100
m = 100

U = [0..(m*n-1)]
X = (mod U m)/(m-1) - 0.5
Y = (U - (mod U m))/(n*(m-1))

f0 = (F-y1)/Y
c0 = (C-y1)/Y
l0 = (L - x1)/((sin A1) + (cos A1)*X)
r0 = (R - x1)/((sin A1) + (cos A1)*X)


fN :: [Numeric] -> [Numeric]
fN x = (x)/(0.5 * ((sign x) + 1) - 0.001)

C0 = map (min) (L.transpose [(fN f0),(fN c0),(fN l0),(fN r0)])
C1 = [[C0!!(i+m*j) | i <- [0..m]] | j <- [0..n]]
img = fromLists C1

I.writeImage "image.png" img
