import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("=== 사용 가능한 모델 목록 ===")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"✅ {m.name}")

print("\n=== 테스트: 각 모델로 메시지 보내기 ===")
test_models = [
    'gemini-1.5-flash',
    'gemini-1.5-pro', 
    'gemini-pro',
    'gemini-1.5-flash-latest',
    'models/gemini-1.5-flash',
    'models/gemini-pro'
]

for model_name in test_models:
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("안녕")
        print(f"✅ {model_name} - 성공!")
        print(f"   응답: {response.text[:50]}...")
        break  # 성공하면 중단
    except Exception as e:
        print(f"❌ {model_name} - 실패: {str(e)[:80]}")