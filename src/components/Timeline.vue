<template>
<div>
  <div class="md-layout">
  <TimelineItem class="tl-item" :key="i.id" v-for="i in items" :titleS="i.title" :ctnt="i.content"
                :style="{top: i.time * px_per_day + 'px', left: (25 + getFloatPos(i)) + 'px'}">
  </TimelineItem>
  </div>

  <md-dialog :md-active.sync="showDialog" :md-backdrop="false">
    <md-dialog-title>Preferences</md-dialog-title>
      <md-dialog-content>CONTENT</md-dialog-content>

    <md-dialog-actions>
      <md-button class="md-primary" @click="showDialog = false">Close</md-button>
      <md-button class="md-primary" @click="showDialog = false">Save</md-button>
    </md-dialog-actions>
  </md-dialog>

  <md-button class="md-fab md-fab-bottom-right md-fixed md-primary" @click="update">
    <md-icon>add</md-icon>
  </md-button>
  <div class="tl-line">
  </div>
</div>
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
      px_per_day: 100,
      test: 1
    }
  },
  methods: {
    update: function () {
      /* this.$http.get('http://localhost:8888/events').then(response => {
        console.log(response.body)
        this.items.push(response.body)
      }) */
      this.items.push({
        id: this.test,
        title: this.test.toString(),
        content: 'lol',
        time: 2
      })
      this.test++
    },
    getFloatPos: function (mt) {
      var mypos = mt.time * this.px_per_day
      var curData = this.items
      var i
      var offset = 0
      console.log('len: ' + curData.length)
      for (i = 0; i < curData.length; i++) {
        if (curData[i].time * this.px_per_day <= mypos &&
          curData[i].time * this.px_per_day + 100 > mypos &&
          curData[i].id !== mt.id) {
          offset++
        }
      }
      return offset * 170
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
