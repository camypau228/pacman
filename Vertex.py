from math import inf
from pygame import Vector2
import sys
import pygame
import map

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)


class Vertex:

    def __init__(self, x=0, y=0, num=0, clr=(255, 0, 0)):
        # self.x = x
        # self.y = y
        self.position = Vector2(x, y)
        self.clr = clr
        self.neighbor = {}
        self.num = num

    def draw(self):
        center = self.position
        pygame.draw.circle(screen, self.clr, center, 10)

    def create_neighbors(self, left=-1, right=-1, top=-1, bottom=-1):
        self.neighbor["LEFT"] = left
        self.neighbor[2] = left
        self.neighbor["RIGHT"] = right
        self.neighbor[-2] = right
        self.neighbor["TOP"] = top
        self.neighbor[1] = top
        self.neighbor["BOTTOM"] = bottom
        self.neighbor[-1] = bottom

    def return_neighbors(self):
        return self.neighbor


class Edge:  # для визуализации

    def __init__(self, v1, v2, ):
        self.coord1 = v1.position
        self.coord2 = v2.position

    def draw(self):
        clr_edge = 255, 255, 255
        pygame.draw.line(screen, clr_edge, self.coord1, self.coord2, 2)


def init_vertex(vertex_arr):
    vertex_arr.append(Vertex(-50, -50))
    # Первая линия
    vertex_arr.append(Vertex(66, 40, 1))
    vertex_arr.append(Vertex(145, 40, 2))
    vertex_arr.append(Vertex(250, 40, 3))
    vertex_arr.append(Vertex(300, 40, 4))
    vertex_arr.append(Vertex(405, 40, 5))
    vertex_arr.append(Vertex(485, 40, 6))
    # Вторая линия
    vertex_arr.append(Vertex(66, 90, 7))
    vertex_arr.append(Vertex(145, 90, 8))
    vertex_arr.append(Vertex(197, 90, 9))
    vertex_arr.append(Vertex(250, 90, 10))
    vertex_arr.append(Vertex(300, 90, 11))
    vertex_arr.append(Vertex(353, 90, 12))
    vertex_arr.append(Vertex(405, 90, 13))
    vertex_arr.append(Vertex(485, 90, 14))
    # Третья линия
    vertex_arr.append(Vertex(66, 144, 15))
    vertex_arr.append(Vertex(145, 144, 16))
    vertex_arr.append(Vertex(197, 144, 17))
    vertex_arr.append(Vertex(250, 144, 18))
    vertex_arr.append(Vertex(300, 144, 19))
    vertex_arr.append(Vertex(353, 144, 20))
    vertex_arr.append(Vertex(405, 144, 21))
    vertex_arr.append(Vertex(485, 144, 22))
    # Четвертая линия
    vertex_arr.append(Vertex(197, 197, 23))
    vertex_arr.append(Vertex(250, 197, 24))
    vertex_arr.append(Vertex(300, 197, 25))
    vertex_arr.append(Vertex(353, 197, 26))
    # Пятая линия
    vertex_arr.append(Vertex(0, 249, 27))
    vertex_arr.append(Vertex(145, 249, 28))
    vertex_arr.append(Vertex(197, 249, 29))
    vertex_arr.append(Vertex(353, 249, 30))
    vertex_arr.append(Vertex(405, 249, 31))
    vertex_arr.append(Vertex(540, 249, 32))
    # Шестая линия
    vertex_arr.append(Vertex(197, 302, 33))
    vertex_arr.append(Vertex(353, 302, 34))
    # Седьмая линия
    vertex_arr.append(Vertex(66, 354, 35))
    vertex_arr.append(Vertex(145, 354, 36))
    vertex_arr.append(Vertex(197, 354, 37))
    vertex_arr.append(Vertex(250, 354, 38))
    vertex_arr.append(Vertex(300, 354, 39))
    vertex_arr.append(Vertex(353, 354, 40))
    vertex_arr.append(Vertex(405, 354, 41))
    vertex_arr.append(Vertex(485, 354, 42))
    # Восьмая линия
    vertex_arr.append(Vertex(66, 406, 43))
    vertex_arr.append(Vertex(91, 406, 44))
    vertex_arr.append(Vertex(145, 406, 45))
    vertex_arr.append(Vertex(197, 406, 46))
    vertex_arr.append(Vertex(250, 406, 47))
    vertex_arr.append(Vertex(300, 406, 48))
    vertex_arr.append(Vertex(353, 406, 49))
    vertex_arr.append(Vertex(405, 406, 50))
    vertex_arr.append(Vertex(458, 406, 51))
    vertex_arr.append(Vertex(485, 406, 52))
    # Девятая линия
    vertex_arr.append(Vertex(66, 459, 53))
    vertex_arr.append(Vertex(91, 459, 54))
    vertex_arr.append(Vertex(145, 459, 55))
    vertex_arr.append(Vertex(197, 459, 56))
    vertex_arr.append(Vertex(250, 459, 57))
    vertex_arr.append(Vertex(300, 459, 58))
    vertex_arr.append(Vertex(353, 459, 59))
    vertex_arr.append(Vertex(405, 459, 60))
    vertex_arr.append(Vertex(458, 459, 61))
    vertex_arr.append(Vertex(485, 459, 62))
    # Десятая линия
    vertex_arr.append(Vertex(66, 510, 63))
    vertex_arr.append(Vertex(250, 510, 64))
    vertex_arr.append(Vertex(300, 510, 65))
    vertex_arr.append(Vertex(485, 510, 66))
    # Стартовый карман
    vertex_arr.append(Vertex(250, 249, 67))
    vertex_arr.append(Vertex(275, 249, 68))
    vertex_arr.append(Vertex(300, 249, 69))
    vertex_arr.append(Vertex(275, 197, 70))


