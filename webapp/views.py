from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def prediction(request):
    if request.method == 'POST' and request.FILES['myfile']:
        post = request.method == 'POST'
        myfile = request.FILES['myfile']
        img = image.load_img(myfile, target_size=(64,64,3))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        with graph.as_default():
            preds = model.predict(img)
        if preds[0][0] >= 0.7:
            result = 'The Car is not Damaged'
        else:
            result = 'The Car is Damaged'
        return render(request, "templates/index.html", {
            'result': result})
    else:
        return render(request, "templates/index.html")
