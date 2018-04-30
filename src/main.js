// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Timeline from './components/Timeline'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

Vue.config.productionTip = false
Vue.use(VueMaterial)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { Timeline },
  template: '<Timeline/>'
})
