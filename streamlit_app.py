import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman (Wajib di paling atas)
st.set_page_config(page_title="Kalkulator Senyawa Kimia", layout="wide", page_icon="🧪")

st.title("🧪 Komposer Senyawa Kimia")
st.write("Klik kepingan puzzle unsur di bawah untuk merakit senyawa kimia!")

# 2. Database Lengkap 118 Unsur Kimia dengan Kode Warna Golongan
ELEMENT_DATA = {
    "H": {"No": 1, "Ar": 1.008, "color": "#3A96B4"},
    "He": {"No": 2, "Ar": 4.0026, "color": "#9B59B6"},
    "Li": {"No": 3, "Ar": 6.94, "color": "#E74C3C"},
    "Be": {"No": 4, "Ar": 9.0122, "color": "#E67E22"},
    "B": {"No": 5, "Ar": 10.81, "color": "#1ABC9C"},
    "C": {"No": 6, "Ar": 12.011, "color": "#3A96B4"},
    "N": {"No": 7, "Ar": 14.007, "color": "#3A96B4"},
    "O": {"No": 8, "Ar": 15.999, "color": "#3A96B4"},
    "F": {"No": 9, "Ar": 18.998, "color": "#2ECC71"},
    "Ne": {"No": 10, "Ar": 20.180, "color": "#9B59B6"},
    "Na": {"No": 11, "Ar": 22.990, "color": "#E74C3C"},
    "Mg": {"No": 12, "Ar": 24.305, "color": "#E67E22"},
    "Al": {"No": 13, "Ar": 26.982, "color": "#BDC3C7"},
    "Si": {"No": 14, "Ar": 28.085, "color": "#1ABC9C"},
    "P": {"No": 15, "Ar": 30.974, "color": "#3A96B4"},
    "S": {"No": 16, "Ar": 32.06, "color": "#3A96B4"},
    "Cl": {"No": 17, "Ar": 35.45, "color": "#2ECC71"},
    "Ar": {"No": 18, "Ar": 39.948, "color": "#9B59B6"},
    "K": {"No": 19, "Ar": 39.098, "color": "#E74C3C"},
    "Ca": {"No": 20, "Ar": 40.078, "color": "#E67E22"},
    "Sc": {"No": 21, "Ar": 44.956, "color": "#F1C40F"},
    "Ti": {"No": 22, "Ar": 47.867, "color": "#F1C40F"},
    "V": {"No": 23, "Ar": 50.942, "color": "#F1C40F"},
    "Cr": {"No": 24, "Ar": 51.996, "color": "#F1C40F"},
    "Mn": {"No": 25, "Ar": 54.938, "color": "#F1C40F"},
    "Fe": {"No": 26, "Ar": 55.845, "color": "#F1C40F"},
    "Co": {"No": 27, "Ar": 58.933, "color": "#F1C40F"},
    "Ni": {"No": 28, "Ar": 58.693, "color": "#F1C40F"},
    "Cu": {"No": 29, "Ar": 63.546, "color": "#F1C40F"},
    "Zn": {"No": 30, "Ar": 65.38, "color": "#F1C40F"},
    "Ga": {"No": 31, "Ar": 69.723, "color": "#BDC3C7"},
    "Ge": {"No": 32, "Ar": 72.630, "color": "#1ABC9C"},
    "As": {"No": 33, "Ar": 74.922, "color": "#1ABC9C"},
    "Se": {"No": 34, "Ar": 78.971, "color": "#3A96B4"},
    "Br": {"No": 35, "Ar": 79.904, "color": "#2ECC71"},
    "Kr": {"No": 36, "Ar": 83.798, "color": "#9B59B6"},
    "Rb": {"No": 37, "Ar": 85.468, "color": "#E74C3C"},
    "Sr": {"No": 38, "Ar": 87.62, "color": "#E67E22"},
    "Y": {"No": 39, "Ar": 88.906, "color": "#F1C40F"},
    "Zr": {"No": 40, "Ar": 91.224, "color": "#F1C40F"},
    "Nb": {"No": 41, "Ar": 92.906, "color": "#F1C40F"},
    "Mo": {"No": 42, "Ar": 95.95, "color": "#F1C40F"},
    "Tc": {"No": 43, "Ar": 98.0, "color": "#F1C40F"},
    "Ru": {"No": 44, "Ar": 101.07, "color": "#F1C40F"},
    "Rh": {"No": 45, "Ar": 102.91, "color": "#F1C40F"},
    "Pd": {"No": 46, "Ar": 106.42, "color": "#F1C40F"},
    "Ag": {"No": 47, "Ar": 107.87, "color": "#F1C40F"},
    "Cd": {"No": 48, "Ar": 112.41, "color": "#F1C40F"},
    "In": {"No": 49, "Ar": 114.82, "color": "#BDC3C7"},
    "Sn": {"No": 50, "Ar": 118.71, "color": "#BDC3C7"},
    "Sb": {"No": 51, "Ar": 121.76, "color": "#1ABC9C"},
    "Te": {"No": 52, "Ar": 127.60, "color": "#1ABC9C"},
    "I": {"No": 53, "Ar": 126.90, "color": "#2ECC71"},
    "Xe": {"No": 54, "Ar": 131.29, "color": "#9B59B6"},
    "Cs": {"No": 55, "Ar": 132.91, "color": "#E74C3C"},
    "Ba": {"No": 56, "Ar": 137.33, "color": "#E67E22"},
    "La": {"No": 57, "Ar": 138.91, "color": "#9C27B0"},
    "Ce": {"No": 58, "Ar": 140.12, "color": "#9C27B0"},
    "Pr": {"No": 59, "Ar": 140.91, "color": "#9C27B0"},
    "Nd": {"No": 60, "Ar": 144.24, "color": "#9C27B0"},
    "Pm": {"No": 61, "Ar": 145.0, "color": "#9C27B0"},
    "Sm": {"No": 62, "Ar": 150.36, "color": "#9C27B0"},
    "Eu": {"No": 63, "Ar": 151.96, "color": "#9C27B0"},
    "Gd": {"No": 64, "Ar": 157.25, "color": "#9C27B0"},
    "Tb": {"No": 65, "Ar": 158.93, "color": "#9C27B0"},
    "Dy": {"No": 66, "Ar": 162.50, "color": "#9C27B0"},
    "Ho": {"No": 67, "Ar": 164.93, "color": "#9C27B0"},
    "Er": {"No": 68, "Ar": 167.26, "color": "#9C27B0"},
    "Tm": {"No": 69, "Ar": 168.93, "color": "#9C27B0"},
    "Yb": {"No": 70, "Ar": 173.05, "color": "#9C27B0"},
    "Lu": {"No": 71, "Ar": 174.97, "color": "#9C27B0"},
    "Rf": {"No": 104, "Ar": 267.0, "color": "#F1C40F"},
    "Db": {"No": 105, "Ar": 268.0, "color": "#F1C40F"},
    "Sg": {"No": 106, "Ar": 271.0, "color": "#F1C40F"},
    "Bh": {"No": 107, "Ar": 272.0, "color": "#F1C40F"},
    "Hs": {"No": 108, "Ar": 270.0, "color": "#F1C40F"},
    "Mt": {"No": 109, "Ar": 276.0, "color": "#F1C40F"},
    "Ds": {"No": 110, "Ar": 281.0, "color": "#F1C40F"},
    "Rg": {"No": 111, "Ar": 280.0, "color": "#F1C40F"},
    "Cn": {"No": 112, "Ar": 285.0, "color": "#F1C40F"},
    "Nh": {"No": 113, "Ar": 284.0, "color": "#BDC3C7"},
    "Fl": {"No": 114, "Ar": 289.0, "color": "#BDC3C7"},
    "Mc": {"No": 115, "Ar": 288.0, "color": "#BDC3C7"},
    "Lv": {"No": 116, "Ar": 293.0, "color": "#BDC3C7"},
    "Ts": {"No": 117, "Ar": 294.0, "color": "#2ECC71"},
    "Og": {"No": 118, "Ar": 294.0, "color": "#9B59B6"}
}

