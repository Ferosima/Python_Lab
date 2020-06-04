#12. Знайдіть медіану графа, тобто таку його вершину, що сума відстаней від неї до інших вершин мінімальна.
import networkx as nx
import matplotlib.pyplot as plt
G = nx.gnm_random_graph(6,6)
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
print( "Медіана: ",nx.barycenter(G))
plt.show()
