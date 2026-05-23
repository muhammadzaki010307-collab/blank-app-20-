import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# ... (Database ELEMENT_DATA tetap sama seperti sebelumnya) ...

# FUNGSI TAMBAHAN: Menentukan kategori/legend unsur
def get_legend(unsur):
    no = ELEMENT_DATA[unsur]["No"]
    if no in [1, 6, 7, 8, 15, 16, 34]: return "Non-logam"
    if no in [2, 10, 18, 36, 54, 86, 118]: return "Gas Mulia"
    if no in [3, 11, 19, 37, 55, 87]: return "Logam Alkali"
    if no in [4, 12, 20, 38, 56, 88]: return "Logam Alkali Tanah"
    if 21 <= no <= 30 or 39 <= no <= 48 or 72 <= no <= 80 or 104 <= no <= 112: return "Logam Transisi"
    if no in [57, 89] or (58 <= no <= 71) or (90 <= no <= 103): return "Logam Lantanida/Aktinida"
    return "Logam/Metaloid Lain"

# --- RENDER PAPAN DENGAN LEGEND ---
st.subheader("🖼️ 2. Papan Senyawa Aktif & Informasi Unsur")

if not st.session_state.puzzle_comp:
    st.info("Papan kosong. Silakan klik unsur kimia di atas.")
else:
    # Update CSS agar kartu lebih tinggi untuk menampung legend
    st.markdown("""
        <style>
        .element-card {
            border: 2px solid #222222; border-radius: 8px; padding: 10px; text-align: center;
            color: #FFFFFF !important; box-shadow: 3px 4px 6px rgba(0,0,0,0.2);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; min-height: 150px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4); margin-bottom: 5px;
        }
        .el-no { font-size: 10px; text-align: left; margin: 0; font-weight: bold; opacity: 0.8; }
        .el-sym { font-size: 28px; font-weight: 900; margin: 0; }
        .el-ar { font-size: 10px; font-weight: bold; margin: 2px 0; opacity: 0.9; }
        .el-legend { font-size: 9px; font-style: italic; background: rgba(0,0,0,0.2); border-radius: 4px; padding: 2px; margin-top: 5px; }
        </style>
    """, unsafe_allow_html=True)
    
    # ... (Proses perulangan puzzle_comp) ...
    for idx, item in enumerate(st.session_state.puzzle_comp):
        unsur = item["unsur"]
        jumlah = item["jumlah"]
        
        no_atom = ELEMENT_DATA[unsur]["No"]
        ar = ELEMENT_DATA[unsur]["Ar"]
        warna = ELEMENT_DATA[unsur]["color"]
        legend = get_legend(unsur) # Mengambil kategori legend
        
        with papan_kolom[idx]:
            card_html = f"""
            <div class="element-card" style="background-color: {warna};">
                <div class="el-no">#{no_atom}</div>
                <div class="el-sym">{unsur}</div>
                <div class="el-ar">Mr: {ar}</div>
                <div class="el-legend">{legend}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            # ... (Tombol +/- tetap sama) ...
