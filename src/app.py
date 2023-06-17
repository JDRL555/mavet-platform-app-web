from flask                import Flask, render_template, redirect
from flask_login          import LoginManager
from models.User          import User
from routes.index_routes  import index_router
from routes.auth_routes   import auth_router
from routes.user_routes   import user_router
from routes.posts_routes  import posts_router 
from utils.db             import db
from utils.var            import *

app = Flask(__name__)

def notFound(error):
  return render_template("404.html")

def notAuthorized(error):
  return redirect("/signin")

app.secret_key                                = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']         = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

app.register_error_handler(401, notAuthorized)
app.register_error_handler(404, notFound)

db.init_app(app=app)

login_manager = LoginManager(app=app)
login_manager.init_app(app=app)

with app.app_context():
  db.create_all()
  
@login_manager.user_loader
def load_user(id):
  response = User.getById(db, id)
  return response["user"]

@login_manager.unauthorized_handler
def handle_unauthorized():
  return redirect("/signin")

@app.context_processor
def render_layout():
  data = {
    "navbar": [
      {"element": "Iniciar Sesión", "link": "/signin"},
      {"element": "Registrarme", "link": "/signup"},
    ],
    "contents": [
      {
        "title": "¿Quiénes somos?",
        "description": "Somos El Museo de Artes visuales y del Espacio MAVET."
      },
      {
        "title": "Objetivo General:",
        "description": "Coleccionar, conservar, exhibir, educar, investigar, difundir y recrear sobre las artes visuales y del espacio en la región, el país y el mundo, sin limitaciones en estilo y tiempo."
      },
      {
        "title": "Misión:",
        "description": "Rescatar y conservar el Patrimonio Cultural de las Artes Visuales y del Espacio."
      },
      {
        "title": "Visión:",
        "description": 'Reiterar en el proyecto: "Ciudad Museo de las Artes Visuales y del Espacio" el cual se concibe como una manera de esparcimiento a lo largo y ancho del casco histórico de la ciudad de San Cristóbal.'
      },
      {
        "title": "Servicios:",
        "description": 'Sala de exposiciones, Tienda de Arte Popular (venta de artesania popular, tradicional y moderna), Biblioteca de las artes "Abdón Villamizar", Café "El Rincón del poeta Manuel Felipe Rugeles", Aulas para talleres, Auditorio: Valentín Hernández Useche, Visitas guiadas llamar a: (numero), Horario de visita: de martes a sábado.'
      },
      {
        "title": "Reseña Historica:",
        "description": 'De acuerdo a los registros, en el año de 1880, hasta el año de 1891, en este lugar existía un lote de terreno, compuesto de pastos y ciertos frutos menores, y este sitio era conocido para aquel entonces con el nombre del Palmar, fue el patio del Monasterio en el siglo XVII (en los años 1630 a 1870 fue el monasterio de Los Agustinos, el cual desapareció por un decreto del Presidente de la Republica Guzmán Blanco y un terremoto ocurrido en 1875 destruyo el inmueble). Posteriormente en sociedad por los señores Anselmo Villasmil Y Juan Coberes, mediante documento registrado en la oficina de Registro Público del Distrito de San Cristóbal bajo el No 100, de fecha 19 de diciembre de 1880; luego fue adquirido por el Sr. Juan Coberes, venta esta que se le hizo a su copropietario anterior o sea el Sr. Anselmo Villasmil, esta venta quedo asentada bajo el No 70, de fecha 10 de noviembre de 1903. En 1899 por decreto general del Presidente de la Republica Guzman Blanco el patrimonio fue cancelado y a finales de 1895 fue destruido por un terremoto'
      },
      {
        "description": 'Desde 1900 hasta 1904 han venido haciendo en dichos terrenos ciertas mejoras, ya se habla de una casa construida de baharaque (barro y caña), techo de tejas, varias habitaciones, cocina, otros.'
      },
      {
        "description": 'En 1920, el General Juan Alberto Ramírez (Presidente del estado) realiza una transformación arquitectónica de la casona, quitando parte de las tejas de techo volada y los suple por cornisas con un mampostería francesa y en la parte interna, con un estilo toscano y colonial, sus techos son medificados, salones más amplios, pisos de mosaico y patio ornamentado, la cocina ubicada al fondo, con un patío lateral, por donde entraba el café en grano y los carruajes de la época (actualmente en este espacio está el Banco Banfoandes, lado este). Todos estos cambios hacen de esta casona una de las más hermosas de su época.'
      },
      {
        "description": 'Las paredes laterales son una altura de 3,20 mts, y 68 cms. de un grosor, su pasillo se encuentra delimitado con una puerta de vitral de diversos colores y ornamentos arabescos que delimita la entrada del interior del patio, las columnas de orden compuesto toscano con capitel corintio simétrico de color azul claro, tanto en el piso como en las paredes se llevan acordes con su estructura arquitectóica, a excepción del patio central que fue intervenido, eliminándoles los mosaicos y la fuente con un querubín de hoja en bronce.'
      },
      {
        "description": 'En 1930 la familia Cárdenas Dávila, son los nuevos propietarios de la casona 25.'
      },
      {
        "title": 'Características Constructivas:',
        "description": 'Es un inmueble construido en el año 1890, con una rica arquitectura rico-colonial con sus salones laterales, pasillos amplios y un patio central; las 8 columnas que bordean el patio son de orden compuesto toscano con gótico y capitel corintio, con diez (10) habitaciones, seis (06) pincipales, un (01) comedor, cuatro (04) son de servicio, cinco (05) baños, sus puertas son de madera sencilla de dos alas, con techo de volada en teja, ventanas en madera; su arquitectura es sencilla, hasta 1920 le colocaron cornisas y le cambiaron ventanas por hierro. Tiene valor histórico y arquitectónico a principios del siglo XX, enmarcado dentro de una importancia testimonial en la ciudad para los años de su reestructuración urbana y marcada como la casa No 25 de la ciudad de San Cristóbal.'
      },
      {
        "description": 'Las investigaciones estratigráficas realizadas en el inmueble en 1989 por un restaurador de muros (Héctor Rojas), hallaron decoraciones de cenefas en forma de espigas de trigo y zócalos con diversos matrices de colores pasteles muy usados en la época (1904). Luego se encontraron, colores dorados y azul ultramar, cenefas de color pastel y zócalos de rojo oscuro (1920).'
      },
      {
        "description": 'La planta de una forma U invertida de un solo nivel es la parte principal y en los servicios hay desnivel de 50 cms. de altura, sus espacios son amplios y dan frescura, es iluminada por sus patios, ventanas. Tiene corredores con diez columnas, ventanas internas, tres arcos tipo gótico de medio punto.'
      }
    ]
  }
    
  return dict(data=data)

app.register_blueprint(index_router)
app.register_blueprint(auth_router)
app.register_blueprint(user_router)
app.register_blueprint(posts_router)