import os

from dashscope import api_key
from openai import OpenAI
import json
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate


def get_response(question: str):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key="sk-b3fe75fe3a3a4cfbbaee21f0518d6a21",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': question}],
    )

    print(completion.model_dump_json())
    result = completion.model_dump_json()
    result = json.loads(result)
    return result["choices"][0]["message"]["content"]


def langchain(question):
    api_key = "sk-b3fe75fe3a3a4cfbbaee21f0518d6a21"
    # llm = Tongyi()
    # llm = Tongyi(dashscope_api_key=api_key)
    # 指定模型
    llm = Tongyi(model_name="qwen-plus", temperature=0,api_key=api_key)
    template = """
    #角色
    你是一位老师，你正在复盘你的上课内容，进行课程整理。
    #场景
    现在你获得了你的课程记录，你需要整理课程中的内容，包括讲解了哪些知识点，知识点的主要内容，并且给出该知识点的对应题目。
    #限制：
    1. 请提供严格根据课程记录进行整理，不要随意发散。
    2. 你的工作很重要，因此你必须保证你的内容是正确的。
    3. 请生成json格式的输出，保证可以被json.loads函数加载，务必保证不包含```json，否则你将受到惩罚。格式要求如下：
    {{
      "知识点1": {{
        "知识点名":""
        "知识点讲解":""
        "知识点例题":""
        "例题答案":""
      }},
      "知识点2": {{
        "知识点名":""
        "知识点讲解":""
        "知识点例题":""
        "例题答案":""
      }},
    }}
    课程记录如下：
    {question}
    """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"question": question})
    print(response)
    response = json.loads(response)
    return response

def conservation(question):
    api_key="sk-b3fe75fe3a3a4cfbbaee21f0518d6a21"
    # llm = Tongyi()
    # 指定模型
    llm=Tongyi(model_name="qwen-plus",temperature=0,api_key=api_key)
    template = """
    #角色
    你是一位老师，你正在复盘你和学生的对话，诊断学生的问题并推荐对应的题目。
    #场景
    现在你获得了你和学生的对话记录，你需要整理学生与你对话中的问题，包括问题包含哪些知识点，知识点的主要内容，并且给出该知识点的对应题目。
    #限制：
    1. 请提供严格根据对话记录进行整理，不要随意发散。
    2. 你的工作很重要，因此你必须保证你的内容是正确的。
    3. 请生成json格式的输出，保证可以被json.loads函数加载，务必保证不包含```json，否则你将受到惩罚。格式要求如下：
    {{
      "知识点1": {{
        "知识点名":""
        "知识点讲解":""
        "知识点例题":""
        "例题答案":""
      }},
      "知识点2": {{
        "知识点名":""
        "知识点讲解":""
        "知识点例题":""
        "例题答案":""
      }},
    }}
    对话记录如下：
    {question}
    """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response=chain.invoke({"question": question})
    print(response)
    response=json.loads(response)
    return response
# response = langchain("这节课我讲了sin函数和cos函数")
# print(response)
# response = json.loads(response)
# print(response["知识点1"])

