using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dead : MonoBehaviour
{
    public float spawnX;
    public float spawnY;

    // Start is called before the first frame update
    void Start()
    {
        spawnX = transform.position.x;
        spawnY = transform.position.y;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnCollisionEnter2D(Collision2D col)
    {
        if (col.gameObject.name.Contains("Killzone"))
        {
            transform.position = new Vector3(spawnX, spawnY, transform.position.z);
        }

    }



}
