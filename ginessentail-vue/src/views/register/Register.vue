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
                v-model="$v.user.name.$model"
                type="text"
                placeholder="请输入名称（选填）"
              />
            </b-form-group>
            <b-form-group label="手机号">
              <b-form-input
                v-model="$v.user.telephone.$model"
                type="number"
                placeholder="请输入手机号"
                :state="validateState('telephone')"
              />
              <b-form-invalid-feedback :state="validateState('telephone')">
                手机号非法
              </b-form-invalid-feedback>
              <b-form-valid-feedback :state="validateState('telephone')">
                手机号合法
              </b-form-valid-feedback>
            </b-form-group>
            <b-form-group label="密码">
              <b-form-input
                v-model="$v.user.password.$model"
                type="password"
                placeholder="请输入密码"
                :state="validateState('password')"
              />
              <b-form-invalid-feedback :state="validateState('password')">
                密码不能小于6位
              </b-form-invalid-feedback>
              <b-form-valid-feedback :state="validateState('password')">
                密码合法
              </b-form-valid-feedback>
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
import {
  required, minLength,
} from 'vuelidate/lib/validators'
import customValidator from '../../helper/validator'

export default {
  data() {
    return {
      user: {
        name: '',
        telephone: '',
        password: '',
      },
      validation: null,
    }
  },
  validations: {
    user: {
      name: {

      },
      telephone: {
        required,
        // minLength: minLength(11),
        // maxLength: maxLength(11),
        telephone: customValidator.telephoneValidator,
      },
      password: {
        required,
        minLength: minLength(6),
      },
    },
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.user[name]
      return $dirty ? !$error : null
    },
    register() {
      if (this.user.telephone.length !== 11) {
        this.validation = false
        return
      }
      this.validation = true

      console.log('register')
    },
  },
}
</script>

<style></style>
