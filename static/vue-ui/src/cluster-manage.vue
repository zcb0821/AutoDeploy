<template>
    <div class="ui container" id="myclusters">
        <div class="ui icon message">
            <i class="cloud icon"></i>
            <div class="content">
                <p>共有&nbsp;<span class="ui grey circular label">{{clusters.length}}</span>&nbsp;个集群</p>
            </div>
            <button class="ui right floated blue button" v-on:click="newCluster()">添加集群</button>
        </div>
        <cluster v-for="cluster in clusters" track-by="$index" :cluster="cluster" :index="$index"></cluster>
        <deploy-wizard v-ref:deploy-wizard></deploy-wizard>

        <div class="ui small modal" id="confirm-modal">
            <div class="header">
                删除集群
            </div>
            <div class="content">
                <p>你确定要删除集群吗？</p>
            </div>
            <div class="actions">
                <div class="ui negative button">
                    否
                </div>
                <div class="ui positive right labeled icon button">
                    是
                    <i class="checkmark icon"></i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Cluster from './cluster.vue'
    import DeployWizard from './deploy/deploy-wizard.vue'

    function clusterFactory() {
        return {
            info: {
                name: '我的集群',
                id: Math.random(),
                isCompleted: true,
                ips: ['166.111.81.206', '166.111.81.207', '166.111.81.208'],
                systems: ['HDFS', 'Spark']
            },
            management: [{
                name: 'baidu',
                addr: 'http://www.baidu.com'
            }, {
                name: 'tsinghua',
                addr: 'http://info.tsinghua.edu.cn'
            }]
        }
    }

    export default {
        components: {Cluster, DeployWizard},
        data () {
            return {
                clusters: []
            }
        },
        methods: {
            newCluster: function () {
                this.$refs.deployWizard.init()
                this.$refs.deployWizard.show()
            },
            getClusters: function() {
                //todo: 获取用户的所有集群
            }
        },
        ready: function() {
            var vm = this
            $.get('/rest/clusters/', function(data) {
                var r = JSON.parse(data)
                vm.clusters = r
            })

        },
        events: {
            'deploy-finished': function (data) {
                this.clusters.push(data)
            },
            'cluster-deleted': function (index) {
                this.clusters.splice(index, 1)
            },
            'confirm': function(setting) {
                var $modal = $(this.$el).find('#confirm-modal')
                $modal.modal({
                    offset: 300,
                    detachable: false,
                    onDeny    : setting.deny,
                    onApprove : setting.approve
                }).modal('show')
            }
        }
    }
</script>

<style>

</style>