# 3. State Management yang Aman & Stabil
if "puzzle_comp" not in st.session_state:
    st.session_state.puzzle_comp = []

def tambah_unsur(unsur):
    for item in st.session_state.puzzle_comp:
        if item["unsur"] == unsur:
            item["jumlah"] += 1
            return
    st.session_state.puzzle_comp.append({"unsur": unsur, "jumlah": 1})

def reset_puzzle():
    st.session_state.puzzle_comp = []

# --- INJEKSI CSS STRATEGI BARU (Membidik Atribut ID Tombol Secara Presisi) ---
css_styles = """
<style>
/* Hilangkan margin bawaan kolom agar muat 18 kolom tanpa patah teks */
div[data-testid="stColumn"] {
    padding-left: 2px !important;
    padding-right: 2px !important;
}

/* Membidik langsung elemen tombol berdasarkan pola ID pembuka */
button[id^="b-t-n-e-l-"] {
    color: #FFFFFF !important;
    font-family: 'Arial Black', Gadget, sans-serif !important;
    font-size: 13px !important;
    font-weight: bold !important;
    height: 42px !important;
    width: 100% !important;
    border-radius: 5px !important;
    border: 1px solid rgba(0,0,0,0.2) !important;
    box-shadow: inset -2px -2px 0px rgba(0,0,0,0.2), inset 2px 2px 0px rgba(255,255,255,0.2) !important;
    text-shadow: 1px 1px 1px rgba(0,0,0,0.3) !important;
    padding: 0px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
"""

