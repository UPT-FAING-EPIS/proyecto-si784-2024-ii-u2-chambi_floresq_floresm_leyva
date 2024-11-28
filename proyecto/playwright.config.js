// playwright.config.js
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
    testDir: './tests', // Reemplaza con tu directorio de pruebas
    use: {
        slowMo: 4000,
        video: 'on', // Habilita la grabación de video para todas las pruebas
        // Alternativamente, usa 'retain-on-failure' para grabar solo si la prueba falla
        // video: 'retain-on-failure',
    },
});