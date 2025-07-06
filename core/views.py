import logging
from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client

twilio_number = 'whatsapp:+12565307557'
client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
logger = logging.getLogger('django')


def index(request):
    return render(request, 'index.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


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
