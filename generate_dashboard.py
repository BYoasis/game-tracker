import json
from datetime import datetime

# 当前时间
update_time = "2026-04-15 01:00:00"

# 数据整理
data = {
    "update_time": update_time,
    "games": [
        {
            "name": "洛克王国世界",
            "items": {
                "news": [
                    {"title": "官方发布致小洛克的一封信，回应近期体验痛点", "url": "https://m.weibo.cn/detail/5287351724018661", "time": "2026-04-13"},
                    {"title": "4.16更新白送两个异色蛋，咕噜球直接白菜价", "url": "http://m.toutiao.com/group/7628566151882113590/", "time": "2026-04-14"},
                    {"title": "3000万小洛克重返卡洛西亚，不逼氪改写开放世界规则", "url": "http://m.toutiao.com/group/7628415306804822562/", "time": "2026-04-14"},
                    {"title": "《洛克王国世界》全解析：2026实机演示+多平台评分+游玩指南", "url": "http://m.toutiao.com/group/7627171717374394934/", "time": "2026-04-11"},
                    {"title": "官方发布水域连续捕捉异常修复公告，严打外挂黑产", "url": "https://m.weibo.cn/detail/5287376693235669", "time": "2026-04-13"}
                ],
                "ugc": [
                    {"title": "【进阶必读】高阶攻略大全：体系队搭配详解", "url": "https://www.taptap.cn/moment/786567056207120843", "time": "2026-03-27"},
                    {"title": "公测全攻略：从开局小白到天梯大佬", "url": "http://news.17173.com/content/03172026/112645099.shtml", "time": "2026-03-17"},
                    {"title": "新手开荒攻略：御三家选择与速刷升级路线", "url": "https://app.ali213.net/gl/1758035.html", "time": "2026-03-27"},
                    {"title": "新手图文全攻略与兑换码攻略", "url": "https://www.taptap.cn/moment/788201714976032027", "time": "2026-04-01"},
                    {"title": "玩法指南与兑换码攻略", "url": "https://a.9game.cn/lkwgsy/11449981.html", "time": "2025-10-14"}
                ],
                "social": [
                    {"title": "TapTap论坛676万关注，5.5万帖子", "url": "https://www.taptap.cn/app/188212", "time": "持续活跃"},
                    {"title": "抖音精选APP站内相关内容播放量超200万", "url": "https://www.douyin.com", "time": "持续活跃"}
                ]
            }
        },
        {
            "name": "幻兽帕鲁",
            "items": {
                "news": [
                    {"title": "Pocketpair确认1.0版仍在开发，临近完成将有预告", "url": "https://gamingbolt.com/palworld-1-0-is-still-in-the-oven-says-pocketpairs-head-of-communications-and-publishing", "time": "2026-04-14"},
                    {"title": "v0.7.3平衡调整和Bug修复（2026年4月10日）", "url": "https://steamcommunity.com/app/1623730/eventcomments/?gidtopic=4351116701412495127&sort=time", "time": "2026-04-10"},
                    {"title": "官方确认1.0将于2026年内上线，五只新帕鲁亮相", "url": "https://www.ali213.net/news/html/2026-1/994951.html", "time": "2026-01-20"},
                    {"title": "GDC 2026：1.0版内容规模令人震惊，建议删档重玩", "url": "http://m.toutiao.com/group/7617897265311384073/", "time": "2026-03-17"},
                    {"title": "1.0版将带来新帕鲁、新地图、多结局叙事", "url": "https://worldofgeek.fr/palworld-version-1-0-nouveautes/", "time": "2026-03-24"}
                ],
                "ugc": [
                    {"title": "《幻兽帕鲁》全面解析：玩法、攻略与问题解决", "url": "https://game.sohu.com/a/995267258_122519711", "time": "2026-03-11"},
                    {"title": "新手开局攻略：零基础快速上手、资源获取与帕鲁捕捉", "url": "https://a.9game.cn/news/11593141.html", "time": "2025-12-17"},
                    {"title": "新手玩法技巧与实用攻略", "url": "https://m.sohu.com/a/952425539_120134470/", "time": "2025-11-11"},
                    {"title": "帕鲁指南：帕鲁球制作与捕捉注意事项", "url": "https://www.local.gamekee.com/pal/611890.html", "time": "持续更新"},
                    {"title": "新手速通秘籍：选址建家与帕鲁培养", "url": "https://a.9game.cn/biji/1053377.html", "time": "2025-12-18"}
                ],
                "social": [
                    {"title": "Steam活跃玩家社区，法国市场占比12%", "url": "https://store.steampowered.com/app/1623730/Palworld/", "time": "持续活跃"},
                    {"title": "450+法国内容创作者，预计2026年增长至650+", "url": "https://twitter.com/Pocketpair", "time": "持续活跃"}
                ]
            }
        },
        {
            "name": "宝可梦",
            "items": {
                "news": [
                    {"title": "《宝可梦冠军》正式发布登陆Switch，支持跨平台对战", "url": "https://wap.gamersky.com/news/Content-2120396.html", "time": "2026-04-08"},
                    {"title": "宝可梦30周年庆：Winds和Waves新游戏公布", "url": "https://pokemon.gamespress.com/pt", "time": "2026-02-27"},
                    {"title": "Mega Evolution超级进化系统正式回归", "url": "https://pokemon.gamespress.com/pt", "time": "2026-03-27"},
                    {"title": "2026官方卡牌道馆杯4月25日全国8城市同步开赛", "url": "http://m.toutiao.com/group/7627865541222433321/", "time": "2026-04-12"},
                    {"title": "宝可梦卡牌城市赛2026年第二赛季4月18日全面开展", "url": "http://m.toutiao.com/group/7627865541222433321/", "time": "2026-04-12"}
                ],
                "ugc": [
                    {"title": "PokemonDB新闻订阅源最新资讯", "url": "https://pokemondb.net/news/feed", "time": "持续更新"},
                    {"title": "《宝可梦 朱/紫》体验指南", "url": "https://www.pokemon.co.jp/ex/sv/tc/features/220803_01/", "time": "官方内容"},
                    {"title": "口袋妖怪新手玩法攻略", "url": "http://m.toutiao.com/group/7498174634190586403/", "time": "2025-05-05"},
                    {"title": "《宝可梦传说阿尔宙斯》新手入坑攻略", "url": "http://m.toutiao.com/group/7587698995749831202/", "time": "2025-12-25"},
                    {"title": "《宝可梦剑/盾》培育指南", "url": "https://game.portal-pokemon.com/sword_shield/sc/howtoplay/08.html", "time": "官方内容"}
                ],
                "social": [
                    {"title": "抖音/B站\"店长对决\"热梗引爆全民宝可梦热潮", "url": "http://m.toutiao.com/group/7627865541222433321/", "time": "2026-04"},
                    {"title": "全国宝可梦主题店铺社群蓬勃发展", "url": "http://m.toutiao.com/group/7627865541222433321/", "time": "持续活跃"}
                ]
            }
        }
    ],
    "stats": {
        "total": 30,
        "news_count": 15,
        "ugc_count": 15
    }
}

