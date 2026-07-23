import gradio as gr

# 1. 간단한 함수 정의
def say_hello(name):
    """
    실행
    """
    return "Hello, " + name
# 2. gradio 인터페이스 생성
gr_web = gr.Interface(
    fn=say_hello,
    inputs="text",
    outputs="text"
)
# 3. 웹앱 실행
gr_web.launch(share=True)