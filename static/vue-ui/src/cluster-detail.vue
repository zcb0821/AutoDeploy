<template>
    <div class="ui sidebar inverted vertical menu visible" style="width: 250px;">
        <div class="item">
            <h3 class="ui header grey inverted">集群管理</h3>
            <div class="menu">
                <div class="item">名称：{{ cluster.name }}</div>
                <div class="item">时间：{{ cluster.created }}</div>
            </div>
        </div>
        <a class="item active" data-value="{{ cluster.addrs[0] }}">日志管理</a>
        <div class="item" >
            <div class="header">存储层</div>
            <div class="menu">
                <a class="item">HDFS</a>
            </div>
        </div>
        <div class="item">
            <div class="header">计算层</div>
            <div class="menu">
                <a class="item">Spark History</a>
                <a class="item">Ganglia</a>
                <a class="item">YARN</a>
            </div>
        </div>
        <div class="item">
            <div class="header">优化与诊断</div>
            <div class="menu">
                <a class="item">参数优化</a>
                <a class="item">日志诊断</a>
            </div>
        </div>
    </div>

    <div style="margin-left: 250px; min-width: 960px; height: 99%; background-color: white">
        <iframe src="" style="width: 100%; height: 100%; border:none"></iframe>
    </div>
</template>

<script>
    export default {
        ready: function() {

        },
        data: function() {
            return {
                cluster: {}
            }
        },
        methods: function() {

        }
    }
</script>

<style>

</style>