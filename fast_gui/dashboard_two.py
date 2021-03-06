# AUTOGENERATED! DO NOT EDIT! File to edit: 02_dashboard_two.ipynb (unless otherwise specified).

__all__ = ['RED', 'BLUE', 'GREEN', 'BOLD', 'ITALIC', 'RESET', 'style', 'dashboard_two', 'ds_choice', 'plt_classes',
           'display_images']

# Cell
RED = '\033[31m'
BLUE = '\033[94m'
GREEN = '\033[92m'
BOLD   = '\033[1m'
ITALIC = '\033[3m'
RESET  = '\033[0m'

style = {'description_width': 'initial'}

import ipywidgets as widgets
from IPython.display import clear_output
from fastai2.vision.all import*

# Cell
def dashboard_two():
    """GUI for Data tab"""
    dashboard_two.datas = widgets.ToggleButtons(
        options=['PETS', 'CIFAR', 'IMAGENETTE_160', 'IMAGEWOOF_160', 'MNIST_TINY'],
        description='Choose',
        value=None,
        disabled=False,
        button_style='info',
        tooltips=[''],
        style=style
    )

    display(dashboard_two.datas)

    button = widgets.Button(description='Explore', button_style='success')
    display(button)
    out = widgets.Output()
    display(out)
    def on_button_explore(b):
        with out:
            clear_output()
            ds_choice()

    button.on_click(on_button_explore)


# Cell
def ds_choice():
    """Helper for current fastai datasets: PETS, CIFAR, IMAGENETTE_160, IMAGEWOOF_160 and MNIST_TINY"""
    if dashboard_two.datas.value == 'PETS':
        ds_choice.source = untar_data(URLs.DOGS)
    elif dashboard_two.datas.value == 'CIFAR':
        ds_choice.source = untar_data(URLs.CIFAR)
    elif dashboard_two.datas.value == 'IMAGENETTE_160':
        ds_choice.source = untar_data(URLs.IMAGENETTE_160)
    elif dashboard_two.datas.value == 'IMAGEWOOF_160':
        ds_choice.source = untar_data(URLs.IMAGEWOOF_160)
    elif dashboard_two.datas.value == 'MNIST_TINY':
        ds_choice.source = untar_data(URLs.MNIST_TINY)

    print(BOLD + BLUE + "Dataset: " + RESET + BOLD + RED + str(dashboard_two.datas.value))
    plt_classes()

# Cell
def plt_classes():
    """Helper for plotting classes in folder"""
    disp_img_but = widgets.Button(description='View Images?', button_style='success')
    Path.BASE_PATH = ds_choice.source
    train_source = (ds_choice.source/'train/').ls().items
    print(BOLD + BLUE + "Folders: " + RESET + BOLD + RED + str(train_source))
    print(BOLD + BLUE + "\n" + "No of classes: " + RESET + BOLD + RED + str(len(train_source)))

    num_l = []
    class_l = []
    for j, name in enumerate(train_source):
        fol = (ds_choice.source/name).ls().sorted()
        names = str(name)
        class_split = names.split('train')
        class_l.append(class_split[1])
        num_l.append(len(fol))

    y_pos = np.arange(len(train_source))
    performance = num_l

    plt.style.use('seaborn')
    plt.bar(y_pos, performance, align='center', alpha=0.5, color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.xticks(y_pos, class_l, rotation=90)
    plt.ylabel('Images')
    plt.title('Images per Class')
    plt.show()

    display(disp_img_but)
    out_img = widgets.Output()
    display(out_img)
    def on_disp_button(b):
        with out_img:
            clear_output()
            display_images()
    disp_img_but.on_click(on_disp_button)

# Cell
def display_images():
    """Helper for displaying images from folder"""
    train_source = (ds_choice.source/'train/').ls().items
    for i, name in enumerate(train_source):
        fol = (ds_choice.source/name).ls().sorted()
        fol_disp = fol[0:5]
        filename = fol_disp.items
        fol_tensor = [tensor(Image.open(o)) for o in fol_disp]
        print(BOLD + BLUE + "Loc: " + RESET + str(name) + " " + BOLD + BLUE + "Number of Images: " + RESET +
              BOLD + RED + str(len(fol)))

        fig = plt.figure(figsize=(30,13))
        columns = 5
        rows = 1
        ax = []

        for i in range(columns*rows):
            for i, j in enumerate(fol_tensor):
                img = fol_tensor[i]    # create subplot and append to ax
                ax.append( fig.add_subplot(rows, columns, i+1))
                ax[-1].set_title("ax:"+str(filename[i]))  # set title
                plt.tick_params(bottom="on", left="on")
                plt.imshow(img)
                plt.xticks([])
        plt.show()