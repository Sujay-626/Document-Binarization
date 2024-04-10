from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/binarize', methods=['POST'])
def binarize():
    img_file = request.files['image']
    model_file = request.files['model']
    img_path = 'uploads/input.png'  # Save uploaded image to a file
    model_path = 'uploads/model.h5'  # Save uploaded model to a file
    img_file.save(img_path)
    model_file.save(model_path)
    cmd = f"python binarize.py -imgpath {img_path} -modelpath {model_path} -w 256 -s 96 -f 64 -k 5 -stride 2 -th 0.5 --demo"
    subprocess.run(cmd, shell=True, check=True)
    output_img_path = "output_img.png"  # Relative path to the output image within the static folder
    return jsonify({'output_img': output_img_path})

if __name__ == '__main__':
    app.run(debug=True)
