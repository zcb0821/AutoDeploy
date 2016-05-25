<template>
    <div class="ui segment">
        <div class="ui form" :class="{error:errors.length > 0}">
            <div class="ui message error">
                <div class="ui bulleted list">
                    <div class="item" v-for="error in errors">{{error}}</div>
                </div>
            </div>
            <div class="field">
                <label>集群名称</label>
                <input type="text" v-model="name">
            </div>
            <div class="field">
                <label>集群描述</label>
                <textarea v-model="description"></textarea>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            name: {}
        },
        data () {
            return {
                description: ''
            }
        },
        computed: {
            errors: function() {
                var errors = []
                if (!this.name.trim()) {
                    errors.push('请输入名称')
                }
                return errors
            }
        },
        methods: {
            isCompleted() {
                return this.errors.length == 0
            }
        }
    }
</script>

<style>
</style>
