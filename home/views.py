import subprocess

from django.shortcuts import render
from .forms import CreateNewList
from django.http import HttpResponse
from django.http import HttpResponseRedirect

info = [0, 0]


# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def create(request):
    if request.method == "POST":
        info[0] = request.POST['nodeID']
        info[1] = request.POST['mtn']

        print(info[0], info[1])
        cmd = "./out/host/chip-tool pairing code " + str(info[0]) + " MT:" + str(info[1])
        subprocess.run(cmd, shell=True, cwd="../workspace/connectedhomeip")


        return HttpResponse("Successfully Paired")
    
def on(request):
    if request.method == "POST":

        print("turning on")
        cmd = "./out/host/chip-tool onoff on " + str(info[0]) + " 1"
        output = subprocess.check_output(cmd, shell=True, cwd="../workspace/connectedhomeip")
        print(cmd)


        return HttpResponse("Successfully Paired")
    
def read(request):
    if request.method == "POST":
        cmd = "./out/host/chip-tool onoff read on-off " + str(info[0]) + " 1"
        subprocess.run(cmd, shell=True, cwd="../workspace/connectedhomeip")
        print(cmd)


        return HttpResponse("Successfully Paired")
    
def write(request):
    if request.method == "POST":
        cmd = "./out/host/chip-tool onoff write on-time 1 " + str(info[0]) + " 1"
        subprocess.run(cmd, shell=True, cwd="../workspace/connectedhomeip")


        return HttpResponse("Successfully Paired")