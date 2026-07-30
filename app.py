from flask import Flask, render_template, request, redirect

app = Flask(__name__)
url_list = []
id_list = []


@app.route('/')
def index():
    print("index")
    return render_template("index.html")


@app.route('/watch', methods=['POST', 'GET'])
def watch():
    url_list = []
    if request.method == 'POST':
        print("post")
        if request.form['URL1'] != '':
            url_list.append(request.form['URL1'])
        if request.form['URL2'] != '':
            url_list.append(request.form['URL2'])
        if request.form['URL3'] != '':
            url_list.append(request.form['URL3'])
        if request.form['URL4'] != '':
            url_list.append(request.form['URL4'])
        print(url_list)
        url = "/multistream"
        i = 0
        for x in url_list:
            x = x.split('=')
            x = x[len(x)-1]
            print(x)
            id_list.append(x)
            if i == 0:
                url = url + "?id1={ytid}".format(ytid=x)
            else:
                url = url + "&id{num}={id}".format(num=i+1, id=x)
            i += 1

        print(id_list)
        print(url)
        return redirect(url)
    return None


@app.route('/multistream')
def multistream():
    id_list_view = []
    for i in range(4):
        e = i + 1
        print(request.args.get(str('id' + str(e))))
        if request.args.get(str('id' + str(e))) is None:
            print('pass')
            pass
        else:

            id_list_view.append(request.args.get(str('id' + str(e))))
    print(len(id_list_view))

    return render_template('multistream.html',idlist_length=len(id_list_view), idlist=id_list_view)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)