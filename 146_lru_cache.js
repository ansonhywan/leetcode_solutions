function DoublyNode(key, val, next, prev) {
  this.key = key || 0;
  this.val = val || 0;
  this.next = next || null;
  this.prev = prev || null;
}

/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {
  this.capacity = capacity;
  this.cache_map = new Map();
  this.lru = new DoublyNode();
  this.mru = new DoublyNode();
  this.lru.next = this.mru;
  this.mru.prev = this.lru;
};

/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
  if (this.cache_map.has(key)) {
    got = this.cache_map.get(key);
    this.delete(got);
    this.insert(got);
    return got.val;
  } else {
    return -1;
  }
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
  if (this.cache_map.has(key)) {
    this.delete(this.cache_map.get(key));
  }
  if (this.cache_map.size === this.capacity) {
    this.delete(this.lru.next);
  }
  new_node = new DoublyNode(key, value);
  this.insert(new_node);
};

LRUCache.prototype.insert = function (node) {
  old_mru = this.mru.prev;
  old_mru.next = node;
  node.next = this.mru;
  node.prev = old_mru;
  this.mru.prev = node;
  this.cache_map.set(node.key, node);
};

LRUCache.prototype.delete = function (node) {
  prev = node.prev;
  next = node.next;
  prev.next = next;
  next.prev = prev;
  this.cache_map.delete(node.key);
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
