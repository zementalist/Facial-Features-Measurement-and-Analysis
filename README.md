# Facial Features Measurement & Analysis

<h3>Conclusion:</h3>
<h5>Measure 19 facial features using basic geometry equations, and produce scaled measurements in pixels</h5>

<h4><b>Note:</b></h4>
<p>
    Some improvements are applied to the landmarks detection, for more information visit <a href="https://www.kaggle.com/zeyadkhalid/full-face-81-landmarks-detection-highly-improved" target="_blank">(this)</a> notebook
</p>

<h4>Features Visual Description</h4>
<img src="https://user-images.githubusercontent.com/50156227/140836123-92d5e97f-059a-437a-ba63-56d95664f667.png">

<h4>Features Textual Description:</h4>
<ol>
    <li>
        <b>Forehead Height</b>: distance between the top edge of eyebrows and the top edge of forehead.
    </li>
    <li>
        <b>Middle Face Height</b>: distance between the top edge of eyebrows and nose tip.
    </li>
    <li>
        <b>Lower Face Height</b>: distance between nose tip and the baseline of chin.
    </li>
    <li>
        <b>Jaw Shape</b>: A number to differentiate between jaw shapes. this number can be replaced if you use Face Shape Recognition, see <a href="https://www.kaggle.com/zeyadkhalid/face-shape-recognition-73-accuracy" target="_blank">(this)</a> notebook.
    </li>
    <li>
        <b>Left Eye Area</b>
    </li>
    <li>
        <b>Right Eye Area</b>
    </li>
    <li>
        <b>Eye to Eye Distance</b>: distance between eyes (closest edges)
    </li>
    <li>
        <b>Eye to Eyebrow Distance</b>: distance between eye and eyebrow (left or right is determined by whice side of the face is more directed to the -screen-)
    </li>
    <li>
        <b>Eyebrows Distance</b>: horizontal distance between eyebrows
    </li>
    <li>
        <b>Eyebrow Shape Detector 1</b>: The angle between 3 points (eyebrow left edge, eyebrow center, eyebrow right edge), to differentiate between (Straight | Non-straight) eyebrow shapes
    </li>
    <li>
        <b>Eyebrow Shape Detector 2</b>: A number to differentiate between (Curved | Angled) eyebrow shapes.
    </li>

    <li>
        <b>Eyebrow Slope</b>
    </li>
    <li>
        <b>Eye Slope Detector 1</b>: A method to calculate the slope of the eye. it's the slope of the line between eye's center point and eye's edge point. this detector is used to represent 3 types of eye slope (Upward, Downward, Straight).
    </li>
    <li>
        <b>Eye Slope Detector 2</b>: Another method to calculate the slope of the eye. it's the difference on Y-axis between eye's center point and eye's edge point. this detector isn't a 'mathematical' slope, but a number that can be clustered into 3 types of eye slope (Upward, Downward, Straight).
    </li>
    <li>
        <b>Nose Length</b>
    </li>
    <li>
        <b>Nose Width</b>: width of the lower part of the nose
    </li>
    <li>
        <b>Nose Arch</b>: Angle of the curve of the lower edge of the nose (longer nose = larger curve = smaller angle)
    </li>
    <li>
        <b>Upper Lip Height</b>
    </li>
    <li>
        <b>Lower Lip Height</b>
    </li>
</ol>
<h3><b>Inspirational Ideas</b></h3>
<ul>
    <li>Emotion Recognition from facial features</li>
    <li>Face Identification / Authentication</li>
    <li>Detect personality traits from facial features</li>
    <li>Gender Classification</li>
    <li>Down Syndrome Detection</li>
    <li>In General: use it as a preprocessing step to study the relation between numeric data instead of images</li>
</ul>
<h3>Any Suggestions?</h3>
<p>What else would be useful to measure? face width? mouth width (for smile detection)? distance between eyes and mouth? let me know your thoughts and I'll try to apply in a notebook update</p>
