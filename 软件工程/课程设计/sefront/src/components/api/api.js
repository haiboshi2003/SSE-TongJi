//创建新的axios对象
// 创建新的 axios 对象
import axios from 'axios'
const _axios = axios.create({
  baseURL: 'http://localhost:7078'
})

// 请求拦截器
_axios.interceptors.request.use(
  config => {
    // 每次发送请求之前判断vuex中是否存在token
    // 如果存在，则统一在http请求的header都加上token，这样后台根据token判断你的登录情况
    // 即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `${token}`;
    } else {
      config.headers.Authorization = `Bearer ${"fail"}`;
      
    }
 
    return config;
  },
  error => {
    return Promise.error(error);
  }
  )

export default _axios