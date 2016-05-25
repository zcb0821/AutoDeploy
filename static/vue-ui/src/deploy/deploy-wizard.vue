<template>
    <div class="ui long modal" id="new-deployment-model">
        <i class="close icon"></i>
        <div class="header">添加集群</div>
        <div class="content">
            <div class="ui ordered four steps">
                <div class="step" :class="{active: $index==state.activeStep, completed: $index < state.activeStep}"
                     v-for="step in steps">
                    <div class="content">
                        <div class="title">{{step.title}}</div>
                    </div>
                </div>
            </div>
            <info v-show="steps[state.activeStep].title=='基本信息'" v-ref:info :name.sync="name"></info>
            <asistance v-show="steps[state.activeStep].title=='辅助选型'" v-ref:asistance></asistance>
            <system-selection v-show="steps[state.activeStep].title=='构件选择'" v-ref:system-selection></system-selection>
            <config v-show="steps[state.activeStep].title=='参数配置'" v-ref:system-config></config>
        </div>
        <div class="actions">
            <div class="ui button" :class="{disabled:state.activeStep==0}" v-on:click="stepBackward()">上一步</div>
            <div class="ui button" v-if="steps[state.activeStep].skippable" v-on:click="skip()">跳过</div>
            <div class="ui button" v-on:click="willStepForward()">{{ state.activeStep==steps.length - 1 ? '启动部署':'下一步'}}
            </div>
        </div>
    </div>
</template>


<script>
    import Info from './info.vue'
    import Config from './config.vue'
    import SystemSelection from './system-selection.vue'
    import Asistance from './asistance.vue'

    export default {
        components: {Config, SystemSelection, Asistance, Info},
        data () {
            return {
                name: '',
                state: {
                    activeStep: 0
                },
                steps: [{
                    title: '基本信息',
                    skippable: false
                }, {
                    title: '辅助选型',
                    skippable: true
                }, {
                    title: '构件选择',
                    skippable: false
                }, {
                    title: '参数配置',
                    skippable: false
                }]
            }
        },
        computed: {
            activeComponent: function () {
                switch (this.state.activeStep) {
                    case 0:
                        return this.$refs.info
                    case 1:
                        return this.$refs.asistance
                    case 2:
                        return this.$refs.systemSelection
                    case 3:
                        return this.$refs.systemConfig
                    default:
                        return null
                }
            },
            nextComponent: function () {
                switch (this.state.activeStep) {
                    case 0:
                        return this.$refs.asistance
                    case 1:
                        return this.$refs.systemSelection
                    case 2:
                        return this.$refs.systemConfig
                    default:
                        return null
                }
            }
        },
        events: {
            error (message) {
                this.errorMessage = message
            }
        },
        methods: {
            stepBackward: function () {
                if (this.state.activeStep > 0) {
                    this.state.activeStep--
                }
                this.$nextTick(function () {
                    $(this.$el).modal('refresh')
                })
            },
            willStepForward () {
                var vm = this
                if (vm.activeComponent.isCompleted()) {
                    switch (vm.steps[vm.state.activeStep].title) {
                        case '基本信息':
                            vm.stepForward()
                            break
                        case '辅助选型':
                            var data = vm.activeComponent.requestData()
                            data.id = vm.id
                            $.post('/rest/assist/', data, function (response) {
                                if (!response.error) {
                                    vm.stepForward(response)
                                }
                            }, 'json')
                            break
                        case '构件选择':
                            var data = vm.activeComponent.requestData()
                            data.id = vm.id
                            this.systems = data
                            $.post("/rest/selectsystem/", data, function (response) {
                                if (!response.error) {
                                    vm.stepForward(response)
                                }
                            }, 'json')
                            break
                        case '参数配置':
                            var data = {
                                name: vm.name,
                                id: vm.id,
                                systems: vm.systems,
                                config: vm.activeComponent.requestData()
                            }
                            $.ajax({
                                url: "/rest/clusters/",
                                method: 'POST',
                                data: JSON.stringify(data),
                                success: function (response) {
                                    if (!response.error) {
                                        vm.$dispatch('deploy-finished', response)
                                        vm.stepForward(response)
                                    }
                                },
                                contentType: 'application/json',
                                dataType: 'json'
                            })
                            break
                        default:
                            break
                    }
                }
            },
            stepForward: function (data) {
                if (this.state.activeStep < this.steps.length - 1) {
                    this.nextComponent.init(data)
                    this.state.activeStep++
                    this.$nextTick(function () {
                        $(this.$el).modal('refresh')
                    })
                } else {
                    $(this.$el).modal('hide')
                }
            },
            skip () {
                this.state.activeStep++
                this.$nextTick(function () {
                    $(this.$el).modal('refresh')
                })
            },
            newCluster () {
                return {
                    name: ''
                }
            },
            init () {
                var vm = this
                this.state.activeStep = 0
                this.name = ''
                $.get('/rest/uuid/', function (response) {
                    if (!response.error) {
                        vm.id = response.uuid;
                        console.log('uuid: ' + vm.id)
                    }
                }, 'json')
            },
            show () {
                $(this.$el).modal('setting', 'closable', false)
                        .modal('setting', 'detachable', false)
                        .modal('setting', 'offset', 300)
                        .modal('show')
            }
        }
    }
</script>

<style>
</style>