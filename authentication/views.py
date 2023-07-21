from django.shortcuts import render, redirect
from .firebase import authe, database

def login(request):
    if request.session.has_key('uid'):
        return render(request,"Home.html")
    if request.method=='POST':
        email=request.POST.get('email')
        pasw=request.POST.get('pass')
        try:
            user=authe.sign_in_with_email_and_password(email,pasw)
        except:
            message="Invalid Credentials!!Please ChecK your Data"
            return render(request,"Login.html",{"message":message})
        session_id=user['idToken']

        request.session['uid']=str(session_id)

        return redirect('home')

    return render(request,"Login.html")

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pasw=request.POST.get('pass')
        name=request.POST.get('name')
        try:
            user=authe.create_user_with_email_and_password(email,pasw)
            uid = user['localId']
            print(user)
            data={"name":name}
            database.child("users").child(uid).child('details').set(data)
        except Exception as e:
            print(e.args.__getitem__(1))
            # print(d)
            print(type(e))
            message="Unable to create account try again"
            return render(request,"Registration.html",{"message":message})
        return render(request,"Login.html")
    return render(request,"Registration.html")


def home(request):
    if not  request.session.has_key('uid'):
        return redirect('login')
    uid=request.session['uid']
    # name=database.child('users').child(uid).child('name').get()

    return render(request,"Home.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('home')
 

def reset(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            authe.send_password_reset_email(email)
            message  = "A email to reset password is successfully sent"
            return render(request, "Reset.html", {"msg":message})
        except:
            message  = "Something went wrong, Please check the email you provided is registered or not"
            return render(request, "Reset.html", {"msg":message})
    return render(request, "Reset.html")
 


