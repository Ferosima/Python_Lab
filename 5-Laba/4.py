# 17*. Дано дерево глибини N, кожна внутрішня вершина якого має K (<10) безпосередніх нащадків
# (нумеруються від 1 до K). Корінь дерева має номер 0. Записати в текстовий файл з даними
# ім'ям всі можливі шляхи, що ведуть від кореня до листя. Перебирати шляху, починаючи з «самого лівого»
# і закінчуючи «самим правим» (при цьому першими замінювати кінцеві елементи шляху).
f=open('4.txt','w')

class Tree:
    def __init__(self):
        self.branching=[]
        self.data="0"
    def add_branching(self,data):
     if len(self.branching)<10:
        self.branching.append(Tree())
        self.branching[len(self.branching)-1].data=data
    def set_data(self,data):
        self.data=data
    def deep_way(self,s):
        if len(self.branching)==0:
            print(self.data,"br")
            return s+self.data+'\n'
        else:
            for i in range(len(self.branching)):
                if isinstance(self.branching[i],Tree):
                 print(s + self.data,'way')
                 #print(self.branching[i].deep_way(s + self.data))
                 print(i,s+self.data)
                 f.write(self.branching[i].deep_way(s+self.data))
                # print(self.branching[i].deep_way(s+self.data))
        return ''


b=Tree()
b.set_data('x')
b.add_branching('0')
b.add_branching('1')
b.add_branching('2')
b.branching[0].add_branching('3')
b.branching[0].add_branching('4')
b.branching[1].add_branching('5')
b.deep_way("")
f.close()