# Generasikan warna latar belakang dinamis untuk masing-masing ID unsur
for sym, data in ELEMENT_DATA.items():
    # Streamlit mengubah karakter key menjadi lowercase ID dengan strip khusus, kita bidik polanya
    clean_id = sym.lower()
    css_styles += f"""
    button[id*="btn_el_{clean_id}"] {{
        background-color: {data['color']} !important;
    }}
    button[id*="btn_el_{clean_id}"]:hover {{
        filter: brightness(1.15) !important;
        color: #FFFFFF !important;
    }}
    """
css_styles += "</style>"
st.markdown(css_styles, unsafe_allow_html=True)


# --- BAGIAN 1: RENDER TABEL PERIODIK (18 KOLOM NATIVE) ---
st.subheader("🧩 1. Tabel Periodik Unsur (Klik untuk Menambahkan)")

grid_structure = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]

# Render Grid Utama 7 Baris
for row_idx, row in enumerate(grid_structure):
    cols = st.columns(18)
    for col_idx, sym in enumerate(row):
        if sym != "":
            with cols[col_idx]:
                # Gunakan key lowercase yang konsisten dipetakan oleh CSS
                if st.button(sym, key=f"btn_el_{sym.lower()}"):
                    tambah_unsur(sym)

st.write("") 

# Render Baris Lantanida
cols_lan = st.columns(18)
with cols_lan[0]:
    st.markdown("<p style='font-weight:bold; margin-top:10px; color:#555; font-size:13px;'>Lan:</p>", unsafe_allow_html=True)
lan_elements = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
for idx, sym in enumerate(lan_elements):
    with cols_lan[idx + 2]: 
        if st.button(sym, key=f"btn_el_{sym.lower()}"):
            tambah_unsur(sym)

# Render Baris Aktinida
cols_akt = st.columns(18)
with cols_akt[0]:
    st.markdown("<p style='font-weight:bold; margin-top:10px; color:#555; font-size:13px;'>Akt:</p>", unsafe_allow_html=True)
akt_elements = ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]
for idx, sym in enumerate(akt_elements):
    with cols_akt[idx + 2]:
        if st.button(sym, key=f"btn_el_{sym.lower()}"):
            tambah_unsur(sym)


