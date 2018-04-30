<template>
<div>
  <div class="md-layout">
  <TimelineItem :key="i" v-for="i in items" :titleS="i.title" :ctnt="i.ctnt"
                style="position: absolute; left: 25px" :style="{top: i.time * 120 + 'px'}">
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

  <md-button class="md-fab md-fab-bottom-right md-fixed md-primary" @click="showDialog = true">
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
      items: [{
        title: '1',
        ctnt: 'lol',
        time: 1
      }, {
        title: '2',
        ctnt: 'lol',
        time: 2
      }, {
        title: '3',
        ctnt: 'lol',
        time: 10
      }],
      showDialog: false
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
</style>
