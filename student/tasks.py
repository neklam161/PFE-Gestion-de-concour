from celery import shared_task, Task
from .models import attente,concours
from django.utils import timezone
from datetime import datetime


@shared_task
def set_status():
    if datetime.now().hour == 0 and datetime.now().minute == 0:
        list_concours = concours.objects.all()
        for concour in list_concours:
            if concour.end_date > timezone.now().date() :
                concour_participants = attente.objects.filter(concour = concour)
                admis_places = concour_participants.order_by('classement') 
                for etudiant in admis_places:
                    etudiant.status = "A"
                refus_places = concour_participants.order_by('classement')[concour.n_place:]
                for etudiant in refus_places:
                    etudiant.status = "R"
        