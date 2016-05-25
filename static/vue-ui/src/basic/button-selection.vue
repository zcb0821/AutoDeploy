<template>
    <div class="ui buttons">
        <button class="ui button" :class="{blue: value==option.value}" v-for="option in options" v-on:click="select(option)">
            {{option.title}}
        </button>
    </div>
</template>

<script>
    export default {
        props: {
            options: {
                required: true,
                type: Array,
                coerce: function(val) {
                    for (var i = 0; i < val.length; i++) {
                        if (typeof(val[i]) != "object") {
                            val[i] = {
                                value: val[i],
                                title: val[i].toString()
                            }
                        }
                    }
                    return val
                },
                default: function() {
                    return []
                }
            },
            value: {
                required: true
            }
        },
        data () {
            return {

            }
        },
        methods: {
            select: function(option) {
                this.value = option.value
            }
        }
    }
</script>

<style>

</style>