# Import library yang digunakan dalam main.py
from transaction import Transaction

cart = []
def menu():
    """Fungsi untuk menampilkan daftar pilihan tugas.
    """
    print("-"*50)
    print("SELAMAT DATANG DI SUPERCASHIER PACMANN")
    print("-"*50)
    print("1. Menambahkan Transaksi ke Keranjang")
    print("2. Mengganti Item pada Keranjang")
    print("3. Mengganti Jumlah Item pada Keranjang")
    print("4. Mengganti Harga pada Keranjang")
    print("5. Menghapus Item pada Keranjang")
    print("6. Menghapus Semua Item pada Keranjang")
    print("7. Menampilkan Harga Transaksi Pembayaran")
    print("8. Exit\n")

    no_menu = int(input('Masukkan Nomor Menu : '))

    try:
      if no_menu == 1:
        Transaction.add_item(cart)
        Transaction.check_item(cart)
        menu()
      elif no_menu == 2:
        Transaction.update_item(cart)
        Transaction.check_item(cart)
        menu()
      elif no_menu == 3:
        Transaction.update_quantity(cart)
        Transaction.check_item(cart)
        menu()
      elif no_menu == 4:
        Transaction.update_price(cart)
        Transaction.check_item(cart)
      elif no_menu == 5:
        Transaction.delete_item(cart)
        Transaction.check_item(cart)
        menu()
      elif no_menu == 6:
        Transaction.reset(cart)
        Transaction.check_item(cart)
        menu()
      elif no_menu == 7:
        Transaction.total_price(cart)
      elif no_menu == 8:
        print("*"*55)
        print("Terima kasih telah berbelanja di Supercashier Pacmann.")
        print("*"*55)
        pass
      else:
        print("Input Anda Salah.\n")
        menu()
    except:
        print("Input Anda salah.\n")
        menu()

menu()