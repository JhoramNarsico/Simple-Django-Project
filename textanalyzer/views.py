from django.shortcuts import render

def home(request):
    """Renders the input form."""
    return render(request, 'home.html')

def analyze(request):
    """Processes the text and renders the result."""
    # Get the text from the form (default to empty string if not found)
    djtext = request.POST.get('text', 'default')
    
    # Get checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    countwords = request.POST.get('countwords', 'off')

    analyzed_text = djtext
    operations = []

    # Logic: Remove Punctuation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp_str = ""
        for char in analyzed_text:
            if char not in punctuations:
                temp_str += char
        analyzed_text = temp_str
        operations.append("Removed Punctuation")

    # Logic: Capitalize
    if fullcaps == "on":
        analyzed_text = analyzed_text.upper()
        operations.append("Changed to Uppercase")

    # Logic: Word Count (Calculated separately)
    word_count = len(analyzed_text.split()) if countwords == "on" else None

    # Prepare data to send to template
    params = {
        'purpose': ', '.join(operations),
        'analyzed_text': analyzed_text,
        'word_count': word_count
    }

    return render(request, 'analyze.html', params)