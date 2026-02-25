
# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("calculadora rebajas")
st.markdown("Bienvenido. Introduce tus descuentos junto al precio.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
preciooriginal = st.sidebar.number_input("precio original ($)", min_value=0, max_value=1000000, value=60)
rebaja = st.sidebar.slider("Tu descuento ($)", 00, 100, 15)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    uuu = preciooriginal * (rebaja / 100)
    precio = preciooriginal - uuu
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="precio final" value=f"{precio:.2f}")
        st.success(f"Te ahorras {uuu}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if rebaja >= 50:
            st.error("Éxito")
            st.balloons()
        elif 50 > rebaja < 20:
            st.error("No está mal")
            st.balloons() # ¡Premio!
        elif 20 >= rebaja:
            st.error("Algo es algo")
            st.snow()
