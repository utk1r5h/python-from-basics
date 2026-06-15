# class Model:
#   def __init__(self, model_type, is_Trained=False):
#     self.model_type=model_type
#     self.is_Trained=is_Trained
  
#   def summary(self):
#     print(f"Model is {self.model_type} and Trained: {self.is_Trained}")


# first_model = Model(
#   model_type="linear regression",
#   is_Trained=False
# )

# second_model = Model(
#   model_type="logistic regression",
#   is_Trained=True
# )
# third_model = Model("ML Model")

# first_model.summary()
# second_model.summary()
# third_model.summary()


# new model 


# class Model:
#   def __init__(self, modelType, isTrained=False, hyperparams=None):

#     allowed = {"linear", "logistic", "decisionTree"}
#     if modelType not in allowed:
#       raise ValueError(
#         f"unknown model type {self.modelType}, choose from {allowed}"
#       )
    
#     self.modelType=modelType
#     self.isTrained=isTrained
#     self.hyperparams=hyperparams if hyperparams is not None else {}
#     self.weights = None

#   def summary(self):
#     print(
#       f"model type is {self.modelType} | Trained: {self.isTrained}, "
#       f" hyperparams: {self.hyperparams}"
#     )

# m = Model("linear", hyperparams={"lr": 0.01, "epochs":100})
# m.summary()

# m = model("new model")



# final model class 


class Model:
  def __init__(self, model_type, is_trained = False, hyperparams=None):
    if(type(model_type)!= str):
      raise TypeError(
        f"{model_type} is not in the correct string format, please correct it"
      )
    
    self.model_type=model_type
    self.is_trained=is_trained
    self.hyperparams=hyperparams if hyperparams is not None else {}
    self.weights = None

  def summary(self):
        print(
        f"model type is {self.model_type} | Trained: {self.is_trained}, "
        f" hyperparams: {self.hyperparams}"
        )


m = Model("linear", hyperparams={"lr": 0.01, "epochs":100})
m.summary()

m = Model(123)






  

