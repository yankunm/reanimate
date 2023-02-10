//
//  ViewController.swift






















// not in the Tutorial, Keep Alwayse at the bottom of the file outside of any {scope}

extension ViewController  {



	func session(_ session: ARSession, didFailWithError error: Error) {
			// Present an error message to the user

	}

	func sessionWasInterrupted(_ session: ARSession) {
			// Inform the user that the session has been interrupted, for example, by presenting an overlay

	}

	func sessionInterruptionEnded(_ session: ARSession) {
			// Reset tracking and/or remove existing anchors if consistent tracking is required

	}

}
