
async function retrieve_data(param,param1,param2){
    const s ={
        factor:param,
        flag:param1,
        target:param2
     }
    const a = await fetch('/test_data',{method:"post",
    mode:"cors",
    redirect:"follow",
    body:JSON.stringify(s)

})
    const results = await a.json()
    obj=JSON.parse(results)
    const b=document.getElementsByTagName('td')
    c=Object.values(obj)
    let i=0
    for(const key in obj){
        d=Object.values(obj[key])
        b.item(i).innerText=d[0]
        i++
    }
    for(const key in obj){
        d=Object.values(obj[key])
        b.item(i).innerText=d[1]
        i++
    } 
   
    
  
   
    return  true

 
}

async function post_hoc(param,param1,param2){
    const s ={
       factor:param,
       flag:param1,
       target:param2
    }
    const a = await fetch('/test_data',{method:"post",
    mode:"cors",
    redirect:"follow",
    body:JSON.stringify(s)

})
    const results = await a.json()
    obj=JSON.parse(results)
    doc=document.getElementById('posthoc')
    doc.innerText=obj
    doc_=document.getElementById('posthc')
    doc_.style.display="block"

    return  true


}

function PrintDoc(){
    const a = document.getElementById('mainview')
    window.print()
}