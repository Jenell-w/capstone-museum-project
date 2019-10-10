<template>
  <div id="app">
    <img alt="museum image" src="/assets/cartoon-mona-lisa.jpg" />
    <HelloWorld msg="Welcome to Family ViewSeums!" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import MuseumHome from "./components/MuseumHome.vue";

export default {
  name: "app",
  components: {
    HelloWorld,
    MuseumHome
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
