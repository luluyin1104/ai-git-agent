
=== 错误分析 ===
函数名为add（加法），但内部使用了乘法运算符*，导致结果错误。
原代码运行add(2, 3)会输出6，正确结果应为5。

=== 修复后的代码 ===
function add(a, b) {
  return a + b;
}
console.log(add(2, 3))
