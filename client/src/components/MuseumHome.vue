<template>
  <div>
    <div class="art-generator">
      <button
        class="art-button"
        @click="showArtActivity = !showArtActivity"
        @click.prevent="showArtwork"
      >
        Click for Artwork and Activity!
      </button>
      <br />
      <div v-show="showArtActivity">
        <p>
          <strong>Ask your child</strong>
        </p>
        <ul>
          <li>What is going on in this image?</li>
          <li>What type of artwork is it?</li>
          <li>Have we seen anything similar?</li>
        </ul>
        <img class="artwork-image" v-bind:src="imgSrc" v-if="imgSrc" />
        <p>
          **Thank you
          <a href="https://www.harvardartmuseums.org/">Harvard Art Museum!**</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MuseumHome",
  props: [],
  data() {
    return {
      results: [],
      imgSrc: null,
      showArtActivity: false
    };
  },
  methods: {
    showArtwork() {
      const apiKey = "da60e2a0-f542-11e9-9327-73371ae36eb5";
      // external API call, random art is shown at each click.
      //potential to add a search feature.  This API is extremely easy to use and well documented.

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
  margin-left: auto;
  padding: 8px 16px;
  border: none;
  background: #333;
  color: #f2f2f2;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  border-radius: 2px;
}
img.artwork-image {
  -moz-transform: scale(0.65);
  -webkit-transform: scale(0.65);
  transform: scale(0.65);
}
</style>
