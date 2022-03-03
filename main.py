from flask import Flask
app = Flask('a')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)

# import keyboard
# while True:
#     try:
#         if keyboard.is_pressed('s'):
#             print("stop")
#         elif keyboard.is_pressed('p'):
#             print("pause")
#     except:
#         pass