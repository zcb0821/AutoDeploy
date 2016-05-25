<template>
    <div class="ui segment">
        <div class="ui form">
            <!-- 需求类型 -->
            <field :param.sync="parameters.requiretype"></field>
            <!-- 存储参数 -->
            <field :param.sync="parameters.storagetype"></field>
            <!-- 计算参数 -->
            <field :param.sync="parameters.computereactiontime"
                   v-show="parameters.requiretype.value=='compute'"></field>
            <field :param.sync="parameters.computetype" v-show="parameters.requiretype.value=='compute'"></field>
            <!-- 分析参数 -->
            <field :param.sync="parameters.analysereactiontime"
                   v-show="parameters.requiretype.value=='analyse'"></field>

            <field :param.sync="parameters.consistency"></field>
            <field :param.sync="parameters.queryreactiontime"></field>
            <field :param.sync="parameters.availablity"></field>
            <field :param.sync="parameters.replication"></field>
            <field :param.sync="parameters.dataimport"></field>

            <field :param.sync="parameters.datatype"></field>
            <field :param.sync="parameters.dataaveragesize"></field>
            <field :param.sync="parameters.datasizeofcount" v-show="isCount"></field>
            <field :param.sync="parameters.dataincreaseofcount" v-show="isCount"></field>
            <field :param.sync="parameters.readthroughputofcount" v-show="isCount"></field>
            <field :param.sync="parameters.writethroughputofcount" v-show="isCount"></field>

            <field :param.sync="parameters.datasizeofgb" v-show="isSize"></field>
            <field :param.sync="parameters.dataincreaseofmb" v-show="isSize"></field>
            <field :param.sync="parameters.readthroughputofkb" v-show="isSize"></field>
            <field :param.sync="parameters.writethroughputofkb" v-show="isSize"></field>

            <field :param.sync="parameters.readlatency"></field>
            <field :param.sync="parameters.writelatency"></field>
            <field :param.sync="parameters.concurrent"></field>
            <field :param.sync="parameters.maxconcurrent"></field>
        </div>
    </div>
</template>

