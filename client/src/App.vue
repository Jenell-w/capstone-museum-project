<template>
  <div id="app">
    <div class="opening-text">
      <h1>Welcome to Family ViewSeums!</h1>
      <h2>Visiting an art museum can be kid-friendly: let us show you how!</h2>
    </div>
    <div class="img-container">
      <img
        class="header-image"
        v-if="!showMuseumHome"
        alt="mona-lisa-cartoon"
        src="./assets/cartoon-mona-lisa.jpg"
        width="250"
        height="167"
      />
    </div>
    <MuseumActivities title="BEFORE Your Visit" />
  </div>
</template>

<script>
import MuseumActivities from "./components/MuseumActivities.vue";

export default {
  name: "app",
  components: {
    MuseumActivities
  },
  data() {
    return {
      component: "",
      showMuseumHome: false,
      showMuseumInfo: false,
      buttonText: "Get Information about museums"
    };
  },
  methods: {}
};
</script>

<style>
.opening-text {
  text-align: center;
  display: inline-block;
}
img.header-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
