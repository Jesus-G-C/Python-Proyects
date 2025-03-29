#///////////////////////////////////////////////////////////////////
#/////////////////          Team Quizzzz          //////////////////
#///////////////////////////////////////////////////////////////////

import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.font

class QuizApp:
    
    def __init__(self, vent):
        self.vent = vent
        self.vent.title("Crazzy Quizz")
        vent.geometry("600x600")

        self.label_question1 = tk.Label(vent, text="Bienvenido al Quizzz")
        self.label_question1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)
        self.label_question1.config(bg="#8290df", relief="sunken")
        self.label_question1.configure(font = Desired_font)

        self.label_question2 = tk.Label(vent, text="Elija un tema de preguntas:")
        self.label_question2.place(relx=0.18, rely=0.22, relwidth=0.625, relheight=0.1)
        self.label_question2.config(bg="#95a0da", relief="sunken")
        self.label_question2.configure(font = Desired_font)
      
        self.button_cultura = tk.Button(vent, text="Cultura General", command=self.questions_cultura)
        self.button_cultura.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.1)
        self.button_cultura.config(bg="#9FA9CA", relief="sunken")
        self.button_cultura.configure(font = Desired_font)

        self.button_deporte = tk.Button(vent, text="Deporte", command=self.questions_deporte)
        self.button_deporte.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.1)
        self.button_deporte.config(bg="#9FA9CA", relief="sunken")
        self.button_deporte.configure(font = Desired_font)

        self.button_historia = tk.Button(vent, text="Historia", command=self.questions_historia)
        self.button_historia.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)
        self.button_historia.config(bg="#9FA9CA", relief="sunken")
        self.button_historia.configure(font = Desired_font)
        
        self.current_question = 0
        self.puntos = 0
        self.label_question = None
        self.entry_respuesta = None

    def hide_category_buttons(self):
        self.label_question1.destroy()
        self.label_question2.destroy()
        self.button_cultura.destroy()
        self.button_deporte.destroy()
        self.button_historia.destroy()

    def setup_quiz_interface(self):
        vent.geometry("350x300")
        if self.label_question:
            self.label_question.destroy()
        if self.entry_respuesta:
            self.entry_respuesta.destroy()
        
        self.label_question = tk.Label(self.vent, text="")
        self.label_question.pack()
        self.label_question.config(bg="#95a0da", relief="sunken")

        self.entry_respuesta = tk.Entry(self.vent)
        self.entry_respuesta.pack()
        self.entry_respuesta.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.1)
        
        self.button_submit = tk.Button(self.vent, text="Enviar respuesta", command=self.check_respuesta)
        self.button_submit.pack()
        self.button_submit.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.09)
        self.button_submit.config(bg="#66d7da", relief="sunken")

        self.update_question()

    def questions_cultura(self):
        self.hide_category_buttons()
        self.pregunta = [
            {"question": "¿Cuál es la capital de Francia?", "respuesta": "Paris"},
            {"question": "¿Quién pintó la Mona Lisa?", "respuesta": "da Vinci"},
            {"question": "¿Cuándo acabó la II Guerra Mundial?", "respuesta": "1945"},
            {"question": "¿Qué día es la fiesta de la Hispanidad?", "respuesta": "12 de octubre"},
            {"question": "¿Qué día es la fiesta nacional de Estados Unidos?", "respuesta": "4 de julio"},
            {"question": "¿Qué es Goku?", "respuesta": "Un Sayan"},
            {"question": "¿Quién inventó la bombilla?", "respuesta": "Thomas Edison"},
            {"question": "¿En qué país se usó la primera bomba atómica?", "respuesta": "Japón"},
            {"question": "¿Cuántas veces ha estado el hombre en la Luna?", "respuesta": "6"},
            {"question": "¿Qué presidente de Estados Unidos fue asesinado en Dallas?", "respuesta": "John Kennedy"}
        ]
        self.setup_quiz_interface()

    def questions_deporte(self):
        self.hide_category_buttons()
        self.pregunta = [
            {"question": "¿Quién ganó la copa América en 2016?", "respuesta": "Chile"},
            {"question": "¿Quién quedó en segundo lugar en la copa América en 2016?", "respuesta": "Argentina"},
            {"question": "¿Quién hizo la mano de Dios?", "respuesta": "Maradona"},
            {"question": "¿En qué país ganó Alemania su primer mundial?", "respuesta": "Suiza"},
            {"question": "¿A quién representa el 10?", "respuesta": "Messi"},
            {"question": "¿Quién es el rey del basquetball?", "respuesta": "Michael Jordan"},
            {"question": "¿Quién es conocido como O Rei?", "respuesta": "Pelé"},
            {"question": "¿Qué equipo ha ganado más champions league de la historia?", "respuesta": "Real Madrid"},
            {"question": "¿Cúal es el país con más medallas de Oro?", "respuesta": "USA"},
            {"question": "¿Quién fue el mejor beisbolista de la historia?", "respuesta": "Babe Ruth"}
        ]
        self.setup_quiz_interface()

    def questions_historia(self):
        self.hide_category_buttons()
        self.pregunta = [
            {"question": "¿Cuándo fue la independencia de México?", "respuesta": "1810"},
            {"question": "¿Quién dio el grito de independencia?", "respuesta": "Miguel Hidalgo"},
            {"question": "¿Quién tenía el bigote gracioso en 1939?", "respuesta": "Adolf Hitler"},
            {"question": "¿Quién inventó la bombilla?", "respuesta": "Thomas Edison"},
            {"question": "¿Apellidos de los dos presidentes asesinados por disparo a la cabeza?", "respuesta": "Lincoln y Kennedy"},
            {"question": "¿Cuándo terminó la SGM (añ0)?", "respuesta": "1945"},
            {"question": "¿Qué año se firmó el tratado de Ginebra?", "respuesta": "1949"},
            {"question": "¿Cuándo terminó la SGM (añ0)?", "respuesta": "1945"},
            {"question": "¿Qué año empezó el calendario Gregoriano?", "respuesta": "1582"},
            {"question": "¿Quién fue el emperador más conocido de Roma?", "respuesta": "Julio Cesar"}
        ]
        self.setup_quiz_interface()
    
    def update_question(self):
        if self.current_question < len(self.pregunta):
            self.label_question.config(text=self.pregunta[self.current_question]["question"])
        else:
            messagebox.showinfo("Fin del cuestionario", f"Has terminado. Puntuación final: {self.puntos}")
            self.vent.destroy()

    def check_respuesta(self):
        user_respuesta = self.entry_respuesta.get().strip()
        correcta_respuesta = self.pregunta[self.current_question]["respuesta"]
        if user_respuesta.lower() == correcta_respuesta.lower():
            self.puntos += 1
            messagebox.showinfo("Correcto", "Respuesta correcta.")
        else:
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. La respuesta correcta es: {correcta_respuesta}")
        self.current_question += 1
        self.entry_respuesta.delete(0, tk.END)
        self.update_question()

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        f1 = GradientFrame(self, borderwidth=1, relief="sunken")
        f1.pack(side="top", fill="both", expand=True)

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="#7fdede", color2="#e6f2f2", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")


if __name__ == "__main__":
    vent = tk.Tk()
    Desired_font = tk.font.Font( family = "Helvetica Nue", size = 20,   weight = "bold") 
    Example(vent).pack(fill="both", expand=True)
    vent.config(relief="sunken")
    app = QuizApp(vent)
    vent.mainloop()