import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

const modes = {
  classify: { label: '文本分类', action: '分类', english: 'TEXT CLASSIFICATION', description: '识别金融文本的内容类别', sample: '今日，央行宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。', details: ['新闻报道', '财务报告', '公司公告', '分析师报告'], detailsTitle: '识别类别', detailsDesc: '模型可识别的常见文本类型' },
  extract: { label: '信息抽取', action: '抽取', english: 'INFORMATION EXTRACTION', description: '从文本中提取关键金融信息', sample: '2025-02-15，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量增加至460,000。', details: ['日期', '股票名称', '开盘价', '收盘价', '成交量'], detailsTitle: '抽取字段', detailsDesc: '从文本中寻找以下信息' },
  match: { label: '文本匹配', action: '匹配', english: 'TEXT MATCHING', description: '判断两段文本的含义是否相似', sample: '股票市场今日大涨，投资者乐观。', sample2: '持续上涨的市场让投资者感到满意。', details: ['相似', '不相似'], detailsTitle: '判断结果', detailsDesc: '根据两段文本的语义进行判断' },
};

function ExtractResult({ value }) {
  let parsed;
  try {
    const cleaned = value.trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/, '');
    parsed = JSON.parse(cleaned);
  } catch { return <pre className="raw-result">{value}</pre>; }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return <pre className="raw-result">{value}</pre>;
  return <dl className="extract-list">{Object.entries(parsed).map(([key, item]) => <div key={key}><dt>{key}</dt><dd>{Array.isArray(item) ? item.join('、') || '未提及' : typeof item === 'object' ? JSON.stringify(item) : String(item ?? '未提及')}</dd></div>)}</dl>;
}

function App() {
  const [mode, setMode] = useState('classify');
  const [text, setText] = useState('');
  const [text2, setText2] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const current = modes[mode];

  function switchMode(next) {
    setMode(next); setText(''); setText2(''); setResult(''); setError('');
  }
  function updateText(setter, value) { setter(value); setResult(''); setError(''); }
  async function analyze(event) {
    event.preventDefault();
    if (!text.trim() || (mode === 'match' && !text2.trim()) || loading) return;
    setLoading(true); setError(''); setResult('');
    try {
      const response = await fetch(`/api/${mode}`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text.trim(), ...(mode === 'match' ? { text2: text2.trim() } : {}) }),
      });
      let data;
      try { data = await response.json(); } catch { throw new Error('服务响应异常，请确认后端已启动。'); }
      if (!response.ok) throw new Error(data.error || '分析失败，请重试。');
      const value = mode === 'classify' ? data.category : data.result;
      if (typeof value !== 'string' || !value.trim()) throw new Error('模型未返回有效结果，请重试。');
      setResult(value);
    } catch (err) {
      setError(err.message === 'Failed to fetch' ? '无法连接分析服务，请确认后端已启动。' : err.message);
    } finally { setLoading(false); }
  }

  return <div className="app">
    <header><div className="brand"><span className="brand-icon">✳</span><span>文本实验室 <small>TEXT LAB</small></span></div><span className="header-label"><span className="dot" /> FINANCIAL AI TOOLKIT</span></header>
    <main>
      <div className="eyebrow"><span>AI 文本分析</span><span className="line" /><span>{current.english}</span></div>
      <section className="intro"><div><div className="tag">FINANCIAL INTELLIGENCE <span>↗</span></div><h1>让金融文本<br /><em>一目了然。</em></h1><p>分类、抽取、匹配，一站式分析金融文本。<br />从海量信息中，找到清晰的方向。</p></div><div className="intro-art" aria-hidden="true"><div className="art-circle"><span>文</span><i>↗</i></div><div className="art-caption">READ BETWEEN<br />THE LINES <b>✳</b></div></div></section>
      <nav className="mode-nav" aria-label="分析功能">{Object.entries(modes).map(([key, item], index) => <button type="button" key={key} className={mode === key ? 'mode active' : 'mode'} aria-current={mode === key ? 'page' : undefined} disabled={loading} onClick={() => switchMode(key)}><span className="mode-number">0{index + 1}</span><span><b>{item.label}</b><small>{item.description}</small></span><span className="mode-arrow">↗</span></button>)}</nav>
      <div className="workspace">
        <section className="card input-card"><div className="card-heading"><div><span className="section-number">01</span><h2>输入文本</h2><p>{mode === 'match' ? '输入两段需要比较的文本' : `将需要${current.action}的内容粘贴至下方`}</p></div><span className="icon-box">↗</span></div>
          <form onSubmit={analyze}><label className="sr-only" htmlFor="input-text">{mode === 'match' ? '第一段文本' : '需要分析的文本'}</label><textarea id="input-text" className={mode === 'match' ? 'match-input' : ''} value={text} onChange={e => updateText(setText, e.target.value)} placeholder={mode === 'match' ? '输入第一段文本...' : '在这里输入或粘贴金融文本...'} maxLength={20000} disabled={loading} />{mode === 'match' && <><label className="sr-only" htmlFor="input-text2">第二段文本</label><textarea id="input-text2" className="match-input second-input" value={text2} onChange={e => updateText(setText2, e.target.value)} placeholder="输入第二段文本..." maxLength={20000} disabled={loading} /></>}<div className="input-meta"><button type="button" className="sample" disabled={loading} onClick={() => {setText(current.sample); setText2(current.sample2 || ''); setResult(''); setError('');}}>＋ 使用示例文本</button><span>{mode === 'match' ? `${text.length.toLocaleString()} / ${text2.length.toLocaleString()} 字` : `${text.length.toLocaleString()} / 20,000`}</span></div><button className="submit" disabled={!text.trim() || (mode === 'match' && !text2.trim()) || loading}>{loading ? '正在分析...' : `开始${current.action}`}<span>{loading ? '···' : '↗'}</span></button></form>
        </section>
        <section className="card result-card"><div className="card-heading"><div><span className="section-number">02</span><h2>{current.action}结果</h2><p>模型识别结果将在这里展示</p></div><span className="icon-box light">✳</span></div><div className="result-area" aria-live="polite">{loading ? <div className="empty"><div className="empty-icon pulse">···</div><strong>正在分析文本</strong><p>请稍等片刻</p></div> : error ? <div className="empty error"><div className="empty-icon">!</div><strong>暂时无法完成{current.action}</strong><p>{error}</p></div> : result ? <div className="result"><span className="result-kicker"><span className="dot" /> ANALYSIS COMPLETE</span><p>{mode === 'classify' ? '识别类别' : mode === 'match' ? '语义判断' : '抽取信息'}</p>{mode === 'extract' ? <ExtractResult value={result} /> : <strong>{result}</strong>}<div className="result-divider" /><span>基于输入文本的语义分析结果</span></div> : <div className="empty"><div className="empty-icon">✳</div><strong>等待分析</strong><p>输入文本并点击「开始{current.action}」</p></div>}</div><div className="result-footer"><span>✧</span> 由大语言模型提供分析支持</div></section>
      </div>
      <div className="categories"><div><span className="categories-title">{current.detailsTitle}</span><span className="categories-desc">{current.detailsDesc}</span></div><div className="pills">{current.details.map((item, i) => <span key={item}><b>0{i + 1}</b>{item}</span>)}</div></div>
    </main><footer><span>© TEXT LAB · FINANCIAL INTELLIGENCE</span><span>让信息更有条理 <b>✳</b></span></footer>
  </div>;
}

createRoot(document.getElementById('root')).render(<App />);
