class Model:
  def __init__(self, model_type, is_Trained=False):
    self.model_type=model_type
    self.is_Trained=is_Trained
  
  def summary(self):
    print(f"Model is {self.model_type} and Trained: {self.is_Trained}")


first_model = Model(
  model_type="linear regression",
  is_Trained=False
)

second_model = Model(
  model_type="logistic regression",
  is_Trained=True
)
third_model = Model("ML Model")

first_model.summary()
second_model.summary()
third_model.summary()