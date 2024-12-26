/**
 * @Time 2024/10/01 23:42
 * @Author  : https://github.com/hakusai22
 * @题目     :
 * @参考     :
 * @时间复杂度:
 * @空间复杂度:
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
    return n > 0 && (n & (n - 1)) === 0;
};