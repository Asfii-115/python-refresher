class ExampleClass:
  class_attr = 0

  def __init__(self, instance_attr):
    self.instance_attr = instance_attr

foo = ExampleClass(1)
bar = ExampleClass(2)
print(ExampleClass.class_attr)

print(foo.instance_attr)
print(foo.class_attr)