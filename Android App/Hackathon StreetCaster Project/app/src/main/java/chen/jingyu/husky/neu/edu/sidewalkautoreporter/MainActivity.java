package chen.jingyu.husky.neu.edu.sidewalkautoreporter;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    static final int REQUEST_IMAGE_CAPTURE = 1;
    ImageView imageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button pictureButton = findViewById(R.id.pictureButton);
        imageView = findViewById(R.id.imageView);
        pictureButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText streetEditText = findViewById(R.id.streetEditText);
                EditText cityEditText = findViewById(R.id.cityEditText);
                EditText stateEditText = findViewById(R.id.stateEditText);
                EditText zipCodeEditText = findViewById(R.id.zipCodeEditText);

                if(TextUtils.isEmpty(streetEditText.getText())
                        || TextUtils.isEmpty(cityEditText.getText())
                        || TextUtils.isEmpty(stateEditText.getText())
                        || TextUtils.isEmpty((zipCodeEditText.getText()))) {
                    TextView textView = findViewById(R.id.textView);
                    textView.setText("Missing Required Item");
                    textView.setTextSize(12);
                    textView.setTextColor(Color.RED);
                } else {
                    dispatchTakePictureIntent();
                    //next step request machine learning prediction from project algorithm
                    //parse prediction results and quantify damage score
                }
            }
        });

        Button streetCastButton = findViewById(R.id.streetCastButton);
        streetCastButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String streetCastURI =
                        "https://www.boston.gov/departments/new-urban-mechanics/streetcaster ";
                Uri webAddress = Uri.parse(streetCastURI);
                Intent browserOpen = new Intent(Intent.ACTION_VIEW, webAddress);
                if (browserOpen.resolveActivity(getPackageManager()) != null) {
                    startActivity(browserOpen);
                }
            }
        });

        Button websiteButton = findViewById(R.id.websiteButton);
        websiteButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String websiteURI = "https://www.boston.gov/departments/new-urban-mechanics";
                Uri webAddress = Uri.parse(websiteURI);
                Intent browserOpen = new Intent(Intent.ACTION_VIEW, webAddress);
                if (browserOpen.resolveActivity(getPackageManager()) != null) {
                    startActivity(browserOpen);
                }
            }
        });
    }

    private void dispatchTakePictureIntent() {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takePictureIntent, REQUEST_IMAGE_CAPTURE);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_IMAGE_CAPTURE && resultCode == RESULT_OK) {
            Bundle extras = data.getExtras();
            Bitmap imageBitmap = (Bitmap) extras.get("data");
            imageView.setImageBitmap(imageBitmap);
        }
    }
}
