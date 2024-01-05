import {createRouter, createWebHashHistory} from 'vue-router'

// 路由 => 路径和组件之间的对应关系
const routes = [
    {
        path: '/',
        component: () => import('../components/log-in.vue')
    },
    {
        path: '/menu',
        component: () => import('../components/MainMenu.vue'),  
        children: [
           
           
            {
                path: 'menu2',
                component: () => import('../components/menu-menu.vue'),
                children: [
                    {
                        path: 'r1',
                        component: () => import('../components/myTest.vue')
                    },
                    {
                        path: 'r2',
                        component: () => import('../components/SvmTest.vue')
                    },
                ]
            },
            
           
            
        ]
    }
    
]

const router = createRouter({ 
  history: createWebHashHistory(), // 路径格式
  routes: routes // 路由数组
})

export default router