def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! Need assistance with a chatbot or a 1-page website?",
        "สวัสดี": "สวัสดีค่ะ ยินดีต้อนรับสู่ Soft Power Thailand!",
        "บริการ": "เรามีบริการแชทบอทและเว็บไซต์สำหรับธุรกิจไทย",
        "price": "Our pricing starts at ฿1,000 for a basic chatbot.",
        "how much": "Starter package begins at ฿1,000 only!",
        "ติดต่อ": "คุณสามารถจองเวลาได้ผ่าน Calendly หรือติดต่อเราทางแบบฟอร์ม",
    }
    return responses.get(user_input, "Sorry, I didn't understand that. Please try again.")
