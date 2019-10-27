# lua-pb

A Protocol Buffer implementation that runs on World of Warcraft Addons.
The lua-pb is based on the work of <https://github.com/Neopallium/lua-pb> by Neopallium

## Generate lua stub for your addon

 * install lpge
 
 `luarocks install lpeg`

 * generate with `saveast.lua`

```
lua saveast.lua VARNAME < FILE.proto > STUB.lua
```

exmaple for using person.proto in wowtest folder
```
lua saveast.lua pbperson < person.proto > wowtest/person.lua
```

## Import in your addon

You have two choices to use `lua-pb` as a library

### As files inside your addon

 1. Download relase zip from <https://www.wowace.com/projects/protobuf/files>
 1. Copy `lua-pb` folder to your addon
 1. Add `path\to\lua-pb\lua-pb.xml` in your `.toc` file
 1. Add `path\to\pbstub.lua` in your `.toc` file

After loaded, lua-pb would be availiable in your `addon ctx`

Example (you can find exmaple in <wowtest/pb-wow-test.lua>)

```
local _, ADDONSELF = ...

local luapb = ADDONSELF.luapb
local person = luapb.load_proto_ast(ADDONSELF.pbperson).Person

local msg0 = person()

msg0.name = "aa"
msg0.id = 1

print("serialize: name " .. msg0.name .. " id " .. msg0.id)

local t = msg0:Serialize()

assert(#t > 0, "size of t > 0")

local msg1 = person()
msg1:Parse(t)

assert(msg1.name == msg0.name, "name not equal")
assert(msg1.id == msg0.id, "id not equal")

print("deserialize: name " .. msg1.name .. " id " .. msg1.id)

```


### Use as an dependency (Optional for LibStub)

```
local luapb = LibStub:GetLibrary('luapb')
```

## Powered by lua-pb

 * [Myslot](https://www.wowace.com/projects/myslot)
