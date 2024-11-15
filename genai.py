import google.generativeai as genai

apikey="AIzaSyCEn5YfcEEUnKFTRhLYXO-ebLrAmSW6AUE"
genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")
def text(prompt):
    response = model.generate_content(prompt+"only give me the mail no other content should be there")
    return response.text