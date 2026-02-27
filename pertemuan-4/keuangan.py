# keuangan.py - Module untuk perhitungan keuangan sederhana
def hitung_ppn(harga, persen=11):
    ppn = harga * (persen / 100)
    return ppn
def format_rupiah(jumlah):
    return f'Rp {jumlah:,.0f}'.replace(',', '.')
def hitung_cicilan(pokok, bunga_persen, bulan):
    total_bunga = pokok * (bunga_persen / 100) * (bulan / 12)
    return (pokok + total_bunga) / bulan