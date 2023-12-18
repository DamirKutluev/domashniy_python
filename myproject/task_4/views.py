from django.shortcuts import render



def multiplication_table(request, *args, **kwargs):
    data = []
    for i in range(1, 11):
        data_2 = []
        for j in range(1, 11):
            data_2.append(i*j)
        data.append(data_2)
    context = {
        'data': data
    }
    return render(request, 'task_4/index.html', context=context)


data = []
for i in range(1, 11):
    data_2 = []
    for j in range(1, 11):
        data_2.append(i*j)
    data.append(data_2)