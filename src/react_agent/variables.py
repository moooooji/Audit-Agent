import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# 빈 맵 초기화
actors_map = {}
assets_map = {}
components_map = {}
data_flows_map = {}
trust_boundaries_map = {}
behaviors_map = {}
# 아키텍처 분석을 위한 프롬프트 호출
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
model = "gemini-2.0-flash"
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
client = genai.Client(
    api_key=GOOGLE_API_KEY
)

ARCHITECTURE_FEEDBACK_LOOP_COUNT = 1
CHECKLIST_FEEDBACK_LOOP_COUNT = 1
CODE_BINDING_FEEDBACK_LOOP_COUNT = 1