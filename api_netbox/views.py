from django.shortcuts import render, redirect
from .forms import NetboxForm
from .models import Netbox
from django.urls import reverse
from django.views.generic.edit import DeleteView



class NetboxDeleteView(DeleteView):
    model = Netbox
    template_name = 'netbox_confirm_delete.html'

    def get_success_url(self):
        return reverse('netbox_list')


def netbox_create(request):
    if request.method == 'POST':
        form = NetboxForm(request.POST)
        if form.is_valid():
            # Save the main fields from the form
            hostname = form.cleaned_data['hostname']
            username = form.cleaned_data['username']
            pod_count = form.cleaned_data['pod_count']

            # Extract pod data from request.POST
            pods = []
            for i in range(1, pod_count + 1):
                pod_name = request.POST.get('pod_{}'.format(i))
                if pod_name:
                    pods.append(pod_name)

            # Create or update the Netbox instance
            netbox = Netbox.objects.create(
                hostname=hostname,
                username=username,
                pod_count=pod_count,
                pods=pods
            )

            return redirect('netbox_list')
    else:
        form = NetboxForm()
    return render(request, 'netbox_form.html', {'form': form})

def netbox_update(request, pk):
    netbox = Netbox.objects.get(pk=pk)
    if request.method == 'POST':
        form = NetboxForm(request.POST, instance=netbox)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace 'success_url' with the URL you want to redirect to after form submission
    else:
        form = NetboxForm(instance=netbox)
    return render(request, 'netbox_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def netbox_list(request):
    netboxes = Netbox.objects.all()
    return render(request, 'netbox_list.html', {'netboxes': netboxes})