<script>
    import Dropdown from '../basic/dropdown.vue'
    import Field from '../basic/field.vue'

    export default {
        components: {Dropdown, Field},
        data () {
            return {
                parameters: this.newParameters()
            }
        },
        ready () {
            $('.ui.checkbox').checkbox()
        },
        watch: {
            'isSize': function () {
                this.parameters.dataaveragesize.title = this.isSize ? '文件平均大小' : '单条数据平均大小'
            },
            'requiretype': function () {
                if (this.parameters.requiretype.value == 'store') {
                    this.parameters.computereactiontime.value = 'NA'
                    this.parameters.computetype.value = 'NA'
                    this.parameters.analysereactiontime.value = 'NA'
                } else if (this.parameters.requiretype.value == 'compute') {
                    this.parameters.analysereactiontime.value = 'NA'
                }
            }
        },
        computed: {
            isCount () {
                return this.parameters.datatype.value == 'table' || this.parameters.datatype.value == 'kv'
            },
            isSize () {
                return this.parameters.datatype.value == 'file' || this.parameters.datatype.value == 'text'
            }
        },
        methods: {
            isCompleted () {
                return true
            },
            init () {
                this.parameters = this.newParameters()
            },
            newParameters () {
                return {
                    requiretype: {
                        title: '需求类型',
                        name: 'requiretype',
                        type: 'single',
                        default: 'store',
                        value: 'store',
                        options: [{
                            title: '存储',
                            value: 'store',
                        }, {
                            title: '计算',
                            value: 'compute'
                        }, {
                            title: '分析',
                            value: 'analyse'
                        }]
                    },
                    storagetype: {
                        title: '存储类型',
                        name: 'storagetype',
                        type: 'single',
                        default: 'write',
                        value: 'write',
                        options: [{
                            title: '写为主',
                            value: 'write'
                        }, {
                            title: '读为主',
                            value: 'read'
                        }, {
                            title: '读写混合',
                            value: 'any'
                        }]
                    },
                    consistency: {
                        title: '数据一致性',
                        name: 'consistency',
                        type: 'single',
                        default: 'strong',
                        value: 'strong',
                        options: [{
                            title: '强一致性',
                            value: 'strong'
                        }, {
                            title: '最终一致性',
                            value: 'eventual'
                        }, {
                            title: '弱一致性',
                            value: 'weak'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    computetype: {
                        title: '计算类型',
                        name: 'computetype',
                        type: 'single',
                        default: 'single',
                        value: 'single',
                        options: [{
                            title: '单次',
                            value: 'single'
                        }, {
                            title: '迭代',
                            value: 'iteration'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    queryreactiontime: {
                        title: '数据查询实时性(响应速度)',
                        name: 'queryreactiontime',
                        type: 'single',
                        default: 'realtime',
                        value: 'realtime',
                        options: [{
                            title: '实时',
                            value: 'realtime'
                        }, {
                            title: '秒级',
                            value: 'secound'
                        }, {
                            title: '分钟级',
                            value: 'minute'
                        }, {
                            title: '小时级',
                            value: 'hour'
                        }, {
                            title: '离线',
                            value: 'offline'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    computereactiontime: {
                        title: '计算响应速度',
                        name: 'computereactiontime',
                        type: 'single',
                        default: 'realtime',
                        value: 'realtime',
                        options: [{
                            title: '实时',
                            value: 'realtime'
                        }, {
                            title: '秒级',
                            value: 'secound'
                        }, {
                            title: '分钟级',
                            value: 'minute'
                        }, {
                            title: '小时级',
                            value: 'hour'
                        }, {
                            title: '离线',
                            value: 'offline'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    analysereactiontime: {
                        title: '数据分析实时性(响应速度)',
                        name: 'analysereactiontime',
                        type: 'single',
                        default: 'realtime',
                        value: 'realtime',
                        options: [{
                            title: '实时',
                            value: 'realtime'
                        }, {
                            title: '秒级',
                            value: 'secound'
                        }, {
                            title: '分钟级',
                            value: 'minute'
                        }, {
                            title: '小时级',
                            value: 'hour'
                        }, {
                            title: '离线',
                            value: 'offline'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    availablity: {
                        title: '系统可用性',
                        name: 'availablity',
                        type: 'single',
                        default: 'high',
                        value: 'high',
                        options: [{
                            title: '高',
                            value: 'high'
                        }, {
                            title: '低',
                            value: 'low'
                        }, {
                            title: '不知道',
                            value: 'NA'
                        }]
                    },
                    datatype: {
                        title: '数据类型',
                        name: 'datatype',
                        type: 'single',
                        default: 'table',
                        value: 'table',
                        options: [{
                            title: '关系表',
                            value: 'table'
                        }, {
                            title: '键值对',
                            value: 'kv'
                        }, {
                            title: '二进制文件',
                            value: 'file'
                        }, {
                            title: '文档/日志',
                            value: 'text'
                        }]
                    },
                    replication: {
                        title: '最少副本数',
                        name: 'replication',
                        type: 'single',
                        default: 1,
                        value: 1,
                        options: [{
                            title: '1',
                            value: 1
                        }, {
                            title: '2',
                            value: 2
                        }, {
                            title: '3',
                            value: 3
                        }]
                    },
                    dataimport: {
                        title: '是否导入数据',
                        name: 'dataimport',
                        type: 'boolean',
                        value: true,
                        default: true
                    },
                    dataaveragesize: {
                        title: '文件平均大小',
                        name: 'dataaveragesize',
                        type: 'integer',
                        value: null,
                        unit: '字节'
                    },

                    datasizeofgb: {
                        title: '数据量',
                        name: 'datasizeofgb',
                        type: 'integer',
                        unit: 'GB',
                        value: null
                    },
                    dataincreaseofmb: {
                        title: '日增量（总MB）',
                        name: 'dataincreaseofmb',
                        type: 'integer',
                        value: null
                    },
                    readthroughputofkb: {
                        title: '读吞吐量（KB/秒）',
                        name: 'readthroughputofkb',
                        type: 'integer',
                        value: null
                    },
                    writethroughputofkb: {
                        title: '写吞吐量（KB /秒）',
                        name: 'writethroughputofkb',
                        type: 'integer',
                        value: null
                    },

                    datasizeofcount: {
                        title: '数据量（总条数）',
                        name: 'datasizeofcount',
                        type: 'integer',
                        value: null
                    },
                    dataincreaseofcount: {
                        title: '日增量（总条数）',
                        name: 'dataincreaseofcount',
                        type: 'integer',
                        value: null
                    },
                    readthroughputofcount: {
                        title: '读吞吐量（读条数/秒）',
                        name: 'readthroughputofcount',
                        type: 'integer',
                        value: null
                    },
                    writethroughputofcount: {
                        title: '写吞吐量（写条数/秒）',
                        name: 'writethroughputofcount',
                        type: 'integer',
                        value: null
                    },

                    readlatency: {
                        title: '客户端并发数为100时的读延迟',
                        name: 'readlatency',
                        type: 'integer',
                        unit: 'ms',
                        value: null
                    },
                    writelatency: {
                        title: '客户端并发数为100时的写延迟',
                        name: 'writelatency',
                        type: 'integer',
                        unit: 'ms',
                        value: null
                    },
                    concurrent: {
                        title: '平均情况下的客户端并发数',
                        name: 'concurrent',
                        type: 'integer',
                        value: null
                    },
                    maxconcurrent: {
                        title: '最大客户端并发数',
                        name: 'maxconcurrent',
                        type: 'integer',
                        value: null
                    }
                }
            },
            requestData() {
                var data = {}
                for (var key in this.parameters) {
                    if (this.parameters[key].value != null) {
                        data[key] = this.parameters[key].value
                    }
                }
                console.log(data)
                return data
            }
        }
    }
</script>

<style>
</style>
