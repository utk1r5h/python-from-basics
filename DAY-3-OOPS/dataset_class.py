class Dataset:
  def __init__(self, samples, labels, name="unnamed"):
    self.samples = samples
    self.labels = labels
    self.name = name
  
  def size(self):
    return print(len(self.samples))
  
  def info(self):
    print(f"Dataset '{self.name}' : '{self.size}' samples")


train_ds = Dataset(
  samples = [0.1,0.5,0.9,1.1],
  labels = [0,1,1,0],
  name = "mnist-train"
)

val_ds = Dataset(
  samples=[0.3,0,7],
  labels=[0,1],
  name="mnist-val"
)


train_ds.info()
print()
val_ds.info()
print()
train_ds.size()

print(train_ds is val_ds)



# everything is public by default
# self means this particular object. 
# diff instance occupy diff memory, so self targets that particular memory for that object 


# class variable -> shared by everyone 
# instance varibale ( variable in a function )-> each object gets its own
