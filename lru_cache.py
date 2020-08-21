

class LRUCach:
  def __init__(self, size):
    self.queue = []
    self.entries = {}
    self.counter = 0
    self.size = size

  def add(self, name, value):
    """Adds the name value pair to the cache, maintaining the size of our cache
      the time complexity if this method is O(lon(n))"""
    if name in self.enrtries:
      update_name(name, value)
      return

#private methods
  def update_name(self, name, value):
    entry = self.entries.pop(name)
    entry[-1] = -1

if __name__ == "__main__":
  cache = LRUCach(3)



# vim: set cindent sw=2 expandtab :

