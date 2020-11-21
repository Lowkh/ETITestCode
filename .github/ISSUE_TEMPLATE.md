---
title: Someone just pushed
assignees: Lowkh
labels: bug
---
console.log({payload: github.context.payload})

Someone just pushed, oh no! Here's who did it: {{ payload.sender.login }}. 
