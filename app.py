from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# بيانات تليجرام الخاصة بك
TOKEN = "8469404169:AAG07_9xJC5qvri-GzlK8EUBo8oCZd37qkM"
CHAT_ID = "6465012385"

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, data=data)
    except:
        pass

@app.route('/')
def index():
    # إرسال تنبيه عند دخول الصفحة الرئيسية
    send_telegram_alert(f"🚀 *دخول جديد للأقصى نت*\n🌐 IP: `{request.remote_addr}`")
    return render_template('index.html')

@app.route('/services') # هذا هو المسار الذي يمنع خطأ Not Found
def services():
    send_telegram_alert("💳 الزبون يتصفح *قائمة الباقات* الآن")
    return render_template('services.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.json
    lat, lon = data.get('lat'), data.get('lon')
    google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    send_telegram_alert(f"📍 *موقع الزبون (دبوس):*\n{google_maps_link}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)