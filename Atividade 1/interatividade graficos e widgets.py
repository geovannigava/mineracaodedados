#--------------------------- graficos 1 e 2 

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as wg
from IPython.display import display

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


def grafico(r):
    
    x = np.linspace(-5,5,10)
    y = r * x**2
    plt.plot(x,y, 'r--') # plota eixo x e y, e o  'r--' é a cor red com linha tracejada
    plt.ylabel('y(x)')
    plt.xlabel('x')
    plt.ylim([0,120])
    plt.xlim([-5,5])

controle = wg.IntSlider(value=1,min=0,max=10, step=1)
wg.interact(grafico, r=controle)


brancos = 0

a = wg.IntSlider(value=60,
    step=1,
    description='Bolsonaro:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal')
b = wg.IntSlider(value=30,
    step=1,
    description='Haddad:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal')
c = wg.IntSlider(value=10,
    step=1,
    description='Marina:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal')
ui = wg.HBox([a, b, c])

def f(a, b, c):
    labels = 'Bolsonaro', 'Haddad', 'Marina', 'Em Branco'
    brancos = 100 - a - b - c
    sizes = [a, b, c, brancos]
    explode = (0.1, 0, 0, 0) 
    

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

out = wg.interactive_output(f, {'a': a, 'b': b, 'c': c})

display(ui, out)


#--------------------------- grafico 3
from ipywidgets import Button, HBox, VBox
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as wg
plt.rcdefaults()
titulo = wg.HTML(
    value="Habilidades do Desenvolvedor: <b>Selecione o Valor para cada uma das Habilidades:</b>",
)

valor = wg.IntSlider(value=5,
    step=1,
    max=10,
    description='Valor :',
    disabled=False,
    continuous_update=False,
    orientation='horizontal')

habilidade = wg.Select(
    options=['Java', 'C#', 'Python','Angular', 'Bootstrap', 'React','Oracle', 'SQLServer', 'Mysql'],
    value='Java',
    rows=9,
    description='Skills:',
    disabled=False
)

lvlB = wg.ToggleButtons(
    options=['Regular', 'Bom', 'Excelente'],
    description='Back-End:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Nível Regular', 'Nível Bom', 'Nível Excelente'],
    )
lvlF = wg.ToggleButtons(
    options=['Regular', 'Bom', 'Excelente'],
    description='Front-End:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Nível Regular', 'Nível Bom', 'Nível Excelente'],
    )

lvlBd = wg.ToggleButtons(
    options=['Regular', 'Bom', 'Excelente'],
    description='BD:',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=['Nível Regular', 'Nível Bom', 'Nível Excelente'],
    )

valores = np.array(list(range(9)))
box = VBox([ habilidade])
box2 = VBox([valor])
ui = HBox([box, box2])

habilidades = ('Java', 'C#', 'Python', 'Angular', 'Bootstrap', 'React', 'Oracle', 'SQLServer', 'Mysql')
skills = np.array(habilidades)
def f(c, d):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(habilidades))
    index = np.where(skills == d)
    np.put(valores, [index], [c])
    performance = valores
    ax.barh(y_pos, valores, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(habilidades)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Pontos')
    ax.set_title('Gráfico de Habilidades')
    
    mediaB = np.mean((valores[0:3]))
    mediaF = np.mean((valores[3:6]))
    mediaBd = np.mean((valores[6:9]))

    
    if mediaB >= 0 and mediaB <=4:
        lvlB.value = 'Regular'
    elif mediaB > 4 and mediaB <= 9:
        lvlB.value = 'Bom'
    else:
        lvlB.value = 'Excelente'
        
    if mediaF >= 0 and mediaF <=4:
        lvlF.value = 'Regular'
    elif mediaF > 4 and mediaF <= 9:
        lvlF.value = 'Bom'
    else:
        lvlF.value = 'Excelente'
        
    if mediaBd >= 0. and mediaBd <=4.:
        lvlBd.value = 'Regular'
    elif mediaBd > 4. and mediaBd <= 9.:
        lvlBd.value = 'Bom'
    else:
        lvlBd.value = 'Excelente'
    
plt.show()

out = wg.interactive_output(f, { 'c': valor, 'd': habilidade})

display(titulo, ui, out, lvlB, lvlF, lvlBd)