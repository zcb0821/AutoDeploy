<template>
    <div>
        <div class="ui attached top clearing segment">
            <label>{{cluster.name}}&nbsp;</label>
            <label class="ui teal label">{{cluster.is_completed ? '已完成' : '部署中'}}</label>
            <button class="ui right floated red button" v-on:click="deleteCluster()">删除</button>
            <a class="ui right floated blue button" href="{{'/clusters/' + cluster.id + '/'}}" target="_blank">管理</a>
        </div>

        <div class="ui bottom attached bottom small message">
            <div class="header">
                IP地址
            </div>
            <p>{{cluster.addrs ? cluster.addrs.join(', ') : '正在部署中'}}</p>
            <div class="header">
                集群构件
            </div>
            <p>{{cluster.systems ? cluster.systems.join(', ') : ''}}</p>
        </div>
        <div></div>
    </div>
</template>

<script>
    export default {
        props: {
            'cluster': {
                required: true
            },
            'index': {

            }
        },
        data () {
            return {
                deployPollingTimer: null
            }
        },
        watch: {},
        ready: function () {
            if (this.cluster.is_completed == false) {
                this.deployPollingTimer = setInterval(this.getDeployStatus, 5000)
            }
        },
        methods: {
            getDeployStatus: function () {
                var vm = this
                $.get('/rest/clusters/' + this.cluster.id + '/status/',
                        function (response) {
                            if (response.is_completed) {
                                window.clearInterval(vm.deployPollingTimer)
                                vm.cluster.is_completed = true
                                vm.cluster.addrs = response.addrs
                            }
                        }, 'json')
            },
            deleteCluster: function () {
                var vm = this
                vm.$dispatch('confirm', {
                    approve: function() {
                        $.ajax({
                            url: '/rest/clusters/' + vm.cluster.id,
                            method: 'delete',
                            success: function () {
                                vm.$dispatch('cluster-deleted', vm.index)
                                window.clearInterval(vm.deployPollingTimer)
                            }
                        })
                    }
                })

            }
        }
    }
</script>

<style>

</style>