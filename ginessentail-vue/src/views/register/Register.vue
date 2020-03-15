<template>
  <div class="register">
    <b-row class="mt-5">
      <b-col
        md="8"
        offset-md="2"
        lg="6"
        offset-lg="3"
      >
        <b-card title="注册">
          <b-form>
            <b-form-group label="名称">
              <b-form-input
                v-model="user.name"
                type="text"
                placeholder="请输入名称（选填）"
              />
            </b-form-group>
            <b-form-group label="手机号">
              <b-form-input
                v-model="user.telephone"
                type="number"
                placeholder="请输入手机号"
              />
            </b-form-group>
            <b-form-group label="密码">
              <b-form-input
                v-model="user.password"
                type="password"
                placeholder="请输入密码"
              />
            </b-form-group>
            <b-form-group>
              <b-button
              @click="register"
              variant="outline-primary"
              block
              >注册</b-button>
            </b-form-group>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        name: '',
        telephone: '',
        password: '',
      },
    }
  },
  methods: {
    register() {
      console.log('register')
    },
  },
}
</script>

<style></style>
