from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime, date
from django.utils import formats
from . forms import *
from . views import *



#HOMEPAGE OF THE PLATFORM
#Function to display the homepage of the Online Book Shopping Platform
def index(request):
    return render(request = request, template_name = 'home.html')



#CUSTOMER FUNCTIONS
#Customer Sign Up function
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # newUser = Customer()
            # newUser.user_id = form.cleaned_data.get('user_id')
            # newUser.email = form.cleaned_data.get('email')
            # newUser.password = form.cleaned_data.get('password')
            # newUser.first_name = form.cleaned_data.get('first_name')
            # newUser.middle_name = form.cleaned_data.get('middle_name')
            # newUser.last_name = form.cleaned_data.get('last_name')
            # newUser.phone_no = form.cleaned_data.get('phone_no')
            # newUser.save()

            #username = form.cleaned_data.get('user_id')
            #raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #messages.info(request, "Welcome to KGP")
            user_id = form.cleaned_data.get('user_id')
            userCount = Customer.objects.filter(user_id = user_id).count()

            if userCount == 0:
                form.save()
                username = form.cleaned_data.get('first_name')
                messages.info(request, "You have now signed up as {username}")
                return render(request, 'users/signUpSuccess.html', context={"form":form})               
                # return redirect('index')
            else:
                messages.error(request, "Invalid Form")
                return render(request, 'users/signUpFail.html', {})
        else:
            messages.error(request, "Invalid Form Details")
            return render(request, 'users/signUpFail.html', {})    
    else:
        form = SignupForm()

    return render(request, 'users/sign_up.html', {'form': form})




