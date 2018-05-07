<template>
<v-app id="inspire">
  <div>
  <TimelineItem class="tl-item" :key="i.id" v-for="i in items" :titleS="i.title" :ctnt="i.content"
                :style="{top: getVerticalOffset(i.date) + 'px', left: (25 + getFloatPos(i)) + 'px'}">
  </TimelineItem>
  </div>

  <v-dialog v-model="showDialog" max-width="600px">
    <v-card>
    <v-card-title>Preferences</v-card-title>
    <v-card-text>
      <v-text-field
        id="date"
        v-model="input_date"
        label="Date"
      ></v-text-field>
      <v-text-field
        id="title"
        v-model="input_title"
        label="Title"
      ></v-text-field>
      <v-text-field
        id="content"
        v-model="input_content"
        label="Content"
      ></v-text-field>
    </v-card-text>

    <v-card-actions>
      <v-btn right color="primary" @click="update">Add</v-btn>
    </v-card-actions>
    </v-card>
  </v-dialog>

  <v-btn fab fixed right bottom v-on:click="showDialog = true">
    <v-icon>add</v-icon>
  </v-btn>
  <div class="tl-line">
  </div>
</v-app>
</template>

<script>
import TimelineItem from './TimelineItem'
export default {
  name: 'Timeline',
  components: {
    TimelineItem
  },
  data: () => {
    return {
      items: [],
      showDialog: false,
      px_per_unit: 100,
      col_float: [0, 0, 0, 0, 0, 0, 0],
      input_title: '',
      input_date: '',
      input_content: '',
      startTimeStamp: new Date('2016-10-09').getTime(),
      WIDTH: 170,
      HEIGHT: 150
    }
  },
  methods: {
    update: function () {
      var bodyData = {
        id: Math.round(Date.now() / 100),
        title: this.input_title,
        date: this.input_date,
        content: this.input_content
      }

      this.$http.post('http://localhost:8888/events', bodyData).then((response) => {
        if (response.data === 'OKAY') {
          bodyData.offset = -1
          this.items.push(bodyData)
        }
      })
      this.input_content = ''
      this.input_title = ''
      this.input_date = ''
      // this.showDialog = false
    },
    getFloatPos: function (mt) {
      if (mt.offset !== -1) {
        return mt.offset * WIDTH
      }
      var mypos = this.getVerticalOffset(mt.date)
      var i
      var offset = 0

      for (i = 0; i < this.col_float.length; i++) {
        if (mypos >= this.col_float[i]) {
          this.col_float[i] = mypos + this.HEIGHT
          offset = i
          break
        }
      }
      mt.offset = offset

      // mt.title = offset.toString()

      return offset * this.WIDTH
    },
    getVerticalOffset: function(date) {
      var diffMilli = date.getTime() - this.startTimeStamp
      diffMilli /= (1000 * 60 * 60 * 24)
      return diffMilli * this.px_per_unit
    }
  }
}
</script>

<style scoped>
.tl-line{
  background-color: aquamarine;
  width: 7px;
  height: 100vh;
  position: fixed;
  top:0;
  left: 10px;
}
.tl-item {
  position: absolute;
  left: 25px;
}
</style>
