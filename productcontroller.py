from flask import Flask,request,render_template
from configuration import app


@app.route('/')
@app.route('/product/index',methods=['GET'])
def ecom_app_landing_page():
    return render_template('index1.html')

productList = []
from product_info import Product
@app.route('/product/save',methods=['GET','POST'])
def save_update_product():
    message = ''
    if request.method=='POST':
        formdata = request.form
        pid = int(formdata.get('pid'))
        isDuplicate = False
        for prod in productList:
            if prod.prodId == pid:
                prod.prodName = formdata.get('pnm')
                prod.prodQty = int(formdata.get('pqty'))
                prod.prodPrice = float(formdata.get('pprc'))
                prod.prodVendor = formdata.get('pven')

                isDuplicate = True
                break
        if isDuplicate:
            message = "Product Successfully Update..."

        else:
            product = Product(pid=formdata.get('pid'),
                    prnm=formdata.get('pnm'),
                    pqty=formdata.get('pqty'),
                    prc=formdata.get('pprc'),
                    pven=formdata.get('pven'))
            productList.append(product)
            message = "Product Successfully Added...!"
    return render_template('add_update_product.html',
                           message=message,
                           product = Product())

@app.route('/product/delete/<int:pid>')
def delete_product(pid):
    for prod in productList:
        if prod.prodId == pid:
            productList.remove(prod)
            # message = "Product Successfully Removed...!"
            break
    return render_template('show_products.html',
                           prodList=productList)

@app.route('/product/edit/<int:pid>',methods=['GET'])
def edit_product(pid):
    product = None
    for prod in productList:
        if prod.prodId == pid:
            product = prod
    return render_template('add_update_product.html',
                           product = product)

@app.route('/product/list',methods=['GET'])
def show_all_products():
    return render_template('show_products.html',
                           prodList = productList)

@app.route('/product/search',methods=['GET','POST'])
def search_products():
    if request.method == "POST":
        formdata = request.form
        pid = int(formdata.get('pid'))
        for prod in productList:
            if prod.prodId == pid:
                return render_template('search_product.html',product=prod)

    return render_template('search_product.html',product = None)

@app.route('/sample')
def dummy_method():
    return "hi.."

if __name__ == '__main__':
    app.run(debug=True)