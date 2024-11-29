from behave import *

def before_scenario(context, scenario):
    # Se ejecuta antes de cada escenario
    pass

def after_scenario(context, scenario):
    # Si el escenario falla, imprime un mensaje pero no detiene la ejecución
    if scenario.status == "failed":
        print(f"Escenario fallado: {scenario.name}. La ejecución continuará.")
    pass

def before_step(context, step):
    pass

def after_step(context, step):
    pass

def on_failure(context, step, exception):
    # Captura la excepción pero no interrumpe la ejecución
    print(f"Error en el paso: {step.name} - {exception}")
    return False  # Permite que la ejecución continúe
