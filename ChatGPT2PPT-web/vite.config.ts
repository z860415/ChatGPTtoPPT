import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
       alias: {
         '@': resolve(__dirname, './src'),
         '#': resolve(__dirname, './src/types'),
          utils: resolve(__dirname, './src/utils'),
          api: resolve(__dirname, './src/api')
    }
    },
  plugins: [vue()],
  server:{
    host: true,
    port: 8888,
  },
  define: {
  },
  build: {
    chunkSizeWarningLimit: 1600,
  }
})
