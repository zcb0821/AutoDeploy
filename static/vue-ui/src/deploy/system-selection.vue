<template>
    <div class="ui segment">
        <div class="ui form">
            <div class="field" id="deploy-storage">
                <label>{{storage.title}}</label>
                <div class="inline fields">
                    <div class="field" v-for="option in storage.options">
                        <div class="ui radio checkbox">
                            <input type="radio" name="storage" value="{{option}}" v-model="systems.storage | array">
                            <label>{{option}}</label>
                        </div>
                    </div>
                </div>
            </div>

            <div class="field" id="deploy-compute">
                <label>{{compute.title}}</label>
                <div class="inline fields">
                    <div class="field" v-for="option in compute.options">
                        <div class="ui checkbox">
                            <input type="checkbox" value="{{option}}" v-model="systems.compute">
                            <label>{{option}}</label>
                        </div>
                    </div>
                </div>
            </div>

            <div class="field" id="deploy-analysis">
                <label>{{analysis.title}}</label>
                <div class="inline fields">
                    <div class="field" v-for="option in analysis.options">
                        <div class="ui checkbox">
                            <input type="checkbox" value="{{option}}">
                            <label>{{option}}</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                systems: {
                    storage: ['HDFS'],
                    compute: ['MapReduce']
                },
                storage: {
                    title: '存储层',
                    name: 'storage',
                    options: ['HDFS', 'HDFS,HBase', 'Cassandra']
                },
                compute: {
                    title: '计算层',
                    name: 'compute',
                    options: ['MapReduce', 'Spark']
                },
                analysis: {
                    title: '分析层',
                    name: 'analysis',
                    options: ['SparkSQL', 'MLBase']
                }
            }
        },
        watch: {
            'systems.storage': function() {
                console.log(this.systems.storage)
            },
            'systems.compute': function() {
                var checkboxes = $(this.$el).find('#deploy-analysis .ui.checkbox')
                if (this.systems.compute.indexOf('Spark') >= 0) {
                    checkboxes.checkbox('check')
                } else {
                    checkboxes.checkbox('uncheck')
                }
            }
        },
        ready: function() {
            $(this.$el).find('#deploy-analysis .ui.checkbox').checkbox('set disabled')
        },
        methods: {
            isCompleted () {
                return true
            },
            willLeave: function(id, success) {
                $.post("/rest/selectsystem/", {
                    "selection": JSON.stringify(this.systems).toLowerCase()
                }, function(data) {
                    if (data.result == 'success') {
                        success()
                    }
                }, 'json')
            },
            init: function(data) {
                if (data) {
                    this.systems.storage = data.storage ? data.storage : []
                    this.systems.compute = data.compute ? data.compute : []
                }
            },
            requestData () {
                return this.systems
            }
        }
    }
</script>

<style>
</style>