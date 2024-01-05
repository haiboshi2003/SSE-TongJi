<template>
  <div class="body">
    <div class="container">
      <div :class="{ 'right-panel-active': isRightPanelActive }">
        <!-- Sign Up -->
        <div class="container__form container--signup">
          <form action="#" class="form" id="form1" @submit.prevent>
            <h2 class="form__title">Sign Up</h2>
            <input
              type="text"
              placeholder="Username"
              class="input"
              v-model="signUp.username"
              autocomplete="off"
            />
            <input
              type="text"
              placeholder="Id"
              class="input"
              v-model="signUp.id"
              autocomplete="off"
            />
            <input
              type="password"
              placeholder="Password"
              class="input"
              v-model="signUp.password"
              autocomplete="off"
            />

            <button class="btn" @click="addUser">Sign Up</button>
          </form>
        </div>

        <!-- Sign In -->

        <div class="container__form container--signin">
          <div class="form" id="form2">
            <h2 class="form__title">Sign In</h2>
            <input
              type="text"
              placeholder="Id"
              class="input"
              v-model="signIn.id"
              autocomplete="off"
            />
            <input
              type="password"
              placeholder="Password"
              class="input"
              v-model="signIn.password"
              autocomplete="off"
            />
            <button class="btn" @click="logIn">Sign In</button>
          </div>
          <!-- <form action="#" class="form" id="form2" @submit.prevent>
            <h2 class="form__title">Sign In</h2>
            <input
              type="email"
              placeholder="Email"
              class="input"
              v-model="signIn.email"
              autocomplete="off"
            />
            <input
              type="password"
              placeholder="Password"
              class="input"
              v-model="signIn.password"
              autocomplete="off"
            />
            <button class="btn" @click="logIn">Sign In</button>
          </form> -->
        </div>

        <!-- Overlay -->
        <div class="container__overlay">
          <div class="overlay">
            <div class="overlay__panel overlay--left">
              <button class="btn" id="signIn" @click="activateLeftPanel">
                Sign In
              </button>
            </div>
            <div class="overlay__panel overlay--right">
              <button class="btn" id="signUp" @click="activateRightPanel">
                Sign Up
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-if="false" id="inline">
    <vue-particles
      id="tsparticles"
      :particlesInit="particlesInit"
      :particlesLoaded="particlesLoaded"
    />
    <vue-particles
      id="tsparticles"
      :particlesInit="particlesInit"
      :particlesLoaded="particlesLoaded"
      :options="{
        background: {
          color: {
            value: '#7af9e8',
          },
        },
        fpsLimit: 80,
        interactivity: {
          events: {
            onClick: {
              enable: false,
              mode: 'push',
            },
            onHover: {
              enable: true,
              mode: 'attract',
              parallax: { enable: false, force: 60, smooth: 10 },
            },
            resize: true,
          },
          modes: {
            push: { quantity: 4 },
            attract: { distance: 200, duration: 0.4, factor: 5 },
          },
        },
        particles: {
          color: {
            value: '#3a71f3',
          },
          line_linked: {
            color: '#3a71f3',
            distance: 150,
            enable: true,
            opacity: 0.4,
            width: 1,
          },
          move: {
            attract: { enable: false, rotateX: 600, rotateY: 1200 },
            bounce: false,
            direction: 'none',
            enable: true,
            out_mode: 'out',
            random: false,
            speed: 2,
            straight: false,
          },
          number: {
            density: {
              enable: true,
              area: 850,
            },
            value: 60,
          },
          opacity: {
            anim: { enable: false, opacity_min: 0.1, speed: 1, sync: false },
            random: false,
            value: 0.5,
          },
          shape: {
            type: 'circle',
          },
          size: {
            random: true,
            value: 5,
          },
        },
        detectRetina: true,
      }"
    />
  </div>
</template>

<script setup lang="js">
import { message } from 'ant-design-vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';



//滑动效果js代码段
const isRightPanelActive = ref(false);
const activateLeftPanel = () => {
  isRightPanelActive.value = false;
  // console.log('left');
};
const activateRightPanel = () => {
  isRightPanelActive.value = true;
  // console.log('right');

};

//POST请求发送
  //发送数据Object
const signIn = ref({
  id: '',
  password: '',
})
const signUp = ref({
  id: '',
  password: '',
  username: '',
})

//控制跳转路径
const router = useRouter();

  //发送请求
async function addUser() {
  console.log('注册成功')
  message.success('注册成功', 2);
}

async function logIn() {
  if ((signIn.value.id.trim()) && (signIn.value.password.trim())) {
    console.log('登录成功')
    message.success('登录成功', 2);
    router.push({ path: '/menu/menu2/r1' })
  }
  else {
    message.error('账号密码不能为空', 2);

  }


}
</script>

<style scoped>
:root {
  /* COLORS */
  --white: #e9e9e9;
  --gray: #333;
  --blue: #0367a6;
  --lightblue: #008997;

  /* RADII */
  --button-radius: 0.7rem;

  /* SIZES */
  --max-width: 758px;
  --max-height: 420px;

  font-size: 16px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.body {
  align-items: center;
  background-color: var(--white);
  background: url("../assets/background_oeuhe7.jpg");
  /* 决定背景图像的位置是在视口内固定，或者随着包含它的区块滚动。 */
  /* https://developer.mozilla.org/zh-CN/docs/Web/CSS/background-attachment */
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  display: grid;
  height: 100vh;
  place-items: center;
}
.form__title {
  font-weight: 300;
  margin: 0;
  margin-bottom: 1.25rem;
}

.link {
  color: #333;
  font-size: 0.9rem;
  margin: 1.5rem 0;
  text-decoration: none;
}

.container {
  background-color: #e9e9e9;
  border-radius: 0.7rem;
  box-shadow: 0 0.9rem 1.7rem rgba(0, 0, 0, 0.25),
    0 0.7rem 0.7rem rgba(0, 0, 0, 0.22);
  height: 420px;
  max-width: 758px;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.container__form {
  height: 100%;
  position: absolute;
  top: 0;
  transition: all 0.6s ease-in-out;
}

.container--signin {
  left: 0;
  width: 50%;
  z-index: 2;
}

.right-panel-active .container--signin {
  transform: translateX(100%);
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

.overlay {
  background-color: #008997;
  background: url("../assets/background_oeuhe7.jpg");
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  left: -100%;
  position: relative;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 200%;
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

.overlay--right {
  right: 0;
  transform: translateX(0);
}

.right-panel-active .overlay--right {
  transform: translateX(20%);
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

.form {
  background-color: #e9e9e9;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 3rem;
  height: 100%;
  text-align: center;
}

.input {
  background-color: #fff;
  border: none;
  padding: 0.9rem 0.9rem;
  margin: 0.5rem 0;
  width: 100%;
}

@keyframes show {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
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

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}
</style>
