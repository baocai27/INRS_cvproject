import os

import gradio as gr
from gradio import components as gc

method = ["数显", "指针"]
my_theme = gr.themes.Soft(primary_hue="red", secondary_hue="pink")



with gr.Blocks(title="INRS", theme=my_theme) as demo:
    with gr.Row():
        gr.HTML("""<h1 style="text-align: center; color: red;">INRS</h1>""")

    with gr.Row():
        with gr.Column(scale=4):
            with gr.Row():
                llm_model = gr.Dropdown(
                    label="选择识别方式",
                    choices=method,
                    value="指针",
                    interactive=True,
                )

    with gr.Row():
        with gr.Column(scale=3):
            btn_llm = gr.Button("① 开始检测", variant="primary")
            model_output = gr.Textbox(
                label="读数结果", 
                placeholder="这里展示读数的结果...",
                lines=25
            )



def main():
    demo.launch(
        server_port=8005, 
        share=True, 
        inbrowser=True, 
        server_name="0.0.0.0", 
        root_path="/INRS_cvproject"
    )

# 确保只有在直接运行脚本时才启动
if __name__ == "__main__":
    main()
