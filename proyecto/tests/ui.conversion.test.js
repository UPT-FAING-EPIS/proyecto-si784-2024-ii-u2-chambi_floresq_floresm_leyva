// ui.conversion.test.js

const { test, expect } = require('@playwright/test');

test.describe('Pruebas de Conversión', () => {
    
    test('mostrar advertencia al enviar formulario vacío', async ({ page }) => {
        await page.goto('http://localhost:5000/conversion');

        // Hacer clic en el botón de convertir sin llenar el formulario
        await page.click('button[type="submit"]');

        // Esperar un corto periodo para que el mensaje de advertencia aparezca
        await page.waitForTimeout(100); // Espera para asegurar que el mensaje se muestre

        // Verificar el mensaje de advertencia en el campo "Monto"
        const montoInput = page.locator('input[name="monto"]');
        const isInvalid = await montoInput.evaluate((input) => input.validity.valueMissing);
        expect(isInvalid).toBeTruthy(); // Verifica que el campo "Monto" tiene el estado de valor faltante
    
        // También puedes verificar el foco en el campo que falló la validación
        const isFocused = await montoInput.evaluate((input) => document.activeElement === input);
        expect(isFocused).toBeTruthy(); // Verifica que el campo "Monto" tiene el foco
    });

    test('no permitir envío con monto negativo', async ({ page }) => {
        await page.goto('http://localhost:5000/conversion');

        // Introducir un monto negativo
        await page.fill('input[name="monto"]', '-100');
        await page.selectOption('select[name="divisa_origen"]', 'USD');
        await page.selectOption('select[name="divisa_destino"]', 'EUR');

        // Hacer clic en el botón de convertir
        await page.click('button[type="submit"]');

        // Verificar que el formulario no se envía (puedes verificar la URL o algún elemento visible)
        await expect(page).toHaveURL('http://localhost:5000/conversion'); // Asegúrate de que sigue en la misma página
    });

    test('enviar formulario con datos válidos', async ({ page }) => {
        await page.goto('http://localhost:5000/conversion');

        // Llenar el formulario con datos válidos
        await page.fill('input[name="monto"]', '100');
        await page.selectOption('select[name="divisa_origen"]', 'USD');
        await page.selectOption('select[name="divisa_destino"]', 'EUR');

        // Hacer clic en el botón de convertir
        await page.click('button[type="submit"]');

        // Verificar que la conversión se realizó (puedes verificar la redirección o un mensaje en la página resultante)
        await expect(page).toHaveURL('http://localhost:5000/conversion'); // Asegúrate de que la URL cambie según tu lógica
    });

    test('mostrar mensaje de error por valor inválido en el campo "Monto"', async ({ page }) => {
        await page.goto('http://localhost:5000/conversion');
    
        // Seleccionar el campo "Monto"
        const montoInput = page.locator('input[name="monto"]');
        
        // Asignar un valor inválido directamente al elemento
        await montoInput.evaluate((input) => input.value = '4366345.34543512--34');
    
        // Intentar enviar el formulario
        await page.click('button[type="submit"]');
    
        // Verificar que el campo tiene un error de tipo inválido (HTML5 validation)
        const isInvalid = await montoInput.evaluate((input) => !input.checkValidity());
        expect(isInvalid).toBeTruthy(); // Verifica que el campo es inválido
    
        // Verificar el mensaje de validación nativo
        const validationMessage = await montoInput.evaluate((input) => input.validationMessage);
        expect(validationMessage).not.toBe(''); // Confirma que hay un mensaje de error
    });
});