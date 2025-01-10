from django.core.management.base import BaseCommand
from oprogreso.models import Bloque, Tema, Actividad
from datetime import datetime

class Command(BaseCommand):
    help = 'Importar temas y crear actividades'

    def handle(self, *args, **kwargs):
        
        bloques_data = [
            {
            "orden": 1,
            "titulo":"General"
            },
            {
            "orden": 2,
            "titulo":"Especifico"
            }
        ]

        for bloque in bloques_data:
            # Create Tema object
            nuevo_bloque = Bloque.objects.create(
                titulo=bloque["titulo"],
                orden=bloque["orden"]
            )
            
    
        temas_data = [
            {
            "numero": 1,
            "titulo": "El derecho a la protección de la salud en la Constitución española de 1978 y en la Ley 14/1986, de 25 de abril, General de Sanidad.",
            "contenido": "Ley 41/2002, de 14 de noviembre, básica reguladora de la autonomía del paciente y de derechos y obligaciones en materia de información y documentación clínica.",
            "bloque":"General"
            },
            {
            "numero": 2,
            "titulo": "Ley 44/2003, de 21 de noviembre, de Ordenación de las Profesiones Sanitarias",
            "contenido": "Objeto, ámbito de aplicación, ejercicio de las profesiones sanitarias, formación y desarrollo profesional. Ley 55/2003, de 16 de diciembre, del Estatuto Marco del personal estatutario de los servicios de salud: objeto y ámbito de aplicación; clasificación de personal estatutario; derechos y deberes; situaciones; selección, incompatibilidades; régimen disciplinario y modelo de desarrollo profesional.",
            "bloque":"General"
            },
            {
            "numero": 3,
            "titulo": "Estructura, organización y competencias del Ministerio de Defensa.",
            "contenido": "Resolución 400/38239/2009, de 23 de octubre, de la Subsecretaría, por la que se delegan competencias en materia de personal estatutario de la Red Hospitalaria del Ministerio de Defensa.",
            "bloque":"General"
            },
            {
            "numero": 4,
            "titulo": "La ley Orgánica 1/2004, de Medidas de Protección Integral contra la Violencia de Género",
            "contenido": "Principios rectores, medidas de sensibilización, prevención y detección en el ámbito sanitario; derechos de las funcionarias públicas. Ley Orgánica 3/2007, para la igualdad efectiva de mujeres y hombres: objeto y ámbito de la ley; integración del principio de igualdad en la política de salud; modificaciones de la Ley General de Sanidad. La Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas trans y para la garantía de los derechos de las personas LGTBI.",
            "bloque":"General"
            },
            {
            "numero": 5,
            "titulo": "La Ley 31/1995, de 8 de noviembre, de Prevención de Riesgos Laborales",
            "contenido": "Derechos y obligaciones; consulta y participación de los trabajadores.",
            "bloque":"General"
            },
            {
            "numero": 6,
            "titulo": "Principios fundamentales de la Bioética",
            "contenido": "Dilemas éticos. Código deontológico.",
            "bloque":"General"
            },
            {
            "numero": 7,
            "titulo": "Plan de calidad para el Sistema Nacional de Salud",
            "contenido": "Áreas de actuación; estrategias y objetivos. Estrategia 8: mejorar la seguridad de los pacientes atendidos en los centros sanitarios del Sistema Nacional de Salud.",
            "bloque":"General"
            },
            {
            "numero": 8,
            "titulo": "Técnicas y habilidades de comunicación y relación interpersonal",
            "contenido": "Trabajo en equipo. Entrevista clínica: concepto y características. Identificación de necesidades de apoyo emocional y psicológico al paciente, cuidador principal y familia. Colaboración con otros profesionales.",
            "bloque":"General"
            },
            {
            "numero": 9,
            "titulo": "El secreto profesional: concepto y regulación jurídica",
            "contenido": "El consentimiento informado. Derechos y deberes de los ciudadanos en el Sistema de Salud. La protección de datos. Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales.",
            "bloque":"General"
            },
            {
            "numero": 10,
            "titulo": "Metodología de Investigación Básica e Investigación Aplicada",
            "contenido": "Estudios descriptivos y analíticos. Estudios de procesos y resultados. Estructura metodológica de un trabajo científico. Fuentes de datos.",
            "bloque":"General"
            },
            {
            "numero": 11,
            "titulo": "Estadística descriptiva",
            "contenido": "Tipos de distribución y parámetros que la definen. Estadística inferencial: intervalos de confianza. Los test de hipótesis.",
            "bloque":"General"
            },
            {
            "numero": 12,
            "titulo": "Enfermería basada en la evidencia: niveles de evidencia y grados de recomendación",
            "contenido": "Búsqueda de evidencias científicas: bases de datos bibliográficas, fuentes documentales de evidencia y revisión bibliográfica. Instrumentos de la evidencia científica. Formulación de preguntas y búsqueda de respuestas sobre la práctica clínica. Evaluación y síntesis de los hallazgos de la revisión bibliográfica. Guías de práctica clínica.",
            "bloque":"Especifico"
            },
            {
            "numero": 13,
            "titulo": "Organización de los cuidados obstétrico-ginecológicos en Atención Primaria y Atención Hospitalaria",
            "contenido": "Consulta de Matrona. Coordinación de cuidados obstétrico ginecológicos entre ambos niveles asistenciales. Programas y planificación de cuidados obstétrico-ginecológicos.",
            "bloque":"Especifico"
            },
            {
            "numero": 14,
            "titulo": "La docencia como actividad necesaria para el desarrollo profesional",
            "contenido": "Participación de la Matrona en la formación de pregrado y postgrado. Formación continuada.",
            "bloque":"Especifico"
            },
            {
            "numero": 15,
            "titulo": "Administración de los servicios obstétrico-ginecológicos",
            "contenido": "Elaboración de objetivos. Sistemas de registro. Historia clínica.",
            "bloque":"Especifico"
            },
            {
            "numero": 16,
            "titulo": "La Matrona como agente de Educación Sanitaria",
            "contenido": "Sistemas de comunicación e información en la educación para la salud de la mujer. Educación para la salud de la mujer y el neonato. Aplicación de la dinámica de grupos en los programas educativos para la salud de la mujer. Educación para la prevención del consumo de sustancias adictivas.",
            "bloque":"Especifico"
            },
            {
            "numero": 17,
            "titulo": "Reproducción humana",
            "contenido": "Gametogénesis: ovogénesis y espermatogénesis. Conceptos generales sobre reproducción humana. Estructura y funciones del sistema reproductor masculino y femenino. Ciclo ovárico, ciclo endometrial, ciclo menstrual.",
            "bloque":"Especifico"
            },
            {
            "numero": 18,
            "titulo": "Consejo genético, diagnóstico prenatal",
            "contenido": "Nociones básicas de genética, enfermedades genéticas y malformaciones genéticas. Identificación prenatal de cromosomopatías. Técnicas de diagnóstico prenatal. Técnicas básicas de determinación de cariotipo y biología molecular.",
            "bloque":"Especifico"
            },
            {
            "numero": 19,
            "titulo": "Anatomía del aparato reproductor femenino",
            "contenido": "Pelvis ósea. Pelvis blanda. Órganos genitales internos y externos. Vascularización. Ligamentos. Inervación.",
            "bloque":"Especifico"
            },
            {
            "numero": 20,
            "titulo": "Desarrollo prenatal humano",
            "contenido": "Fecundación; período pre embrionario. Período embrionario: diferenciación de las hojas germinativas. Período fetal: desarrollo. Características morfológicas y funcionales de la placenta, hormonas placentarias. Circulación fetoplacentaria.",
            "bloque":"Especifico"
            },
            {
            "numero": 21,
            "titulo": "Fecundación artificial",
            "contenido": "Fecundación múltiple. La pareja con problemas de infertilidad: causas de esterilidad, valoración clínica, alternativas a la esterilidad. Esterilidad/infertilidad. Diagnóstico prenatal/postnatal. Técnicas de reproducción asistida.",
            "bloque":"Especifico"
            },
            {
            "numero": 22,
            "titulo": "Concepto de embarazo",
            "contenido": "Anatomía y fisiología del embarazo. Cambios estructurales, funcionales, emocionales y psicológicos en la mujer. Diagnóstico del embarazo. Pruebas de embarazo. Autocuidados derivados del embarazo. Alimentación, eliminación, actividad/descanso, aseo y vestido.",
            "bloque":"Especifico"
            },
            {
            "numero": 23,
            "titulo": "Consulta prenatal",
            "contenido": "Atención a la mujer gestante. Objetivos de control prenatal. Historia de la embarazada. Exploración general y obstétrica: las maniobras de Leopold. Identificación de problemas. Control y seguimiento de la embarazada. Valoración del bienestar fetal: métodos clínicos, monitorización biofísica, ecografía, doppler, amnioscopia, otras técnicas.",
            "bloque":"Especifico"
            },
            {
            "numero": 24,
            "titulo": "Factores que inciden en el desarrollo de la gestación",
            "contenido": "Alcohol, tabaco. Drogodependencia. Sustancias tóxicas. Radiaciones. Estrés. Fármacos en la gestación. Asesoramiento a la gestante.",
            "bloque":"Especifico"
            },
            {
            "numero": 25,
            "titulo": "Prevención de infecciones en el embarazo",
            "contenido": "Inmunización activa o pasiva. La embarazada con problemas derivados del SIDA y/o de la hepatitis B y C. Cuidados en embarazo, parto, posparto, lactancia. Educación sanitaria.",
            "bloque":"Especifico"
            },
            {
            "numero": 26,
            "titulo": "Educación sanitaria de la gestante",
            "contenido": "Programas de educación para la maternidad: contenido teórico y práctico. Ejercicios físicos, del suelo pélvico y estática corporal. Ejercicios respiratorios y de relajación.",
            "bloque":"Especifico"
            },
            {
            "numero": 27,
            "titulo": "Atención y cuidados a la mujer en el parto normal",
            "contenido": "El partograma, signos y síntomas. Exploraciones al ingreso. Monitorización interna y externa. Amniorrexis. Etapas del trabajo del parto: fisiología del parto, adaptación del organismo materno al trabajo del parto, adaptación del feto al canal del parto. Mecanismo de parto en presentación de vértice. Biomecánica del parto. Valoración materna y fetal.",
            "bloque":"Especifico"
            },
            {
            "numero": 28,
            "titulo": "La episiotomía",
            "contenido": "Indicaciones y procedimientos. Episiorrafia. Aspectos psicológicos de la mujer durante el parto. Alternativas al parto tradicional. El parto en casa. Atención y cuidados de la mujer en el alumbramiento; la inspección placentaria.",
            "bloque":"Especifico"
            },
            {
            "numero": 29,
            "titulo": "Farmacoterapia durante el proceso de parto",
            "contenido": "La dilatación inducida: problemas y complicaciones. Métodos no farmacológicos de alivio del dolor. Mórficos. Anestésicos locales. Óxido nitroso. Anestesia regional. Anestesia general.",
            "bloque":"Especifico"
            },
            {
            "numero": 30,
            "titulo": "Asistencia y cuidados de la mujer en el parto dirigido",
            "contenido": "Inducción de parto. Fármacos uteroestimulantes: oxitocina, prostaglandinas. Estimulación del parto: amniorrexis artificial, maniobra de Hamilton. Complicaciones en el trabajo de parto y alumbramiento: parto distócico. Distocias dinámicas, mecánicas y de la estática fetal. Fiebre intraparto. Instrumentación: fórceps, espátulas de Thierry, ventosa, cesárea.",
            "bloque":"Especifico"
            },
            {
            "numero": 31,
            "titulo": "Situaciones especiales de urgencia obstétrica",
            "contenido": "Procidencia, prolapso de cordón, distocia de hombros, embolias, reanimación cardiopulmonar. Conducta obstétrica. Atención de la Matrona.",
            "bloque":"Especifico"
            },
            {
            "numero": 32,
            "titulo": "Atención inmediata al recién nacido",
            "contenido": "Valoración inicial, registros y cuidados inmediatos. Examen general: test de Apgar. Valoración neurológica. Identificaciones de situaciones de riesgo. Adaptación del recién nacido a la vida extrauterina. Cuidados al recién nacido: aporte de oxígeno, termorregulación, bienestar y seguridad. Alimentación, eliminación, actividad, sueño. Vacunación. Vínculos de relación madre/pareja/recién nacido. Cribaje de metabolopatías. Orientación a los padres sobre sus cuidados. Asesoramiento al alta.",
            "bloque":"Especifico"
            },
            {
            "numero": 33,
            "titulo": "Donación de sangre de cordón",
            "contenido": "Definición, procedimiento, aspectos legales.",
            "bloque":"Especifico"
            },
            {
            "numero": 34,
            "titulo": "Atención a la mujer durante el puerperio",
            "contenido": "Puerperio normal. Modificaciones físicas y psicológicas. Molestias posparto. Atención al puerperio inmediato. Exploración general, identificación de problemas y prevención de los mismos. Autocuidados derivados del puerperio: alimentación, actividad y descanso, eliminación, seguridad, bienestar, adaptación al nuevo rol. Control y seguimiento en el puerperio: visita a domicilio, programas de control puerperal y del recién nacido. Revisión posparto.",
            "bloque":"Especifico"
            },
            {
            "numero": 35,
            "titulo": "Situaciones de riesgo en el puerperio",
            "contenido": "Concepto, factores etiológicos y concurrentes. Complicaciones generales: hemorragias, enfermedad tromboembólica. Infección puerperal: profilaxis, atención y cuidados de la mujer. Complicaciones locales: mastitis. Infección urinaria. Dehiscencias de suturas, hematomas perineales. Cuidados de Matrona. Adaptación psicosocial de la puérpera: depresión posparto.",
            "bloque":"Especifico"
            },
            {
            "numero": 36,
            "titulo": "Lactancia materna",
            "contenido": "Fisiología de la secreción láctea: problemas más frecuentes. Supresión de la lactancia. Educación sanitaria y promoción de la lactancia materna.",
            "bloque":"Especifico"
            },
            {
            "numero": 37,
            "titulo": "Atención a la mujer con complicaciones durante el embarazo",
            "contenido": "Anemia, tuberculosis, cardiopatías, listeriosis, nefritis, rubeola. Problemas hemorrágicos en el primer y segundo trimestre: aborto, amenaza de aborto, embarazo ectópico y molar. Signos de alarma. Implicaciones, intervenciones específicas. Hemorragias en el tercer trimestre. Placenta previa, abruptio placentae. Implicaciones materno-fetales. Intervenciones específicas.",
            "bloque":"Especifico"
            },
            {
            "numero": 38,
            "titulo": "Embarazo de riesgo I",
            "contenido": "Concepto. Situaciones de riesgo. Clasificación, descripción, planificación de los cuidados obstétricos-ginecológicos. Implicaciones maternofetales. Intervenciones y valoración de la situación en los trastornos cardiovasculares, respiratorios, digestivos, hematológicos, músculoesqueléticos y neurológicos durante el embarazo.",
            "bloque":"Especifico"
            },
            {
            "numero": 39,
            "titulo": "Embarazo de riesgo II",
            "contenido": "Hiperemesis. Hipertensión. Diabetes. Problemas de isoinmunización: valoración. Implicaciones materno-fetales. Intervenciones específicas.",
            "bloque":"Especifico"
            },
            {
            "numero": 40,
            "titulo": "Complicaciones fetales durante la gestación",
            "contenido": "Valoración del crecimiento y desarrollo fetal. Valoración de la madurez fetal. Intervenciones específicas. Problemas derivados de los anejos fetales: anomalías de placenta, del cordón, membranas y líquido amniótico.",
            "bloque":"Especifico"
            },
            {
            "numero": 41,
            "titulo": "Problemas relacionados con la duración de la gestación",
            "contenido": "Amenaza de parto prematuro, embarazo prolongado. Intervenciones específicas.",
            "bloque":"Especifico"
            },
            {
            "numero": 42,
            "titulo": "Embarazo múltiple y parto múltiple",
            "contenido": "Valoración y cuidados de la matrona. Parto de riesgo: concepto, factores etiológicos y contribuyentes. Situaciones psicosociales de riesgo: mujer adolescente, mujer sola. Muerte intraparto: concepto, intervenciones específicas. Atención de la Matrona.",
            "bloque":"Especifico"
            },
            {
            "numero": 43,
            "titulo": "Recién nacido de riesgo",
            "contenido": "Prematuro, dismaduro, posmaduro, bajo peso. Clasificación de los problemas. Anoxía del recién nacido. Reanimación cardiopulmonar básica y avanzada del recién nacido. Hiperbilirrubinemia: causas, prevención de complicaciones. Cuidados específicos. Sepsis neonatal: causas y prevención de complicaciones. Problemas neurológicos y renales. El recién nacido con malformaciones.",
            "bloque":"Especifico"
            },
            {
            "numero": 44,
            "titulo": "Educación sanitaria en planificación familiar",
            "contenido": "Concepto. Métodos anticonceptivos: naturales, de barrera, hormonales, DIU, quirúrgicos. Contracepción. Contracepción en situaciones especiales. Interrupción voluntaria del embarazo.",
            "bloque":"Especifico"
            },
            {
            "numero": 45,
            "titulo": "Plan integral de asistencia a la mujer",
            "contenido": "Programa de atención a la mujer: Exploración ginecológica: citología y toma de muestra. Exploración mamaria. Atención y cuidados de la mujer: en la adolescencia, menarquía y pubertad. Aspectos psicológicos y sociales. Problemas ginecológicos de la mujer en edad fértil. Sexualidad: conceptos generales. Psicofisiología de la respuesta sexual. La sexualidad en las diferentes etapas de la vida. Disfunciones sexuales. Mutilación genital femenina. Fomento de hábitos saludables, prevención y control de riesgos. Delitos contra la libertad sexual.",
            "bloque":"Especifico"
            },
            {
            "numero": 46,
            "titulo": "Enfermedades de transmisión sexual",
            "contenido": "Sífilis, gonorrea, herpes genital, tricomoniasis, candidiasis. Otras enfermedades: sida y hepatitis. Diagnóstico y tratamiento. Prevención. Control. Educación para la salud. Las enfermedades de transmisión sexual como problema de salud pública. Epidemiología.",
            "bloque":"Especifico"
            },
            {
            "numero": 47,
            "titulo": "Climaterio y menopausia",
            "contenido": "Cronología del climaterio. Evolución morfológica y biológica. Aspectos psicológicos y sociales. Problemas de salud más frecuentes. Tratamiento farmacológico y no farmacológico. Programa de menopausia.",
            "bloque":"Especifico"
            },
            {
            "numero": 48,
            "titulo": "Cuidados a la mujer con problemas ginecológicos",
            "contenido": "Alteraciones del ciclo menstrual. La mujer con problemas estructurales del sistema reproductor. Procesos inflamatorios e infecciones del sistema reproductor. Incontinencias urinarias.",
            "bloque":"Especifico"
            },
            {
            "numero": 49,
            "titulo": "Diagnóstico precoz del cáncer genital y de mama",
            "contenido": "Programas de prevención. Epidemiología. Pautas de asistencia. Atención y cuidados a la mujer con cáncer ginecológico.",
            "bloque":"Especifico"
            },
            {
            "numero": 50,
            "titulo": "Demografía sanitaria maternal y reproductiva",
            "contenido": "Inscripción del recién nacido. Estructura de la población. Índices demográficos. Morbilidad reproductiva. Propuestas de la Organización Mundial de la Salud.",
            "bloque":"Especifico"
            }
        ]

        for tema in temas_data:
            
            # Obtener el bloque correspondiente
            bloque = Bloque.objects.get(titulo=tema["bloque"])
    
            # Create Tema object
            nuevo_tema = Tema.objects.create(
                titulo=tema["titulo"],
                contenido=tema["contenido"],
                orden=tema["numero"],
                bloque=bloque
            )
            
            # Create Activities
            actividades = [
                {"titulo": "Estudiar", "puntos": 80, "orden": 1},
                {"titulo": "Podcast", "puntos": 15, "orden": 2},
                {"titulo": "Tests", "puntos": 5, "orden": 3},
            ]
            
            for actividad in actividades:
                Actividad.objects.create(
                    tema=nuevo_tema,
                    titulo=actividad["titulo"],
                    puntos=actividad["puntos"],
                    orden=actividad["orden"]
                )

        self.stdout.write(self.style.SUCCESS('Temas y actividades importados exitosamente.'))