# __init__ is Python's onboarding checklist for objects
import datetime

"""
Dataset(samples, labels)
       ↓
Step 1: __new__()   → Python allocates memory, creates the empty object
Step 2: __init__()  → YOUR code runs, fills in the object's data

"""

"""
init-> bare min from dataset.class
irl we validate inputs as well

"""

# level 2 validation

class Dataset:
  def __init__(self, samples, labels, name="unnamed"):
    if len(samples)!= len(labels):
      raise ValueError(

        f"samples and labels must match"
        f"got {len(samples)} as sample length but the length of labels is {len(labels)}"
      )
    if not samples:
      raise ValueError(
        "Dataset can not be empty"
      )


    self.samples=samples
    self.labels=labels
    self.name = name
    self.size = len(self.samples)


# level 3-> creation timestamp and mata data


class Dataset:
  def __init__(self, samples, labels, name="unnamed"):
    if len(samples)!= len(labels):
      raise ValueError(

        f"samples and labels must match"
        f"got {len(samples)} as sample length but the length of labels is {len(labels)}"
      )
    if not samples:
      raise ValueError(
        "Dataset can not be empty"
      )


    self.samples=samples
    self.labels=labels
    self.name = name
    self.size = len(self.samples)
    self.created_at =datetime.datetime.now()
    self.matadata = {}

  def info(self):
        print(f"[{self.name}] {self.size} samples | created: {self.created_at:%Y-%m-%d %H:%M}")



train_ds = Dataset([0.1, 0.5, 0.9], [0, 1, 1], name="train")
train_ds.info()


bad_ds = Dataset([0.1, 0.5], [0, 1, 1], name="broken")

