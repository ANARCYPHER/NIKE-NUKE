#include <iostream>
#include <set>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <iomanip>
using namespace std;

typedef long long int lli;

vector<lli> p,rank1,setSize;   /* p keeps track of the parent
                                * rank1 keeps track of the rank
                                * setSize keeps track of the size of the set. 
                                */ 

lli findSet(lli i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); } 

bool sameSet(lli x,lli y) { return findSet(x) == findSet(y); }


void union1(lli x,lli y) {      // union merges two sets.

    if(!sameSet(x,y)) {

        lli i = findSet(x), j = findSet(y);

        if(rank1[i] > rank1[j]) {
            p[j] = i;
            setSize[i] += setSize[j];           

        }

        else {
            p[i] = j;
            setSize[j] += setSize[i];
            if(rank1[i] == rank1[j])
                rank1[j]++;
        }
    }
}

int main() {

    freopen("input","r",stdin);

    lli n;
    cin >> n;                               //number of nuclear rods

    setSize.assign(n,1);                    //Initialize the setSize with 1 because every element is in its own set
    p.assign(n,0);          
    rank1.assign(n,0);                      //Initialize ranks with 0's.

    for(lli i = 0; i < n; i++) p[i] = i;    //Every set is distinct. Thus it is its own parent.

    lli f;
    cin >> f;                               //Number of fusions.

    while(f--){                 

        lli x,y;
        cin >> x >> y;                      //combine two rods
        union1(x,y);                        

    }   

    double ans; 

    set<lli> s (p.begin(),p.end());         //Get the representative of all the sets.

    for(lli i : s){     
        ans += sqrt(setSize[i]);            //sum the sqrt of all the members of that set.

    }

    printf("\n%.2f", ans);                  //display the answer in 2 decimal places.
}