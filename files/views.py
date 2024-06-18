from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from files.models import File


def index(request):
    latest_files_list = File.objects.order_by("-uploaded_at")[:5]

    context = {
        "latest_files_list": latest_files_list,
    }

    return render(request, "files/index.html", context)


def detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)

    context = {
        "file": file,
    }

    return render(request, "files/detail.html", context)


def upload(request):
    uploaded_file = request.FILES["file"]

    file = File(uploaded_at=timezone.now(), file=uploaded_file)
    file.save()

    send_mail(
        "New upload.",
        f"File {uploaded_file.name} with size {uploaded_file.size} has been uploaded.",
        "noreply@example.com",
        ["guest@example.com"],
        fail_silently=False,
    )

    return redirect("files:detail", file_id=file.id)
