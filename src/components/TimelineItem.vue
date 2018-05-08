<template>
  <v-card class="event-card">
    <v-layout row warp style="height:170px">
    <v-card-title style="position:absolute;right:0;height:110px;width:100%;text-align: right;" :style="{backgroundColor: getColor()}">
    {{ date }}
    </v-card-title>

    <v-card-text style="position:absolute; height: 60px;top:110px;">
      {{titleS}}
    </v-card-text>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'TimelineItem',
  props: {
    titleS: String,
    date: String
  },
  data: function () {
    return {
      colors: ['#F44336',
        '#E91E63',
        '#9C27B0',
        '#673AB7',
        '#3F51B5',
        '#2196F3',
        '#03A9F4',
        '#00BCD4',
        '#009688',
        '#4CAF50',
        '#8BC34A',
        '#CDDC39',
        '#FFEB3B',
        '#FFC107',
        '#FF9800',
        '#FF5722',
        '#795548',
        '#9E9E9E',
        '#607D8B'],
      color_count: 19
    }
  },
  methods: {
    getColor: function () {
      var t = this.colors[Math.floor(Math.random() * Math.floor(this.color_count))]
      console.log(t)
      return t
    }
  }
}
</script>

<style scoped>
.event-card {
  width: 250px;
}
</style>
