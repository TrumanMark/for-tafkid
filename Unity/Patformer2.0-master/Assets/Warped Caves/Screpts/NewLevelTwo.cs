using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class NewLevelTwo : MonoBehaviour
{
    private void OnTriggerEnter2D(Collider2D other2)
    {
        if (other2.tag == "Player")
        {

            SceneManager.LoadScene("Map3");
        }
    }
}
