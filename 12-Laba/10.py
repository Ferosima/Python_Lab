# 10. Заданий граф (орграф) у вигляді матриці суміжності. Скласти програму:
# а) перевірки, чи є в графі петлі;
# б) пошуку в графі ізольованої вершини (не суміжної з іншими);
# в) визначення ступеня графа;
# г) отримання послідовності ребер.
import networkx as nx
import matplotlib.pyplot as plt
G = nx.gnm_random_graph(6,6)
G.add_edge(1, 1)#петля
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
print(G.edges)
print( "a)петлі: ",list(nx.nodes_with_selfloops(G)))
print( "б)ізольованої вершини: ",list(nx.isolates(G)))
print( "г)ребра: ",list(nx.edges(G)))
plt.show()
