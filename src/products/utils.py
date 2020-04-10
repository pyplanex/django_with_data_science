import matplotlib.pyplot as plt 
import seaborn as sns
from io import BytesIO
import base64
from django.contrib.auth.models import User

def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman

def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor the begining of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free the memory of the buffer 
    buffer.close()

    return graph

def get_simple_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/faq/usage_faq.html?highlight=backend#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    if chart_type == 'bar plot':
        title = "total price by day (bar)"
        plt.title(title)
        plt.bar(x, y) 
    elif chart_type == 'line plot':
        title = "total price by day (line)"
        plt.title(title)
        plt.plot(x, y)
    else:
        title = "Product count"
        plt.title(title)
        sns.countplot('name', data=data)
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_image()
    return graph