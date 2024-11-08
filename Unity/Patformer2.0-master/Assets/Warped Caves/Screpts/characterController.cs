using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class characterController : MonoBehaviour {
	public float maxSpeed = 10f;
	public float jumpForce = 700f;
	bool facingRight = true;
	bool grounded = false;
	public Transform groundCheck;
	public float groundRadius = 0.2f;
	public LayerMask whatIsGround;
	public float score;
	public float move;
    private bool isFacingRight = true;
    private Animator anim;
    private bool isGrounded = false;


	private GameObject star;
    /// <summary>
    /// 
    /// </summary>
	// Use this for initialization
	void Start () {
        anim = GetComponent<Animator>();
	}
	/// <summary>
    /// 
    /// </summary>
	// Update is called once per frame
	void FixedUpdate () {


		grounded = Physics2D.OverlapCircle (groundCheck.position, groundRadius, whatIsGround);

		move = Input.GetAxis ("Horizontal");

        anim.SetFloat("Speed", Mathf.Abs(move));

        anim.SetBool("Ground", grounded);
        anim.SetFloat("vSpeed", GetComponent<Rigidbody2D>().velocity.y);

        if (!grounded)
            return;

        if (move > 0 && !isFacingRight)

            Flip();
        else if (move < 0 && isFacingRight)
            Flip();

	}
    /// <summary>
    /// 
    /// </summary>
	void Update(){
		if (grounded && (Input.GetKeyDown (KeyCode.W)||Input.GetKeyDown (KeyCode.UpArrow))) {

			GetComponent<Rigidbody2D>().AddForce (new Vector2(0f,jumpForce));
            anim.SetBool("Ground", false);

		}
		GetComponent<Rigidbody2D>().velocity = new Vector2 (move * maxSpeed, GetComponent<Rigidbody2D>().velocity.y);
		
		if (move > 0 && !facingRight)
			Flip ();
		else if (move < 0 && facingRight)
			Flip ();



		if (Input.GetKey(KeyCode.Escape))
		{
			Application.Quit();
		}




	}
	
	void Flip(){
		facingRight = !facingRight;
		Vector3 theScale = transform.localScale;
		theScale.x *= -1;
		transform.localScale = theScale;
        isFacingRight = !isFacingRight;
	}


		
}
