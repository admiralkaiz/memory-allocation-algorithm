# Tugas Besar Strategi Algoritma: Alokasi Memori dengan Solusi _Brute Force_ dan _Greedy Algorithm_

## Latar Belakang

Memori komputer adalah tempat di mana sistem komputer menyimpan data program sementara pada saat eksekusi program berlangsung. Setelah selesai menjalankan program, maka data program akan dilepaskan dari memori. Setelah melepaskan data tersebut, terdapat kemungkinan terbentuknya "lubang" ruang kosong ditengah-tengah blok memori yang masih ditempati data program. Maka dari itu, untuk mencegah terjadinya _resource exhaustion_, dirancanglah algoritma dalam mengalokasikan data program baru dan mengoptimalkan penggunaan ruang kosong agar kinerja lebih efisien.

## Problem Modelling

Terdapat dua array masukan, yakni array $P$ dan array $F$.
- P adalah array yang berisi $n$ elemen, dan untuk setiap $i = \set{ x | 0 \lt x \le n \}$, elemen $P_i$ adalah ukuran data program ke- $i$.
- F adalah array yang berisi $m$ elemen, dan untuk setiap $j = \set{ x | 0 \lt x \le m \}, elemen $F_j$ adalah ukuran _internal fragmentation_ ke- $j$. _Internal fragmentation_ adalah "lubang" ruang memori kosong ditengah-tengah blok memori. 

Solusi ada dalam bentuk array $S$ yang berisi $n$ elemen, dan untuk setiap $i = \set{ x | 0 \lt x \le n \}$, elemen $S_i$ adalah nomor _internal fragmentation_ yang harus ditempatkan oleh data ke- $i$ 

## Brute Force Strategy

Brute force strategy is done by enumerating every possibilities and potential solutions, then pick one of the most suitable and optimal solution.

This strategy is simple, easy-to-grasp, and complete, with additional time and space complexity.

### Algorithm Design

Let say that there are _n_ programs with corresponding program data size and _m_ internal fragmentations with corresponding sizes, find every possibilites to allocate all data to existing spaces.

Eliminante every possibilities that in at least one of the internal fragmentation _Fi_ for i from 1 to _m_, data size allocated to _Fi_ exceeds the capacity of _Fi_ itself.

The most optimal solution is the solution where the final condition leaves the least remaining internal fragmentation.

### Implementation

TBA

### Complexity Analysis

Each data program in Pi have m possible internal fragmentations to occupy. Therefore, there are m^n possibilities of solution.
Hence, the complexity is m^n.

## Greedy Strategy

### Algorithm Design

### Implementation

### Complexity Analysis
