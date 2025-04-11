import streamlit as st

# Judul Aplikasi
st.title("Optimasi Iklan Shopee")
st.write("Masukkan data performa iklan harian:")

st.markdown(
    " **Contoh Kondisi:** <br>"
    "• **Modal** = 200000 <br>"
    "• **Pengeluaran** = 300000 <br>"
    "• **Penjualan** hanya 10 pcs <br>"
    " Maka sistem akan memberi rekomendasi: `Matikan Iklan`",
    unsafe_allow_html=True
)


# Input dari user
modal = st.number_input("Modal Iklan (Rp)", value=100.0000)
pengeluaran = st.number_input("Pengeluaran Iklan (Rp)", value=50.0000)
penjualan = st.number_input("Jumlah Produk Terjual", value=0)

# Fungsi logika rekomendasi
def rekomendasi_iklan(modal, pengeluaran, penjualan):

    if pengeluaran > modal and penjualan < 20:
        return "Matikan iklan: sudah rugi dan penjualan rendah"

    elif pengeluaran > modal and penjualan >= 20:
        return "Pertimbangkan optimasi: biaya lebih tinggi dari modal"

    elif pengeluaran < modal and penjualan >= 100:
        return "Iklan efektif: pertahankan strategi saat ini"

    elif pengeluaran < modal and penjualan <= 20:
        return "Iklan belum maksimal, tapi belum rugi — tetap pantau performa"

    else:
        return "Tidak ada nilai yang di masukkan"


# Tampilkan rekomendasi
if st.button("Cek Rekomendasi"):
    hasil = rekomendasi_iklan(modal, pengeluaran, penjualan)
    st.subheader("Rekomendasi:")
    st.success(hasil)



st.subheader("🧠 Kode Fungsi Rekomendasi Iklan")

st.code("""
# Kode logika sederhana rekomendasi iklan
def rekomendasi_iklan(modal, pengeluaran, penjualan):
    
    # Kondisi 1
    # Jika pengeluaran lebih besar dari modal dan penjualan kurang dari 20,maka print return
    elif pengeluaran > modal and penjualan < 20:
        return "Matikan iklan: sudah rugi dan penjualan rendah"
    
    # Kondisi 2
    # Jika pengeluaran lebih besar dari modal dan penjualan lebih besar atau sama dengan 20,maka print return
    elif pengeluaran > modal and penjualan >= 20:
        return "Pertimbangkan optimasi: biaya lebih tinggi dari modal"

    # Kondisi 3
    # Jika pengeluaran lebih kecil dari modal dan penjualan lebih besar atau sama dengan 100,maka print return
    elif pengeluaran < modal and penjualan >= 100:
        return "Iklan efektif: pertahankan strategi saat ini"

    # Kondisi 4
    # Jika pengeluaran lebih kecil dari modal dan penjualan kurang dari atau sama dengan 20,maka print return
    elif pengeluaran < modal and penjualan <= 20:
        return "Iklan belum maksimal, tapi belum rugi — tetap pantau performa"

    # Kondisi fallback
    else:
        return "Tidak ada nilai yang di masukkan"
""", language="python")
