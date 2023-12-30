const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: 'localhost', // 设置你想要的主机地址
    port: 8080, // 设置你想要的端口号
  },

})
