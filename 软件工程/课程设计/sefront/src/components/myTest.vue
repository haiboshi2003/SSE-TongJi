<template>
  <div class="contain1">
    <input class="button" type="file" @change="handleFileChange" />
  </div>

  <div class="contain2">
    <div class="building">
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
    const response = await axios.post(
      "http://localhost:7078/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

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
.contain1 {
  display: flex;
}
.contain2 {
  width: 100%;
  height: 100%;
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
  max-width: 500px;
  max-height: 300px;
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
</style>