# --- BAGIAN 2: LEGENDA GOLONGAN WARNA ---
st.markdown("""
    <style>
    .bottom-legend-container {
        display: flex; flex-wrap: wrap; justify-content: center; gap: 12px;
        background-color: #fdfdfd; border: 1px solid #EAEAEA; border-radius: 8px;
        padding: 10px; margin-top: 25px; margin-bottom: 25px;
    }
    .legend-item { display: flex; align-items: center; gap: 6px; font-size: 11px; font-weight: bold; color: #444; }
    .legend-color-box { width: 16px; height: 12px; border-radius: 2px; border: 1px solid rgba(0,0,0,0.15); }
    </style>
<div class="bottom-legend-container">
    <div class="legend-item"><div class="legend-color-box" style="background-color: #E74C3C;"></div>Logam Alkali</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #E67E22;"></div>Alkali Tanah</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #F1C40F;"></div>Logam Transisi</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #BDC3C7;"></div>Logam Pasca-Transisi</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #1ABC9C;"></div>Metaloid</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #3A96B4;"></div>Non-Logam Lain</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #2ECC71;"></div>Halogen</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #9B59B6;"></div>Gas Mulia</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #9C27B0;"></div>Lantanida</div>
    <div class="legend-item"><div class="legend-color-box" style="background-color: #E91E63;"></div>Aktinida</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# --- BAGIAN 3: PAPAN SENYAWAMU ---
st.subheader("🖼️ 2. Papan Senyawa Aktif")

if not st.session_state.puzzle_comp:
    st.info("Papan kosong. Klik kepingan puzzle unsur di atas untuk mulai merakit.")
else:
    st.markdown("""
        <style>
        .element-card {
            border: 2px solid #222222; border-radius: 8px; padding: 8px; text-align: center;
            color: #FFFFFF !important; box-shadow: 3px 4px 6px rgba(0,0,0,0.25);
            font-family: 'Courier New', Courier, monospace; min-height: 105px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5); margin-bottom: 5px;
        }
        .el-no { font-size: 11px; text-align: left; margin: 0; font-weight: bold; opacity: 0.8; }
        .el-sym { font-size: 28px; font-weight: 900; margin: -5px 0; }
        .el-ar { font-size: 11px; font-weight: bold; margin: 0; opacity: 0.9; }
        </style>
    """, unsafe_allow_html=True)
    
    total_komponen = len(st.session_state.puzzle_comp)
    papan_kolom = st.columns(max(total_komponen, 8))
    
    rumus_visual = ""
    total_bm = 0.0
    rincian_data = []
    
    for idx, item in enumerate(st.session_state.puzzle_comp):
        unsur = item["unsur"]
        jumlah = item["jumlah"]
        
        no_atom = ELEMENT_DATA[unsur]["No"]
        ar = ELEMENT_DATA[unsur]["Ar"]
        warna = ELEMENT_DATA[unsur]["color"]
        subtotal = ar * jumlah
        total_bm += subtotal
        
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        rumus_visual += f"{unsur}{str(jumlah).translate(SUB) if jumlah > 1 else ''}"
        
        rincian_data.append({
            "Unsur": unsur,
            "Ar": ar,
            "Jumlah": jumlah,
            "Subtotal (g/mol)": round(subtotal, 4)
        })
        
        with papan_kolom[idx]:
            card_html = f"""
            <div class="element-card" style="background-color: {warna};">
                <div class="el-no">{no_atom}</div>
                <div class="el-sym">{unsur}</div>
                <div class="el-ar">{ar}</div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 1, 1])
            if c1.button("➖", key=f"papan_min_{unsur}_{idx}"):
                if item["jumlah"] > 1:
                    item["jumlah"] -= 1
                else:
                    st.session_state.puzzle_comp.pop(idx)
                st.rerun()
                
            c2.markdown(f"<p style='text-align:center; font-size:16px; font-weight:bold; margin-top:2px;'>{jumlah}</p>", unsafe_allow_html=True)
            
            if c3.button("➕", key=f"papan_plus_{unsur}_{idx}"):
                item["jumlah"] += 1
                st.rerun()

    st.write("")
    res_col1, res_col2 = st.columns([1, 2])
    with res_col1:
        st.success(f"### 🧪 Rumus: **{rumus_visual}**")
        st.metric(label="Berat Molekul Total (Mr)", value=f"{round(total_bm, 4)} g/mol")
        st.button("🗑️ Bersihkan Papan", key="btn_reset", on_click=reset_puzzle, type="primary")
        
    with res_col2:
        st.write("**📋 Kontribusi Massa Molar:**")
        st.dataframe(pd.DataFrame(rincian_data), hide_index=True, use_container_width=True)
