# ui/generation_handlers.py
# -*- coding: utf-8 -*-
import os
import threading
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import traceback
from utils import read_file, save_string_to_txt, clear_file_content
from novel_generator import (
    Novel_architecture_generate,
    Chapter_blueprint_generate,
    generate_chapter_draft,
    finalize_chapter,
    import_knowledge_file,
    clear_vector_store,
    enrich_chapter_text
)
from consistency_checker import check_consistency

def generate_novel_architecture_ui(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please select the save file path first")
        return

    def task():
        self.disable_button_safe(self.btn_generate_architecture)
        try:
            interface_format = self.interface_format_var.get().strip()
            api_key = self.api_key_var.get().strip()
            base_url = self.base_url_var.get().strip()
            model_name = self.model_name_var.get().strip()
            temperature = self.temperature_var.get()
            max_tokens = self.max_tokens_var.get()
            timeout_val = self.safe_get_int(self.timeout_var, 600)

            topic = self.topic_text.get("0.0", "end").strip()
            genre = self.genre_var.get().strip()
            num_chapters = self.safe_get_int(self.num_chapters_var, 10)
            word_number = self.safe_get_int(self.word_number_var, 3000)

            self.safe_log("Starting to generate the novel structure...")
            Novel_architecture_generate(
                interface_format=interface_format,
                api_key=api_key,
                base_url=base_url,
                llm_model=model_name,
                topic=topic,
                genre=genre,
                number_of_chapters=num_chapters,
                word_number=word_number,
                filepath=filepath,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout_val
            )
            self.safe_log("✅ Novel structure generation complete. Please check or edit in the 'Novel Architecture' tab.")
        except Exception:
            self.handle_exception("Error occurred while generating the novel structure")
        finally:
            self.enable_button_safe(self.btn_generate_architecture)
    threading.Thread(target=task, daemon=True).start()

def generate_chapter_blueprint_ui(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please select the save file path first")
        return

    def task():
        self.disable_button_safe(self.btn_generate_directory)
        try:
            interface_format = self.interface_format_var.get().strip()
            api_key = self.api_key_var.get().strip()
            base_url = self.base_url_var.get().strip()
            model_name = self.model_name_var.get().strip()
            number_of_chapters = self.safe_get_int(self.num_chapters_var, 10)
            temperature = self.temperature_var.get()
            max_tokens = self.max_tokens_var.get()
            timeout_val = self.safe_get_int(self.timeout_var, 600)

            self.safe_log("Starting to generate the chapter blueprint...")
            Chapter_blueprint_generate(
                interface_format=interface_format,
                api_key=api_key,
                base_url=base_url,
                llm_model=model_name,
                number_of_chapters=number_of_chapters,
                filepath=filepath,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout_val
            )
            self.safe_log("✅ Chapter blueprint generation complete. Please check or edit in the 'Chapter Blueprint' tab.")
        except Exception:
            self.handle_exception("Error occurred while generating the chapter blueprint")
        finally:
            self.enable_button_safe(self.btn_generate_directory)
    threading.Thread(target=task, daemon=True).start()

def generate_chapter_draft_ui(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please configure the save file path first.")
        return

    def task():
        self.disable_button_safe(self.btn_generate_chapter)
        try:
            interface_format = self.interface_format_var.get().strip()
            api_key = self.api_key_var.get().strip()
            base_url = self.base_url_var.get().strip()
            model_name = self.model_name_var.get().strip()
            temperature = self.temperature_var.get()
            max_tokens = self.max_tokens_var.get()
            timeout_val = self.safe_get_int(self.timeout_var, 600)

            chap_num = self.safe_get_int(self.chapter_num_var, 1)
            word_number = self.safe_get_int(self.word_number_var, 3000)
            user_guidance = self.user_guide_text.get("0.0", "end").strip()

            char_inv = self.characters_involved_var.get().strip()
            key_items = self.key_items_var.get().strip()
            scene_loc = self.scene_location_var.get().strip()
            time_constr = self.time_constraint_var.get().strip()

            embedding_api_key = self.embedding_api_key_var.get().strip()
            embedding_url = self.embedding_url_var.get().strip()
            embedding_interface_format = self.embedding_interface_format_var.get().strip()
            embedding_model_name = self.embedding_model_name_var.get().strip()
            embedding_k = self.safe_get_int(self.embedding_retrieval_k_var, 4)

            self.safe_log(f"Generating chapter {chap_num} draft: Preparing to generate request prompt...")

            # 调用新添加的 build_chapter_prompt 函数构造初始提示词
            from novel_generator.chapter import build_chapter_prompt
            prompt_text = build_chapter_prompt(
                api_key=api_key,
                base_url=base_url,
                model_name=model_name,
                filepath=filepath,
                novel_number=chap_num,
                word_number=word_number,
                temperature=temperature,
                user_guidance=user_guidance,
                characters_involved=char_inv,
                key_items=key_items,
                scene_location=scene_loc,
                time_constraint=time_constr,
                embedding_api_key=embedding_api_key,
                embedding_url=embedding_url,
                embedding_interface_format=embedding_interface_format,
                embedding_model_name=embedding_model_name,
                embedding_retrieval_k=embedding_k,
                interface_format=interface_format,
                max_tokens=max_tokens,
                timeout=timeout_val
            )

            # 弹出可编辑提示词对话框，等待用户确认或取消
            result = {"prompt": None}
            event = threading.Event()

            def create_dialog():
                dialog = ctk.CTkToplevel(self.master)
                dialog.title("Current Chapter Request Prompt (Editable)")
                dialog.geometry("600x400")
                text_box = ctk.CTkTextbox(dialog, wrap="word", font=("Microsoft YaHei", 12))
                text_box.pack(fill="both", expand=True, padx=10, pady=10)
                text_box.insert("0.0", prompt_text)
                button_frame = ctk.CTkFrame(dialog)
                button_frame.pack(pady=10)
                def on_confirm():
                    result["prompt"] = text_box.get("1.0", "end").strip()
                    dialog.destroy()
                    event.set()
                def on_cancel():
                    result["prompt"] = None
                    dialog.destroy()
                    event.set()
                btn_confirm = ctk.CTkButton(button_frame, text="Confirm Usage", font=("Microsoft YaHei", 12), command=on_confirm)
                btn_confirm.pack(side="left", padx=10)
                btn_cancel = ctk.CTkButton(button_frame, text="Cancel Request", font=("Microsoft YaHei", 12), command=on_cancel)
                btn_cancel.pack(side="left", padx=10)
                # 若用户直接关闭弹窗，则调用 on_cancel 处理
                dialog.protocol("WM_DELETE_WINDOW", on_cancel)
                dialog.grab_set()
            self.master.after(0, create_dialog)
            event.wait()  # 等待用户操作完成
            edited_prompt = result["prompt"]
            if edited_prompt is None:
                self.safe_log("❌ User canceled the draft generation request.")
                return

            self.safe_log("Starting to generate the chapter draft...")
            from novel_generator.chapter import generate_chapter_draft
            draft_text = generate_chapter_draft(
                api_key=api_key,
                base_url=base_url,
                model_name=model_name,
                filepath=filepath,
                novel_number=chap_num,
                word_number=word_number,
                temperature=temperature,
                user_guidance=user_guidance,
                characters_involved=char_inv,
                key_items=key_items,
                scene_location=scene_loc,
                time_constraint=time_constr,
                embedding_api_key=embedding_api_key,
                embedding_url=embedding_url,
                embedding_interface_format=embedding_interface_format,
                embedding_model_name=embedding_model_name,
                embedding_retrieval_k=embedding_k,
                interface_format=interface_format,
                max_tokens=max_tokens,
                timeout=timeout_val,
                custom_prompt_text=edited_prompt  # 使用用户编辑后的提示词
            )
            if draft_text:
                self.safe_log(f"✅ Chapter {chap_num} draft generation complete. Please check or edit on the left.")
                self.master.after(0, lambda: self.show_chapter_in_textbox(draft_text))
            else:
                self.safe_log("⚠️ Chapter draft generation failed or has no content.")
        except Exception:
            self.handle_exception("Error occurred while generating the chapter draft")
        finally:
            self.enable_button_safe(self.btn_generate_chapter)
    threading.Thread(target=task, daemon=True).start()

def finalize_chapter_ui(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please configure the save file path first.")
        return

    def task():
        self.disable_button_safe(self.btn_finalize_chapter)
        try:
            interface_format = self.interface_format_var.get().strip()
            api_key = self.api_key_var.get().strip()
            base_url = self.base_url_var.get().strip()
            model_name = self.model_name_var.get().strip()
            temperature = self.temperature_var.get()
            max_tokens = self.max_tokens_var.get()
            timeout_val = self.safe_get_int(self.timeout_var, 600)

            embedding_api_key = self.embedding_api_key_var.get().strip()
            embedding_url = self.embedding_url_var.get().strip()
            embedding_interface_format = self.embedding_interface_format_var.get().strip()
            embedding_model_name = self.embedding_model_name_var.get().strip()

            chap_num = self.safe_get_int(self.chapter_num_var, 1)
            word_number = self.safe_get_int(self.word_number_var, 3000)

            self.safe_log(f"Starting to finalize chapter {chap_num}...")

            chapters_dir = os.path.join(filepath, "chapters")
            os.makedirs(chapters_dir, exist_ok=True)
            chapter_file = os.path.join(chapters_dir, f"chapter_{chap_num}.txt")

            edited_text = self.chapter_result.get("0.0", "end").strip()

            if len(edited_text) < 0.7 * word_number:
                ask = messagebox.askyesno("Word Count Insufficient", f"Current chapter word count ({len(edited_text)}) is less than 70% of the target word count ({word_number}). Would you like to try expanding it?")
                if ask:
                    self.safe_log("Expanding chapter content...")
                    enriched = enrich_chapter_text(
                        chapter_text=edited_text,
                        word_number=word_number,
                        api_key=api_key,
                        base_url=base_url,
                        model_name=model_name,
                        temperature=temperature,
                        interface_format=interface_format,
                        max_tokens=max_tokens,
                        timeout=timeout_val
                    )
                    edited_text = enriched
                    self.master.after(0, lambda: self.chapter_result.delete("0.0", "end"))
                    self.master.after(0, lambda: self.chapter_result.insert("0.0", edited_text))
            clear_file_content(chapter_file)
            save_string_to_txt(edited_text, chapter_file)

            finalize_chapter(
                novel_number=chap_num,
                word_number=word_number,
                api_key=api_key,
                base_url=base_url,
                model_name=model_name,
                temperature=temperature,
                filepath=filepath,
                embedding_api_key=embedding_api_key,
                embedding_url=embedding_url,
                embedding_interface_format=embedding_interface_format,
                embedding_model_name=embedding_model_name,
                interface_format=interface_format,
                max_tokens=max_tokens,
                timeout=timeout_val
            )
            self.safe_log(f"✅ Chapter {chap_num} finalization complete (Global summary, character status, and vector library updated).")

            final_text = read_file(chapter_file)
            self.master.after(0, lambda: self.show_chapter_in_textbox(final_text))
        except Exception:
            self.handle_exception("Error occurred while finalizing the chapter")
        finally:
            self.enable_button_safe(self.btn_finalize_chapter)
    threading.Thread(target=task, daemon=True).start()

def do_consistency_check(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please configure the save file path first.")
        return

    def task():
        self.disable_button_safe(self.btn_check_consistency)
        try:
            api_key = self.api_key_var.get().strip()
            base_url = self.base_url_var.get().strip()
            model_name = self.model_name_var.get().strip()
            temperature = self.temperature_var.get()
            interface_format = self.interface_format_var.get()
            max_tokens = self.max_tokens_var.get()
            timeout = self.timeout_var.get()

            chap_num = self.safe_get_int(self.chapter_num_var, 1)
            chap_file = os.path.join(filepath, "chapters", f"chapter_{chap_num}.txt")
            chapter_text = read_file(chap_file)

            if not chapter_text.strip():
                self.safe_log("⚠️ The current chapter file is empty or does not exist, and cannot be reviewed.")
                return

            self.safe_log("Starting consistency review...")
            result = check_consistency(
                novel_setting="",
                character_state=read_file(os.path.join(filepath, "character_state.txt")),
                global_summary=read_file(os.path.join(filepath, "global_summary.txt")),
                chapter_text=chapter_text,
                api_key=api_key,
                base_url=base_url,
                model_name=model_name,
                temperature=temperature,
                interface_format=interface_format,
                max_tokens=max_tokens,
                timeout=timeout,
                plot_arcs=""
            )
            self.safe_log("Review result:")
            self.safe_log(result)
        except Exception:
            self.handle_exception("Error occurred during the review")
        finally:
            self.enable_button_safe(self.btn_check_consistency)
    threading.Thread(target=task, daemon=True).start()

def import_knowledge_handler(self):
    selected_file = tk.filedialog.askopenfilename(
        title="Select the knowledge base file to import",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if selected_file:
        def task():
            self.disable_button_safe(self.btn_import_knowledge)
            try:
                emb_api_key = self.embedding_api_key_var.get().strip()
                emb_url = self.embedding_url_var.get().strip()
                emb_format = self.embedding_interface_format_var.get().strip()
                emb_model = self.embedding_model_name_var.get().strip()

                self.safe_log(f"Starting to import knowledge base file: {selected_file}")
                import_knowledge_file(
                    embedding_api_key=emb_api_key,
                    embedding_url=emb_url,
                    embedding_interface_format=emb_format,
                    embedding_model_name=emb_model,
                    file_path=selected_file,
                    filepath=self.filepath_var.get().strip()
                )
                self.safe_log("✅ Knowledge base file import complete.")
            except Exception:
                self.handle_exception("Error occurred while importing the knowledge base")
            finally:
                self.enable_button_safe(self.btn_import_knowledge)
        threading.Thread(target=task, daemon=True).start()

def clear_vectorstore_handler(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please configure the save file path first.")
        return

    first_confirm = messagebox.askyesno("Warning", "Are you sure you want to clear the local vector store? This action cannot be undone!")
    if first_confirm:
        second_confirm = messagebox.askyesno("Confirmation", "Are you sure you really want to delete all vector data? This action cannot be undone!")
        if second_confirm:
            if clear_vector_store(filepath):
                self.log("Vector store cleared.")
            else:
                self.log(f"Failed to clear the vector store. Please close the program and manually delete the vectorstore folder under {filepath}.")

def show_plot_arcs_ui(self):
    filepath = self.filepath_var.get().strip()
    if not filepath:
        messagebox.showwarning("Warning", "Please set the save file path in the main Tab first")
        return
    plot_arcs_file = os.path.join(filepath, "plot_arcs.txt")
    if not os.path.exists(plot_arcs_file):
        messagebox.showinfo("Plot Points", "No plot points or conflict records have been generated yet.")
        return
    arcs_text = read_file(plot_arcs_file).strip()
    if not arcs_text:
        arcs_text = "There are no recorded plot points or conflicts currently."
    top = ctk.CTkToplevel(self.master)
    top.title("Plot Points / Unresolved Conflicts")
    top.geometry("600x400")
    text_area = ctk.CTkTextbox(top, wrap="word", font=("Microsoft YaHei", 12))
    text_area.pack(fill="both", expand=True, padx=10, pady=10)
    text_area.insert("0.0", arcs_text)
    text_area.configure(state="disabled")
