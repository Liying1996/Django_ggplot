from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Upload
import os


def draw_plot(request):
    if request.method == "POST":
        context = {}
        form = UploadFileForm(request.POST, request.FILES)
        file_name = request.FILES['file'].name
        if form.is_valid():

            title = form.cleaned_data['title']
            file = form.cleaned_data['file']

            # write to database
            user = Upload()
            user.title = title
            user.file = file
            user.save()

            file_path = '/Users/yingli/PycharmProjects/drawggplot/media/upload/' + file_name
            os.system('Rscript /Users/yingli/PycharmProjects/drawggplot/cal/my_plot.R {} {}'.format(file_path, title))

            # image_data = open("/Users/yingli/PycharmProjects/calculator/image/" + title + '.png', "rb").read()
            # return HttpResponse(image_data, content_type="image/png")

            graph_path = title + ".png"
            # image_data = mpimg.imread(graph_path)

            context['graph'] = graph_path
            # return render(request, 'front.html', context)
            return render_to_response('front.html', context)


            # return HttpResponse('upload already!')
    else:

        form = UploadFileForm()
    return render_to_response('front.html', {'form': form})