# 保存JSON
with open('./游戏竞品看板/data/latest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 生成HTML
template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎮 游戏竞品追踪看板</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #fff;
        }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        .header {
            text-align: center;
            padding: 30px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.5em;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf, #ff6b6b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .update-time { color: #888; font-size: 0.9em; }
        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        .game-card {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 25px;
            border: 1px solid rgba(255,255,255,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .game-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        .game-card.locke { border-top: 4px solid #ff6b6b; }
        .game-card.palworld { border-top: 4px solid #4ecdc4; }
        .game-card.pokemon { border-top: 4px solid #ffd93d; }
        .game-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .game-title { font-size: 1.5em; font-weight: bold; }
        .game-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 500;
        }
        .badge-news { background: rgba(255,107,107,0.2); color: #ff6b6b; }
        .badge-update { background: rgba(78,205,196,0.2); color: #4ecdc4; }
        .badge-ugc { background: rgba(255,217,61,0.2); color: #ffd93d; }
        .section { margin-bottom: 20px; }
        .section-title {
            font-size: 1em;
            color: #888;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .section-title::before { content: ''; width: 4px; height: 16px; border-radius: 2px; }
        .news-section .section-title::before { background: #ff6b6b; }
        .ugc-section .section-title::before { background: #ffd93d; }
        .social-section .section-title::before { background: #4ecdc4; }
        .item-list { list-style: none; }
        .item {
            padding: 12px;
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            margin-bottom: 8px;
            transition: background 0.2s;
        }
        .item:hover { background: rgba(255,255,255,0.08); }
        .item-title {
            font-size: 0.95em;
            margin-bottom: 6px;
            color: #fff;
            text-decoration: none;
            display: block;
        }
        .item-title:hover { color: #00d4ff; }
        .item-meta {
            font-size: 0.8em;
            color: #666;
            display: flex;
            gap: 15px;
        }
        .empty-state { text-align: center; padding: 40px; color: #555; }
        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 50px;
            padding: 20px;
            background: rgba(255,255,255,0.03);
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .stat-item { text-align: center; }
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stat-label { font-size: 0.85em; color: #888; margin-top: 5px; }
        .footer {
            text-align: center;
            padding: 30px;
            color: #555;
            font-size: 0.85em;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎮 游戏竞品追踪看板</h1>
            <p class="update-time">最后更新: ''' + update_time + '''</p>
        </div>
        
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number">30</div>
                <div class="stat-label">总内容数</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">15</div>
                <div class="stat-label">新闻动态</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">15</div>
                <div class="stat-label">攻略/二创</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">3</div>
                <div class="stat-label">追踪游戏</div>
            </div>
        </div>

        <div class="games-grid">
            <div class="game-card locke">
                <div class="game-header">
                    <span class="game-title">🔴 洛克王国世界</span>
                    <span class="badge-update">进行中</span>
                </div>
                <div class="section news-section">
                    <div class="section-title">📰 新闻动态</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://m.weibo.cn/detail/5287351724018661" class="item-title" target="_blank">官方发布致小洛克的一封信，回应近期体验痛点</a>
                            <div class="item-meta"><span>2026-04-13</span></div>
                        </li>
                        <li class="item">
                            <a href="http://m.toutiao.com/group/7628566151882113590/" class="item-title" target="_blank">4.16更新白送两个异色蛋，咕噜球直接白菜价</a>
                            <div class="item-meta"><span>2026-04-14</span></div>
                        </li>
                        <li class="item">
                            <a href="http://m.toutiao.com/group/7628415306804822562/" class="item-title" target="_blank">3000万小洛克重返卡洛西亚，不逼氪改写开放世界规则</a>
                            <div class="item-meta"><span>2026-04-14</span></div>
                        </li>
                    </ul>
                </div>
                <div class="section ugc-section">
                    <div class="section-title">📖 攻略/二创</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://www.taptap.cn/moment/786567056207120843" class="item-title" target="_blank">【进阶必读】高阶攻略大全：体系队搭配详解</a>
                            <div class="item-meta"><span>2026-03-27</span></div>
                        </li>
                        <li class="item">
                            <a href="http://news.17173.com/content/03172026/112645099.shtml" class="item-title" target="_blank">公测全攻略：从开局小白到天梯大佬</a>
                            <div class="item-meta"><span>2026-03-17</span></div>
                        </li>
                        <li class="item">
                            <a href="https://app.ali213.net/gl/1758035.html" class="item-title" target="_blank">新手开荒攻略：御三家选择与速刷升级路线</a>
                            <div class="item-meta"><span>2026-03-27</span></div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="game-card palworld">
                <div class="game-header">
                    <span class="game-title">🟢 幻兽帕鲁</span>
                    <span class="badge-update">开发中</span>
                </div>
                <div class="section news-section">
                    <div class="section-title">📰 新闻动态</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://gamingbolt.com/palworld-1-0-is-still-in-the-oven-says-pocketpairs-head-of-communications-and-publishing" class="item-title" target="_blank">Pocketpair确认1.0版仍在开发，临近完成将有预告</a>
                            <div class="item-meta"><span>2026-04-14</span></div>
                        </li>
                        <li class="item">
                            <a href="https://steamcommunity.com/app/1623730/eventcomments/?gidtopic=4351116701412495127&sort=time" class="item-title" target="_blank">v0.7.3平衡调整和Bug修复（2026年4月10日）</a>
                            <div class="item-meta"><span>2026-04-10</span></div>
                        </li>
                        <li class="item">
                            <a href="https://www.ali213.net/news/html/2026-1/994951.html" class="item-title" target="_blank">官方确认1.0将于2026年内上线，五只新帕鲁亮相</a>
                            <div class="item-meta"><span>2026-01-20</span></div>
                        </li>
                    </ul>
                </div>
                <div class="section ugc-section">
                    <div class="section-title">📖 攻略/二创</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://game.sohu.com/a/995267258_122519711" class="item-title" target="_blank">《幻兽帕鲁》全面解析：玩法、攻略与问题解决</a>
                            <div class="item-meta"><span>2026-03-11</span></div>
                        </li>
                        <li class="item">
                            <a href="https://a.9game.cn/news/11593141.html" class="item-title" target="_blank">新手开局攻略：零基础快速上手、资源获取与帕鲁捕捉</a>
                            <div class="item-meta"><span>2025-12-17</span></div>
                        </li>
                        <li class="item">
                            <a href="https://a.9game.cn/biji/1053377.html" class="item-title" target="_blank">新手速通秘籍：选址建家与帕鲁培养</a>
                            <div class="item-meta"><span>2025-12-18</span></div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="game-card pokemon">
                <div class="game-header">
                    <span class="game-title">🟡 宝可梦</span>
                    <span class="badge-update">活跃</span>
                </div>
                <div class="section news-section">
                    <div class="section-title">📰 新闻动态</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://wap.gamersky.com/news/Content-2120396.html" class="item-title" target="_blank">《宝可梦冠军》正式发布登陆Switch，支持跨平台对战</a>
                            <div class="item-meta"><span>2026-04-08</span></div>
                        </li>
                        <li class="item">
                            <a href="https://pokemon.gamespress.com/pt" class="item-title" target="_blank">宝可梦30周年庆：Winds和Waves新游戏公布</a>
                            <div class="item-meta"><span>2026-02-27</span></div>
                        </li>
                        <li class="item">
                            <a href="http://m.toutiao.com/group/7627865541222433321/" class="item-title" target="_blank">2026官方卡牌道馆杯4月25日全国8城市同步开赛</a>
                            <div class="item-meta"><span>2026-04-12</span></div>
                        </li>
                    </ul>
                </div>
                <div class="section ugc-section">
                    <div class="section-title">📖 攻略/二创</div>
                    <ul class="item-list">
                        <li class="item">
                            <a href="https://pokemondb.net/news/feed" class="item-title" target="_blank">PokemonDB新闻订阅源最新资讯</a>
                            <div class="item-meta"><span>持续更新</span></div>
                        </li>
                        <li class="item">
                            <a href="http://m.toutiao.com/group/7498174634190586403/" class="item-title" target="_blank">口袋妖怪新手玩法攻略</a>
                            <div class="item-meta"><span>2025-05-05</span></div>
                        </li>
                        <li class="item">
                            <a href="http://m.toutiao.com/group/7587698995749831202/" class="item-title" target="_blank">《宝可梦传说阿尔宙斯》新手入坑攻略</a>
                            <div class="item-meta"><span>2025-12-25</span></div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>🤖 由 Coze Agent 自动采集更新 | 每小时刷新</p>
            <p>数据来源: 搜索引擎 + 官方RSS</p>
        </div>
    </div>
</body>
</html>'''

with open('./游戏竞品看板/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(template)

print("看板生成完成!")
print(f"- dashboard.html")
print(f"- data/latest.json")
