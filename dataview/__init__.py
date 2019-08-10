from dataview.table import Table
from dataview.model import Model

model = Model()

class Dataview(Table):

    def __init__(self):
        super(Dataview, self).__init__(model)

__all__=["Dataview"]