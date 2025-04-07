from dataclasses import dataclass
from typing import List
import math
import sys
# numpy IS NOT part of the standard libraries

EPS = 1E-8
@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)
    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)
    def dot(self, a):
        return self.x*a.x + self.y*a.y

    def norm(self):
        return math.sqrt(self.dot(self))
    
    def rotate(self, theta):
        return point(
            self.x*math.cos(theta) + self.y*math.sin(theta),
            self.x*math.sin(theta) - self.y*math.cos(theta),
        )
    
    def angle(self, a, c):
        s1 = a - self
        d1 = s1.norm()

        s2 = c - self
        d2 = s2.norm()

        return math.acos(s1.dot(s2)/(d1*d2))

    def cross(self, p):
        return self.x*p.y - p.x*self.y
@dataclass
class line:
    a: float
    b: float
    c: float

    @staticmethod
    def from_points(p1, p2):
        if abs(p1.x - p2.x) < EPS:
            return line(1.0, 0.0, -p1.x)
        else:
            a = -(p1.y - p2.y) / (p1.x - p2.x)
            b = 1.0
            c = -(a * p1.x) - p1.y
            return line(a, b, c)
        
    def slope(self):
        return -self.a / self.b
    def y_cross(self):
        return -self.c / self.b
    def x_cross(self):
        return -self.c / self.a
    
    def normal(self):
        return point(
            self.a / math.sqrt(self.a**2 + self.b**2),
            self.b / math.sqrt(self.a**2 + self.b**2)
        )
    def d(self):
        return -self.c / math.sqrt(self.a**2 + self.b**2)
    
    def intersect(self, l):
        return point(
            (self.b*l.c - l.b*self.c)/ (self.a*l.b - l.a*self.b),
            (self.a*l.c - l.a*self.c)/ (self.a*l.b - l.a*self.b)
        )
    
    def are_parallel(self, line):
        return abs(
            (self.a*line.a* + self.b*line.b)
            / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2 + line.b**2))
        - 1.0) < EPS
    
    def angle(self, line):
        return math.acos(
            (self.a*line.a + self.b*line.b)
            / (math.sqrt(self.a**2 + self.b**2)*math.sqrt(line.a**2+line.b**2))
        )
@dataclass
class segment:
    p: point
    q: point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)
        return (
            (cross1 * cross2 < 0 or
                (include_p and math.fabs(cross2) < EPS)
                or (include_q and math.fabs(cross1) < EPS))
            and (cross3 * cross4 < 0
                or (include_p and math.fabs(cross4) < EPS)
                or (include_q and math.fabs(cross3) < EPS))
        )
from itertools import islice, cycle

@dataclass
class polygon:
    vertices: List[point]

    def shifted_vertices(self, shift=1):
        # v2, v3, ...., vN, v1
        yield from islice(cycle(self.vertices), shift, len(self.vertices) + shift)
    
    @property
    def segments(self):
        for v1, v2 in zip(self.vertices, self.shifted_vertices()):
            yield segment(v1, v2)

    @property
    def perimeter(self):
        return sum((v1 - v2).norm() for v1, v2 in zip(self.vertices, self.shifted_vertices()))
    
    @property
    def area(self):
        return 0.5*sum(p2.y*p1.x - p2.x*p1.y for p1, p2 in zip(self.vertices, self.shifted_vertices()))
    
    @property
    def is_convex(self):
        clockwise = iter((p2 - p1).cross(p3 - p2) > 0
                        for p1, p2, p3 in zip(self.vertices,
                                            self.shifted_vertices(1),
                                            self.shifted_vertices(2)))
        first = next(clockwise)
        return all(first == x for x in clockwise)
    
    def is_inside(self, q):
        p = min(self.vertices, key=lambda v: v.x) - point(1, 0)
        crosses = sum(1 if segment(p, q).does_intersect(s, include_p=True) else 0 for s in self.segments)
        return crosses % 2 == 1
    
    def polygon_split(self, s):
        vertices1 = []
        vertices2 = []
        ds = s.p - s.q
        l = line.from_points(s.p, s.q)
        
        u = self.vertices[-1]
        side = ds.cross(u - s.q)
        for v in self.vertices:
            cross_prod = ds.cross(v - s.q)
            if cross_prod*side < 0: 
                p = line.from_points(u, v).intersect(l)
                vertices1.append(p)
                vertices2.append(p)
            if cross_prod <= 0:
                vertices1.append(v)
            if cross_prod >= 0:
                vertices2.append(v)
            side = cross_prod
            u = v
        return polygon(vertices1), polygon(vertices2)
def hull(points):
    if len(points) < 3:
        return polygon(points)
    q = min(points, key=lambda v: v.x)
    p = point(q.x, q.y - 1)
    ch = [p, q]
    while True:
        p, q = ch[-2], ch[-1]
        u = max((v for v in points if v != p and v != q),
        key=lambda x: q.angle(p, x))
        if u in ch:
            break
        ch.append(u)
    return polygon(ch[1:])


N=int(sys.stdin.readline())
reinos=[]
while N!=-1:
    
    reino={"central":None,"puntos":[],"area": None,"poligono":None}
    for i in range(N):
        if(i==0):
            central=sys.stdin.readline().split(" ")
            
            Pcentral=point(float(central[0]),float(central[1]))
            reino["central"]=Pcentral
            reino["puntos"].append(Pcentral)

        else:
            p=sys.stdin.readline().split(" ")
            reino["puntos"].append(point(float(p[0]),float(p[1])))
    reino["poligono"] = hull(reino["puntos"])
    reino["area"] = abs(reino["poligono"].area)
    reinos.append(reino)
    N=int(sys.stdin.readline())

misiles=[]
misil=sys.stdin.readline().strip()
while misil!="":
    misil=misil.split(" ")
    mx1=int(misil[0])
    my1=int(misil[1])
    
    misiles.append(point(mx1,my1))
    misil=sys.stdin.readline().strip()
    


area_afectada=0
for misil in misiles:
    for reino in reinos:
        if reino["poligono"].is_inside(misil):
            reinos.remove(reino)
            area_afectada+=reino["area"]

print(f"{area_afectada:.2f}")


        


        