<template>
  <div class="art-generator">
    <!-- how to make this button only appear when on this page? -->
    <button @click.prevent="showArtwork">Show Me Some Artwork!</button>
    <br />
    <img id="artwork-image" v-bind:src="imgSrc" v-if="imgSrc" />
    <!-- could the external api call be another component? -->

    <div class="museum-activities-container">
      <br />
      <button @click="deleteActivity">Delete this entry</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MuseumHome",
  props: ["activities", "viewAllActivities"],
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
      // write route with PATCH method in MusAPI.py.  see Phil's patch
      //       @todos_api.route('/todo', methods=['PATCH'])
      // def toggle_done():
      //     todo_id = request.json["id"]
      //     target_todo = db.session.query(Todo).filter_by(id=todo_id).first()
      //     target_todo.done = not target_todo.done
      //     db.session.add(target_todo)
      //     db.session.commit()
      //     return jsonify(success=True)
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
.museum-activities-container {
  display: flex;
}
</style>
