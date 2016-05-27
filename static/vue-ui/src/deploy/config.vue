<template>
    <div class="ui segment">
        <div class="ui pointing menu">
            <a class="item" :class="{active: state.activeIndex == $index}"v-for="system in systemConfigs" v-on:click="selectSystem($index)">{{system.title ? system.title : system.name}}</a>
        </div>
        <div class="ui segment">
            <div class="ui form" v-for="system in systemConfigs" v-show="state.activeIndex == $index">
                <div class="field" v-for="param in system.paramlist">
                    <label>{{fieldTitle(param)}}</label>
                    <!-- txt or number -->
                    <input type="text" v-model="param.value" name="{{param.name}}" v-if="param.type=='txt' || param.type=='number'">

                    <!-- btn_enum -->
                    <button-select :options="param.options" :value.sync="param.value" v-if="param.type=='btn_enum'"></button-select>

                    <!-- boolean -->
                    <div class="ui toggle checkbox" v-if="param.type=='boolean'">
                        <input type="checkbox"  v-model="param.value" :true-value="true"  :false-value="false">
                    </div>

                    <!-- selection -->
                    <dropdown :options="param.options" :value.sync="param.value" v-if="param.type=='enum'"></dropdown>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    function HWParams() {
        return {
            title: '硬件',
            name: 'Hardware',
            paramlist: [{
                title: '节点数',
                name: "nodeNumber",
                type: 'btn_enum',
                options: [1, 2, 3, 4, 5, 6, 7, 8, 9],
                default: 2,
                value: 2
            }, {
                title: 'CPU 核数',
                name: "cpuCoreNumber",
                type: 'btn_enum',
                options: [1, 2, 4, 8, 16],
                default: 2,
                value: 2
            }, {
                title: '内存',
                name: "memorySize",
                type: 'btn_enum',
                options: [1, 2, 4, 8, 16],
                default: 2,
                value: 2,
                unit: 'GB'
            }, {
                title: '硬盘',
                name: "diskSize",
                type: 'number',
                default: 2,
                value: 50,
                unit: 'GB'
            }]
        }
    }

    function LinuxParams() {
        return {
            name: "Linux",
            title: 'Linux 系统',
            paramlist: [{
                type: 'number',
                name: 'file_max',
                default: 4096,
                value: 4096
            }, {
                type: 'number',
                name: 'ulimit',
                default: 1024,
                value: 1024
            }, {
                type: 'number',
                name: 'max_map_count',
                default: 65530,
                value: 65530
            }, {
                type: 'number',
                name: 'wmem_max',
                default: 131071,
                value: 131071
            }, {
                type: 'number',
                name: 'rmem_max',
                default: 131071,
                value: 131071
            }]
        }
    }

    import ButtonSelect from '../basic/button-selection.vue'
    import Dropdown from '../basic/dropdown.vue'

    export default {
        components: {ButtonSelect, Dropdown},
        data () {
            return {
                systemConfigs: [HWParams(), LinuxParams()],
                state: {
                    activeIndex: 0
                }
            }
        },
        watch: {
            systemConfigs: function() {
                this.$nextTick(function () {
                    $(this.$el).find('.ui.checkbox').checkbox()
                })
            }
        },
        methods: {
            // dom events
            selectSystem: function(index) {
                this.state.activeIndex = index
            },

            // utilities
            fieldTitle: function(param) {
                var title = param.title ? param.title : param.name
                return param.unit ? title + ' (' + param.unit + ')' : title;
            },

            isCompleted () {
                return true
            },

            // wizard
            willLeave: function(id, success) {
                console.log(this.getConfigs())
                $.post("/rest/clusters/", this.requestData(), function(data) {
                    // todo：do something when success
                    if (data.result == 'success') {

                    } else {
                        // todo: error
                    }
                }, 'json')
            },

            init: function(data) {
                this.systemConfigs = [HWParams(), LinuxParams()]
                if (data && data.paramgroup) {
                    var paramgroup = data.paramgroup
                    for (var i = 0; i < paramgroup.length; i++) {
                        paramgroup[i].name = paramgroup[i].systemname
                        paramgroup[i].title = paramgroup[i].showname ? paramgroup[i].showname : paramgroup[i].systemname

                        var plist = paramgroup[i].paramlist
                        for (var j in plist) {
                            plist[j].title = plist[j].showname ? plist[j].showname : plist[j].name
                            plist[j].value = plist[j].defaultval
                            plist[j].options = plist[j].selections
                        }
                        this.systemConfigs.push(paramgroup[i]);
                    }
                }
            },
            requestData: function() {
                var systems = JSON.parse(JSON.stringify(this.systemConfigs));
                var postData = {};
                for (var i in systems) {
                    var temp = {}
                    for (var j in systems[i].paramlist) {
                        temp[systems[i].paramlist[j].name] = systems[i].paramlist[j].value;
                    }
                    postData[systems[i].name] = temp
                }
                return postData
            }
        }
    }
</script>

<style>
</style>