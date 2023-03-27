import json
import requests
from PIL import Image,ImageDraw
import io
import numpy as np
from flask import Flask,request,send_file
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')	# 注册CORS, "/*" 允许访问所有api



def our_prototype():
    #download image
    IMAGE_URL='https://media.nationalgeographic.org/assets/photos/180/373/87b29588-8cdf-44d1-9ed5-798e29482750.jpg'
    url = 'http://172.16.192.6:8501/v1/models/typhoon:predict'#shou IP by tensorflow zheng
    dl_request = requests.get(IMAGE_URL, stream=True)
    dl_request.raise_for_status()
    # convert to b64 by zszheng
    jpeg_rgb=Image.open(io.BytesIO(dl_request.content))
    jpeg_rgb2=jpeg_rgb.resize((640, 640),Image.ANTIALIAS)
    jpeg_rgb=np.expand_dims(np.array(jpeg_rgb2)/255.0,0).tolist()
    #predict_request = '{"instances" : [{"b64": "%s"}]}' % base64.b64encode(jpeg_rgb)
    predict_request = json.dumps({'instances':jpeg_rgb})
    response = requests.post(url, data=predict_request)
    #response.raise_for_status()
    prediction = response.json()['predictions'][0]
    #print(prediction['output_0'])
    for item in prediction['output_0']:
        if(item[0]>0):
            lst = [i * 640 for i in item]
    [x,y,w,h]=map(int,lst)
    #jpeg_rgb2=np.array(jpeg_rgb2)
    #cv2.rectangle(jpeg_rgb2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    draw = ImageDraw.Draw(jpeg_rgb2)
    draw.rectangle((x, y, w, h), outline='red')
    jpeg_rgb2.show(jpeg_rgb2)

@app.route('/get_image',methods=['POST'])
def get_image():
    uploaded_files = request.files.getlist("file")
    filename=''
    # print (os.path.abspath('.'))
    for file in uploaded_files:
        file_path='C:/Users/86139/Desktop/storm/storm_request/upload_file'+file.filename
        filename=file.filename
        file.save(file_path)
    url = 'http://172.16.192.6:8501/v1/models/typhoon:predict'  # shou IP by tensorflow zheng
    jpeg_rgb=Image.open(file_path)
    jpeg_rgb2=jpeg_rgb.resize((640, 640),Image.ANTIALIAS)
    jpeg_rgb=np.expand_dims(np.array(jpeg_rgb2)/255.0,0).tolist()
    #predict_request = '{"instances" : [{"b64": "%s"}]}' % base64.b64encode(jpeg_rgb)
    predict_request = json.dumps({'instances':jpeg_rgb})
    response = requests.post(url, data=predict_request)
    #response.raise_for_status()
    prediction = response.json()['predictions'][0]
    #print(prediction['output_0'])
    for item in prediction['output_0']:
        #if(item[0]>0):
            lst = [i * 640 for i in item]

    print(lst)
    [x,y,w,h]=map(int,lst)
    #jpeg_rgb2=np.array(jpeg_rgb2)
    #cv2.rectangle(jpeg_rgb2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    draw = ImageDraw.Draw(jpeg_rgb2)
    draw.rectangle((x, y, w, h), outline='red')
    processed_file_path='C:/Users/86139/Desktop/storm/storm_request/processed_file/'+filename
    jpeg_rgb2.save(processed_file_path)
    # p_path = os.path.abspath(os.path.dirname(__file__))
    # processed_file_path=p_path+'\\processed_file\\'+filename
    return send_file(processed_file_path,filename)


@app.route('/resize_image',methods=['POST'])
def resize_image():
    return 0

@app.route('/')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.run(port=5554)
