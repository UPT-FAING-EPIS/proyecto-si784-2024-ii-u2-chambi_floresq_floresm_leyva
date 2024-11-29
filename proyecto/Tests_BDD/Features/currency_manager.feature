Feature: Gestión de monedas
  Descripción: Permite a los usuarios consultar y convertir monedas.

  Scenario: Consultar el tipo de cambio de una moneda válida
    Given el sistema tiene acceso a tipos de cambio actualizados
    When el usuario consulta el tipo de cambio de USD a EUR
    Then se muestra el tipo de cambio actual

  Scenario: Intentar consultar el tipo de cambio de una moneda inexistente
    Given el sistema no tiene registro de la moneda XYZ
    When el usuario consulta el tipo de cambio de XYZ
    Then se muestra un mensaje de error indicando moneda desconocida

  Scenario: Convertir una cantidad de una moneda a otra
    Given un usuario quiere convertir 100 USD a EUR
    When realiza la conversión
    Then se muestra el monto equivalente en EUR

  Scenario: Intentar convertir una cantidad negativa
    Given un usuario intenta convertir -50 USD a EUR
    When realiza la conversión
    Then se muestra un mensaje indicando que la cantidad debe ser positiva
