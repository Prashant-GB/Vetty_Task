from flask import Flask, render_template, request,jsonify
import traceback
import os

app = Flask(__name__)

@app.route('/files/<filename>')
def read_folder(filename="file1.txt"):
    folder_path = './Python_test_jr'
    start = request.args.get('start')
    end = request.args.get('end')
    try:
        with open(os.path.join(folder_path,filename),'r',encoding='cp437') as f:
            lines = f.readlines()
            if start and end:
                lines = lines[int(start)-1:int(end)+1]
        return render_template('index.html', content=lines)
    except Exception:
        return render_template('error.html', error=traceback.format_exc())

@app.route('/')
def read_files(filename="file1.txt"):
    folder_path = './Python_test_jr'
    with open(os.path.join(folder_path,filename),'r') as f:
        line = f.readlines()
    return render_template('file.html',content=line)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'}), 404


    

if __name__ == '__main__':
    app.run(debug=True,port=5005)