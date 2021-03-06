from django.shortcuts import render

from message_form.models import Message

def message_form(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message_text = request.POST.get('message')

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()

        return render(request, 'message_form.html', {
                "message": message
            })
    
    if request.method == 'GET':
        var_dict = {}
        all_messages = Message.objects.all()
        if all_messages:
            message = all_messages[0]
            var_dict =  {
                "message": message
            }
        return render(request, "message_form.html", var_dict)

   
