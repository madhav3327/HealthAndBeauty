import google.generativeai as genai

# Step 1: Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyBWWCbjWJ3cyeMC2ozg-NcWP8fc1vzoLw8")  # 👈 Replace this with your real key

# Step 2: List all available models and their capabilities
print("🔍 Available Gemini Models:\n")
try:
    models = genai.list_models()
    for m in models:
        print(f"- {m.name} | Supports: {m.supported_generation_methods}")
except Exception as e:
    print(f"❌ Failed to list models: {e}")

# Step 3: Try to use gemini-pro (if available)
print("\n🧪 Testing gemini-pro...\n")
try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Hi Gemini, what can you do?")
    print("✅ Gemini Response:")
    print(response.text)
except Exception as e:
    print(f"❌ Error generating content with gemini-pro: {e}")