def init_neighbors(vertex_arr):
    v_arr = vertex_arr
    v_arr[1].create_neighbors(bottom=v_arr[7], right=v_arr[2])
    v_arr[2].create_neighbors(left=v_arr[1], bottom=v_arr[8], right=v_arr[3])
    v_arr[3].create_neighbors(left=v_arr[2], bottom=v_arr[10])
    v_arr[4].create_neighbors(right=v_arr[5], bottom=v_arr[11])
    v_arr[5].create_neighbors(left=v_arr[4], right=v_arr[6], bottom=v_arr[13])
    v_arr[6].create_neighbors(left=v_arr[5], bottom=v_arr[14])
    v_arr[7].create_neighbors(top=v_arr[1], right=v_arr[8], bottom=v_arr[15])
    v_arr[8].create_neighbors(top=v_arr[2], right=v_arr[9], bottom=v_arr[16], left=v_arr[7])
    v_arr[9].create_neighbors(right=v_arr[10], bottom=v_arr[17], left=v_arr[8])
    v_arr[10].create_neighbors(top=v_arr[3], right=v_arr[11], left=v_arr[9])
    v_arr[11].create_neighbors(top=v_arr[4], right=v_arr[12], left=v_arr[10])
    v_arr[12].create_neighbors(right=v_arr[13], bottom=v_arr[20], left=v_arr[11])
    v_arr[13].create_neighbors(top=v_arr[5], right=v_arr[14], bottom=v_arr[21], left=v_arr[12])
    v_arr[14].create_neighbors(top=v_arr[6], bottom=v_arr[22], left=v_arr[13])
    v_arr[15].create_neighbors(top=v_arr[7], right=v_arr[16])
    v_arr[16].create_neighbors(top=v_arr[8], bottom=v_arr[28], left=v_arr[15])
    v_arr[17].create_neighbors(top=v_arr[9], right=v_arr[18])
    v_arr[18].create_neighbors(bottom=v_arr[24], left=v_arr[17])
    v_arr[19].create_neighbors(right=v_arr[20], bottom=v_arr[25])
    v_arr[20].create_neighbors(top=v_arr[12], left=v_arr[19])
    v_arr[21].create_neighbors(top=v_arr[13], right=v_arr[22], bottom=v_arr[31])
    v_arr[22].create_neighbors(top=v_arr[14], left=v_arr[21])
    v_arr[23].create_neighbors(right=v_arr[24], bottom=v_arr[29])
    v_arr[24].create_neighbors(top=v_arr[18], right=v_arr[25], left=v_arr[23])
    v_arr[25].create_neighbors(top=v_arr[19], right=v_arr[26], left=v_arr[24])
    v_arr[26].create_neighbors(bottom=v_arr[30], left=v_arr[25])
    v_arr[27].create_neighbors(right=v_arr[28])
    v_arr[28].create_neighbors(top=v_arr[16], right=v_arr[29], bottom=v_arr[36], left=v_arr[27])
    v_arr[29].create_neighbors(top=v_arr[23], bottom=v_arr[33], left=v_arr[28])
    v_arr[30].create_neighbors(top=v_arr[26], right=v_arr[31], bottom=v_arr[34])
    v_arr[31].create_neighbors(top=v_arr[21], right=v_arr[32], bottom=v_arr[41], left=v_arr[30])
    v_arr[32].create_neighbors(left=v_arr[31])
    v_arr[33].create_neighbors(top=v_arr[29], right=v_arr[34], bottom=v_arr[37])
    v_arr[34].create_neighbors(top=v_arr[30], bottom=v_arr[40], left=v_arr[33])
    v_arr[35].create_neighbors(right=v_arr[36], bottom=v_arr[43])
    v_arr[36].create_neighbors(top=v_arr[28], right=v_arr[37], bottom=v_arr[45], left=v_arr[35])
    v_arr[37].create_neighbors(top=v_arr[33], right=v_arr[38], left=v_arr[36])
    v_arr[38].create_neighbors(bottom=v_arr[47], left=v_arr[37])
    v_arr[39].create_neighbors(right=v_arr[40], bottom=v_arr[48])
    v_arr[40].create_neighbors(top=v_arr[34], right=v_arr[41], left=v_arr[39])
    v_arr[41].create_neighbors(top=v_arr[31], right=v_arr[42], bottom=v_arr[50], left=v_arr[40])
    v_arr[42].create_neighbors(bottom=v_arr[52], left=v_arr[41])
    v_arr[43].create_neighbors(top=v_arr[35], right=v_arr[44])
    v_arr[44].create_neighbors(bottom=v_arr[54], left=v_arr[43])
    v_arr[45].create_neighbors(top=v_arr[36], right=v_arr[46], bottom=v_arr[55])
    v_arr[46].create_neighbors(right=v_arr[47], bottom=v_arr[56], left=v_arr[45])
    v_arr[47].create_neighbors(top=v_arr[38], right=v_arr[48], left=v_arr[46])
    v_arr[48].create_neighbors(top=v_arr[39], right=v_arr[49], left=v_arr[47])
    v_arr[49].create_neighbors(right=v_arr[50], bottom=v_arr[59], left=v_arr[48])
    v_arr[50].create_neighbors(top=v_arr[41], bottom=v_arr[60], left=v_arr[49])
    v_arr[51].create_neighbors(right=v_arr[52], bottom=v_arr[61])
    v_arr[52].create_neighbors(top=v_arr[42], left=v_arr[51])
    v_arr[53].create_neighbors(right=v_arr[54], bottom=v_arr[63])
    v_arr[54].create_neighbors(top=v_arr[44], right=v_arr[55], left=v_arr[53])
    v_arr[55].create_neighbors(top=v_arr[45], left=v_arr[54])
    v_arr[56].create_neighbors(top=v_arr[46], right=v_arr[57])
    v_arr[57].create_neighbors(bottom=v_arr[64], left=v_arr[56])
    v_arr[58].create_neighbors(right=v_arr[59], bottom=v_arr[65])
    v_arr[59].create_neighbors(top=v_arr[49], left=v_arr[58])
    v_arr[60].create_neighbors(top=v_arr[50], right=v_arr[61])
    v_arr[61].create_neighbors(top=v_arr[51], right=v_arr[62], left=v_arr[60])
    v_arr[62].create_neighbors(bottom=v_arr[66], left=v_arr[61])
    v_arr[63].create_neighbors(top=v_arr[53], right=v_arr[64])
    v_arr[64].create_neighbors(top=v_arr[57], right=v_arr[65], left=v_arr[63])
    v_arr[65].create_neighbors(top=v_arr[58], right=v_arr[66], left=v_arr[64])
    v_arr[66].create_neighbors(top=v_arr[62], left=v_arr[65])
    v_arr[67].create_neighbors(right=v_arr[68])
    v_arr[68].create_neighbors(top=v_arr[70])
    v_arr[69].create_neighbors(left=v_arr[68])
    v_arr[70].create_neighbors(left=v_arr[24], right=v_arr[25])

def draw_graph():
    vertex_arr = []
    init_vertex(vertex_arr)
    init_neighbors(vertex_arr)
    edges = []
    for v in vertex_arr:
        for where in v.neighbor:
            if v.neighbor[where] != -1:
                edges.append(Edge(v, v.neighbor[where]))
    for v in vertex_arr:
        v.draw()
    for e in edges:
        e.draw()

def main():
    clr = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(clr)

    vertex_arr = []
    init_vertex(vertex_arr)
    init_neighbors(vertex_arr)

    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        map.Map.render(map.Map(), screen)
        draw_graph()
        pygame.display.flip()
        screen.fill(clr)
        pygame.time.wait(1)
    sys.exit()

if __name__ == '__main__':
    main()








