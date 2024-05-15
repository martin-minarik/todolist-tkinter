import customtkinter as ctk
from tkinter import ttk

title_font: ctk.CTkFont
button_font: ctk.CTkFont
form_label_font: ctk.CTkFont
legend_label_font: ctk.CTkFont


def init_styles():
    global title_font, button_font, form_label_font, legend_label_font
    title_font = ctk.CTkFont(size=36, weight="bold")
    button_font = ctk.CTkFont(family="ButtonFont", size=14)
    form_label_font = ctk.CTkFont(family="FormLabelFont", size=16, weight="bold")
    legend_label_font = ctk.CTkFont(family="LegendLabelFont", size=12, weight="bold")

    tree_style = ttk.Style()
    tree_style.configure("table.Treeview",
                         foreground=ctk.ThemeManager.theme["CTkLabel"]["text_color"][0],
                         fieldbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
                         borderwidth=0, font=ctk.CTkFont(size=25))
    tree_style.configure('table.Treeview.Heading',
                         background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0],
                         foreground=ctk.ThemeManager.theme["CTkLabel"]["text_color"][0],
                         font=ctk.CTkFont(size=25, weight="bold"))
    tree_style.map('table.Treeview', background=[('selected', ctk.ThemeManager.theme["CTkFrame"]["fg_color"][0])],
                   foreground=[('selected', "blue")])
