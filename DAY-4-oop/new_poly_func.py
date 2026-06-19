class Model:
  def __init__(self, model_type):
    self.model_type=model_type
    self._weights = None 
  
  def train(self, dataset):
    raise NotImplementedError("subclass must implement")
  def predict(self, sample):
    raise NotImplementedError("subclass must implement")


class LinearRegressio(Model):
  def __init__(self):
    super().__init__("linear regression")

  def train(self, dataset):
    print(f"fitting a line to {dataset.size} samples")
    self._weights=[0.5,0.2]

  def predict(self, sample):
    return self._weights[0]*sample + self._weights[1]


class DT(Model):
  def __init__(self, depth =5):
    super().__init__("decision tree")
    self.depth=depth

  def train(self, dataset):
    print(f"building a tree with depth {self.depth} and with {dataset.size} samples")
    self._weights= "details"
  
  def predict(self, sample):
    return "class A" if sample >0.5 else "class b"




class Trainer:
  def run(self, model, dataset):
    model.train(dataset)

class Dataset:
  def __init__(self, samples, name ="unnamed"):
    self.samples = samples
    self.size = len(samples)
    self.name = name

ds = Dataset([0.1, 0.2, 0.3, 0.4], "new")

trainer = Trainer()

models = [LinearRegressio(), DT(depth =5)]

for model in models:
  trainer.run(model, ds)