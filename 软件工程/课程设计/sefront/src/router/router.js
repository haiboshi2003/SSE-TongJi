import {createRouter, createWebHashHistory} from 'vue-router'

// 路由 => 路径和组件之间的对应关系
const routes = [
    {
        path: '/',
        component: () => import('../components/MainMenu.vue'),
        //redirect: '/r1',  //重定向，访问/a3立即跳转到/a3/student
        children: [
            {
                path: 'r1',
                component: () => import('../myMain.vue')

            },
            {
                path: 'r2',
                component: () => import('../components/myTest.vue')
            },
            {
                path: 'test',
                component: () => import('../components/MyTest2.vue')
            },
            
        ]
    },
]

const router = createRouter({ 
  history: createWebHashHistory(), // 路径格式
  routes: routes // 路由数组
})

export default router