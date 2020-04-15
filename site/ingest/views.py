import string
import random

from django.views.generic import CreateView, UpdateView

from django.urls import reverse_lazy

from django_tables2.views import SingleTableView

from brooks.views_mixins import LogginRequired

from ingest import apps, models, forms, tables


# =============================================================================
# CONSTANTS
# =============================================================================

LETTERS = string.ascii_uppercase + string.digits


# =============================================================================
# CLASSES
# =============================================================================

class UploadRawFileView(LogginRequired, CreateView):

    model = models.RawFile
    form_class = forms.UploadRawFileForm
    template_name = "ingest/UploadRawFile.html"
    success_message = "Archivo ({id}) '{filename}' subido con éxito"

    def get_success_url(self):
        rawfile = self.object
        return reverse_lazy('ingest:check_file', args=[rawfile.pk])

    def get_success_message(self, cleaned_data):
        return self.success_message.format(
            id=self.object.id, filename=self.object.filename)

    def form_valid(self, form):
        rawfile = form.save(commit=False)
        rawfile.created_by = self.request.user

        rawfile.save()
        return super().form_valid(form)


class CheckRawFileView(LogginRequired, UpdateView):

    template_name = "ingest/CheckRawFileView.html"
    form_class = forms.UpdateRawFileForm
    model = models.RawFile
    success_url = reverse_lazy("ingest:list_files")

    def get_context_data(self):
        context_data = super().get_context_data()
        if not self.object.merged:
            filepath = self.object.file.path
            merge_info = apps.IngestConfig.dmodels.merge_info(filepath)
            context_data["merge_info"] = merge_info
        context_data["conf_code"] = "".join(random.sample(LETTERS, 6))
        return context_data


class ListRawFileView(LogginRequired, SingleTableView):

    model = models.RawFile
    table_class = tables.RawFileTable
    template_name = "ingest/ListRawFileView.html"

# class ListPatientView(LogginRequired, SingleTableView):

#     model = models.Patient
#     table_class = tables.PatientTable
#     template_name = "ingest/ListPatientView.html"


# class PatientDetailView(LogginRequired, UpdateView):

#     template_name = "ingest/PatientDetailView.html"
#     form_class = forms.PatientDetailForm
#     model = models.Patient

#     def get_success_url(self):
#         patient = self.object
#         return reverse_lazy('ingest:patient_detail', args=[patient.pk])

#     def get_context_data(self):
#         context_data = super().get_context_data()
#         context_data["pp_patient"] = pprinter.PatientPrinter(self.object)
#         return context_data
