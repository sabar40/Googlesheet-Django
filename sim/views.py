from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import EntryForm
from django.contrib import messages
from sim.services import initialize_gspread, get_all_rows


# sim/views.py
def index(request):
    expected_headers = ['Prenom', 'Telephone', 'lieu_naissance', 'Actue']
    query = request.GET.get('q', '')
    all_data = get_all_rows('Sheet-Django', expected_headers=expected_headers, return_row_numbers=True)
    
    if query:
        filtered_data = [(row, row_number) for row, row_number in all_data if query.lower() in ' '.join(map(str, row.values())).lower()]
    else:
        filtered_data = all_data

    return render(request, 'index.html', {'data': filtered_data, 'query': query})




class AddEntryView(View):
    def get(self, request):
        form = EntryForm()
        return render(request, 'add_entry.html', {'form': form})

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                client = initialize_gspread()
                sheet = client.open("Sheet-Django").sheet1
                sheet.append_row([data['prenom'], data['telephone'], data['lieu_naissance'], data['Actue']])
                messages.success(request, 'Entry added successfully!')
                return redirect('index')
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        return render(request, 'add_entry.html', {'form': form})

class EditEntryView(View):
    def get(self, request, entry_id):
        client = initialize_gspread()
        sheet = client.open("Sheet-Django").sheet1
        row_data = sheet.row_values(entry_id)
        form = EntryForm(initial={
            'prenom': row_data[0],
            'telephone': row_data[1],
            'lieu_naissance': row_data[2],
            'Actue': row_data[3]
        })
        return render(request, 'edit_entry.html', {'form': form, 'entry_id': entry_id})

    def post(self, request, entry_id):
        form = EntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                client = initialize_gspread()
                sheet = client.open("Sheet-Django").sheet1
                sheet.update(f'A{entry_id}', [[data['prenom'], data['telephone'], data['lieu_naissance'], data['Actue']]])
                messages.success(request, 'Entry updated successfully!')
                return redirect('index')
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        return render(request, 'edit_entry.html', {'form': form, 'entry_id': entry_id})

class DeleteEntryView(View):
    def get(self, request, entry_id):
        try:
            client = initialize_gspread()
            sheet = client.open("Sheet-Django").sheet1
            sheet.delete_row(entry_id)
            messages.success(request, 'Entry deleted successfully!')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
        return redirect('index')
