<!-- AudioPlayer.vue -->
<template>
  <div>
    <audio ref="audioPlayer" controls>
      <source :src="audioSource" type="audio/mp3" />
    </audio>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const audioSource = ref("./1.mp3");
const isPlaying = ref(false);
const audioPlayer = ref(null);

onMounted(() => {
  audioPlayer.value.addEventListener("ended", () => {
    isPlaying.value = false;
  });
});
</script>
