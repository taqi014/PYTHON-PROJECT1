# SUPER CASHIER PACMANN - PROJECT PYTHON
## A. Latar Belakang 

Sebuah Supermarket "PACMANN" ingin mempermudah pelanggannya untuk melakukan transaksi pembelian, dengan begitu dirancanglah sebuah sistem kasir otomatis yang dapat digunakan oleh pelanggan. 


#### Tujuan Pengerjaan Project
- Membuat program 'Cashier' menggunakan Python.
- Menggunakan method function dan objek (OOP).
- Mengaplikasikan penulisan clean code (PEP 8).

## B. Objectives


| Name |Type| Input |  Output |  Note  |
| ------ | ------ | ------ | ------ | ------ |
| Transaction| Class | | |  |
| add_item()| Method |name_item : string, quantity_item : int, price_item : float| |  |
| check_item()| Method | | | Menampilkan Transaksi pembelian |
| upadate_item()| Method |update_item : string | |  |
| upadate_qty()| Method |update_qty : int | |  |
| upadate_price()| Method |update_price : float| |  |
| delete_item()| Method | | delete_item()| ketika menghapus item, jumlah dan harga juga terhapus |
| reset_item()| Method | |reset_item |  Menghapus semua item transaksi pembelian|
| total_price()| Method | | total_price : float| price Rp 200,000 disc 5%, price Rp 300,000 disc 8%, price Rp 500,000 disc 10%|


## C. Flow Chart
![Requirements Project I (1)](https://github.com/taqi014/Images/assets/138283551/46524d09-0274-48af-bcdd-56ed9a22a447)


#### Cara Menjalankan Program:
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Jalankan module python transaction.py di terminal.
3. Jalankan module python main.py di terminal.

## D. Hasil Test Case
1. Menggunakan menu fungsi add_item(), untuk menambahkan item pada cart
Input Item yang akan ditambahkan ke keranjang.

![Test Case1](https://github.com/taqi014/Images/assets/138283551/832e7f5e-f2d8-48d0-8b10-6f412a3c6c67)

2. Menggunakan menu fungsi delete_item(), untuk menghapus suatu item. 
Contoh: hapus item Pasta gigi.

![Test Case 2](https://github.com/taqi014/Images/assets/138283551/0fa0c7be-9098-4262-9cf6-8564f24d9df7)

3. Menghapus semua item pada cart, menggunakan menu fungsi reset_item().

![Test Case 3](https://github.com/taqi014/Images/assets/138283551/363644f6-7828-43fa-8d33-7868e933f581)

4. Menjumlahkan harga semua item pada cart, menggunakan menu fungsi total_price() setelah Input beberapa item ke keranjang.

![Test Case 4](https://github.com/taqi014/Images/assets/138283551/c6898092-14ea-4dbe-869d-994216ece711)


## E. Conclusion
1. Mengembangkan program salah satunya dengan cara menambahkan database untuk daftar barang(item) beserta harga.
2. Menampilkan pada list keranjang untuk total harga item yang sudah dikalikan dengan jumlah item.
