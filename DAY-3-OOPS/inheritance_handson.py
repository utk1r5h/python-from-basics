class Dataset:
  def __init__(self, name, params=None):
    self.name = name
    self.params = params if params is not None else {}
  
  def describe(self):
    print(f"model name is {self.name}, and its params are {self.params}")


class JSONDataset(Dataset):
  def __init__(self, name, schema=None, params=None):
    
    if type(schema) is not dict:
      raise TypeError(f"{schema} is not of the correct type")
    super().__init__(name, params)
    self.schema = schema if schema is not None else {}

  def describe(self):
    super().describe()
    print(f"the schema is {self.schema}")


a = Dataset("new", {"100mb", "train"})
a.describe()
b= JSONDataset("second", {"feature": "float", "label": "int"}, {"200mb"})
b.describe()

c = JSONDataset("third", 100, {"300nb"})
c.describe()



  


    