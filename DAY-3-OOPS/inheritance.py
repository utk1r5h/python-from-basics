# inheritance practice example

class Dataset:
  def __init__(self, samples, labels, name="unnamed"):
    if len(samples) != len(labels):
      raise ValueError(
        f"samples and label size mismatch: {len(samples)} vs {len(labels)}"
      )
    if not samples:
      raise ValueError("data set can not be empty")
    
    self.samples = list(samples)
    self.labels= list(labels)
    self.name = name 
    self.size= len(self.samples)

  def info(self):
    print(f"[{self.name}] {self.size} samples")

  def shuffle(self):
    import random 
    combined = list(zip(self.samples, self.labels))
    random.shuffle(combined)

    self.samples, self.labels = zip(*combined)
    print(f"shuffles {self.name}")


class CSVDataset(Dataset):
  def __init__(self, samples, labels, filepath, name ="unnamed"):
    super().__init__(samples, labels, name)
    self.filepath= filepath
    self.delimiter = ","
  
  def preview(self):
    print(f"Source: {self.filepath} | First sample: {self.samples[0]}")


class JSONDataset(Dataset):
    def __init__(self, samples, labels, schema, name="unnamed"):
        super().__init__(samples, labels, name)
        self.schema = schema  

    def validate_schema(self):
        print(f"Validating against schema: {self.schema}")



csv_ds = CSVDataset([0.1, 0.5, 0.9], [0, 1, 1], filepath="data/train.csv", name="train")
json_ds = JSONDataset([0.2, 0.8], [0, 1], schema={"feature": "float", "label": "int"})

csv_ds.info()        
csv_ds.preview()      
csv_ds.shuffle()    

json_ds.info()             
json_ds.validate_schema()  




"""

super() means "go to my parent class and use its version". Without it, you'd have to manually re-run all the validation logic from Dataset.__init__ inside every child class — defeating the entire point.

"""


"""
What is MRO? When you call a method on an object, Python needs to decide which class to look in first. The order it searches is called the MRO.

single inheritance -> child then parent 

print(CSVDataset.__mro__). ----> inspect using 


C3 linearization algorithm


list more specific parents first, more generic ones last.

"""


