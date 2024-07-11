var TimeMap = function () {
  this.map = {};
};

/**
 * @param {string} key
 * @param {string} value
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function (key, value, timestamp) {
  if (this.map[key] == null) {
    this.map[key] = [[value, timestamp]];
  } else {
    this.map[key].push([value, timestamp]);
  }
};

/**
 * @param {string} key
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function (key, timestamp) {
  // Can use binary search to find key value
  // This is because because timestamps are strictly increasing since time cant go backwards
  // Thus the list is sorted and binary search can be applied

  to_search = this.map[key];
  if (to_search == null) return "";
  if (timestamp < to_search[0][1]) return "";

  l = 0;
  r = to_search.length - 1;
  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    if (to_search[m][1] === timestamp) {
      return to_search[m][0];
    }
    if (to_search[m][1] < timestamp) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }
  return to_search[m][1] > timestamp ? to_search[m - 1][0] : to_search[m][0];
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
