import gradio as gr
from pathlib import Path

BASE_DIR = Path(__file__).parent

def generate_pilot():
    prompt = (BASE_DIR / "scripts" / "pilot_prompt.txt").read_text(encoding="utf-8")
    return prompt

with gr.Blocks() as demo:
    gr.Markdown("# Equilibrium: Тишина Храма — пилот")
    btn = gr.Button("Generate 5-minute pilot")
    out = gr.Textbox(lines=25)
    btn.click(fn=generate_pilot, outputs=out)

if __name__ == "__main__":
    demo.launch()
