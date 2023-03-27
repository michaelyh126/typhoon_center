import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import baidumap from "@/baidumap.vue";
import Test from "@/view/test.vue"



Vue.use(Router)

export default new Router({
  mode:'history',
  // base:'baidumap',
  routes: [
    {
      path: '/',
      name: 'baidumap',
      component: baidumap
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component:HelloWorld
    },
    {
      path: '/test',
      component:Test
    }

  ]
})
