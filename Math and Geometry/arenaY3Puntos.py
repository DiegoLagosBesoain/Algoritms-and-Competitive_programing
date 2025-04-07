from dataclasses import dataclass
from typing import List
import math
import sys
from itertools import *
from itertools import islice, cycle,takewhile
EPS = 1E-8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * (b / gcd(a, b))
def primos_hasta_N(N):
    primos=[]
    for i,p in enumerate(primes()):
        if p > N:
            break
        primos.append(p)
        
    return primos
def factorize(N):
    """
    division: a / b             e.g. 2 / 1 = 2.0 : float
    integer division: a // b    e.g. 2 // 1 = 2 : int
    remainder: a % b remainder of the integer division a / b = a // b + (a %
    4 % 2 = 0
    """
    sqN = math.sqrt(N)
    for p in primes(): # potentially infinite
        if p > sqN: # guarantees it ends
            yield N
            break
        while N % p == 0:
            yield p
            N //= p # N = N // p
            sqN = math.sqrt(N)
        if N == 1:
            break

def primes():
    i = 3
    prime_list = [2]
    yield 2
    while True:
        sqi = math.sqrt(i)
        if next((False for p in takewhile(lambda x: x <= sqi, prime_list) if i%p == 0), True):
            prime_list.append(i)
            yield i
        i += 2
def is_prime(n):
    
    if n < 2:
        return False
    # Casos pequeños
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n == p:
            return True
        if n % p == 0:
            return False

    
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

from itertools import islice

class lazy_list:
    def __init__(self, gen):
        self.gen = gen
        self.mem = []
    def __iter__(self):
        class __iter:
            def __init__(self, m):
                self.i = 0
                self.m = m
            def __next__(self):
                self.i += 1
                return self.m[self.i-1]
        return __iter(self)
    def __getitem__(self, k):
        N = k - len(self.mem) + 1
        if N > 0:
            self.mem += list(islice(self.gen, 0, N))
        return self.mem[k]
primes_ = lazy_list(primes())
def factorize_optimal(N):
    sqN = math.sqrt(N)
    for p in primes_: # potentially infinite
        if p > sqN: # guarantees it ends
            yield N
            break
        while N % p == 0:
            yield p
            N //= p # N = N // p
            sqN = math.sqrt(N)
        if N == 1:
            break
def different_prime_factor_count(N):
    """
    Count the number of unique prime factors of N.
    If N = p_1**a_1 * p_2**a_2 ... * p_k**a_k,
    then different_prime_factor_count(N) = k
    """
    
    if N == 1:
        return 0
    factors = set(factorize_optimal(N))
    
    
    factors.discard(1)
    
    
    return len(factors)

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
    def distance_bewtn(self,p2):
        return math.sqrt((self.x-p2.x)**2 + (p2.y-self.y)**2)
    def punto_medio(self,p2):
        return point((self.x+p2.x)/2,(self.y+p2.y)/2)

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
    @staticmethod
    def from_point_slope(p, m):
        
        if math.isinf(m):
            return line(1.0, 0.0, -p.x)
        return line(-m, 1.0, m * p.x - p.y)    
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
            -(self.a*l.c - l.a*self.c)/ (self.a*l.b - l.a*self.b)
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
# numpy IS NOT part of the standard libraries
@dataclass
class segment:
    p: point
    q: point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)

        xmax=max(self.p.x,self.q.x)
        xmin=min(self.p.x,self.q.x)
        ymax=max(self.p.y,self.q.y)
        ymin=min(self.p.y,self.q.y)
        linea=line.from_points(self.p,self.q)
        if(seg2.p.x>=xmin and seg2.p.x<=xmax and seg2.p.y<=ymax and seg2.p.y>=ymin):
            if(linea.a*seg2.p.x+linea.b*seg2.p.y+linea.c==0):
                include_p=True
        if(seg2.q.x>=xmin and seg2.q.x<=xmax and seg2.q.y<=ymax and seg2.q.y>=ymin):
            if(linea.a*seg2.q.x+linea.b*seg2.q.y+linea.c==0):
                include_q=True
                

        return (
            (cross1 * cross2 < 0 or
                (include_p and math.fabs(cross2) < EPS)
                or (include_q and math.fabs(cross1) < EPS))
            and (cross3 * cross4 < 0
                or (include_p and math.fabs(cross4) < EPS)
                or (include_q and math.fabs(cross3) < EPS))
        )
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
def generar_poligono_regular_de_N_lados_y_un_punto(punto,radio,centro,N):
    vertices = []
    theta0 = math.atan2(punto.y - centro.y, punto.x - centro.x)
    for k in range(N):
        theta = theta0 + 2 * math.pi * k / N
        x = centro.x + radio * math.cos(theta)
        y = centro.y + radio * math.sin(theta)
        vertices.append((x, y))
    return vertices
def encontrar_centro_circulo(puntos):
    AB=line.from_points(puntos[0],puntos[1])
    BC=line.from_points(puntos[1],puntos[2])
    if(abs(AB.slope())<EPS):
        punto_medio=puntos[0].punto_medio(puntos[1])
        punto_hacia_arriba=point(punto_medio.x,punto_medio.y+1)
        l1=line.from_points(punto_medio,punto_hacia_arriba)
    else:
        punto_medio=puntos[0].punto_medio(puntos[1])
        l1=line.from_point_slope(punto_medio,-1/AB.slope())
    if(abs(BC.slope())<EPS):
        punto_medio=puntos[1].punto_medio(puntos[2])
        punto_hacia_arriba=point(punto_medio.x,punto_medio.y+1)
        l2=line.from_points(punto_medio,punto_hacia_arriba)
    else:
        punto_medio=puntos[1].punto_medio(puntos[2])
        l2=line.from_point_slope(punto_medio,-1/BC.slope())
    punto_interseccion=l1.intersect(l2)
    return punto_interseccion

N = int(sys.stdin.readline())
while N!=0:
    puntos_visibles=[]
    for i in range(3):
        x,y = map(float,sys.stdin.readline().split())
        puntos_visibles.append(point(x,y))
    a=puntos_visibles[0].distance_bewtn(puntos_visibles[1])
    b=puntos_visibles[1].distance_bewtn(puntos_visibles[2])
    c=puntos_visibles[2].distance_bewtn(puntos_visibles[0])
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    R=(a*b*c)/(A*4)
    centro=encontrar_centro_circulo(puntos_visibles)
    print(centro)
    
    vertices=generar_poligono_regular_de_N_lados_y_un_punto(puntos_visibles[0],R,centro,N)
    xs = [p[0] for p in vertices]
    ys = [p[1] for p in vertices]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    area = (maxx - minx) * (maxy - miny)
    print(area)
    N = int(sys.stdin.readline())

