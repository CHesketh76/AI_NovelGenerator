# ui/summary_tab.py
# -*- coding: utf-8 -*-
import os
import customtkinter as ctk
from tkinter import messagebox
from utils import read_file, save_string_to_txt, clear_file_content
from ui.context_menu import TextWidgetContextMenu

def build_summary_tab(self):
    self.summary_tab = self.tabview.add("Global Summary")
    self.summary_tab.rowconfigure(0, weight=0)
    self.summary_tab.rowconfigure(1, weight=1)
    self.summary_tab.columnconfigure(0, weight=1)

    load_btn = ctk.CTkButton(self.summary_tab, text="Load global_summary.txt", command=self.load_global_summary, font=("Microsoft YaHei", 12))
    load_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    save_btn = ctk.CTkButton(self.summary_tab, text="Save Changes", command=self.save_global_summary, font=("Microsoft YaHei", 12))
    save_btn.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    self.summary_text = ctk.CTkTextbox(self.summary_tab, wrap="word", font=("Microsoft YaHei", 12))
    TextWidgetContextMenu(self.summary_text)
    self.summary_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

def load_global_summary(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please set the save file path first")
        return
    filename = os.path.join(filepath, "global_summary.txt")
    content = read_file(filename)
    self.summary_text.delete("0.0", "end")
    self.summary_text.insert("0.0", content)
    self.log("Content of global_summary.txt has been loaded into the edit area.")

def save_global_summary(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please set the save file path first")
        return
    content = self.summary_text.get("0.0", "end").strip()
    filename = os.path.join(filepath, "global_summary.txt")
    clear_file_content(filename)
    save_string_to_txt(content, filename)
    self.log("Modifications to global_summary.txt have been saved.")
