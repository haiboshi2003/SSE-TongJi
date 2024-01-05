<template>
  <div class="contain2">
    <div class="building">
      <input class="button" type="file" @change="handleFileChange" />

      <p>图片预览</p>

      <div class="mybutton" @click="handleButtonClick2">
        <p>检测</p>
      </div>
      <img
        v-if="selectedFile"
        :src="previewUrl"
        alt="Selected Image"
        class="scaled-image"
      />
    </div>
    <div class="building">
      <p>检测结果</p>
      <img :src="imagePath" alt="Detected Image" class="scaled-image" />
    </div>
  </div>
  <div v-if="false" id="qoe">
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

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const imagePath = ref(null);
const selectedFile = ref(null);

const uploadImage = async () => {
  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await axios.post("http://localhost:7078/svm", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    imagePath.value = `data:image/jpeg;base64,` + response.data.imageBase64;
    console.log(imagePath.value);
    console.log(imagePath.value);
    //console.log(imagePath.value);
  } catch (error) {
    console.error("Error uploading image:", error);
  }
};

//选择图片的预览部分
const previewUrl = ref(null);

const handleFileChange = (event) => {
  selectedFile.value = event.target.files[0];

  if (selectedFile.value) {
    const reader = new FileReader();

    reader.onload = () => {
      previewUrl.value = reader.result;
    };

    reader.readAsDataURL(selectedFile.value);
  }
};

//按钮
import { TweenMax, Expo, Back } from "gsap"; // 请确保已安装 gsap 库

const buttonRef = ref(null);

const handleButtonClick2 = () => {
  const duration = 0.3;
  const delay = 0.08;

  TweenMax.to(buttonRef.value, duration, { scaleY: 1.6, ease: Expo.easeOut });
  TweenMax.to(buttonRef.value, duration, {
    scaleX: 1.2,
    scaleY: 1,
    ease: Back.easeOut,
    easeParams: [3],
    delay: delay,
  });
  TweenMax.to(buttonRef.value, duration * 1.25, {
    scaleX: 1,
    scaleY: 1,
    ease: Back.easeOut,
    easeParams: [6],
    delay: delay * 3,
  });
  uploadImage();
};

onMounted(() => {
  // 获取按钮元素的引用
  buttonRef.value = document.querySelector(".mybutton");
});
</script>

<style scoped>
.app {
  width: calc(100%); /* 设置根组件的宽度 */
  height: calc(100%); /* 设置根组件的高度 */
  margin: auto; /* 居中显示 */
  border: 2px solid #ccc; /* 为了更好的可视化效果，添加边框 */
}

.contain2 {
  width: 90%;
  height: 85%;
  position: fixed;

  display: flex;
}

.building {
  background-color: rgba(255, 255, 255, 0.85);
  border: 1px solid #000; /* 黑色边框 */

  padding: 10px; /* 内边距，使内容不贴紧边框 */

  margin: 200px auto;
  width: 450px;
  height: 400px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  border: 2px solid #333;
  color: #333;
  background-color: #fff;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.button:hover {
  background-color: #333;
  color: #fff;
}
.limited-size {
  max-width: 100%;
  max-height: 100%;
}

.scaled-image {
  max-width: 100%; /* 设置最大宽度为父元素宽度 */
  max-height: 100%; /* 设置最大高度为父元素高度 */
  object-fit: contain; /* 保持图像的纵横比，完全适应元素框，可能会在父元素内留有空白 */
}

.mybutton {
  background: #3498db;
  width: 180px;
  padding: 4px 0;

  position: absolute;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  border-radius: 3px;
}
.mybutton p {
  font-family: "Roboto";
  text-align: center;
  text-transform: uppercase;
  color: #fff;
  user-select: none;
}

.mybutton:after {
  content: "";
  display: block;
  position: absolute;
  width: 100%;
  height: 10%;
  border-radius: 50%;
  background-color: darken(#000, 20%);
  opacity: 0.4;
  bottom: -30px;
}
.mybutton:hover {
  cursor: pointer;
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

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}
.busahd {
  background-color: #bb27d2;
  background-image: linear-gradient(90deg, #d2dade 0%, #1b2628 74%);
  border-radius: 20px;
  border: 1px solid #ccb508;
  color: #6cd813;
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

.form > .btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}
.njs {
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
</style>
