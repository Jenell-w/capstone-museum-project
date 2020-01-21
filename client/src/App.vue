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
  display: flex;
  align-items: center;
}
.flex-outer li button,
.activity-button,
.art-button,
.delete-activity,
.museum-info-button {
  margin-left: auto;
  margin: 10px;
  padding: 8px 16px;
  border: white;
  background: #333;
  color: #f2f2f2;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  border-radius: 2px;
}
</style>
