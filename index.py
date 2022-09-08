

from ast import Delete
from cProfile import label
from cgitb import text
from inspect import Parameter
from select import select
from tkinter import ttk
from tkinter import *

import sqlite3
from unicodedata import name
from unittest import result
from xml.dom.minidom import Element


class Product:
    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Aplicacion de productos')

        #name input
        frame = LabelFrame(self.wind, text= 'Registrar un nuevo producto')
        frame.grid(row= 0, column= 0, columnspan= 3, pady= 20)

        #name input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row= 1, column= 1)

        #Tabla precion
        Label(frame, text= 'Precio: ').grid(row= 2, column= 0)
        self.price = Entry(frame)
        self.price.grid(row= 2, column= 1)

        #Button add product
        ttk.Button(frame, text= 'Guardar Producto' ,command= self.add_product).grid(row= 3,columnspan=2, sticky= W + E)

        #salida de mensaje
        self.mensaje = Label(text= '', fg= 'red')
        self.mensaje.grid(row=3, column= 0, columnspan= 2, sticky= W + E )

        #table
        self.tree = ttk.Treeview(height= 10, columns= 2)
        self.tree.grid(row= 4, column= 0, columnspan= 2)
        self.tree.heading('#0', text= 'Nombre', anchor= CENTER)
        self.tree.heading('#1', text='Precio', anchor= CENTER)

        ttk.Button(text='BORRAR' , command= self.delete_product).grid(row= 5, column= 0, sticky= W + E)
        ttk.Button(text= 'EDITAR' , command= self.editar_producto).grid(row= 5, column= 1, sticky= W + E)

        self.get_products()

    def run_query(self, query, parameters = ()):

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit
        return result

    def get_products(self):
        #limpiendo tablas
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #filing data
        query = 'SELECT * FROM products ORDER BY name DESC'
        db_rows = self.run_query(query)

    
        for row in db_rows:
            self.tree.insert('', 0, text= row[1], values= row[2])

    def validacion(self):
        return len(self.name.get()) != 0 and len(self.price.get()) !=0

    def add_product(self):
        if self.validacion():
            query = 'INSERT INTO products VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.mensaje['text'] = 'products {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)

        else:
            self.mensaje['text'] = 'el nombre y el precio son requeridos'
        self.get_products()

    def delete_product(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Por favor selecciona un record'
            return
        self.mensaje['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM products WHERE name = ?'
        self.run_query(query, (name, ))
        self.mensaje['text'] = 'Record {} borrado satisfactoriamenta'.format(name)
        self.get_products()

    def editar_producto(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Porfavor seleciona un record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.editar_wind = Toplevel()
        self.editar_wind.title = 'Editar Producto'

        #editar nombre
        Label(self.editar_wind, text= ' Editar Nombre: ').grid(row= 0, column= 1)
        Entry(self.editar_wind, textvariable= StringVar(self.editar_wind, value= name), state= 'readonly').grid(row = 0, column = 2)
        #nuevo nombre
        Label(self.editar_wind, text= 'Nuevo nombre').grid(row= 1, column= 1)
        new_name = Entry(self.editar_wind)
        new_name.grid(row= 1, column= 2)

        #precio viejo
        Label(self.editar_wind, text= 'Precio viejo').grid(row= 2, column= 1)
        Entry(self.editar_wind, textvariable= StringVar(self.editar_wind, value= 'Precio viejo'), state= 'readonly').grid(row= 2, column= 2)
        #nuevo precio
        Label(self.editar_wind, text= 'Nuevo precio').grid(row= 3, column= 1)
        nuevo_precio = Entry(self.editar_wind)
        nuevo_precio.grid(row= 3, column= 2)
        Button(self.editar_wind, text='Update', command= lambda: self.editar_records(new_name.get(), name, nuevo_precio.get().old_price)).grid(row = 4, column=2, sticky= W)

    def editar_records(self, new_name, name, nuevo_precio, old_price):
        query = 'UPDATE products SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, nuevo_precio, name, old_price)
        self.run_query(query, parameters)
        self.editar_wind.destroy()
        self.mensaje['text'] = 'Records {} actualizado satisfactoriamente'.format(name)
        self.get_products()

if __name__=='__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
        