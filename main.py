import gradio as gr
def get_application_text(receiver_name: str, date1: str, number_of_days: str, date2: str, name: str) -> str:
    return f"""
                                      {receiver_name}

                            ЗАЯВА

  Прошу надати мені відпустку з {date1} на {number_of_days} calendar days.

  Дата: {date2}          {name}
  """

def generate_doc(receiver_name: str, date1: str, number_of_days: str, date2: str, name: str) -> str:
    text = get_application_text(receiver_name, date1, number_of_days, date2, name)
    return f"<pre style='font-family: monospace; font-size: 14px;'>{text}</pre>"

with gr.Blocks(title="Генератор заяв") as demo:
    gr.Markdown("#Генератор заяв за шаблоном")
    gr.Markdown("Заповніть поля нижче, щоб згенерувати текст заяви про відпустку.")
    
    with gr.Row():
        with gr.Column():
            receiver = gr.Textbox(label="Отримувач (кому)", placeholder="Директору ТОВ 'Ромашка' Прізвище І.О.")
            date_start = gr.Textbox(label="Дата початку відпустки", placeholder="dd.mm.yyyy")
            days_count = gr.Textbox(label="Кількість календарних днів", placeholder="14")
            date_today = gr.Textbox(label="Поточна дата (дата підписання)", placeholder="dd.mm.yyyy")
            user_name = gr.Textbox(label="Ваше ім'я (від кого)", placeholder="Прізвище Ім'я")
            
            btn = gr.Button("Згенерувати документ", variant="primary")
            
        with gr.Column():
            output = gr.HTML(label="Результат")

    btn.click(
        fn=generate_doc,
        inputs=[receiver, date_start, days_count, date_today, user_name],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()