import gradio as gr

TITLE = "MPlato"
DESCRIPTION = "Minimal Gradio app scaffold for the Hugging Face Space. Replace the logic with your own."


def echo(text: str) -> str:
    return text or ""


with gr.Blocks(title=TITLE, theme="soft") as demo:
    gr.Markdown(f"# {TITLE}\n{DESCRIPTION}")
    with gr.Row():
        inp = gr.Textbox(label="Input", placeholder="Type something…")
    with gr.Row():
        out = gr.Textbox(label="Output", interactive=False)
    with gr.Row():
        btn = gr.Button("Echo")

    btn.click(echo, inp, out)
    inp.submit(echo, inp, out)


if __name__ == "__main__":
    # On Spaces, launch is handled automatically; this is for local runs
    demo.launch()
