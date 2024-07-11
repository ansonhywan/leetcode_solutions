/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  l = 1;
  r = Math.max(...piles);
  min_k = 0;

  while (l <= r) {
    m = Math.trunc((l + r) / 2);
    hours = eatBananas(piles, m);
    if (hours <= h) {
      min_k = m;
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  return min_k;
};

var eatBananas = function (piles, k) {
  h_elapsed = 0;
  for (pile of piles) {
    h_elapsed += Math.ceil(pile / k);
  }
  return h_elapsed;
};
