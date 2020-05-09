# -*- coding: utf-8 -*-
# https://pypi.org/project/imgkit/1.0.2/

import imgkit
options = {
    'format': 'png',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('customLocale', 'zh_TW'),
    ]
}


#imgkit.from_url('https://tw.op.gg/champion/alistar/statistics/support', 'out.jpg', options=options)

body = """
<html lang="zh_TW">
  <head>
  	<meta charset="utf-8"/>
    <meta name="imgkit-format" content="png"/>
  </head>
  <body>
<table class="champion-overview__table champion-overview__table--summonerspell">
<colgroup>
<col>
<col width="86">
<col width="86">
<col width="58">
</colgroup>
<thead><tr>
<th class="champion-overview__header">
						<a href="#">
							<h2>推薦召喚師法術</h2>
						</a>
					</th>
					<th class="champion-overview__header">
						<span>Pick率</span>
					</th>
					<th class="champion-overview__header">
						<span>階級</span>
					</th>
					<th class="champion-overview__header">
											</th>
				</tr></thead>
<tbody>
<tr>
<td class="champion-overview__data">
							<ul class="champion-stats__list">
<li class="champion-stats__list__item">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=q_auto,w_42&amp;v=1586932751" title="<b style='color: #ffc659'>閃現</b><br><span>英雄朝著滑鼠游標指向的位置瞬間傳送一小段距離。</span>" class="tip">
</li>
																											<li class="champion-stats__list__arrow">
																		</li><li class="champion-stats__list__item">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/SummonerDot.png?image=q_auto,w_42&amp;v=1586932751" title="<b style='color: #ffc659'>點燃</b><br><span>點燃敵方英雄，在 5 秒內造成 70-410 真實傷害（隨英雄等級提升），同時獲得該敵軍的視野，並且在作用期間降低目標治癒效果。</span>" class="tip">
</li>
															</ul>
</td>
						<td class="champion-overview__stats champion-overview__stats--pick">
							<strong>81.79%</strong>
							<span>5,812</span>
						</td>
						<td class="champion-overview__stats champion-overview__stats--win">
							<strong>50.52%</strong>
						</td>
						<td></td>
					</tr>
<tr>
<td class="champion-overview__data">
							<ul class="champion-stats__list">
<li class="champion-stats__list__item">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/SummonerFlash.png?image=q_auto,w_42&amp;v=1586932751" title="<b style='color: #ffc659'>閃現</b><br><span>英雄朝著滑鼠游標指向的位置瞬間傳送一小段距離。</span>" class="tip">
</li>
																											<li class="champion-stats__list__arrow">
																		</li><li class="champion-stats__list__item">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/SummonerExhaust.png?image=q_auto,w_42&amp;v=1586932751" title="<b style='color: #ffc659'>虛弱</b><br><span>虛弱敵方英雄，降低其 30% 跑速及 40% 傷害輸出，持續 3 秒。</span>" class="tip">
</li>
															</ul>
</td>
						<td class="champion-overview__stats champion-overview__stats--pick">
							<strong>17.1%</strong>
							<span>1,215</span>
						</td>
						<td class="champion-overview__stats champion-overview__stats--win">
							<strong>50.62%</strong>
						</td>
						<td></td>
					</tr>
</tbody>
<thead><tr>
<th class="champion-overview__header">
						<a href="/champion/alistar/support/skill">
							<h2>推薦殺戮構建</h2>
						</a>
					</th>
					<th class="champion-overview__header">
						<span>Pick率</span>
					</th>
					<th class="champion-overview__header">
						<span>階級</span>
					</th>
					<th class="champion-overview__header">
						<a href="/champion/alistar/support/skill" class="champion-overview__more"><img src="https:////opgg-static.akamaized.net/images/site/champion/detail-icon.png" alt="查看更多"></a>
					</th>
				</tr></thead>
<tbody><tr>
<td class="champion-overview__data">
							<ul class="champion-stats__list">
<li class="champion-stats__list__item tip" title="<b style='color: #ffc659'>大地粉碎</b>
<br><span style='color: #999'>冷卻時間（秒）: 17/16/15/14/13</span>
<br><span style='color: #999'>消耗: 65/70/75/80/85 ?</span>
<br><span style='color: #999'>範圍: 365</span>
<br><br><span>亞歷斯塔猛擊地面，造成 60/105/150/195/240 <scaleAP>(+50% 法術傷害)</scaleAP> 魔法傷害並將目標拋向空中 1 秒。</span><br><br><span style=&quot;font-size:11px; color: #ffc659;&quot;>用[?]顯示的值是Riot API不提供的數據。可通過LoL客戶端確認正確的值。</span>">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/Pulverize.png?image=q_auto,w_42&amp;v=1586932751" alt=""><span>Q</span>
									</li>
																																				<li class="champion-stats__list__arrow">
											<img src="https:////opgg-static.akamaized.net/images/site/champion/blet.png" alt="">
</li>
																		<li class="champion-stats__list__item tip" title="<b style='color: #ffc659'>野蠻衝撞</b>
<br><span style='color: #999'>冷卻時間（秒）: 14/13/12/11/10</span>
<br><span style='color: #999'>消耗: 65/70/75/80/85 ?</span>
<br><span style='color: #999'>範圍: 650</span>
<br><br><span>亞歷斯塔撞向一名敵人，造成 55/110/165/220/275 <scaleAP>（+70% 法術傷害）</scaleAP>魔法傷害並且擊退他們。</span><br><br><span style=&quot;font-size:11px; color: #ffc659;&quot;>用[?]顯示的值是Riot API不提供的數據。可通過LoL客戶端確認正確的值。</span>">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/Headbutt.png?image=q_auto,w_42&amp;v=1586932751" alt=""><span>W</span>
									</li>
																																				<li class="champion-stats__list__arrow">
											<img src="https:////opgg-static.akamaized.net/images/site/champion/blet.png" alt="">
</li>
																		<li class="champion-stats__list__item tip" title="<b style='color: #ffc659'>蠻牛之力</b>
<br><span style='color: #999'>冷卻時間（秒）: 12/11.5/11/10.5/10</span>
<br><span style='color: #999'>消耗: 50/60/70/80/90 ?</span>
<br><span style='color: #999'>範圍: 350</span>
<br><br><span>亞歷斯塔踐踏地面，忽略單位碰撞並於 5 秒內對附近敵人造成? <scaleAP>(+?)</scaleAP> 魔法傷害， 若衝擊波傷害到至少一個敵方英雄，亞歷斯塔會獲得一層<span class=&quot;colorFF6E1C&quot;> 踐踏</span> 層數。<br /><br />在擁有 5 <span class=&quot;colorFF6E1C&quot;>踐踏</span> 層數時，亞歷斯塔下次對敵方英雄的基本攻擊，會造成額外 <scaleLevel>?</scaleLevel> 魔法傷害並暈眩  1 秒。</span><br><br><span style=&quot;font-size:11px; color: #ffc659;&quot;>用[?]顯示的值是Riot API不提供的數據。可通過LoL客戶端確認正確的值。</span>">
										<img src="https:////opgg-static.akamaized.net/images/lol/spell/AlistarE.png?image=q_auto,w_42&amp;v=1586932751" alt=""><span>E</span>
									</li>
															</ul>
<table class="champion-skill-build__table"><tbody>
<tr>
<th>
						1
					</th>
									<th>
						2
					</th>
									<th>
						3
					</th>
									<th>
						4
					</th>
									<th>
						5
					</th>
									<th>
						6
					</th>
									<th>
						7
					</th>
									<th>
						8
					</th>
									<th>
						9
					</th>
									<th>
						10
					</th>
									<th>
						11
					</th>
									<th>
						12
					</th>
									<th>
						13
					</th>
									<th>
						14
					</th>
									<th>
						15
					</th>
							</tr>
<tr>
<td>
													Q
																	</td>
																									
															<td>
													W
																	</td>
																									
															<td>
													E
																	</td>
																															
															<td>
													Q
																	</td>
																															
															<td>
													Q
																	</td>
																									
															<td>
													R
																	</td>
																															
															<td>
													Q
																	</td>
																															
															<td>
													W
																	</td>
																															
															<td class="tip" title="<b style='color: #ffc659'>大地粉碎</b>
<br><span style='color: #999'>冷卻時間（秒）: 17/16/15/14/13</span>
<br><span style='color: #999'>消耗: 65/70/75/80/85 ?</span>
<br><span style='color: #999'>範圍: 365</span>
<br><br><span>亞歷斯塔猛擊地面，造成 60/105/150/195/240 <scaleAP>(+50% 法術傷害)</scaleAP> 魔法傷害並將目標拋向空中 1 秒。</span><br><br><span style=&quot;font-size:11px; color: #ffc659;&quot;>用[?]顯示的值是Riot API不提供的數據。可通過LoL客戶端確認正確的值。</span>">
													<img src="https:////opgg-static.akamaized.net/images/lol/spell/Pulverize.png?image=q_auto&amp;v=1586932751" alt="大地粉碎"><span>Q</span>
																	</td>
																															
															<td>
													W
																	</td>
																															
															<td>
													R
																	</td>
																															
															<td>
													W
																	</td>
																															
															<td class="tip" title="<b style='color: #ffc659'>野蠻衝撞</b>
<br><span style='color: #999'>冷卻時間（秒）: 14/13/12/11/10</span>
<br><span style='color: #999'>消耗: 65/70/75/80/85 ?</span>
<br><span style='color: #999'>範圍: 650</span>
<br><br><span>亞歷斯塔撞向一名敵人，造成 55/110/165/220/275 <scaleAP>（+70% 法術傷害）</scaleAP>魔法傷害並且擊退他們。</span><br><br><span style=&quot;font-size:11px; color: #ffc659;&quot;>用[?]顯示的值是Riot API不提供的數據。可通過LoL客戶端確認正確的值。</span>">
													<img src="https:////opgg-static.akamaized.net/images/lol/spell/Headbutt.png?image=q_auto&amp;v=1586932751" alt="野蠻衝撞"><span>W</span>
																	</td>
																															
															<td>
													E
																	</td>
																															
															<td>
													E
																	</td>
							</tr>
</tbody></table>
</td>
						<td class="champion-overview__stats champion-overview__stats--pick">
							<strong>72.68%</strong>
							<span>548</span>
						</td>
						<td class="champion-overview__stats champion-overview__stats--win">
							<strong>71.17%</strong>
						</td>
						<td></td>
					</tr></tbody>
</table>
  </body>
  </html>
"""

css = ['common.css', 'champion2.css']
imgkit.from_string(body, 'out.jpg', css=css)
