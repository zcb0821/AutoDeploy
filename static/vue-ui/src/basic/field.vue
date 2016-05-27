<template>
    <div class="field" :class="{error: error}">
        <label> {{ fieldLabel }} </label>
        <!-- integer -->
        <input type="text" v-model="param.value | integer" placeholder="请输入整数" name="{{param.name}}" v-if="param.type=='integer'">

        <!-- boolean -->
        <div class="ui toggle checkbox" v-if="param.type=='boolean'">
            <input type="checkbox"  v-model="param.value" name="{{param.name}} ":true-value="true"  :false-value="false">
            <lable></lable>
        </div>

        <!-- single -->
        <dropdown :options="param.options" :value.sync="param.value" v-if="param.type=='single'"></dropdown>
        <p class="error">{{ error }}</p>
    </div>
</template>

<script>
    import Dropdown from '../basic/dropdown.vue'
    import VueInput from '../basic/vue-input.vue'

    export default {
        components: {Dropdown, VueInput},
        props: {
            param: {
                required: true
            },
            canBlank: {
                default () {
                    return true
                }
            }
        },
        computed: {
            fieldLabel () {
                var title = this.param.title ? this.param.title : this.param.name
                return this.param.unit ? title + ' (' + this.param.unit + ')' : title
            }
        },
        data () {
            return {
                error: ''
            }
        },
        events: {
            'error': function (message) {
                this.error = message
            }
        }
    }
</script>

<style>
    .field > p {
        margin-top: 6px;
        margin-left: 10px;
    }
    .filed > p.error {
        color: #9f3a38;
    }
</style>