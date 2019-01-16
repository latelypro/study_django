// グラフ化するデータ系列のサンプル
const sampleData = {
  labels: ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11"],
  sample1: [1.9, 2.32, 1.52, 0.79, 1.37, 1.28, 1.92, 1.44, 2.58, -0.01, 0.71, 4.25],
  sample2: [7.01, -2.15, -7.29, 1.71, 0.72, -4.83, 2.75, 4.11, 3.08, -2.45, 3.05, -3.93],
  sample3: [-2.97, -2.15, -0.3, -0.65, -8.84, 0.28, 2.95, 2.79, 1.79, 2.87, 0.16, 0.31],
  timestamp: ["2018/04/16 22:18", "2018/04/16 23:18", "2018/04/17 00:18", "2018/04/17 01:18", "2018/04/17 02:18", "2018/04/17 09:18", "2018/04/17 10:18", "2018/04/17 11:18", "2018/04/17 12:18", "2018/04/17 13:18", "2018/04/17 14:18", "2018/04/17 15:18"]
};
 
// グラフ作成の手順を定義
const loadCharts = (id) => {
  const chartDataSet = {
    type: 'line',
    data: {
      labels: sampleData.labels,
      datasets: [{
        label: 'sample1',
        fill: false,
        data: sampleData.sample1,
        backgroundColor: 'rgba(60, 160, 220, 0.3)',
        borderColor: 'rgba(60, 160, 220, 0.8)'
      }]
    },
    options: {
        legend: {
            display: false,
        },
        responsive: false,
    }
  };
  const ctx = document.createElement('canvas');
  ctx.width = "100";
  ctx.height = "100";

  const div = document.createElement('div');
  div.id = id;
  div.appendChild(ctx);
  new Chart(ctx, chartDataSet);
  document.getElementById('body').appendChild(div);
};
 
// グラフ作成
for (id =0; id < 6; ++id) {
  loadCharts(id);
}
