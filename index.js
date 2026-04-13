const fs = require('fs');

async function mockAIDebug(file) {
    console.log(`🔧 正在调试文件：${file}`);
    const code = fs.readFileSync(file, 'utf8');

    let result;
    if (code.includes('function add(a, b)') && code.includes('return a * b;')) {
        result = `
=== 错误分析 ===
函数名为add（加法），但内部使用了乘法运算符*，导致结果错误。
原代码运行add(2, 3)会输出6，正确结果应为5。

=== 修复后的代码 ===
function add(a, b) {
  return a + b;
}
console.log(add(2, 3))
`;
    } else {
        result = `
=== 分析结果 ===
代码未检测到明显错误，运行正常。
`;
    }

    console.log('\n======================================');
    console.log('🤖 AI 调试结果（模拟版）：');
    console.log('======================================');
    console.log(result);
    fs.writeFileSync('DEBUG_RESULT.md', result);
    console.log('\n✅ 调试结果已保存到 DEBUG_RESULT.md');
}

async function main() {
    const args = process.argv.slice(2);
    if (args[0] === 'debug') {
        const file = args[1] || 'test-error.js';
        await mockAIDebug(file);
    } else {
        console.log('🚀 AI 代码调试工具（本地模拟版）');
        console.log('使用方法：node index.js debug test-error.js');
    }
}

main();