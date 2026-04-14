# AI文案/简历小助手 - 主程序
import os
import requests
import gradio as gr
from dotenv import load_dotenv

# 加载配置
load_dotenv()

# ====================== 【你的信息已填好】 ======================
ONEAPI_BASE_URL = "https://oneapi.mikesolar.cn/v1"
ONEAPI_API_KEY = "sk-zewJTkaAdzhVNLzHC295F20b36114060999a9f0d354eB090"
ONEAPI_MODEL = "gpt-3.5-turbo"
# =================================================================

# Agent 提示词模板
PROMPT_TEMPLATES = {
    "朋友圈文案": """
你是一个优质朋友圈文案助手。
根据关键词生成自然、简短、有氛围感的文案。
关键词：{input}
只输出文案，不要多余内容。
""",

    "自我介绍": """
你是自我介绍优化师，根据关键词生成简洁大方的自我介绍。
关键词：{input}
100字左右，只输出结果。
""",

    "活动通知": """
你是活动通知生成助手，生成正式、清晰、通顺的通知。
关键词：{input}
直接输出通知内容。
""",

    "简历亮点": """
你是简历优化师，根据关键词提炼专业、简洁的个人亮点。
关键词：{input}
分点输出，简洁有力。
"""
}

# 生成文案核心函数
def generate_content(style, keyword):
    if not keyword.strip():
        return "请输入关键词"

    prompt = PROMPT_TEMPLATES[style].format(input=keyword)

    headers = {
        "Authorization": f"Bearer {ONEAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": ONEAPI_MODEL,
        "messages": [
            {"role": "system", "content": "你是专业的AI文案助手Agent"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(f"{ONEAPI_BASE_URL}/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"生成失败：{str(e)}"

# 网页界面
with gr.Blocks(title="AI文案小助手") as demo:
    gr.Markdown("# 📝 AI文案/简历小助手")
    gr.Markdown("基于 OneAPI + Agent 实现 | 开源项目")

    with gr.Row():
        style = gr.Dropdown(
            choices=["朋友圈文案", "自我介绍", "活动通知", "简历亮点"],
            label="选择生成类型",
            value="朋友圈文案"
        )
        keyword = gr.Textbox(label="输入关键词", placeholder="例如：学习、生日、面试、社团活动")

    btn = gr.Button("🚀 立即生成")
    output = gr.Textbox(label="生成结果", lines=6)

    btn.click(generate_content, inputs=[style, keyword], outputs=output)

# 启动
if __name__ == "__main__":
    demo.launch(server_port=7860, share=False)