#Customer LogIn Function
def login(request):
    if request.method == "POST":
        print(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            #print(form);
            #return redirect('index');
            user_id = form.cleaned_data.get('user_id')
            raw_password = form.cleaned_data.get('password')
            
            cursor = connection.cursor()
            query_user_check = '''SELECT *
                                  FROM Customer
                                  WHERE user_id=%s AND password=%s'''
            cursor.execute(query_user_check, [user_id, raw_password])
            q_result = cursor.fetchall()
            userCount = len(q_result)

            
            # user = Customer.objects.filter(user_id = username, password = raw_password)
            if userCount == 1:
                messages.info(request, f"You are now logged in as {user_id}")
                request.session['user_id'] = request.POST['user_id']
                return redirect('userProfile')
            else:
                print("Invalid Form Input")
                messeags.error(request, "Invalid Username or Password")
                return render(request, 'users/logInFail.html', {})
        else:
            print("Invalid Form Input")
            messages.error(request, "Invalid USERNAME or PASSWORD")
            return render(request, 'users/logInFail.html', {})
    else:
        form = LoginForm()
        return render(request, "users/login.html", context= {"form":form})




#Customer Profile
def userProfile(request):
    if request.session.has_key('user_id'):
        posts = request.session['user_id']
        query = Customer.objects.filter(user_id = posts)
        return render(request, 'users/profile.html', {"query":query})
    else:
        redirect(request,'users/profile.html', {} )





def userLogout(request):
    try:
        del request.session['user_id']
    except :
        pass
    return redirect( 'index')




#Request contains serach parameter and user_id and returns the list of books
def userSearchResult(request):
    return HttpResponse("Searches are here\n")




#Returns books added by the particular user
def userCart(request):
    return HttpResponse("Cart Page for user")




#Request contains user_id and accordingly we will return the to read List 
def userReadList(request):
    return HttpResponse("Read List for User")




#Returns all the order made by the user
def userOrders(request):
    return HttpResponse("Orders by the user")




def userOrderComplain(request):
    return HttpResponse("Return Complain correspoding to this user and a given order")




def userBookReveiw(request):
    return HttpResponse("Helps in reviewing a book by user")




#Function to change the profile details of the users
def userChangePasswd(request):
    if request.method == "POST":
        form = userChangePasswdForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            user_id = request.session['user_id']
            user = Customer.objects.filter(user_id = user_id)[0]
            if user.password == old_password:
                user.password = new_password
                user.save()
                messages.info(request, "Password Changed Succesfully")
                return redirect('userProfile')
            else:
                messages.error(request, "Wrong Old Password")
        else:
            messages.error(request, "Invalid PASSWORD")
    else:
        form = userChangePasswdForm()
    return render(request, "users/change_password.html", context= {"form":form})













#STORE FUNCTIONS
#Store function for Store Sign Up
def storeSignUp(request):
    if request.method == "POST":
        form = StoreSignUp(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            storeCount = Book_store.objects.filter(email = email).count()
            if storeCount == 0:
                form.save()
                username = form.cleaned_data.get('store_name')
                messages.info(request, "You have now signed up as {username}")
                return render(request, 'store/signUpSuccess.html', context={"form":form})
                #return redirect('index')
            else:
                messages.error(request, 'Email Address already exists')
                return render(request, 'store/signUpFail.html', {})
        else:
            messages.error(request, "Invalid Form")
            return render(request, 'store/signUpFail.html', {})
    else:
        form = StoreSignUp()
    return render(request, 'store/storeSignUp.html', {"form":form})



#Store function for Store Log In
def storeLogin(request):
    if request.method == "POST":
        print("request received", request)
        form = storeLoginForm(request.POST)
        if form.is_valid():
            print("form received ", form);
            #return redirect('index');
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')

            cursor = connection.cursor()
            query = '''SELECT *
                       FROM Book_store
                       WHERE email=%s AND password=%s'''
            cursor.execute(query, [email, raw_password])
            q_result = cursor.fetchall()
            userCount = len(q_result)

            #userCount = Book_store.objects.filter(email = email, password = raw_password).count()
            #user = Book_store.objects.filter(email = email, password = raw_password)
            if userCount == 1:
                #print(user)
                messages.info(request, "You are now logged in with Email Id: {email}")
                #curr_store = Book_store.objects.filter(email = email, password = raw_password).first()
                request.session['email'] = request.POST['email']
                return redirect('storeProfile')
            else:
                print("Invalid Form")
                messages.error(request, "Invalid Email or Password")
                return render(request, 'store/logInFail.html', {})
        else:
            print("Invalid Form Input")
            messages.error(request, "Invalid Email or PASSWORD")
            return render(request, 'store/logInFail.html', {})
    else:
        form = storeLoginForm()
        return render(request, "store/storeLogin.html", context= {"form":form})




#Store function to display homepage of the Store
def storeProfile(request):
    if request.session.has_key('email'):
        posts = request.session['email']
        query = Book_store.objects.filter(email = posts)
        return render(request, 'store/storeProfile.html', {"query":query})
    else:
        redirect(request,'store/storeProfile.html', {} )




#Store function to Edit Store profile details
def storeEditProfile(request):
    if request.method == "POST":
        form = StoreProfile(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            store = Book_store.objects.filter(email = email)[0]
            store.website = form.cleaned_data.get('website')
            store.phone_no = form.cleaned_data.get('phone_no')
            store.rating = form.cleaned_data.get('rating')
            store.address_line1 = form.cleaned_data.get('address_line1')
            store.address_line2 = form.cleaned_data.get('address_line2')
            store.city = form.cleaned_data.get('city')
            store.state = form.cleaned_data.get('state')
            store.district = form.cleaned_data.get('district')
            store.zip_code = form.cleaned_data.get('zip_code')
            store.save()
            messages.info(request, "Profile Edited Sucesfully")
            return redirect('storeProfile')
        else:
            messages.error(request, "Invalid Form")
    else:
        store_id = request.session['email']
        store = Book_store.objects.filter(email = store_id)[0]
        fields = {'store_name':store.store_name, 'email':store.email, 'website':store.website,'phone_no':store.phone_no, 'rating':store.rating, 'address_line1':store.address_line1, 'address_line2':store.address_line2,
        'city':store.city, 'district':store.district, 'state':store.state, 'zip_code':store.zip_code}
        form = StoreProfile(initial=fields)
    return render(request, 'store/storeProfileEdit.html', {"form":form})




#Store function to change password
def storeChangePasswd(request):
    if request.method == "POST":
        form = storeChangePasswdForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            store_id = request.session['email']
            store = Book_store.objects.filter(email = store_id)[0]
            if store.password == old_password:
                store.password = new_password
                store.save()
                messages.info(request, "Password Changed Succesfully")
                return redirect('storeProfile')
            else:
                messages.error(request, "Wrong Old Password")
        else:
            messages.error(request, "Invalid PASSWORD")
    else:
        form = storeChangePasswdForm()
    return render(request, "store/change_password.html", context= {"form":form})





#Function to Logout the session
def storeLogout(request):
    try:
        del request.session['email']
    except :
        pass
    return redirect('index')




#Store Function to Add Book
# def storeBookAdd(request):
#     if request.method == "POST":
#         form = bookAddForm(request.POST)
#         if form.is_valid():
#             newUser = Book()
#             newUser.title = form.cleaned_data.get('title')
#             newUser.author = form.cleaned_data.get('author')
#             newUser.publisher = form.cleaned_data.get('publisher')
#             newUser.genre = form.cleaned_data.get('genre')
#             newUser.year_of_publish = form.cleaned_data.get('year_of_publish')
#             newUser.price = form.cleaned_data.get('price')
#             num_copies = form.cleaned_data.get('no_of_books')
#             this_book_count = Book.objects.filter(title = newUser.title, publisher = newUser.publisher).count()
#             if this_book_count == 0:
#                 newUser.copies_sold = 0
#                 newUser.save()
#                 bookAndStore = Book_available()
#                 bookAndStore.store_email = Book_store.objects.filter(email = request.session['email']).first()
#                 bookAndStore.book_id = newUser
#                 bookAndStore.no_of_copies = num_copies
#                 bookAndStore.save()
#             else:
#                 book_id = Book.objects.filter(title = newUser.title, publisher= newUser.publisher)[0].book_id
#                 store_email = Book_store.objects.filter(email = request.session['email']).first()
#                 myBook = Book_available.objects.get(book_id = book_id, store_email = store_email)
#                 myBook.no_of_copies = myBook.no_of_copies + num_copies
#                 myBook.save()
#         else:
#             messages.error(request, "Invalid Book Data Entered")
#     else:
#         addBookForm = bookAddForm()
#         return render(request, 'store/addBook.html',{"form":addBookForm})
    
#     if request.session.has_key('email'):
#         posts = request.session['email']
#         query = Book_store.objects.filter(email = posts)
#         return render(request, 'store/storeProfile.html', {"query":query})     
def storeBookAdd(request):
    if request.method == "POST":
        form = bookAddForm(request.POST)
        if form.is_valid():
            newUser = Book()
            newUser.title = form.cleaned_data.get('title')
            newUser.author = form.cleaned_data.get('author')
            newUser.publisher = form.cleaned_data.get('publisher')
            newUser.genre = form.cleaned_data.get('genre')
            newUser.year_of_publish = form.cleaned_data.get('year_of_publish')
            num_copies = form.cleaned_data.get('no_of_books')
            price = form.cleaned_data.get('price')
            this_book_count = Book.objects.filter(title = newUser.title, publisher = newUser.publisher).count()
            
            if this_book_count == 0:
                newUser.copies_sold = 0
                newUser.save()
                book_id_ = newUser.pk
                store_email_ = request.session['email']
                bookAndStore = Book_available()
                bookAndStore.store_email = Book_store.objects.filter(email = store_email_)[0]
                bookAndStore.book_id = Book.objects.filter(book_id = book_id_)[0]
                bookAndStore.price = form.cleaned_data.get('price')
                bookAndStore.no_of_copies = num_copies
                bookAndStore.save()
            else:
                book_id_ = Book.objects.filter(title = newUser.title, publisher= newUser.publisher)[0].book_id
                store_email_ = request.session['email']
                cnt = Book_available.objects.filter(book_id = book_id_, store_email = store_email_).count()
                if cnt == 0:
                    bookAndStore = Book_available()
                    bookAndStore.store_email = Book_store.objects.filter(email = store_email_)[0]
                    bookAndStore.book_id = Book.objects.filter(book_id = book_id_)[0]
                    bookAndStore.price = price
                    bookAndStore.no_of_copies = num_copies
                    bookAndStore.save()
                else :
                    myBook = Book_available.objects.filter(book_id = book_id_, store_email = store_email_)[0]
                    myBook.no_of_copies = myBook.no_of_copies + num_copies
                    myBook.price = price
                    myBook.save()
        else:
            messages.error(request, "Invalid Book Data Entered")
    else:
        addBookForm = bookAddForm()
        return render(request, 'store/addBook.html',{"form":addBookForm})
    
    if request.session.has_key('email'):
        posts = request.session['email']
        query = Book_store.objects.filter(email = posts)
        return render(request, 'store/storeProfile.html', {"query":query})     




#Store function to display the list of stock books in the store
def storeBookView(request):
    store_id = request.session['email']
    store = Book_store.objects.filter(email = store_id)[0]
    book_list = []
    books = Book_available.objects.filter(store_email = store_id)

    for b in books:
        book = Book.objects.filter(book_id = b.book_id.book_id)[0]
        book_list.append({'book':book, 'price':b.price, 'copies':b.no_of_copies})
    
    # cursor = connection.cursor()
    # query = '''SELECT Book.book_id, Book.title, Book.author, Book.publisher, Book.genre, Book.year_of_publish, Book.price, Book.copies_sold, Book.rating
    # FROM Book, Book_available WHERE Book_available.store_email = %s AND Book.book_id = Book_available.book_id'''
    # cursor.execute(query, [store_id])
    # book_list = cursor.fetchall()

    return render(request, 'store/book_list.html', {"book_list": book_list, "store":store})




#Store function to delete a book entry from the store
def storeBookDel(request, book_id):
    # cursor = connection.cursor()
    # query = '''DELETE FROM newApp_book_available WHERE book_id = %s;'''
    # cursor.execute(query, [book_id])
    Book_available.objects.filter(book_id = book_id).delete()

    return redirect('storeBookView')




#Store function to update book details
def storeUpdateBook(request, book_id):
    price = request.POST["price"]
    copies = request.POST["copies"]

    bookAndStore = Book_available.objects.filter(book_id = book_id)[0]
    bookAndStore.price = price
    bookAndStore.no_of_copies = copies
    bookAndStore.save()

    return redirect('storeBookView')
    # else:
    #     updateForm = updateBookForm()
    #     return render(request, 'store/updateBook.html',{"form":updateForm})
    
    # if request.session.has_key('email'):
    #     posts = request.session['email']
    #     query = Book_store.objects.filter(email = posts)
    #     return render(request, 'store/storeProfile.html', {"query":query})     





#Shows the Options to see the three different types of order list
def storeOrderList(request):
    if sessionCheck(request) == True:
        email = request.session['email']
        
        cursor = connection.cursor()
        query = '''SELECT *
                   FROM Book_store
                   WHERE email=%s'''

        cursor.execute(query, [email])
        q_result_store = cursor.fetchone()
        
        q_result = {}
        q_result['email'] = email
        q_result['store_name'] = q_result_store[1]
        print(q_result_store)

        return render(request, 'store/storeOrders.html', {'q_result' : q_result})
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to display the order list of the store
def deliveredOrder(request):
    if sessionCheck(request) == True:
        email = request.session['email']
        store_row = fetchStoreRow(email)                                        #1. Store details from the session
        store_id = store_row[0]                                                 #Store ID 
        store_name = store_row[1]                                               #Store name extracted
        
        status = "Delivered"                                                    #2. Status to be searched

        # cursor = connection.cursor()
        # query = '''SELECT *
        #            FROM Order 
        #            WHERE store_id.pk=%d AND status=%s'''
        # cursor.execute(query, [store_id, status])
        # q_result = cursor.fetchall()

        
        q_result = Order.objects.filter(store_id = store_id, status = status)   #3. Selecting all the rows from the Order table with the given store_id and status
        return render(request, 'store/deliveredOrders.html', {'store_email': email, 'store_name' : store_name,  'q_result' : q_result})
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to display the order list of the store
def inProcessOrder(request):
    if sessionCheck(request) == True:
        email = request.session['email']
        store_row = fetchStoreRow(email)                                        #1. Store details from the session
        store_id = store_row[0]                                                 #Store ID 
        store_name = store_row[1]                                               #Store name extracted
        
        status = "Processing"                                                    #2. Status to be searched

        # cursor = connection.cursor()
        # query = '''SELECT *
        #            FROM Order 
        #            WHERE store_id.pk=%d AND status=%s'''
        # cursor.execute(query, [store_id, status])
        # q_result = cursor.fetchall()

        
        q_result = Order.objects.filter(store_id = store_id, status = status)   #3. Selecting all the rows from the Order table with the given store_id and status
        return render(request, 'store/processingOrder.html', {'store_email': email, 'store_name' : store_name,  'q_result' : q_result})
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to display the order list of the store
def cancelledOrder(request):
    if sessionCheck(request) == True:
        email = request.session['email']
        store_row = fetchStoreRow(email)                                        #1. Store details from the session
        store_id = store_row[0]                                                 #Store ID 
        store_name = store_row[1]                                               #Store name extracted
        
        status = "Cancelled"                                                    #2. Status to be searched

        # cursor = connection.cursor()
        # query = '''SELECT *
        #            FROM Order 
        #            WHERE store_id.pk=%d AND status=%s'''
        # cursor.execute(query, [store_id, status])
        # q_result = cursor.fetchall()

        
        q_result = Order.objects.filter(store_id = store_id, status = status)   #3. Selecting all the rows from the Order table with the given store_id and status
        return render(request, 'store/cancelledOrder.html', {'store_email': email, 'store_name' : store_name,  'q_result' : q_result})
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to set the delivered date
def setDelivered(request, order_id):
    if sessionCheck(request) == True:
        form = DateInputForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            
            email = request.session['email']
            store_row = fetchStoreRow(email)                                        #1. Store details from the session
            store_id = store_row[0]                                                 #Store ID 
            store_name = store_row[1]                                               #Store name extracted

            q_result_order = Order.objects.get(store_id = store_id, order_id = order_id)                #2. Fetching the given order by order_id

            q_result_order.delivered_date = date
            q_result_order.status = "Delivered"
            q_result_order.save()
            return redirect('inProcessOrder')
        else:
            messages.error(request, "Invalid Book Data Entered")
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to set the expected delivery date
def setExpectedDeliveryDate(request, order_id):
    if sessionCheck(request) == True:
        form = DateInputForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')

            email = request.session['email']
            store_row = fetchStoreRow(email)                                        #1. Store details from the session
            store_id = store_row[0]                                                 #Store ID 
            store_name = store_row[1]                                               #Store name extracted


            q_result_order = Order.objects.get(store_id = store_id, order_id = order_id)                #2. Fetching the given order by order_id

            q_result_order.expected_delivery_date = date
            q_result_order.save()
            return redirect('inProcessOrder')
        else:
            messages.error(request, "Invalid Book Data Entered")
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store function to set the order as processing
def setProcessing(request, order_id):
    if sessionCheck(request) == True:            
            email = request.session['email']
            store_row = fetchStoreRow(email)                                        #1. Store details from the session
            store_id = store_row[0]                                                 #Store ID 
            store_name = store_row[1]                                               #Store name extracted

            q_result_order = Order.objects.get(store_id = store_id, order_id = order_id)                #2. Fetching the given order by order_id

            old_status = q_result_order.status
            q_result_order.delivered_date = None
            q_result_order.cancelled_date = None
            q_result_order.status = "Processing"
            q_result_order.save()
            if old_status == "Delivered":
                return redirect('deliveredOrder')
            elif old_status == "Cancelled":
                return redirect('cancelledOrder')
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Function to set the order as cancelled
def setCancelled(request, order_id):
    if sessionCheck(request) == True:
        form = TextInputForm(request.POST)
        if form.is_valid():
            remarks = form.cleaned_data.get('text')

            email = request.session['email']
            store_row = fetchStoreRow(email)                                        #1. Store details from the session
            store_id = store_row[0]                                                 #Store ID 
            store_name = store_row[1]                                               #Store name extracted


            q_result_order = Order.objects.get(store_id = store_id, order_id = order_id)                #2. Fetching the given order by order_id

            q_result_order.delivered_date = None
            q_result_order.cancelled_date = None
            q_result_order.status = "Cancelled"
            q_result_order.cancelled_date = date.today()
            q_result_order.cancelled_by = "Store"
            q_result_order.cancellation_remarks = remarks 


            q_result_order.save()
            return redirect('inProcessOrder')
        else:
            messages.error(request, "Invalid Book Data Entered")
    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Store Function to display the details of all the orders
def orderDetails(request, order_id):
    if sessionCheck(request) == True:
        email = request.session['email']
        store_row = fetchStoreRow(email)                                        #1. Store details from the session
        store_id = store_row[0]                                                 #Store ID 
        store_name = store_row[1]                                               #Store name extracted

        
        q_result_order = Order.objects.get(store_id = store_id, order_id = order_id)                #2. Fetching the given order by order_id


        cursor = connection.cursor()                                                                #3. Fetching all the books in the order with id order_id
        # query1 = '''SELECT *
        #             FROM Book_ordered
        #             WHERE order_id =%s'''
        # cursor.execute(query1, [order_id])
        # q_result_bk_ids = cursor.fetchall()
        q_result_bk_ids = Book_ordered.objects.filter(order_id = order_id)                      

        
        address = Customer_address.objects.get(user_id = q_result_order.user_id, address_no = q_result_order.address_no)    #4. Fetching the address where to be sent

        q_result_final = []                                                                                         #List of book and their details                         
        q_result = []                                                                                               #List of books

        for bk_id in q_result_bk_ids:                                                                               #5. Creating a list of books to be sent for html rendering
            instance = {} 

            #books_fetch = Book.objects.get(book_id = bk_id.book_id.pk)                                             #Book entry fetched from the table
            query_fetch_book = '''SELECT *
                                  FROM Book
                                  WHERE book_id=%s'''                                                               #Book id with its details
            cursor.execute(query_fetch_book, [bk_id.book_id.pk])
            books_fetch = cursor.fetchone()

            
            book_avail_price = Book_available.objects.get(book_id = bk_id.book_id.pk, store_email = email)        #Price entry from the Book_available table            
            # query_fetch_price = '''SELECT *
            #                        FROM Book_available
            #                        WHERE book_id=%s AND store_email=%s'''
            # cursor.execute(query_fetch_price, [bk_id.book_id.pk, email])
            # book_avail_price = cursor.fetchone()


            # instance['id'] = books_fetch.book_id
            # instance['title'] = books_fetch.title
            # instance['author'] = books_fetch.author
            instance['id'] = books_fetch[0]
            instance['title'] = books_fetch[1]
            instance['author'] = books_fetch[2]
            instance['price'] = book_avail_price.price
            instance['copies'] = bk_id.no_of_copies


            q_result_final.append(instance)
            q_result.append(books_fetch)

        if q_result_order.status == "Delivered":
            return  render(request, 'store/deliveredOrderDetails.html', {'store_email': email, 'store_name' : store_name, 'q_result_order' : q_result_order, 'books' : q_result, 'copies' : q_result_final , 'address' : address})
        elif q_result_order.status == "Processing":
            form1 = DateInputForm()
            form2 = TextInputForm()
            return  render(request, 'store/processingOrderDetails.html', {'dateform1' : form1, 'dateform2' : form1, 'textform' : form2, 'store_email': email, 'store_name' : store_name, 'q_result_order' : q_result_order, 'books' : q_result, 'copies' : q_result_final , 'address' : address})            
        elif q_result_order.status == "Cancelled":
            return  render(request, 'store/cancelledOrderDetails.html', {'store_email': email, 'store_name' : store_name, 'q_result_order' : q_result_order, 'books' : q_result, 'copies' : q_result_final , 'address' : address})            

    else:
        messages.error(request, "Invalid Form")
        return render(request, 'store/signUpFail.html', {})




#Extract data from order schema and returns books according to status 
def storeSalesList(request):
    return HttpResponse("Return Sales List")





#Uses user_id and store_id 
def storeUserList(request):
    store_id = request.session['email']
    store = Book_store.objects.filter(email = store_id)[0]
    u_list = []
    users = user_list.objects.filter(store_email = store_id)

    for u in users:
        user = Customer.objects.filter(user_id = u.user_id.user_id)[0]
        u_list.append(user)
    
    return render(request, 'store/user_list.html', {"user_list": u_list, "store":store})




def storeUserAddress(request, user_id):
    address = Customer_address.objects.filter(user_id = user_id, is_primary = True)[0]
    user = Customer.objects.filter(user_id = user_id)[0]
    return render(request, 'store/user_address.html', {'address':address, 'user':user})




# Function to check if the HTTP request is on session
def sessionCheck(request):
    email = request.session['email']
    cursor = connection.cursor()
    query = '''SELECT *
               FROM Book_store
               WHERE email=%s'''

    cursor.execute(query, [email])
    q_result = cursor.fetchall()
    userCount = len(q_result)
    if userCount == 1:
        return True
    else:
        return False




#Function to fetch the row of the store table
def fetchStoreRow(email):
    cursor = connection.cursor()
    query = '''SELECT *
               FROM Book_store
               WHERE email=%s'''

    cursor.execute(query, [email])
    q_result = cursor.fetchone()
    #store_row = q_result[0]
    return q_result




#Independent of Store and User
def storeTrendingList(request):
    t_list = Book.objects.all().order_by('-copies_sold')[:10]

    return render(request, 'store/trending_list.html', {"t_list": t_list})

def userTrendingList(request):
    t_list = Book.objects.all().order_by('-copies_sold')[:10]

    return render(request, 'users/trending_list.html', {"t_list": t_list})




