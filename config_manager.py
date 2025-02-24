# config_manager.py
# -*- coding: utf-8 -*-
import json
import os
import threading
from llm_adapters import create_llm_adapter
from embedding_adapters import create_embedding_adapter


def load_config(config_file: str) -> dict:
    """从指定的 config_file 加载配置，若不存在则返回空字典。"""
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_config(config_data: dict, config_file: str) -> bool:
    """将 config_data 保存到 config_file 中，返回 True/False 表示是否成功。"""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def test_llm_config(interface_format, api_key, base_url, model_name, temperature, max_tokens, timeout, log_func, handle_exception_func):
    """测试当前的LLM配置是否可用"""
    def task():
        try:
            log_func("Starting LLM configuration test...")
            llm_adapter = create_llm_adapter(
                interface_format=interface_format,
                base_url=base_url,
                model_name=model_name,
                api_key=api_key,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout
            )

            test_prompt = "Please reply 'OK'"
            response = llm_adapter.invoke(test_prompt)
            if response:
                log_func("✅ LLM configuration test succeeded!")
                log_func(f"Test response: {response}")
            else:
                log_func("❌ LLM configuration test failed: No response received")
        except Exception as e:
            log_func(f"❌ LLM configuration test error: {str(e)}")
            handle_exception_func("Error occurred during LLM configuration test")

    threading.Thread(target=task, daemon=True).start()

def test_embedding_config(api_key, base_url, interface_format, model_name, log_func, handle_exception_func):
    """测试当前的Embedding配置是否可用"""
    def task():
        try:
            log_func("Starting Embedding configuration test...")
            embedding_adapter = create_embedding_adapter(
                interface_format=interface_format,
                api_key=api_key,
                base_url=base_url,
                model_name=model_name
            )
            test_text = "Test text"
            embeddings = embedding_adapter.embed_query(test_text)
            if embeddings and len(embeddings) > 0:
                log_func("✅ Embedding configuration test succeeded!")
                log_func(f"Generated vector dimensions: {len(embeddings)}")
            else:
                log_func("❌ Embedding configuration test failed: No vector received")
        except Exception as e:
            log_func(f"❌ Embedding configuration test error: {str(e)}")
            handle_exception_func("Error occurred during Embedding configuration test")

    threading.Thread(target=task, daemon=True).start()
