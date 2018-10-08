class Hoge:
  def __init__(self, name = "ほげ"):
    self.name = name

  def __del__(self):
    print(self.name + " : インスタンスが破棄されます")

  def Print(self, *args):
    print(args)

class HogeHoge(Hoge):
  def __init__(self, name = "ほげほげ"):
    super().__init__(name)

# hoge = Hoge("ホゲ")
hoge = Hoge()
print(hoge.name)
hoge.Print("Printほげ{0}", hoge.name)

hogehoge = HogeHoge()
print(hogehoge.name)

print("{} {}".format("foo", "ほげ"))