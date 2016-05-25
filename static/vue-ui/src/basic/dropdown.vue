<template>
    <div class="ui selection dropdown">
        <input type="hidden">
        <i class="dropdown icon"></i>
        <div class="text"></div>
        <div class="menu">
            <div class="item" data-value="{{$index}}" v-for="option in options">{{option.title}}</div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            options: {
                required: true,
                type: Array,
                coerce: function (val) {
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
                default: function () {
                    return []
                }
            },
            value: {
                required: true
            }
        },
        watch: {
            value: function () {
                console.log(this.value)
            }
        },
        data () {
            return {

            }
        },
        ready: function() {
            var vm = this

            $(this.$el).dropdown({
                action: 'activate',
                onChange: function(value, text, $choice) {
                    var option = vm.options[parseInt(value)]
                    vm.value = option.value
                }
            })

            for (var i in this.options) {
                if (this.options[i].value == this.value) {
                    $(this.$el).dropdown('set selected ', i.toString())
                    break;
                }
            }
        }
    }
</script>

<style>

</style>