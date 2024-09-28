import tkinter as tk
from tkinter import messagebox

class MeritCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Méritos")

        # Etiquetas y entradas para cada categoría
        self.label_formacion = tk.Label(master, text="Puntuación en Formación:")
        self.label_formacion.grid(row=0, column=0)
        self.entry_formacion = tk.Entry(master)
        self.entry_formacion.grid(row=0, column=1)

        self.label_experiencia = tk.Label(master, text="Puntuación en Experiencia:")
        self.label_experiencia.grid(row=1, column=0)
        self.entry_experiencia = tk.Entry(master)
        self.entry_experiencia.grid(row=1, column=1)

        self.label_idiomas = tk.Label(master, text="Puntuación en Idiomas:")
        self.label_idiomas.grid(row=2, column=0)
        self.entry_idiomas = tk.Entry(master)
        self.entry_idiomas.grid(row=2, column=1)

        self.label_informatica = tk.Label(master, text="Puntuación en Informática:")
        self.label_informatica.grid(row=3, column=0)
        self.entry_informatica = tk.Entry(master)
        self.entry_informatica.grid(row=3, column=1)

        # Botón para calcular la puntuación total
        self.button_calcular = tk.Button(master, text="Calcular Total", command=self.calcular_total)
        self.button_calcular.grid(row=4, column=0, columnspan=2)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.grid(row=5, column=0, columnspan=2)

    def calcular_total(self):
        try:
            formacion = float(self.entry_formacion.get())
            experiencia = float(self.entry_experiencia.get())
            idiomas = float(self.entry_idiomas.get())
            informatica = float(self.entry_informatica.get())
            total = formacion + experiencia + idiomas + informatica
            self.label_resultado.config(text=f"Puntuación Total: {total}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = MeritCalculator(root)
    root.mainloop()
