from django.shortcuts import render
import os

def index(request):
    return render(request, 'index.html')

def convert(request):
    result = ''
    if request.method == 'POST':
        plain_text = request.POST.get('plain_text', '')

        # Convert plain text to smart HTML
        lines = plain_text.split('\n')
        html_output = ''
        for line in lines:
            line = line.strip()
            if not line:
                continue
            elif line.startswith('---') and line.endswith('---'):
                heading_text = line.strip('- ').strip()
                html_output += f"<h2>{heading_text}</h2>\n"
            else:
                html_output += f"<p>{line}</p>\n"

        # Save to file
        save_path = os.path.join('converter', 'static', 'converted.html')
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(html_output)

        return render(request, 'index.html', {'result': html_output})

    return render(request, 'index.html')
