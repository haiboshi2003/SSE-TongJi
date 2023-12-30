<template>
  <div class="body">
    <div class="stars" ref="starsRef">
      <div class="star" v-for="(item, index) in starsCount" :key="index"></div>
    </div>
    <div class="center-div">
      <!-- 包装预览部分的 div 元素 -->
      <div
        style="
          border: 2px solid black;
          padding: 10px;
          margin-top: 10px;
          display: inline-block;
          width: 300px;
          height: 300px;
        "
      >
        <img
          v-if="previewUrl"
          :src="previewUrl"
          alt="预览图片"
          style="max-width: 100%; max-height: 100%"
        />
      </div>
      <div>
        <input ref="fileInput" type="file" @change="handleFileChange" />
        <button @click="uploadFile" class="button">上传图片</button>
      </div>
    </div>

    <div><p>识别结果展示</p></div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";

export default {
  setup() {
    let starsRef = ref(null);

    const starsCount = 800; //星星数量
    const distance = 900; //间距

    onMounted(() => {
      let starNodes = Array.from(starsRef.value.children);
      starNodes.forEach((item) => {
        let speed = 0.2 + Math.random() * 1;
        let thisDistance = distance + Math.random() * 300;
        item.style.transformOrigin = `0 0 ${thisDistance}px`;
        item.style.transform = `
        translate3d(0,0,-${thisDistance}px)
        rotateY(${Math.random() * 360}deg)
        rotateX(${Math.random() * -50}deg)
        scale(${speed},${speed})`;
      });
    });

    return {
      starsRef,
      starsCount,
    };
  },
};
</script>

<style lang="css" scoped>
.center-div {
  height: 10.666667rem;
  width: 100%;
  border: 1px blue solid;
  display: table;
  text-align: center;
}

.body {
  position: absolute;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background: radial-gradient(
    200% 100% at bottom center,
    #f7f7b6,
    #e96f92,
    #1b2947
  );
  background: radial-gradient(
    200% 105% at top center,
    #1b2947 10%,
    #75517d 40%,
    #e96f92 65%,
    #f7f7b6
  );
  background-attachment: fixed;
  overflow: hidden;
}

@keyframes rotate {
  0% {
    transform: perspective(400px) rotateZ(20deg) rotateX(-40deg) rotateY(0);
  }
  100% {
    transform: perspective(400px) rotateZ(20deg) rotateX(-40deg)
      rotateY(-360deg);
  }
}
.stars {
  transform: perspective(500px);
  transform-style: preserve-3d;
  position: absolute;
  perspective-origin: 50% 100%;
  left: 45%;
  animation: rotate 90s infinite linear;
  bottom: 0;
}
.star {
  width: 2px;
  height: 2px;
  background: #f7f7b6;
  position: absolute;
  left: 0;
  top: 0;
  backface-visibility: hidden;
}
</style>
