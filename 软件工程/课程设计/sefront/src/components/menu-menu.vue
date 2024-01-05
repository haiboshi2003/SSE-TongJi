<template>
  <a-space direction="vertical" :style="{ width: '100%' }" :size="[0, 48]">
    <a-layout>
      <a-layout-sider>
        <a-menu mode="inline" class="a-sider">
          <a-menu-item :key="1">
            <router-link to="/menu/menu2/r1">YOLOV5算法检测</router-link>
          </a-menu-item>
          <a-menu-item :key="2">
            <router-link to="/menu/menu2/r2">SVM算法检测</router-link>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-content class="a-content"
          ><router-view></router-view
        ></a-layout-content>
      </a-layout>
    </a-layout>
  </a-space>
</template>
<script setup></script>
<style scoped>
.ma {
  color: red;
  font-size: 16px;
  margin: 10px;
}

.const {
  color: blue;
  font-size: 18px;
  margin: 12px;
}

.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay__panel {
  align-items: center;
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  position: absolute;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 50%;
}

.overlay--left {
  transform: translateX(-20%);
}

.right-panel-active .overlay--left {
  transform: translateX(0);
}

.container--signup {
  left: 0;
  opacity: 0;
  width: 50%;
  z-index: 1;
}

.right-panel-active .container--signup {
  animation: show 0.6s;
  opacity: 1;
  transform: translateX(100%);
  z-index: 5;
}

.container__overlay {
  height: 100%;
  left: 50%;
  overflow: hidden;
  position: absolute;
  top: 0;
  transition: transform 0.6s ease-in-out;
  width: 50%;
  z-index: 100;
}

.right-panel-active .container__overlay {
  transform: translateX(-100%);
}

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}
.btn {
  background-color: #0367a6;
  background-image: linear-gradient(90deg, #0367a6 0%, #008997 74%);
  border-radius: 20px;
  border: 1px solid #0367a6;
  color: #e9e9e9;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}
.btn {
  background-color: #0367a6;
  background-image: linear-gradient(90deg, #0367a6 0%, #008997 74%);
  border-radius: 20px;
  border: 1px solid #0367a6;
  color: #e9e9e9;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.overlay--left {
  transform: translateX(-20%);
}

.right-panel-active .overlay--left {
  transform: translateX(0);
}

.overlay--right {
  right: 0;
  transform: translateX(0);
}

.right-panel-active .overlay--right {
  transform: translateX(20%);
}

.btnsmb {
  background-color: #af44ca;
  background-image: linear-gradient(90deg, #0367a6 0%, #008997 74%);
  border-radius: 20px;
  border: 1px solid #da41ac;
  color: #e9e9e9;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}
.overlay--left {
  transform: translateX(-20%);
}

.right-panel-active .overlay--left {
  transform: translateX(0);
}

.overlay--right {
  right: 0;
  transform: translateX(0);
}

.right-panel-active .overlay--right {
  transform: translateX(20%);
}

.btnknd {
  background-color: #0367a6;
  background-image: linear-gradient(90deg, #0367a6 0%, #008997 74%);
  border-radius: 20px;
  border: 1px solid #0367a6;
  color: #e9e9e9;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}
</style>
