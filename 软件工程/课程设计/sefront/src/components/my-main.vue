<template>
  <div id="ducx" v-if="false">
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
    <router-view></router-view>
  </div>
  <router-view></router-view>
</template>

<script setup></script>

<style scoped>
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
  background-color: #c8b90f;
  background-image: linear-gradient(90deg, #229de9 0%, #20daee 74%);
  border-radius: 20px;
  border: 1px solid #b92655;
  color: #ec0909;
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
