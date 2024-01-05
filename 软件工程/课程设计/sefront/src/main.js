import { createApp } from 'vue'
import ElementPlus from 'element-plus'
// import App from './App.vue'
import router from './router/router'
import maim from './components/my-main.vue'
import VueParticles from 'vue-particles'  
import Particles from "vue3-particles";
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';

const app = createApp(maim)
app.use(ElementPlus)
    .use(VueParticles)
    .use(Particles)
    .use(Antd)
.use(router)

app.mount('#app')
