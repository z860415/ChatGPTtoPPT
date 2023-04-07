<template>
  <div class="container">
    <h1 class="title">AI 教材生成器</h1>
    <div class="form">
      <el-input v-model="inputValue" placeholder="請輸入主題"></el-input>
      <div class="spacer"></div>
      <el-button :loading="isLoading" @click="submit">送出</el-button>
    </div>
    <div v-if="isLoading" class="loading-mask">
      <div class="loading-spinner"></div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { ElInput, ElButton } from 'element-plus';
import axios from 'axios';

export default defineComponent({
  components: { ElInput, ElButton },
  data() {
    return {
      inputValue: '',
      isLoading: false,
    };
  },
  methods: {
    async submit() {
      this.isLoading = true;
      try {
        const response = await axios.post('http://localhost:8086/get_ppt/get_ppt_file', {
          title: this.inputValue,
        }, {
          responseType: 'blob', // 指定响应类型为二进制数据流
        });
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'pptx_file.pptx'); // 指定下载文件名
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      } catch (error) {
        console.error(error);
      } finally {
        this.isLoading = false;
      }
    },
  },
});
</script>


<style scoped>
.container {
  background-color: #1c2331;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  color: #fff;
  font-size: 36px;
  margin-bottom: 30px;
}

.form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.spacer {
  height: 30px;
}

.loading-mask {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-spinner {
  border: 4px solid #fff;
  border-top: 4px solid #1c2331;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
