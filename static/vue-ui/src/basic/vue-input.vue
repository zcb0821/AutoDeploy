<template>
    <input type="text" v-on:change="entered" v-on:keyup.enter="entered"/>
</template>

<script>
    export default {
        props: {
            value: {
                required: true
            },
            type: {
                default () {
                    return 'string'
                }
            },
            validate: {
                default () {
                    return null
                }
            }
        },
        ready () {

        },
        data () {
            return {

            }
        },
        watch: {
            value: function (val, oldval) {
                if (val !== null) {
                    this.$el.setAttribute('value', val)
                }
            }
        },
        methods: {
            convert (text) {
                switch (this.type) {
                    case 'string':
                        this.value = text
                        break
                    case 'integer':
                        this.value = parseInt(text)
                        if (isNaN(this.value)) {
                            this.$dispatch('error', 'Please enter an integer ！')
                            this.value = null
                            return
                        }
                        break
                    case 'number':
                        this.value = parseFloat(text)
                        if (isNaN(this.value)) {
                            this.$dispatch('error', 'Please enter a number ！')
                            this.value = null
                            return
                        }
                        break
                    default:
                        break
                }
                if (typeof(this.validate) === 'function') {
                    this.$dispatch('error', this.validate.call(this, this.value))
                } else {
                    this.$dispatch('error', '')
                }
            }
        },
        entered () {
            var text = this.$el.getattribute('value')
            this.convert(text)
        }
    }
</script>