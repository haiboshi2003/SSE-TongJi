import { createApp } from 'vue'
import ElementPlus from 'element-plus'
// import App from './App.vue'
import router from './router/router'
import menu from './components/MainMenu.vue'
import VueParticles from 'vue-particles'  
import Particles from "vue3-particles";

const app = createApp(menu)
app.use(ElementPlus)
    .use(VueParticles)
    .use(Particles)
.use(router)

app.mount('#app')
