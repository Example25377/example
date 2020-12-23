from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from .forms import DocumentForm
from .models import Document
from django.shortcuts import redirect, render

class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context

#     class FileFieldView(FormView):
#         form_class = FileFieldForm
#         template_name = 'upload.html'  # Replace with your template.
#         success_url = '...'  # Replace with your URL or reverse().
#
#         def post(self, request, *args, **kwargs):
#             form_class = self.get_form_class()
#             form = self.get_form(form_class)
#             files = request.FILES.getlist('file_field')
#             if form.is_valid():
#                 for f in files:
#                     ...  # Do something with each file.
#                 return self.form_valid(form)
#             else:
#                 return self.form_invalid(form)
#
#     def my_view(request):
#         print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
#         message = 'Upload as many files as you want!'
#         # Handle file upload
#         if request.method == 'POST':
#             form = DocumentForm(request.POST, request.FILES)
#             if form.is_valid():
#                 newdoc = Upload(docfile=request.FILES['docfile'])
#                 newdoc.save()
#
#                 # Redirect to the document list after POST
#                 return redirect('my-view')
#             else:
#                 message = 'The form is not valid. Fix the following error:'
#         else:
#             form = DocumentForm()  # An empty, unbound form
#
#         # Load documents for the list page
#         documents = Upload.objects.all()
#
#         # Render list page with the documents and the form
#         context = {'documents': documents, 'form': form, 'message': message}
#         return render(request, 'list.html', context)
#
#
# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'list.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)






def my_view(request):
    # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    # message = 'Upload as many files as you want!'
    message = 'Upload files!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        newdoc = request.FILES.getlist('docfile')
        if form.is_valid():
            for f in newdoc:
                file_instance = Document(docfile=f)
                file_instance.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)