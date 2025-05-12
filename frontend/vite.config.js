import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // any request starting with /search will be forwarded to your backend
      '/search': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
});
