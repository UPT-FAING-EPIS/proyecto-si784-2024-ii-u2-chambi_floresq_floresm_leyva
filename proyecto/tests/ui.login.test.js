// ui.login.test.js
const { test, expect } = require('@playwright/test');

test('iniciar sesión con credenciales válidas', async ({ page }) => {
    await page.goto('http://localhost:5000'); // Asegúrate de que tu servidor esté corriendo

    // Llenar el formulario con credenciales válidas
    await page.fill('input[name="username"]', 'admin'); // Cambia a un usuario válido
    await page.fill('input[name="password"]', 'adxcmin123'); // Cambia a una contraseña válida

    // Hacer clic en el botón de inicio de sesión
    await page.click('button[type="submit"]');

    // Verificar que la redirección o el mensaje de éxito se muestre
    await expect(page).toHaveURL('http://localhost:5000/dashboard'); // Cambia según tu redirección esperada
});

test('intentar iniciar sesión con credenciales inválidas', async ({ page }) => {
    await page.goto('http://localhost:5000');

    // Llenar el formulario con credenciales inválidas
    await page.fill('input[name="username"]', 'usuario_invalido');
    await page.fill('input[name="password"]', 'contraseña_invalida');

    // Hacer clic en el botón de inicio de sesión
    await page.click('button[type="submit"]');

    // Verificar que se muestre un mensaje de error
    const errorMessage = await page.locator('.alert-danger'); // Selecciona el mensaje de error
    await expect(errorMessage).toBeVisible();
});