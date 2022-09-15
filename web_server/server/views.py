from django.shortcuts import render, redirect
from django.contrib import messages
from json2html import *
from django.utils.safestring import mark_safe
from server.forms import *
import json
import os
import shutil


def start(request):
    return redirect('/homePage?')


def home_page(request):
    clear_messages(request)
    return render(request, 'base.html', {})


def system_data(request):
    clear_messages(request)
    if os.path.exists('./database/system_data.json'):
        with open('./web_server/system_data_beginning.html') as html_file:
            data = html_file.read()
        while True:
            try:
                with open('./database/system_data.json') as json_file:
                    data += '\t\t' + json2html.convert(json=json.load(json_file))
                    break
            except json.decoder.JSONDecodeError:
                pass
        with open('./web_server/system_data_end.html') as html_file:
            data += html_file.read()
        with open('./database/system_data.html', 'w') as html_file:
            html_file.write(data)
        return render(request, 'system_data.html', {})
    else:
        return render(request, 'system_data_not_found.html', {})


def fillForm1(request):
    clear_messages(request)
    if request.method == 'POST':
        form = Form_1(request.POST)
        if form.is_valid():
            message = form.cleaned_data['name']
            category = form.cleaned_data['category']
            send_command('f1 ' + message + ' ' + category)
            messages.info(request, 'Form is sent.')
            return redirect('/homePage?')
        else:
            messages.info(request, 'Form is invalid!')
            return redirect('/homePage?')
    else:
        return render(request, 'form_1.html', {'form': Form_1})


def button4(request):
    clear_messages(request)
    messages.info(request, 'Form is cancelled')
    return redirect('/homePage?')


def fillForm2(request):
    clear_messages(request)
    if request.method == 'POST':
        form = Form_2(request.POST)
        if form.is_valid():
            char = form.cleaned_data['name']
            category = form.cleaned_data['category']
            send_command('f2 ' + char + ' ' + category)
            messages.info(request, 'Form sent.')
            return redirect('/homePage?')
        else:
            messages.info(request, 'Form is invalid!')
            return redirect('/homePage?')
    else:
        return render(request, 'form_2.html', {'form': Form_2})


def button1(request):
    clear_messages(request)
    send_command('1')
    messages.info(request, 'Button 1 pressed.')
    return redirect('/homePage?')


def button2(request):
    clear_messages(request)
    send_command('2')
    messages.info(request, 'Button 2 pressed.')
    return redirect('/homePage?')


def button3(request):
    clear_messages(request)
    send_command('3')
    messages.info(request, 'Button 3 pressed.')
    return redirect('/homePage?')


def reset_system(request):
    clear_messages(request)
    with open('./database/command.txt', 'w') as command_file:
        command_file.write('r')
    messages.info(request, 'The system is reset successfully!')
    check_arrival()
    return redirect('/homePage?')


def clear_messages(request):
    system_messages = messages.get_messages(request)
    for _ in system_messages:
        pass
    system_messages.used = True


def send_command(message):
    while True:
        try:
            with open('./database/command.txt', 'w') as command_file:
                command_file.write(message)
                break
        except PermissionError:
            pass
    check_arrival()


def check_arrival():
    while True:
        with open('./database/command.txt') as command_file:
            if len(command_file.read()) == 0:
                break

