import tkinter as tk
from datetime import datetime
from datetime import timedelta

# UNINASSAU
# DOCENTE: Cloves Rocha
# ESTUDANTES: Filipi Farias - 01554219, Gabriel Nunes - 01514154, Guilherme Marcello - 01528565, Mateus Andrade Martins - 01517424, Matheus Henrique - 01515159,


#Metódo para iniciar o timer
def start_timer():
    global running, start_time
    running = True
    start_time = datetime.now()
    update_timer()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    resume_button.config(state=tk.DISABLED)

#Método para parar o timer
def stop_timer():
    global running, history
    running = False
    history.append(time_label['text'])
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.NORMAL)
    resume_button.config(state=tk.NORMAL)
    update_history()

#Método para resetar o timer
def reset_timer():
    global running, history
    running = False
    history = []
    time_label.config(text="00:00:00")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.DISABLED)
    resume_button.config(state=tk.DISABLED)
    history_label.config(text="Histórico:")

#Método para retomar um timer parado
def resume_timer():
    global running, start_time
    running = True
    start_time = datetime.now() - timedelta(seconds=int(time_label['text'].split(":")[2]))
    update_timer()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    resume_button.config(state=tk.DISABLED)

#Método para atualizar o timer a cada segundo que passa
def update_timer():
    if running:
        current_time = datetime.now()
        elapsed_time = current_time - start_time
        time_string = str(elapsed_time).split(".")[0]
        time_label.config(text=time_string)
        root.after(1000, update_timer)

#Método que salva quando você pausou o timer
def update_history():
    history_text = "Histórico:\n"
    for idx, item in enumerate(history, start=1):
        history_text += f"{idx}. {item}\n"
    history_label.config(text=history_text)

running = False
start_time = None
history = []

root = tk.Tk()
root.title("Cronômetro")

start_button = tk.Button(root, text="Iniciar", command=start_timer,width='100',background='lightgrey')
stop_button = tk.Button(root, text="Parar", command=stop_timer, state=tk.DISABLED,width='100',background='lightgrey')
reset_button = tk.Button(root, text="Reiniciar", command=reset_timer, state=tk.DISABLED,width='100',background='lightgrey')
resume_button = tk.Button(root, text="Retomar", command=resume_timer, state=tk.DISABLED,width='100',background='lightgrey')
time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
history_label = tk.Label(root, text="Histórico:")

start_button.pack()
stop_button.pack()
reset_button.pack()
resume_button.pack()
time_label.pack()
history_label.pack()

root.mainloop()