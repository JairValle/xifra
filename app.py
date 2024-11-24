
import os
import streamlit as st
from PIL import Image
from st_on_hover_tabs import on_hover_tabs
from streamlit_image_select import image_select



st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    image_side = Image.open('XIFRA_LOGO.png')
    left = 90
    top = 0
    right = 250
    bottom = 50
    image_side = image_side.crop((left, top, right, bottom))

    st.image(image = image_side, 
             use_column_width = True)
    
    st.write('---')
    tabs = on_hover_tabs(tabName = ['Inicio', 'Inmuebles', 'Administración','Contacto'], 
                         iconName = ['home', 'search', 'dashboard','person'], # https://fonts.google.com/icons
                         default_choice = 0)




if tabs =='Inicio':

    col1, col2 = st.columns([1,3])
    col1.image(image = 'XifraBlanco.png', caption = 'Pedregal del Rio, Privada Volga')
    col2.title("XIFRA")
    col2.subheader("Administración de Inmuebles")
    col2.subheader("¿Quiénes somos?")
    col2.write("##### Xifra nace como respuesta a la necesidad de ofrecer un servicio profesional de administración de inmuebles, cuyo objetivo es el conservar en óptimas condiciones el patrimonio de nuestros clientes, mejoramiento de la convivencia y transparencia en las finanzas.")
    col2.write("##### Somos una empresa joven e innovadora capaz de percibir las necesidades de nuestros clientes, somos una organización sólida, dinámica, flexible y adaptable a los cambios, nuestro equipo lo forman personas comprometidas, capacitadas y altamente profesionales.""")

    col2.write("##### Para su tranquilidad operamos en lineamiento a las normas, leyes y reglamentos vigentes, contando con la certificación de Administradores Profesionales que emite la PROSOC aplicable en la Ciudad de México; se realiza además el Contrato de Prestación de Servicios respectivos. Tenemos la capacidad para adaptarnos a las necesidades de nuestros clientes. Además de contar con la experiencia en la gestión de la entrega-recepción de áreas comunes, mobiliario y equipamiento.")

    st.write('---')

    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Xifra','Cursos y Certificaciones','Servicios','Reportes','Gestión de proyectos'])


    with tab1:
        st.subheader('Valor Agregado')
        col1, col2 = st.columns(2)
        col1.markdown("<br>", unsafe_allow_html=True)
        col1.write("##### En Xifra, estamos convencidos que no hay una única receta o solución para todos los problemas y oportunidades que enfrentan los condominios, por ello no creemos en soluciones pre-empaquetadas. Nosotros creemos que el mejor comienzo es con un diagnóstico inicial detallado hombro con hombro con la Mesa Directiva responsable del condominio, y definiendo claramente los objetivos para dotar del condominio de mayor plusvalía.")
        col2.image(image = 'ValorAgregado.png', width = 600)

        st.write('---')
        st.subheader('Experiencia')
        col1, col2 = st.columns(2)
        col1.image(image = 'Presencia.png')
        col2.markdown("<br>", unsafe_allow_html=True)
        # col2.write("### Nuestro conocimiento y experiencia en estos últimos 12 años, que nos han otorgado en más de 17 condominios (610 indivisos) , hacen posible que el proceso de diagnóstico, implementación y mejora sea mucho más ágil y acelerado.")
        col2.image(image = 'Experiencia.png')

        st.write('---')



    with tab2:
        st.subheader('Cursos y certificaciones')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Administrador Profesional - Procuraduría Social de la Ciudad de México</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='Cer1.jpg', width=600, caption = 'Agosto 2023 - Agosto 2024')
        st.write('---')

        # Segundo título con texto más grande
        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Administradores y Comité de Vigilancia - Procuraduría Social de la Ciudad de México</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='Cer2.jpg', width=600, caption = 'Junio 2023')
        st.write('---')

        # Tercer título con texto más grande
        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Administración de Condominios - ITAM</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='Cer3.jpg', width=300, caption = 'Octubre - 2018')
        st.write('---')



    with tab3:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns([1,3])
        col1.image('SerAdmin.png')
        col2.subheader('Servicios de Administración')
        col2.markdown("<br>", unsafe_allow_html=True)
        col2.markdown("""
        <ul>
        <li><span style="font-size:24px; font-weight: bold;">Cumplimiento y aplicación del reglamento interno de todas las partes involucradas.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Gestión de cobranza por departamento, aplicación de sanciones.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Elaboración de convocatorias, minutas y/o acuerdos de asambleas.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Comunicación en general para todos los residentes.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Elaboración de estados de cuenta generales y por unidad de propiedad privativa.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Diseño personalizado de informes mensuales (Infografías, reporte de ingresos y egresos, etc).</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Emisión de comprobantes de pago.</span></li>
        </ul>
        """, unsafe_allow_html=True)
        st.write('---')

        
        col1, col2 = st.columns([1,3])
        col1.markdown("<br>", unsafe_allow_html=True)
        col1.markdown("<br>", unsafe_allow_html=True)
        col1.image('SerMan.png')
        col2.subheader('Servicios de Mantenimiento')
        col2.markdown("<br>", unsafe_allow_html=True)
        col2.markdown("""
        <ul>
        <li><span style="font-size:24px; font-weight: bold;">Elaboración del plan de mantenimiento anual y control vía bitácoras.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Selección y contratación de proveedores.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Para el caso específico de las empresas de vigilancia, revisamos que estas cuenten con todos los permisos y registros correspondientes, ya que de lo contrario, el condominio podría ser sancionado con multas impuestas por la autoridad.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Solicitud y/o emisión de pagos a proveedores.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Creación y actualizaciones de carpetas compartidas en Drive.</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Organización de eventos para fomentar la integración (Día del niño, Posadas, Noches mexicanas, Día de muertos).</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Envió o publicación de temas de interés del condominio (Protección civil, Día de …, Cuidado del agua, etc.).</span></li>
        <li><span style="font-size:24px; font-weight: bold;">Indicador del avance de actividades (To do).</span></li>
        </ul>
        """, unsafe_allow_html=True)
        st.write('---')



    with tab4:
        st.subheader('Ejemplos de Reportes')
        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Reportes de presupuesto vs gasto real</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepPpto.png', caption = 'Presupuesto vs Gasto real')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Reportes de Ingresos y Egresos</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepEgresos.png', caption = 'Ingresos y Egresos')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Emisión de recibos de pagos</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepRecibos.png')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Envío por correo electrónico de recibos de pagos y notificaciones</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepRecibos2.png', caption = 'Email')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Minutas</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepMinutas.png', caption = 'Minutas')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Revisiones y bitácoras</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepBit.png', caption = 'Revisiones y bitácoras')
        st.write('---')

        st.markdown("""
        <ul>
        <li><b><span style="font-size:20px;">Carpetas compartidas</span></b></li>
        </ul>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        col2.image(image='RepDrive.png', caption = 'Google Drive')
        st.write('---')



    with tab5:
        st.subheader('Gestión de Proyectos', divider = 'gray')

        imd1, imd2, imd3 = st.columns(3) 
        imd1.image('Pro1.png')
        imd2.image('Pro2.png')
        imd3.image('Pro3.png')
        imd1.image('Pro10.png')
        imd2.image('Pro11.png')
        imd3.image('Pro12.png')
        imd1.image('Pro7.png')
        imd2.image('Pro8.png')
        imd3.image('Pro9.png')
        imd1.image('Pro4.png')
        imd2.image('Pro6.png')
        imd3.image('Pro5.png')
        imd1.image('Pro13.png')
        imd2.image('Pro14.png')
        imd3.image('Pro15.png')




elif tabs == 'Inmuebles':
    st.title(body = 'Inmuebles')

    # _select = st.multiselect('Prueba',[1,2,3,4,5])
    # st.subheader(body = 'Resultados', divider = 'gray')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'TST_IMAGES')
    image_paths = [
        os.path.join(images_dir, 'image0.jpg'),
        os.path.join(images_dir, 'image1.jpg'),
        os.path.join(images_dir, 'image2.jpg'),
        os.path.join(images_dir, 'image3.jpg'),
        os.path.join(images_dir, 'image4.jpg'),
        os.path.join(images_dir, 'image5.jpg'),
        os.path.join(images_dir, 'image6.jpg'),
        os.path.join(images_dir, 'image7.jpg'),
        os.path.join(images_dir, 'image8.jpg'),
        os.path.join(images_dir, 'image9.jpg')
    ]

    images = [Image.open(image_path) for image_path in image_paths]
    # img = image_select(
    #     label="Selecciona una imagen",
    #     images=images,
    #     captions=["1", "2", "3", "4", "5", "6", "7","8","9","10"]
    # )


    st.title('Departamento')
    div1, div2 = st.columns(2)
    with div1:
        
        img = image_select(
            label="Selecciona departamento",
            images=images,
            captions=["1", "2", "3", "4", "5", "6", "7","8","9","10"],
            use_container_width = False
        )

    with div2:
        
        st.image(img, width = 350)




elif tabs == 'Administración':
    st.title('')

