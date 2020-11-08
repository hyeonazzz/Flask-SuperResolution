# NEWS
* Nov 11, 2020 -> ADD DBPN-Pytorch [alterzero/DBPN-Pytorch](https://github.com/alterzero/DBPN-Pytorch)
* Nov 10, 2020 -> ADD HTML src [FDBPN | Super-Resolution](http://13.209.19.207:5000/) 

## Download Models
Pretrained Models
https://drive.google.com/file/d/1oUK_YFi_YB8ZFNBI2H3gmO9GyQH-qZrI/view?usp=sharing

Original Models
https://drive.google.com/file/d/1G3UzVgYuvkQbSp2dZBPjHqKc3CcQZkRw/view?usp=sharing

## Dependencies
* Python 3.5
* PyTorch >= 1.0.0

## Model types
1. "DBPN" -> use T = 7
2. "DBPNLL" -> use T = 10
3. PIRM Model -> "DBPNLL" with adversarial loss
4. "DBPN-RES-MR64-3" -> [improvement of DBPN](https://arxiv.org/abs/1904.05677) with recurrent process + residual learning