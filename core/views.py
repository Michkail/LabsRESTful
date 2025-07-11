import os
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from features.user.models import ContactMessage
# from twilio.rest import Client

load_dotenv()

twilio_number = 'whatsapp:+12565307557'
# client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
logger = logging.getLogger('django')


def index(request):
    return render(request, 'index.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


@csrf_exempt
def send_email_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        sender_email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        full_name = f"{first_name} {last_name}"
        subject = f"From {full_name}"
        body = f"""Message form:\n\nName: {full_name}\nEmail: {sender_email}\n\nMessage:\n{message}""".strip()

        try:
            validate_email(sender_email)

        except ValidationError:
            return JsonResponse({'success': False, 'error': 'Invalid email'}, status=400)

        status = 'sent'
        error_message = ''

        try:
            email = EmailMessage(subject=subject,
                                 body=body,
                                 from_email=os.getenv('DEFAULT_FROM_EMAIL'),
                                 to=[os.getenv('RECIPIENT')],
                                 reply_to=[sender_email])
            email.send()

        except Exception as e:
            status = 'failed'
            error_message = str(e)

        ContactMessage.objects.create(full_name=full_name,
                                      email=sender_email,
                                      message=message,
                                      status=status,
                                      error_message=error_message)

        return JsonResponse({'success': status == 'sent'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)



def elys_index(request):
    # if request.method == 'POST':
    # 	answer = request.POST.get('answer')
    # 	message_body = f"The answer is: {answer}"
    #
    # 	message = client.messages.create(
    # 		body=message_body,
    # 		from_=twilio_number,
    # 		to='whatsapp:+628970982297',
    # 	)
    #
    # 	return JsonResponse({"message": "Message sent", "status": message.status})

    if request.method == 'POST':
        answer = request.POST.get('answer')
        logger.info(f"->> Received answer: {answer}")

        return redirect("elys-thanks")

    return render(request, "elysabeth/index.html")


def elys_activities(request):
    selected_activities = request.POST.getlist('activities')

    if selected_activities:
        activities_choices = ', '.join(selected_activities)
        logger.info(f"->> User selected the following activities: {activities_choices}")

    else:
        logger.info("->> No activities selected by the user.")

        return redirect("elys-last")

    return render(request, "elysabeth/activities.html")


def elys_date(request):
    if request.method == "POST":
        answer = request.POST.get('answer')
        logger.info(f"->> Date on: {answer}")

        return redirect("elys-food")

    return render(request, "elysabeth/date.html")


def elys_dessert(request):
    selected_dessert = request.POST.getlist('dessert')

    if selected_dessert:
        dessert_choices = ', '.join(selected_dessert)
        logger.info(f"->> User selected the following dessert: {dessert_choices}")

    else:
        logger.info("->> No dessert selected by the user.")

        return redirect("elys-activities")

    return render(request, "elysabeth/dessert.html")


def elys_food(request):
    if request.method == "POST":
        selected_food = request.POST.getlist('food')

        if selected_food:
            food_choices = ', '.join(selected_food)
            logger.info(f"->> User selected the following food: {food_choices}")

        else:
            logger.info("->> No food selected by the user.")

        return redirect("elys-dessert")

    return render(request, "elysabeth/food.html")


def elys_last_page(request):
    return render(request, "elysabeth/lastpage.html")


def elys_thankyou(request):
    return render(request, "elysabeth/thankyou.html")
