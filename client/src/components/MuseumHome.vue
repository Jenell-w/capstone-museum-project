<template>
  <div class="art-generator">
    <button class="art-button" @click.prevent="showArtwork">
      Show Me Some Artwork!
    </button>
    <br />
    <p>
      Thank you
      <a href="https://www.harvardartmuseums.org/">Harvard Art Museum!</a>
    </p>
    <p>
      <strong>Ask your child</strong>
    </p>
    <ul>
      <li>What is going on in this image?</li>
      <li>What type of artwork is it?</li>
      <li>Have we seen anything similar?</li>
    </ul>
    <br />
    <img id="artwork-image" v-bind:src="imgSrc" v-if="imgSrc" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MuseumHome",
  props: ["activity"],
  data() {
    return {
      results: [],
      imgSrc: null
    };
  },
  methods: {
    deleteActivity() {
      axios
        .delete("/add-activity/" + this.new_activity.id)
        .then(() => this.viewAllActivities);
      // this method needs to move to another component with the Patch method?
    },
    showArtwork() {
      const apiKey = "da60e2a0-f542-11e9-9327-73371ae36eb5";
      // external API call, random art is shown, wish it was a more vivid, classic collection.
      axios
        .get(
          `https://api.harvardartmuseums.org/image?sort=random&apikey=${apiKey}`
        )
        .then(response => {
          console.log("we got a response!");
          this.imgSrc = response.data.records["0"].baseimageurl;
          console.log(response);
        });
    }
  }
};
</script>

<style scoped>
.art-button {
  background-color: coral;
  font-size: 75%;
}
.art-button:hover {
  font-style: italic;
  font-size: 100%;
}
</style>
