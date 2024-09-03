from django.shortcuts import render

import google.generativeai as genai

# Create your views here.
genai.configure(api_key="AIzaSyD_Tj-2Giv_bIbueQqtzEIsZqyGu8NWcK0")

# Create the model

#Gemini
generation_config = {
  "temperature": 1.2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def ai_gemini(request):

    response_text = None
    user_input = "hi"
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
    
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    response = model.generate_content([
    "",
    f"input: {user_input}",
    "output: ",
    ])
    response_text = response.text
    #print(response.text)
    return render(request, 'ai.html', {'response_text': response_text})