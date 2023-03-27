<!--
 * @Author: daidai
 * @Date: 2022-03-04 09:23:59
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-05-07 11:05:02
 * @FilePath: \web-pc\src\pages\big-screen\view\indexs\index.vue
-->
<template>

  <div class="contents">
    <div class="contetn_left">
      <div class="pagetab">
        <!-- <div class="item">实时监测</div> -->

      </div>
      <el-button @click="typhoon_center"></el-button>
      <ItemWrap class="contetn_left-top contetn_lr-item" title="设备总览">
        <LeftTop/>

      </ItemWrap>
      <ItemWrap class="contetn_left-center contetn_lr-item" title="用户总览">
        <LeftCenter />
      </ItemWrap>





      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="设备提醒"
        style="padding: 0 10px 16px 10px"
      >
        <el-image class="img" :src="ty_data">
          <div slot="error" class="image-slot">
            <i class="el-icon-picture-outline"></i>
          </div>
        </el-image>
      </ItemWrap>





    </div>
    <div class="contetn_center">
      <CenterMap ref="centerMap" class="contetn_center_top" />
      <ItemWrap class="contetn_center-bottom" title="安装计划">
        <CenterBottom />
      </ItemWrap>
    </div>
    <div class="contetn_right">






      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="风云数据接入"
      >
<!--        <RightTop />-->
        <div class="block">
          <div></div>
<!--          <div><span class="demonstration">风云数据接入</span></div>-->
          <el-image class="img" :src="src1">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>
        </div>
        <el-upload
            class="upload-demo"
            action="0"
            :http-request="uploadFile"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            multiple
            :limit="1"
            :on-exceed="handleExceed"
            :file-list="fileList">
<!--          <el-button size="small" icon="el-icon-my-export" type="primary">点击上传</el-button>-->
          <!--          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>-->
          <el-image class="icon" :src="icon_button">
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>

        </el-upload>

      </ItemWrap>







      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="台风检测结果"
        style="padding: 0 10px 16px 10px"
      >
        <div class="block">
<!--          <div><span class="demonstration">台风检测结果</span></div>-->

          <el-image class="img" :src="src2"
                    v-loading="loading"
                    element-loading-spinner="el-icon-loading"
                    element-loading-background="rgba(255, 255,255, 0.5)"
                    element-loading-text="加载中..."

          >
            <div slot="error" class="image-slot">
              <i class="el-icon-picture-outline"></i>
            </div>
          </el-image>

        </div>
<!--        <RightCenter />-->
      </ItemWrap>








      <ItemWrap
        class="contetn_left-bottom contetn_lr-item"
        title="数据统计图 "
      >
        <RightBottom />
      </ItemWrap>
    </div>
  </div>
</template>

<script>
import LeftTop from './left-top.vue'
import LeftCenter from "./left-center.vue";
import LeftBottom from "./left-bottom.vue";
import CenterMap from "./center-map.vue";
import CenterBottom from "./center-bottom.vue";
import RightTop from "./right-top.vue";
import RightCenter from "./right-center.vue";
import RightBottom from "./right-bottom.vue";
import jpg from '@/assets/img/storm.jpg'
import Baidumap from "@/views/indexs/baidumap";
import icon_button from '@/assets/img/xiezuo.png'
import loading_gif from '../../assets/img/loading.gif';
import axios from 'axios';

export default {
  components: {
    LeftTop,
    LeftCenter,
    LeftBottom,
    CenterMap,
    RightTop,
    RightCenter,
    RightBottom,
    CenterBottom,
  },
  data() {
    return {
      gif:loading_gif,
      src1:jpg,
      src2:jpg,
      ty_data:"http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG",
      icon_button:icon_button,
      loading: false
    };
  },
  filters: {
    numsFilter(msg) {
      return msg || 0;
    },
  },
  created() {
  },

  mounted() {
    const timer = setInterval(()=>{
      // 这里调用调用需要执行的方法，1为自定义的参数，由于特殊的需求它将用来区分，定时器调用和手工调用，然后执行不同的业务逻辑
      console.log('great')
      this.ty_data="http://img.nsmc.org.cn/CLOUDIMAGE/FY4A/MTCC/FY4A_CHINA.JPG"
    }, 1000*60*60) // 每1h执行1次
// 通过$once来监听定时器，在beforeDestroy钩子可以被清除
    this.$once('hook:beforeDestroy',()=>{
      // 在页面销毁时，销毁定时器
      clearInterval(timer)
    })


  },
  methods: {

    typhoon_center(){
      this.$refs.centerMap.change_src0(120.22,30.33)

    },


    uploadFile(params) {
      // debugger
      console.log("uploadFile", params);
      // this.src1="https://media.nationalgeographic.org/assets/photos/180/373/87b29588-8cdf-44d1-9ed5-798e29482750.jpg"
      const _file = params.file;
      const url1 = window.URL.createObjectURL(_file)
      this.src1=url1
      // const isLt2M = _file.size / 1024 / 1024 < 2;

      // 通过 FormData 对象上传文件
      var formData = new FormData();
      formData.append("file", _file);

      // if (!isLt2M) {
      //   this.$message.error("请上传2M以下的.xlsx文件");
      //   return false;
      var that=this

      that.loading=true
      axios.request({
        url: 'http://127.0.01:5554/get_image',
        method: 'post',
        data: formData,
        responseType: 'blob'
      })

          .then(function (res) {
            // debugger
            const url2 = window.URL.createObjectURL(res.data)
            console.log(url2)
            that.src2=url2
          })
          .catch(function (error) {

          });


      that.loading=false
    },


    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    }

  },
};
</script>
<style lang="scss" scoped>


.el-loading-spinner{
  /*这个是自己想设置的 gif 加载动图*/
  background-image:url('../../assets/img/loading.gif');
  background-repeat: no-repeat;
  background-size: 200px 120px;
  height:100px;
  width:100%;
  background-position:center;
  /*覆盖 element-ui  默认的 50%    因为此处设置了height:100%,所以不设置的话，会只显示一半，因为被top顶下去了*/
  top:40%;
}


.el-loading-spinner .circular {
  /*隐藏 之前  element-ui  默认的 loading 动画*/

  display: none;

}

.el-loading-spinner .el-loading-text {
  /*为了使得文字在loading图下面*/
  margin: 85px 0px;

}

.icon{
  width: 16px;
  height: 16px;
}


.img{
  width:100%;
  height: 250px;
}


// 内容
.contents {
  .contetn_left,
  .contetn_right {
    width: 540px;
    box-sizing: border-box;
    // padding: 16px 0;
  }

  .contetn_center {
    width: 720px;
  }

  //左右两侧 三个块
  .contetn_lr-item {
    height: 310px;
  }

  .contetn_center_top {
    width: 100%;
  }

  // 中间
  .contetn_center {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }

  .contetn_center-bottom {
    height: 315px;
  }

  //左边 右边 结构一样
  .contetn_left,
  .contetn_right {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    position: relative;


  }
}


@keyframes rotating {
    0% {
        -webkit-transform: rotate(0) scale(1);
        transform: rotate(0) scale(1);
    }
    50% {
        -webkit-transform: rotate(180deg) scale(1.1);
        transform: rotate(180deg) scale(1.1);
    }
    100% {
        -webkit-transform: rotate(360deg) scale(1);
        transform: rotate(360deg) scale(1);
    }
}
</style>
