#Django
from django.http import HttpResponse

#utiities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    # return HttpResponse('Hello, world')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def hi(request):
    # print('Esto es e request:',request)
    # import pdb; pdb.set_trace()
    return HttpResponse('Hi!')

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = request.GET['numbers']
    #return HttpResponse(str(numbers))
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)

