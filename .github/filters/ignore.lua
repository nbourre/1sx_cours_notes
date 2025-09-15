-- ignore.lua
-- Ignore blocks between <!-- PANDOC-IGNORE-START --> and <!-- PANDOC-IGNORE-END -->

local ignoring = false

function RawBlock(el)
  if el.format == "html" then
    if el.text:match("PANDOC%-IGNORE%-START") then
      ignoring = true
      return {}
    elseif el.text:match("PANDOC%-IGNORE%-END") then
      ignoring = false
      return {}
    end
  end

  if ignoring then
    return {}
  end
end

function Para(el)
  if ignoring then return {} end
end

function Header(el)
  if ignoring then return {} end
end

function BulletList(el)
  if ignoring then return {} end
end

function CodeBlock(el)
  if ignoring then return {} end
end

function OrderedList(el)
  if ignoring then return {} end
end

function BlockQuote(el)
  if ignoring then return {} end
end

function Div(el)
  if ignoring then return {} end
end
