<template>
    <div class="field">
        <label> {{ fieldLabel }} </label>
        <!-- integer -->
        <input type="text" v-model="param.value | integer" name="{{param.name}}" v-if="param.type=='integer'">

        <!-- boolean -->
        <div class="ui toggle checkbox" v-if="param.type=='boolean'">
            <input type="checkbox"  v-model="param.value" name="{{param.name}} ":true-value="true"  :false-value="false">
            <lable></lable>
        </div>

        <!-- single -->
        <dropdown :options="param.options" :value.sync="param.value" v-if="param.type=='single'"></dropdown>
    </div>
</template>

<script>
    import Dropdown from '../basic/dropdown.vue'

    export default {
        components: {Dropdown},
        props: {
            param: {
                required: true
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

            }
        }
    }
</script>

<style>

</style>