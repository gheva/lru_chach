import heapq
'''
This file contains the class representing an LRU cache. in order to achieve 
O(log(size)) performance, we are using the python's implementation of a
priority queue.
A priority queue holds our entries, and this controls the order in which we
remove the oldest items from the cache.
A dict is holding a mapping between our entries in the queue and the name, this
also gives us a place to store the value for retrieval by name.

running this module as main will run a few operations on a small cache and
print some output
'''

class LRUCach:
  def __init__(self, size, marked_for_removal="<removed>"):
    self.queue = [] # This will be our priority queue
    self.entries = {} # this is the map to our entries
    self.counter = 0
    self.size = size # the size ouf our cache
    self.marked_for_removal = marked_for_removal # this is a marker for items
    # to be removed. The most important restriction on it is that it must be
    # an invalid value in our cache

  def add(self, name, value):
    '''
    Adds the name value pair to the cache, maintaining the size of our cache
    the time complexity if this method is O(lon(n))
    '''
    should_pop = True
    if name in self.entries: # we are updating the touch time of this name
      # remove the entry from our cache
      entry = self.entries.pop(name)
      # mark the entry as null, when popping all entries marked for removal are
      # removed. see the documentation for pop
      entry[-1] = self.marked_for_removal
      # We are adding an existing entry, while the heap will grow by an extra
      # entry, we will keep the heap invariant
      should_pop = False
    entry = [self.counter, name, value] # new entry with a bigger count for the 
    # priority queue

    self.entries[name] = entry
    heapq.heappush(self.queue, entry)
    if len(self.entries) > self.size and should_pop:# if we have too many entries
      self.pop()
    self.counter += 1

  def get(self, name):
    '''
    returns the item with the given name, if the item does not exist, will throw
    accessing the item marks it as used for caching purposes.
    The time complexity of this method is O(log(n))
    (n is the number of items in the cache)
    '''
    entry = self.entries[name]
    ret = entry[-1]
    # Calling add, will take care of updating the access to the item so it will
    # be kept in the cache for longer
    self.add(name, ret)
    return ret

  def remove(self, name):
    '''
    removes an item from the cache
      '''
    entry = self.entries.pop(name)
    entry[-1] = self.marked_for_removal

  def pop(self):
    '''
    pops one active item from the cache along with unused entries
      '''
    while self.queue:
      age, name, value = heapq.heappop(self.queue)
      if value is not self.marked_for_removal:
        print (age, value)
        self.entries.pop(name)
        return

if __name__ == "__main__":

  size = 3
  cache = LRUCach(size)

  cache.add("name1", 3)
  print(cache.entries)
  print (cache.get("name1"))
  cache.add("name2", 3)
  cache.add("name3", 3)
  cache.add("name4", 3)
  print (cache.get("name3"))
  print(cache.entries)
  cache.add("name5", 3)
  print(cache.entries)
  cache.remove("name4")
  print(cache.entries)
  cache.add("name1", 3)
  print(cache.entries)
  cache.add("name2", 3)

# vim: set cindent sw=2 expandtab :

