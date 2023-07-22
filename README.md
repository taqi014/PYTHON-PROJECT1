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
![Objectives](https://github.com/taqi014/PYTHON-PROJECT1/assets/138283551/67bd93cb-f4e9-47fc-accc-542e28337656)


#### Cara Menjalankan Program:
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Jalankan module python transaction.py di terminal.
3. Jalankan module python main.py di terminal.

## D. Hasil Test Case
1. Menggunakan menu fungsi add_item(), untuk menambahkan item pada cart
Input Item yang akan ditambahkan ke keranjang.

![Test Case1](https://github.com/taqi014/PYTHON-PROJECT1/assets/138283551/d2fb2909-b8e8-4caa-97b2-6421b759840a)


2. Menggunakan menu fungsi delete_item(), untuk menghapus suatu item. 
Contoh: hapus item Pasta gigi.

![Test Case 2](https://github.com/taqi014/PYTHON-PROJECT1/assets/138283551/74ed27b5-f91c-4ab2-b076-145f8888e2e5)

3. Menghapus semua item pada cart, menggunakan menu fungsi reset_item().

![Test Case 3](https://github.com/taqi014/PYTHON-PROJECT1/assets/138283551/1a6c47cb-1fa3-4c43-8507-cc1a3589f8bb)

4. Menjumlahkan harga semua item pada cart, menggunakan menu fungsi total_price() setelah Input beberapa item ke keranjang.

![Test Case 4](https://github.com/taqi014/PYTHON-PROJECT1/assets/138283551/f0670899-3b6b-42c3-b1f4-0614b8545eca)

## E. Conclusion
1. Mengembangkan program salah satunya dengan cara menambahkan database untuk daftar barang(item) beserta harga.
2. Menampilkan pada list keranjang untuk total harga item yang sudah dikalikan dengan jumlah item.
