import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/reviews': 'http://localhost:5000', // Proxy API requests to the backend
    },
    preview: {
      port: 3000
    }
  },
});
