# Import library yang digunakan dalam transaction.py
from tabulate import tabulate

cart = []
class Transaction:

  """Kelas ini berisi objek untuk menampilkan dan melakukan 
  sebuah transaksi di Supermarket.

  """
  
  def __init__(self, name_item, quantity_item, price_item):
    '''Menginisiasi semua atribut yang diperlukan untuk objek kelas.'''
    self.name_item = list()
    self.quantity_item = list()
    self.price_item = list()

  def add_item(self):
    '''Fungsi untuk menambahkan item list pada keranjang.'''
    while True:
      try:
        name_item = input('masukkan item : ')
        quantity_item = int(input('masukkan jumlah item : '))
        price_item = float(input('masukkan harga item : '))
        cart_new = [name_item, quantity_item, price_item]
        cart.append(cart_new)
        notif = input('apakah anda mau lanjutkan belanja? (y/n): ')
        print('\n')
        if notif == 'y' and 'Y':
          continue
        else:
          break
      except:
        print("\nTerjadi kesalahan. Periksa kembali input Anda.")

  def check_item(self):
    '''Fungsi untuk mengecek item pada keranjang.'''
    print(tabulate(cart, headers=["item","quantity", "price"]))

  def update_item(self):
    '''Fungsi untuk mengganti item pada keranjang.'''
    item = int(input('ganti item pada indeks ke- '))
    new_item = str(input('ganti item menjadi: '))
    cart[item][0] = new_item

  def update_quantity(self):
    '''fungsi untuk mengganti jumlah item pada keranjang.'''
    qty = int(input('Ganti jumlah pada indeks ke- '))
    new_qty = int(input('ganti jumlah menjadi: '))
    cart[qty][1] = new_qty

  def update_price(self):
    '''Fungsi untuk mengganti harga item pada keranjang.'''
    price = int(input('\nGanti harga pada indeks ke- '))
    new_price= float(input('ganti harga menjadi: \n'))
    cart[price][2] = new_price

  def delete_item(self):
    '''
    Fungsi untuk menghapus item pada keranjang beserta
    jumlah dan harganya.
    '''
    barang = int(input('Hapus item pada indeks ke- \n'))
    del cart[barang]

  def reset(self):
    '''
    Fungsi untuk menghapus seluruh item pada keranjang
    beserta jumlah dan harganya.
    '''
    cart.clear()

  def total_price(self):
    '''Fungsi untuk menjumlahkan total harga semua item pada keranjang.'''
    cart_update = cart.copy()
    sub_total = 0
    for key, y,z in cart_update :
      total = (y*z)
      sub_total += total
    if sub_total >= 500_000:
      total_bayar = sub_total - (sub_total*0.1)
      print(f'Total belanja anda Rp. {sub_total:,}, selamat anda mendapatkan disc 10%')
    elif sub_total >= 300_000:
      total_bayar = sub_total - (sub_total*0.08)
      print(f'Total belanja anda Rp. {sub_total:,}, selamat anda mendapatkan disc 8%')
    elif sub_total >= 200_000:
      total_bayar = sub_total - (sub_total*0.05)
      print(f'Total belanja anda Rp. {sub_total:,}, selamat anda mendapatkan disc %')

    print(f'Total harga yang harus anda bayarkan adalah Rp {total_bayar:,}')