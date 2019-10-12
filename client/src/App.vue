<template>
  <div id="app">
    <div class="navigation-button">
      <button @click="handleNav">{{ buttonText }}</button>
    </div>
    <img
      v-if="!showMuseumHome"
      alt="museum image"
      src="https://thumbs.dreamstime.com/z/museum-visitors-looking-painting-hanging-gallery-wall-people-viewing-museum-museum-visitors-looking-painting-99760302.jpg"
      width="350"
      height="150"
    />
    <MuseumActivities
      v-if="!showMuseumHome"
      title="Welcome to Family ViewSeums!"
    />
    <MuseumHome v-if="showMuseumHome" />
  </div>
</template>

<script>
import MuseumActivities from "./components/MuseumActivities.vue";
import MuseumHome from "./components/MuseumHome.vue";

export default {
  name: "app",
  components: {
    MuseumActivities,
    MuseumHome
  },
  data() {
    return {
      showMuseumHome: false,
      buttonText: "Go to Activity Page"
    };
  },
  methods: {
    handleNav() {
      this.showMuseumHome = !this.showMuseumHome;
      if (this.buttonText === "Go to Activity Page") {
        this.buttonText = "Go to Family Viewseums Home";
      } else {
        this.buttonText = "Go to Activity Page";
      }
    }
  }
};
</script>

<style></style>
