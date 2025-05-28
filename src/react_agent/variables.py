import os
from dotenv import load_dotenv
from google import genai
from openai import OpenAI

load_dotenv()

from langchain_core.runnables import RunnableConfig

graph_config = RunnableConfig(
    recursion_limit=10,  # 최대 10개의 노드까지 방문. 그 이상은 RecursionError 발생
    configurable={"thread_id": "1"},  # 스레드 ID 설정
)

# empty map initialization
actors_map = {}
assets_map = {}
components_map = {}
data_flows_map = {}
trust_boundaries_map = {}
behaviors_map = {}
# for architecture analysis
architecture_analysis = {
    "system_context": {
        "docs": {
            "overview": "",
            "pol": "",
            "tokens": "",
            "governance": "",
            "dapps": ""
        },
        "components": components_map,
        "actors": actors_map,
        "assets": assets_map
    }
}

# all threats list
all_threats = []
# threats list
threats_list = []

checklist_items = []

gemini_model = "gemini-2.5-flash-preview-05-20"

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
gemini_client = genai.Client(
    api_key=GOOGLE_API_KEY
)

chatgpt_model = "gpt-4.1-nano-2025-04-14"
embedding_model = "text-embedding-3-large"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
chatgpt_client = OpenAI(
    api_key=OPENAI_API_KEY
)

ARCHITECTURE_FEEDBACK_LOOP_COUNT = 1
CHECKLIST_FEEDBACK_LOOP_COUNT = 1
CODE_BINDING_FEEDBACK_LOOP_COUNT = 1